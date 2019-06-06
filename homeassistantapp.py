# -*-coding:utf-8-*-
import platform
if platform.machine() == 'armv6l':
    import os
    os.environ['KIVY_GL_BACKEND'] = 'gl'
    os.environ['KIVY_BCM_DISPMANX_ID'] = '2'
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.config import Config
from kivy.clock import Clock
from kivy.event import EventDispatcher
from RsetAPI import RsetAPI
import asyncio
from aiohttp import ClientSession
import asyncws
import json
from main import MainFloatLayout
from easy import EasyFloatLayout
from profession import ProfessionFloatLayout
from setting import SettingFloatLayout
from platform import python_version

ACCESS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTA2NzIzOTAsImlzcyI6ImVmYmU5YWFhMWZlYzQ4YTNhOGVkZTNjNTU2YWE4MTU1IiwiZXhwIjoxODY2MDMyMzkwfQ.GlA1Qb0LmIWqSvkTSgv_7bUyMxq5IfU1kPR9PBBCb5Y'

headers = {
    'Authorization': 'Bearer '+ ACCESS_TOKEN,
    'content-type': 'application/json'}
Config.write()

import threading
import time

kivy.resources.resource_add_path("data/font")
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')

states = []


class EventLoopWorker(EventDispatcher):

    __events__ = ('on_pulse',)  # defines this EventDispatcher's sole event

    def __init__(self):
        super().__init__()
        self._thread = threading.Thread(target=self._run_loop)  # note the Thread target here
        self._thread.daemon = True
        self.loop = None
        # the following are for the pulse() coroutine, see below
        self._pulse = None
        self._pulse_task = None
        self.url = 'http://guoxi.mynatapp.cc/api/states'

    def _run_loop(self):
        self.loop = asyncio.get_event_loop_policy().new_event_loop()
        asyncio.set_event_loop(self.loop)
        self._restart_pulse()
        # this example doesn't include any cleanup code, see the docs on how
        # to properly set up and tear down an asyncio event loop
        self.loop.run_forever()

    def start(self):
        self._thread.start()

    async def pulse(self):
        while True:
            # print('loop')
            async with ClientSession(headers=headers) as session:
                async with session.get(self.url) as r:
                    results = await r.read()
                    if python_version() is not '3.5.3':
                        results = results.decode()
                    msg = json.loads(results)
                    # print(msg)

                    def notify(text):
                        self.dispatch('on_pulse', text)

                    notify(msg)  # dispatch the on_pulse event

                    await asyncio.sleep(1)

    def _restart_pulse(self):
        """Helper to start/reset the pulse task when the pulse changes."""
        if self._pulse_task is not None:
            self._pulse_task.cancel()
        self._pulse_task = self.loop.create_task(self.pulse())

    def on_pulse(self, *_):
        """An EventDispatcher event must have a corresponding method."""
        pass


class EventLoopWorkerWs(EventDispatcher):

    __events__ = ('on_pulse',)  # defines this EventDispatcher's sole event

    def __init__(self):
        super().__init__()
        self._thread = threading.Thread(target=self._run_loop)  # note the Thread target here
        self._thread.daemon = True
        self.loop = None
        # the following are for the pulse() coroutine, see below
        self._pulse = None
        self._pulse_task = None
        self.url = 'http://guoxi.mynatapp.cc/api/states'

    def _run_loop(self):
        self.loop = asyncio.get_event_loop_policy().new_event_loop()
        asyncio.set_event_loop(self.loop)
        self._restart_pulse()
        # this example doesn't include any cleanup code, see the docs on how
        # to properly set up and tear down an asyncio event loop
        self.loop.run_forever()

    def start(self):
        self._thread.start()

    async def pulse(self):
        websocket = await asyncws.connect('ws://guoxi.mynatapp.cc/api/websocket')

        await websocket.send(json.dumps(
            {'type': 'auth',
             'access_token': ACCESS_TOKEN}
        ))

        await websocket.send(json.dumps(
            {'id': 1, 'type': 'subscribe_events', 'event_type': 'state_changed'}
        ))

        await websocket.send(json.dumps(
            {'id': 2, 'type': 'get_states'}
        ))

        while True:
            message = await websocket.recv()
            print(message)
            msg = json.loads(message)

            def notify(text):
                self.dispatch('on_pulse', text)
            notify(msg)  # dispatch the on_pulse event

    def _restart_pulse(self):
        """Helper to start/reset the pulse task when the pulse changes."""
        if self._pulse_task is not None:
            self._pulse_task.cancel()
        self._pulse_task = self.loop.create_task(self.pulse())

    def on_pulse(self, *_):
        """An EventDispatcher event must have a corresponding method."""
        pass


class Homeassistant(App):
    def __init__(self, **kwargs):
        super(Homeassistant, self).__init__(**kwargs)
        self.api = RsetAPI()
        self.men_xi = 'men_xi'
        self.men_xi_state = 'on'
        self.door_state = 'close'
        self.states = []
        self.url = 'http://192.168.1.2:8123/api/states'
        self.event_loop_worker = None
        # Clock.schedule_interval(self._update_clock, 1.)
        # Clock.schedule_interval(self._update_state, 1)

    def build(self):
        self.main = MainFloatLayout()
        main_screen = Screen(name='main')
        main_screen.add_widget(self.main)
        self.root.ids.sm.add_widget(main_screen)

        self.easy = EasyFloatLayout()
        easy_screen = Screen(name='easy')
        easy_screen.add_widget(self.easy)
        self.root.ids.sm.add_widget(easy_screen)

        self.profession = ProfessionFloatLayout()
        profession_screen = Screen(name='profession')
        profession_screen.add_widget(self.profession)
        self.root.ids.sm.add_widget(profession_screen)

        setting = SettingFloatLayout()
        setting_screen = Screen(name='setting')
        setting_screen.add_widget(setting)
        self.root.ids.sm.add_widget(setting_screen)

        self.root.ids.sm.current = 'main'

        self.men_xi_state = 'on'

        def display_on_pulse(instance, text):
            # self.states = text
            # self.get_all_state()
            self.get_all_state_ws(text)
        if self.event_loop_worker is None:
            # self.event_loop_worker = worker = EventLoopWorker()
            self.event_loop_worker = worker = EventLoopWorkerWs()
            worker.bind(on_pulse=display_on_pulse)
            worker.start()
        print('start')

    def on_easy_screen(self):
        self.root.ids.sm.transition.direction = 'left'
        self.root.ids.sm.current = 'easy'

    def on_profession_screen(self):
        self.root.ids.sm.transition.direction = 'left'
        # self.root.ids.sm.transition.duration = 1.
        self.root.ids.sm.current = 'profession'

    def on_main_screen(self):
        self.root.ids.sm.transition.direction = 'right'
        # self.root.ids.sm.transition.duration = 1.
        self.root.ids.sm.current = 'main'

    def on_setting_screen(self):
        self.root.ids.sm.transition.direction = 'left'
        # self.root.ids.sm.transition.duration = 1.
        self.root.ids.sm.current = 'setting'

    def on_door_control(self):
        if self.door_state == 'close':
            self.root.ids.door_control.background_normal = "data/icons/door/opening.jpg"
            self.root.ids.door_control.background_down = "data/icons/door/opening.jpg"
            self.api.set_switch_off(self.men_xi)
            self.door_state = 'opening'
        elif self.door_state == 'opened':
            self.api.set_switch_on(self.men_xi)
            self.door_state = 'close'

    def _update_state(self, dt):
        self.get_all_state()
        pass

    # def _update_clock(self, dt):
    #     if self.men_xi_state == 'on':
    #         if self.door_state == 'opened':
    #             self.door_state = 'close'
    #             self.root.ids.door_control.background_normal = "data/icons/door/open.jpg"
    #             self.root.ids.door_control.background_down = "data/icons/door/open.jpg"
    #     elif self.men_xi_state == 'off':
    #         self.door_state = 'opened'
    #         self.root.ids.door_control.background_normal = "data/icons/door/opened.jpg"
    #         self.root.ids.door_control.background_down = "data/icons/door/opened.jpg"

    # def update_state(self):
    #     self.men_xi_state = self.api.get_switch_state(self.men_xi)
    #     temp = self.api.get_temp()
    #     temp = int(float(str(temp)))
    #     self.main.set_temp(temp)
    #     self.easy.set_temp(temp)
    #     pm25 = self.api.get_PM25()
    #     pm25_level = self.api.get_PM25_level()
    #     self.main.set_pm2_5(pm25, pm25_level)
    #     self.easy.set_pm2_5(pm25, pm25_level)
    #     hum = self.api.get_hum()
    #     hum_level = self.api.get_hum_level()
    #     self.main.set_hum(hum, hum_level)
    #     self.easy.set_hum(hum, hum_level)

    def update_all_state(self):
        self.states = self.api.get_all_state()
        for state in states:
            if state['entity_id'] == 'sensor.wen_du':
                temp = state['state']
                temp = int(float(str(temp)))
                self.main.set_temp(temp)
                self.easy.set_temp(temp)
            elif state['entity_id'] == 'input_select.pm2_5_level':
                pm25_level = state['state']
                self.main.set_pm2_5(0, pm25_level)
                self.easy.set_pm2_5(0, pm25_level)
            elif state['entity_id'] == 'input_select.hum_level':
                hum_level = state['state']
                self.main.set_hum(0, hum_level)
                self.easy.set_hum(0, hum_level)
            elif state['entity_id'] == 'group.canopy_switch':
                self.profession.set_environment_canopy_switch(state['state'])
            elif state['entity_id'] == 'group.floor_heat_switch':
                self.profession.set_environment_floor_heating_switch(state['state'])
            elif state['entity_id'] == 'input_select.ac_setting':
                self.profession.set_climate_mode_state(state['state'])
            elif state['entity_id'] == 'input_select.air_conditioner_temp':
                self.profession.set_climate_temp_state(state['state'])
            elif state['entity_id'] == 'group.bedroom_light_switch':
                self.profession.set_bedroom_lights_state(state['state'])
            elif state['entity_id'] == 'group.vestibule_light_switch':
                self.profession.set_vestibule_lights_state(state['state'])
            elif state['entity_id'] == 'group.livingroom_light_switch':
                self.profession.set_livingroom_lights_state(state['state'])
            elif state['entity_id'] == 'group.bashroom_light_switch':
                self.profession.set_bashroom_lights_state(state['state'])
            elif state['entity_id'] == 'input_select.bedroom_color_light_rgb_setting':
                self.profession.set_atmosphere_bedroom_color(state['state'])
            elif state['entity_id'] == 'input_select.bedroom_color_light_brightness_setting':
                self.profession.set_atmosphere_bedroom_level(state['state'])
            elif state['entity_id'] == 'light.bedroom_color_lights':
                self.profession.set_atmosphere_bedroom_switch(state['state'])
            elif state['entity_id'] == 'input_select.bashroom_color_light_rgb_setting':
                self.profession.set_atmosphere_bashroom_color(state['state'])
            elif state['entity_id'] == 'input_select.bashroom_color_light_brightness_setting':
                self.profession.set_atmosphere_bedroom_level(state['state'])
            elif state['entity_id'] == 'light.bashroom_color_lights':
                self.profession.set_atmosphere_bashroom_switch(state['state'])
            elif state['entity_id'] == 'input_select.right_cover_position':
                self.profession.set_cover_right(state['state'])
            elif state['entity_id'] == 'input_select.mid_cover_position':
                self.profession.set_cover_mid(state['state'])
            elif state['entity_id'] == 'input_select.left_cover_position':
                self.profession.set_cover_left(state['state'])
            elif state['entity_id'] == 'input_select.bashroom_cover_position':
                self.profession.set_cover_bashroom(state['state'])
            elif state['entity_id'] == 'switch.men_xi':
                self.men_xi_state = state['state']
                if self.men_xi_state == 'on':
                    if self.door_state == 'opened':
                        self.door_state = 'close'
                        self.root.ids.door_control.background_normal = "data/icons/door/open.jpg"
                        self.root.ids.door_control.background_down = "data/icons/door/open.jpg"
                elif self.men_xi_state == 'off':
                    self.door_state = 'opened'
                    self.root.ids.door_control.background_normal = "data/icons/door/opened.jpg"
                    self.root.ids.door_control.background_down = "data/icons/door/opened.jpg"

    def get_all_state(self):
        for state in self.states:
            if state['state'] != 'unknown':
                if state['entity_id'] == 'sensor.wen_du':
                    temp = state['state']
                    temp = int(float(str(temp)))
                    self.main.set_temp(temp)
                    self.easy.set_temp(temp)
                elif state['entity_id'] == 'input_select.pm2_5_level':
                    pm25_level = state['state']
                    self.main.set_pm2_5(0, pm25_level)
                    self.easy.set_pm2_5(0, pm25_level)
                elif state['entity_id'] == 'input_select.hum_level':
                    hum_level = state['state']
                    self.main.set_hum(0, hum_level)
                    self.easy.set_hum(0, hum_level)
                elif state['entity_id'] == 'group.canopy_switch':
                    self.profession.set_environment_canopy_switch(state['state'])
                elif state['entity_id'] == 'group.floor_heat_switch':
                    self.profession.set_environment_floor_heating_switch(state['state'])
                elif state['entity_id'] == 'input_select.ac_setting':
                    self.profession.set_climate_mode_state(state['state'])
                elif state['entity_id'] == 'input_select.air_conditioner_temp':
                    self.profession.set_climate_temp_state(state['state'])
                elif state['entity_id'] == 'group.bedroom_light_switch':
                    self.profession.set_bedroom_lights_state(state['state'])
                elif state['entity_id'] == 'group.vestibule_light_switch':
                    self.profession.set_vestibule_lights_state(state['state'])
                elif state['entity_id'] == 'group.livingroom_light_switch':
                    self.profession.set_livingroom_lights_state(state['state'])
                elif state['entity_id'] == 'group.bashroom_light_switch':
                    self.profession.set_bashroom_lights_state(state['state'])
                elif state['entity_id'] == 'input_select.bedroom_color_light_rgb_setting':
                    self.profession.set_atmosphere_bedroom_color(state['state'])
                elif state['entity_id'] == 'input_select.bedroom_color_light_brightness_setting':
                    self.profession.set_atmosphere_bedroom_level(state['state'])
                elif state['entity_id'] == 'light.bedroom_color_lights':
                    self.profession.set_atmosphere_bedroom_switch(state['state'])
                elif state['entity_id'] == 'input_select.bashroom_color_light_rgb_setting':
                    self.profession.set_atmosphere_bashroom_color(state['state'])
                elif state['entity_id'] == 'input_select.bashroom_color_light_brightness_setting':
                    self.profession.set_atmosphere_bedroom_level(state['state'])
                elif state['entity_id'] == 'light.bashroom_color_lights':
                    self.profession.set_atmosphere_bashroom_switch(state['state'])
                elif state['entity_id'] == 'input_select.right_cover_position':
                    self.profession.set_cover_right(state['state'])
                elif state['entity_id'] == 'input_select.mid_cover_position':
                    self.profession.set_cover_mid(state['state'])
                elif state['entity_id'] == 'input_select.left_cover_position':
                    self.profession.set_cover_left(state['state'])
                elif state['entity_id'] == 'input_select.bashroom_cover_position':
                    self.profession.set_cover_bashroom(state['state'])
                elif state['entity_id'] == 'switch.men_xi':
                    self.men_xi_state = state['state']
                    if self.men_xi_state == 'on':
                        if self.door_state == 'opened':
                            self.door_state = 'close'
                            self.root.ids.door_control.background_normal = "data/icons/door/open.jpg"
                            self.root.ids.door_control.background_down = "data/icons/door/open.jpg"
                    elif self.men_xi_state == 'off':
                        self.door_state = 'opened'
                        self.root.ids.door_control.background_normal = "data/icons/door/opened.jpg"
                        self.root.ids.door_control.background_down = "data/icons/door/opened.jpg"

    def get_all_state_ws(self, text):
        if text['type'] == 'event':
            state = text['event']['data']
            if state['entity_id'] == 'sensor.wen_du':
                temp = state['new_state']['state']
                temp = int(float(str(temp)))
                self.main.set_temp(temp)
                self.easy.set_temp(temp)
            elif state['entity_id'] == 'input_select.pm2_5_level':
                pm25_level = state['new_state']['state']
                self.main.set_pm2_5(0, pm25_level)
                self.easy.set_pm2_5(0, pm25_level)
            elif state['entity_id'] == 'input_select.hum_level':
                hum_level = state['new_state']['state']
                self.main.set_hum(0, hum_level)
                self.easy.set_hum(0, hum_level)
            elif state['entity_id'] == 'group.canopy_switch':
                self.profession.set_environment_canopy_switch(state['new_state']['state'])
            elif state['entity_id'] == 'group.floor_heat_switch':
                self.profession.set_environment_floor_heating_switch(state['new_state']['state'])
            elif state['entity_id'] == 'input_select.ac_setting':
                self.profession.set_climate_mode_state(state['new_state']['state'])
            elif state['entity_id'] == 'input_select.air_conditioner_temp':
                self.profession.set_climate_temp_state(state['new_state']['state'])
            elif state['entity_id'] == 'group.bedroom_light_switch':
                self.profession.set_bedroom_lights_state(state['new_state']['state'])
            elif state['entity_id'] == 'group.vestibule_light_switch':
                self.profession.set_vestibule_lights_state(state['new_state']['state'])
            elif state['entity_id'] == 'group.livingroom_light_switch':
                self.profession.set_livingroom_lights_state(state['new_state']['state'])
            elif state['entity_id'] == 'group.bashroom_light_switch':
                self.profession.set_bashroom_lights_state(state['new_state']['state'])
            elif state['entity_id'] == 'input_select.bedroom_color_light_rgb_setting':
                self.profession.set_atmosphere_bedroom_color(state['new_state']['state'])
            elif state['entity_id'] == 'input_select.bedroom_color_light_brightness_setting':
                self.profession.set_atmosphere_bedroom_level(state['new_state']['state'])
            elif state['entity_id'] == 'light.bedroom_color_lights':
                self.profession.set_atmosphere_bedroom_switch(state['new_state']['state'])
            elif state['entity_id'] == 'input_select.bashroom_color_light_rgb_setting':
                self.profession.set_atmosphere_bashroom_color(state['new_state']['state'])
            elif state['entity_id'] == 'input_select.bashroom_color_light_brightness_setting':
                self.profession.set_atmosphere_bedroom_level(state['new_state']['state'])
            elif state['entity_id'] == 'light.bashroom_color_lights':
                self.profession.set_atmosphere_bashroom_switch(state['new_state']['state'])
            elif state['entity_id'] == 'input_select.right_cover_position':
                self.profession.set_cover_right(state['new_state']['state'])
            elif state['entity_id'] == 'input_select.mid_cover_position':
                self.profession.set_cover_mid(state['new_state']['state'])
            elif state['entity_id'] == 'input_select.left_cover_position':
                self.profession.set_cover_left(state['new_state']['state'])
            elif state['entity_id'] == 'input_select.bashroom_cover_position':
                self.profession.set_cover_bashroom(state['new_state']['state'])
            elif state['entity_id'] == 'switch.men_xi':
                self.men_xi_state = state['new_state']['state']
                if self.men_xi_state == 'on':
                    if self.door_state == 'opened':
                        self.door_state = 'close'
                        self.root.ids.door_control.background_normal = "data/icons/door/open.jpg"
                        self.root.ids.door_control.background_down = "data/icons/door/open.jpg"
                elif self.men_xi_state == 'off':
                    self.door_state = 'opened'
                    self.root.ids.door_control.background_normal = "data/icons/door/opened.jpg"
                    self.root.ids.door_control.background_down = "data/icons/door/opened.jpg"
        elif text['type'] == 'result':
            if text['id'] == 2:
                for state in text['result']:
                    if state['state'] != 'unknown':
                        if state['entity_id'] == 'sensor.wen_du':
                            temp = state['state']
                            temp = int(float(str(temp)))
                            self.main.set_temp(temp)
                            self.easy.set_temp(temp)
                        elif state['entity_id'] == 'input_select.pm2_5_level':
                            pm25_level = state['state']
                            self.main.set_pm2_5(0, pm25_level)
                            self.easy.set_pm2_5(0, pm25_level)
                        elif state['entity_id'] == 'input_select.hum_level':
                            hum_level = state['state']
                            self.main.set_hum(0, hum_level)
                            self.easy.set_hum(0, hum_level)
                        elif state['entity_id'] == 'group.canopy_switch':
                            self.profession.set_environment_canopy_switch(state['state'])
                        elif state['entity_id'] == 'group.floor_heat_switch':
                            self.profession.set_environment_floor_heating_switch(state['state'])
                        elif state['entity_id'] == 'input_select.ac_setting':
                            self.profession.set_climate_mode_state(state['state'])
                        elif state['entity_id'] == 'input_select.air_conditioner_temp':
                            self.profession.set_climate_temp_state(state['state'])
                        elif state['entity_id'] == 'group.bedroom_light_switch':
                            self.profession.set_bedroom_lights_state(state['state'])
                        elif state['entity_id'] == 'group.vestibule_light_switch':
                            self.profession.set_vestibule_lights_state(state['state'])
                        elif state['entity_id'] == 'group.livingroom_light_switch':
                            self.profession.set_livingroom_lights_state(state['state'])
                        elif state['entity_id'] == 'group.bashroom_light_switch':
                            self.profession.set_bashroom_lights_state(state['state'])
                        elif state['entity_id'] == 'input_select.bedroom_color_light_rgb_setting':
                            self.profession.set_atmosphere_bedroom_color(state['state'])
                        elif state['entity_id'] == 'input_select.bedroom_color_light_brightness_setting':
                            self.profession.set_atmosphere_bedroom_level(state['state'])
                        elif state['entity_id'] == 'light.bedroom_color_lights':
                            self.profession.set_atmosphere_bedroom_switch(state['state'])
                        elif state['entity_id'] == 'input_select.bashroom_color_light_rgb_setting':
                            self.profession.set_atmosphere_bashroom_color(state['state'])
                        elif state['entity_id'] == 'input_select.bashroom_color_light_brightness_setting':
                            self.profession.set_atmosphere_bedroom_level(state['state'])
                        elif state['entity_id'] == 'light.bashroom_color_lights':
                            self.profession.set_atmosphere_bashroom_switch(state['state'])
                        elif state['entity_id'] == 'input_select.right_cover_position':
                            self.profession.set_cover_right(state['state'])
                        elif state['entity_id'] == 'input_select.mid_cover_position':
                            self.profession.set_cover_mid(state['state'])
                        elif state['entity_id'] == 'input_select.left_cover_position':
                            self.profession.set_cover_left(state['state'])
                        elif state['entity_id'] == 'input_select.bashroom_cover_position':
                            self.profession.set_cover_bashroom(state['state'])
                        elif state['entity_id'] == 'switch.men_xi':
                            self.men_xi_state = state['state']
                            if self.men_xi_state == 'on':
                                if self.door_state == 'opened':
                                    self.door_state = 'close'
                                    self.root.ids.door_control.background_normal = "data/icons/door/open.jpg"
                                    self.root.ids.door_control.background_down = "data/icons/door/open.jpg"
                            elif self.men_xi_state == 'off':
                                self.door_state = 'opened'
                                self.root.ids.door_control.background_normal = "data/icons/door/opened.jpg"
                                self.root.ids.door_control.background_down = "data/icons/door/opened.jpg"


if __name__ == '__main__':
    Homeassistant().run()

