#coding=utf-8

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics import Rectangle
from kivy.clock import Clock
from RsetAPI import RsetAPI
# import gevent
# import gevent.monkey
# gevent.monkey.patch_socket()

with open('data/screens/profession.kv', encoding='utf8') as f:
    Builder.load_string(f.read())

# Builder.load_file('data/screens/profession.kv')


class ProfessionFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(ProfessionFloatLayout, self).__init__(**kwargs)
        self.api = RsetAPI()
        self.profession_current_type = 1
        self.profession_air_switch = 0
        self.profession_canopy_switch = 0
        self.profession_floor_heating_switch = 0
        self.profession_climate_switch = 0
        self.profession_climate_mode = 'None'
        self.profession_climate_temp = 25
        self.profession_lights_bedroom = {'switch': 'None', 'level': 1}
        self.profession_lights_livingroom = {'switch': 'None', 'level': 1}
        self.profession_lights_vestibule = {'switch': 'None', 'level': 1}
        self.profession_lights_bashroom = {'switch': 'None', 'level': 1}

        self.profession_atmosphere_bedroom = {'switch': 'off', 'color': 'None', 'level': 'None'}
        self.profession_atmosphere_livingroom = {'switch': 'off', 'color': 'None', 'level': 'None'}
        self.profession_atmosphere_vestibule = {'switch': 'off', 'color': 'None', 'level': 'None'}
        self.profession_atmosphere_bashroom = {'switch': 'off', 'color': 'None', 'level': 'None'}

        self.profession_cover_left = {'action': 0, 'postion': 'None'}
        self.profession_cover_mid = {'action': 0, 'postion': 'None'}
        self.profession_cover_right = {'action': 0, 'postion': 'None'}
        self.profession_cover_bashroom = {'action': 0, 'postion': 'None'}
        self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
        self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"

        self.api = RsetAPI()

        Clock.schedule_interval(self._update_clock, 1.)
        # Clock.schedule_interval(self._update_state, 2.)

    def set_environment_air_switch(self, air):
        self.profession_air_switch = air

    def set_environment_canopy_switch(self, canopy):
        self.profession_canopy_switch = canopy

    def set_environment_floor_heating_switch(self, floor_heating):
        self.profession_floor_heating_switch = floor_heating

    def set_climate_mode_state(self, mode):
        self.profession_climate_mode = mode

    def set_climate_temp_state(self, temp):
        self.profession_climate_temp = temp

    def set_bedroom_lights_state(self, switch):
        self.profession_lights_bedroom['switch'] = switch

    def set_livingroom_lights_state(self, switch):
        self.profession_lights_livingroom['switch'] = switch

    def set_vestibule_lights_state(self, switch):
        self.profession_lights_vestibule['switch'] = switch

    def set_bashroom_lights_state(self, switch):
        self.profession_lights_bashroom['switch'] = switch

    def set_atmosphere_bedroom_switch(self, switch):
        self.profession_atmosphere_bedroom['switch'] = switch

    def set_atmosphere_bedroom_color(self, color):
        self.profession_atmosphere_bedroom['color'] = color

    def set_atmosphere_bedroom_level(self, level):
        self.profession_atmosphere_bedroom['level'] = level

    def set_atmosphere_livingroom_switch(self, switch):
        self.profession_atmosphere_livingroom['switch'] = switch

    def set_atmosphere_livingroom_color(self, color):
        self.profession_atmosphere_livingroom['color'] = color

    def set_atmosphere_livingroom_level(self, level):
        self.profession_atmosphere_livingroom['level'] = level

    def set_atmosphere_vestibule_switch(self, switch):
        self.profession_atmosphere_vestibule['switch'] = switch

    def set_atmosphere_vestibule_color(self, color):
        self.profession_atmosphere_vestibule['color'] = color

    def set_atmosphere_vestibule_level(self, level):
        self.profession_atmosphere_vestibule['level'] = level

    def set_atmosphere_bashroom_switch(self, switch):
        self.profession_atmosphere_bashroom['switch'] = switch

    def set_atmosphere_bashroom_color(self, color):
        self.profession_atmosphere_bashroom['color'] = color

    def set_atmosphere_bashroom_level(self, level):
        self.profession_atmosphere_bashroom['level'] = level

    def set_cover_left(self, postion):
        self.profession_cover_left['postion'] = postion

    def set_cover_mid(self, postion):
        self.profession_cover_mid['postion'] = postion

    def set_cover_right(self, postion):
        self.profession_cover_right['postion'] = postion

    def set_cover_bashroom(self, postion):
        self.profession_cover_bashroom['postion'] = postion

    def _update_state(self, dt):
        gevent.joinall([
            gevent.spawn(self.update_state())
        ])

    def update_state(self):
        #获取新风状态
        if self.ids.sm_profession.current == 'environment_air':
            pass
        #获取地暖状态
        elif self.ids.sm_profession.current == 'environment_floor_heating':
            self.profession_floor_heating_switch = self.api.get_group_switch_state('floor_heat_switch')
        elif self.ids.sm_profession.current == 'environment_canopy':
            self.profession_canopy_switch = self.api.get_group_switch_state('canopy_switch')
        #获取空调状态
        elif self.ids.sm_profession.current == 'environment_climate':
            self.profession_climate_mode = self.api.get_ac_mode()
            self.profession_climate_temp = self.api.get_ac_temp()
        #获取卧室灯状态
        elif self.ids.sm_profession.current == 'lights_bedroom':
            self.profession_lights_bedroom['switch'] = self.api.get_group_switch_state('bedroom_light_switch')
        #获取客厅灯状态
        elif self.ids.sm_profession.current == 'lights_livingroom':
            self.profession_lights_livingroom['switch'] = self.api.get_group_switch_state('livingroom_light_switch')
        #获取玄关灯状态
        elif self.ids.sm_profession.current == 'lights_vestibule':
            self.profession_lights_vestibule['switch'] = self.api.get_group_switch_state('vestibule_light_switch')
        #获取卫浴灯状态
        elif self.ids.sm_profession.current == 'lights_bashroom':
            self.profession_lights_bashroom['switch'] = self.api.get_group_switch_state('bashroom_light_switch')
        #获取卧室氛围灯状态
        elif self.ids.sm_profession.current == 'atmosphere_bedroom':
            state = self.api.get_group_light_state('bedroom')
            self.profession_atmosphere_bedroom['switch'] = state['state']
            self.profession_atmosphere_bedroom['color'] = self.api.get_light_color('bedroom')
            self.profession_atmosphere_bedroom['level'] = self.api.get_light_brightness('bedroom')
        #获取卫浴氛围灯状态
        elif self.ids.sm_profession.current == 'atmosphere_bashroom':
            state = self.api.get_group_light_state('bashroom')
            self.profession_atmosphere_bashroom['switch'] = state['state']
            self.profession_atmosphere_bashroom['color'] = self.api.get_light_color('bashroom')
            self.profession_atmosphere_bashroom['level'] = self.api.get_light_brightness('bashroom')
        #获取左窗帘状态
        elif self.ids.sm_profession.current == 'cover_left':
            self.profession_cover_left['postion'] = self.api.get_cover_position('left_cover')
        #获取右窗帘状态
        elif self.ids.sm_profession.current == 'cover_mid':
            self.profession_cover_mid['postion'] = self.api.get_cover_position('mid_cover')
        #获取右窗帘状态
        elif self.ids.sm_profession.current == 'cover_right':
            self.profession_cover_right['postion'] = self.api.get_cover_position('right_cover')
        #获取卫浴窗帘状态
        elif self.ids.sm_profession.current == 'cover_bashroom':
            self.profession_cover_bashroom['postion'] = self.api.get_cover_position('bashroom_cover')

    def update_climate_screen(self):
        mode = self.profession_climate_mode
        temp = self.profession_climate_temp
        if mode == 'False':
            self.ids.climate_switch_button.background_normal = "data/icons/profession/climate/off.png"
            self.ids.climate_switch_button.background_down = "data/icons/profession/climate/off.png"
            self.ids.climate_FloatLayout.canvas.before.clear()
            with self.ids.climate_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.70263), pos=(self.width * 0.15, self.height * 0.0421),
                          source='data/icons/profession/climate/background_off.jpg')
            self.ids.climate_heat_button.background_normal = \
                "data/icons/profession/climate/switch_disable.jpg"
            self.ids.climate_heat_button.background_down = \
                "data/icons/profession/climate/switch_disable.jpg"
            self.ids.climate_cool_button.background_normal = \
                "data/icons/profession/climate/switch_disable.jpg"
            self.ids.climate_cool_button.background_down = \
                "data/icons/profession/climate/switch_disable.jpg"
            self.ids.climate_dry_button.background_normal = \
                "data/icons/profession/climate/switch_disable.jpg"
            self.ids.climate_dry_button.background_down = \
                "data/icons/profession/climate/switch_disable.jpg"
            self.ids.climate_up_button.background_normal = \
                "data/icons/profession/climate/up_disable.jpg"
            self.ids.climate_up_button.background_down = \
                "data/icons/profession/climate/up_disable.jpg"
            self.ids.climate_down_button.background_normal = \
                "data/icons/profession/climate/down_disable.jpg"
            self.ids.climate_down_button.background_down = \
                "data/icons/profession/climate/down_disable.jpg"

            self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/off.jpg'
        else:
            self.ids.climate_switch_button.background_normal = "data/icons/profession/climate/on.png"
            self.ids.climate_switch_button.background_down = "data/icons/profession/climate/on.png"
            self.ids.climate_FloatLayout.canvas.before.clear()
            with self.ids.climate_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.70263), pos=(self.width * 0.15, self.height * 0.0421),
                          source='data/icons/profession/climate/background_on.jpg')
            self.ids.climate_up_button.background_normal = \
                "data/icons/profession/climate/up.jpg"
            self.ids.climate_up_button.background_down = \
                "data/icons/profession/climate/up.jpg"
            self.ids.climate_down_button.background_normal = \
                "data/icons/profession/climate/down.jpg"
            self.ids.climate_down_button.background_down = \
                "data/icons/profession/climate/down.jpg"

            self.ids.climate_heat_button.background_normal = \
                "data/icons/profession/climate/select.jpg"
            self.ids.climate_heat_button.background_down = \
                "data/icons/profession/climate/select.jpg"
            self.ids.climate_cool_button.background_normal = \
                "data/icons/profession/climate/select.jpg"
            self.ids.climate_cool_button.background_down = \
                "data/icons/profession/climate/select.jpg"
            self.ids.climate_dry_button.background_normal = \
                "data/icons/profession/climate/select.jpg"
            self.ids.climate_dry_button.background_down = \
                "data/icons/profession/climate/select.jpg"
            if mode == 'COOL':
                self.ids.climate_cool_button.background_normal = "data/icons/profession/climate/selected.jpg"
                self.ids.climate_cool_button.background_down = "data/icons/profession/climate/selected.jpg"
                self.profession_climate_mode = 'COOL'
            elif mode == 'HEAT':
                self.ids.climate_heat_button.background_normal = "data/icons/profession/climate/selected.jpg"
                self.ids.climate_heat_button.background_down = "data/icons/profession/climate/selected.jpg"
                self.profession_climate_mode = 'HEAT'
            elif mode == 'DRY':
                self.ids.climate_dry_button.background_normal = "data/icons/profession/climate/selected.jpg"
                self.ids.climate_dry_button.background_down = "data/icons/profession/climate/selected.jpg"
                self.profession_climate_mode = 'DRY'

            self.profession_climate_temp = temp
            if temp == 18:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/18.jpg'
            elif temp == 19:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/19.jpg'
            elif temp == 20:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/20.jpg'
            elif temp == 21:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/21.jpg'
            elif temp == 22:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/22.jpg'
            elif temp == 23:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/23.jpg'
            elif temp == 24:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/24.jpg'
            elif temp == 25:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/25.jpg'
            elif temp == 26:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/26.jpg'
            elif temp == 27:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/27.jpg'
            elif temp == 28:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/28.jpg'
            elif temp == 29:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/29.jpg'
            elif temp == 30:
                self.ids.cliamate_temp_number.source = 'data/icons/profession/temp/30.jpg'

    def update_floor_heat_screen(self):
        if self.profession_floor_heating_switch == 'on':
            self.ids.floor_heating_switch_button.background_normal = "data/icons/profession/floor_heating/on.png"
            self.ids.floor_heating_switch_button.background_down = "data/icons/profession/floor_heating/on.png"
            self.ids.floor_heating_FloatLayout.canvas.before.clear()
            with self.ids.floor_heating_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/floor_heating/background_on.jpg')
            self.ids.floor_heating_level_1_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_1_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_2_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_2_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_3_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_3_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_4_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_5_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_5_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
        elif self.profession_floor_heating_switch == 'off':
            self.ids.floor_heating_switch_button.background_normal = "data/icons/profession/floor_heating/off.jpg"
            self.ids.floor_heating_switch_button.background_down = "data/icons/profession/floor_heating/off.jpg"
            self.ids.floor_heating_FloatLayout.canvas.before.clear()
            with self.ids.floor_heating_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/floor_heating/background_off.jpg')
            self.ids.floor_heating_level_1_button.background_normal = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_1_button.background_down = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_2_button.background_normal = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_2_button.background_down = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_3_button.background_normal = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_3_button.background_down = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_4_button.background_down = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_5_button.background_normal = \
                "data/icons/profession/floor_heating/switch_disable.jpg"
            self.ids.floor_heating_level_5_button.background_down = \
                "data/icons/profession/floor_heating/switch_disable.jpg"

    def update_canopy_screen(self):
        if self.profession_canopy_switch == 'on':
            self.ids.canopy_switch_button.background_normal = "data/icons/profession/canopy/on.png"
            self.ids.canopy_switch_button.background_down = "data/icons/profession/canopy/on.png"
            self.ids.canopy_FloatLayout.canvas.before.clear()
            with self.ids.canopy_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/canopy/background_on.png')
        elif self.profession_canopy_switch == 'off':
            self.ids.canopy_switch_button.background_normal = "data/icons/profession/canopy/off.png"
            self.ids.canopy_switch_button.background_down = "data/icons/profession/canopy/off.png"
            self.ids.canopy_FloatLayout.canvas.before.clear()
            with self.ids.canopy_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/canopy/background_off.png')

    def update_bedroom_light(self):
        if self.profession_lights_bedroom['switch'] == 'on':
            self.ids.lights_bedroom_switch_button.background_normal = "data/icons/profession/lights/on.png"
            self.ids.lights_bedroom_switch_button.background_down = "data/icons/profession/lights/on.png"
            self.ids.lights_bedroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_bedroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.58684),
                          pos=(self.width * 0.15, self.height * 0.0815789),
                          source='data/icons/profession/lights/bedroom_background_on.jpg')
            self.ids.lights_bedroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
        elif self.profession_lights_bedroom['switch'] == 'off':
                self.ids.lights_bedroom_switch_button.background_normal = "data/icons/profession/lights/off.png"
                self.ids.lights_bedroom_switch_button.background_down = "data/icons/profession/lights/off.png"
                self.ids.lights_bedroom_FloatLayout.canvas.before.clear()
                with self.ids.lights_bedroom_FloatLayout.canvas.before:
                    Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                              source='data/icons/profession/lights/bedroom_background_off.jpg')
                self.ids.lights_bedroom_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bedroom_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bedroom_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bedroom_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bedroom_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bedroom_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bedroom_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bedroom_level_4_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bedroom_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bedroom_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"

    def update_livingroom_light(self):
        if self.profession_lights_livingroom['switch'] == 'on':
            self.ids.lights_livingroom_switch_button.background_normal = "data/icons/profession/lights/on.png"
            self.ids.lights_livingroom_switch_button.background_down = "data/icons/profession/lights/on.png"
            self.ids.lights_livingroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_livingroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.58684),
                          pos=(self.width * 0.15, self.height * 0.0815789),
                          source='data/icons/profession/lights/livingroom_background_on.jpg')
            self.ids.lights_livingroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
        elif self.profession_lights_livingroom['switch'] == 'off':
                self.ids.lights_livingroom_switch_button.background_normal = "data/icons/profession/lights/off.png"
                self.ids.lights_livingroom_switch_button.background_down = "data/icons/profession/lights/off.png"
                self.ids.lights_livingroom_FloatLayout.canvas.before.clear()
                with self.ids.lights_livingroom_FloatLayout.canvas.before:
                    Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                              source='data/icons/profession/lights/livingroom_background_off.jpg')
                self.ids.lights_livingroom_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_livingroom_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_livingroom_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_livingroom_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_livingroom_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_livingroom_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_livingroom_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_livingroom_level_4_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_livingroom_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_livingroom_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"

    def update_vestibule_light(self):
        if self.profession_lights_vestibule['switch'] == 'on':
            self.ids.lights_vestibule_switch_button.background_normal = "data/icons/profession/lights/on.png"
            self.ids.lights_vestibule_switch_button.background_down = "data/icons/profession/lights/on.png"
            self.ids.lights_vestibule_FloatLayout.canvas.before.clear()
            with self.ids.lights_vestibule_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.58684),
                          pos=(self.width * 0.15, self.height * 0.0815789),
                          source='data/icons/profession/lights/vestibule_background_on.jpg')
            self.ids.lights_vestibule_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
        elif self.profession_lights_vestibule['switch'] == 'off':
                self.ids.lights_vestibule_switch_button.background_normal = "data/icons/profession/lights/off.png"
                self.ids.lights_vestibule_switch_button.background_down = "data/icons/profession/lights/off.png"
                self.ids.lights_vestibule_FloatLayout.canvas.before.clear()
                with self.ids.lights_vestibule_FloatLayout.canvas.before:
                    Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                              source='data/icons/profession/lights/vestibule_background_off.jpg')
                self.ids.lights_vestibule_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_vestibule_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_vestibule_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_vestibule_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_vestibule_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_vestibule_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_vestibule_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_vestibule_level_4_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_vestibule_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_vestibule_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"

    def update_bashroom_light(self):
        if self.profession_lights_bashroom['switch'] == 'on':
            self.ids.lights_bashroom_switch_button.background_normal = "data/icons/profession/lights/on.png"
            self.ids.lights_bashroom_switch_button.background_down = "data/icons/profession/lights/on.png"
            self.ids.lights_bashroom_FloatLayout.canvas.before.clear()
            with self.ids.lights_bashroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.58684),
                          pos=(self.width * 0.15, self.height * 0.0815789),
                          source='data/icons/profession/lights/bashroom_background_on.jpg')
            self.ids.lights_bashroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
        elif self.profession_lights_bashroom['switch'] == 'off':
                self.ids.lights_bashroom_switch_button.background_normal = "data/icons/profession/lights/off.png"
                self.ids.lights_bashroom_switch_button.background_down = "data/icons/profession/lights/off.png"
                self.ids.lights_bashroom_FloatLayout.canvas.before.clear()
                with self.ids.lights_bashroom_FloatLayout.canvas.before:
                    Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                              source='data/icons/profession/lights/bashroom_background_off.jpg')
                self.ids.lights_bashroom_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bashroom_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bashroom_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bashroom_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bashroom_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bashroom_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bashroom_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bashroom_level_4_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bashroom_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_disable.jpg"
                self.ids.lights_bashroom_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_disable.jpg"

    def update_atmosphere_bedroom(self):
        if self.profession_atmosphere_bedroom['switch'] == 'on':
            self.ids.atmosphere_bedroom_switch_button.background_normal = "data/icons/profession/atmosphere/on.png"
            self.ids.atmosphere_bedroom_switch_button.background_down = "data/icons/profession/atmosphere/on.png"
            self.ids.atmosphere_bedroom_FloatLayout.canvas.before.clear()
            with self.ids.atmosphere_bedroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/bedroom_background_on.jpg')
            current_color = self.profession_atmosphere_bedroom['color']
            current_level = self.profession_atmosphere_bedroom['level']
            self.ids.atmosphere_bedroom_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_bedroom_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_bedroom_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_bedroom_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_bedroom_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_bedroom_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_bedroom_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_bedroom_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_bedroom_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5.jpg"
            self.ids.atmosphere_bedroom_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5.jpg"

            if current_color == 'WHITE':
                self.ids.atmosphere_bedroom_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
                self.ids.atmosphere_bedroom_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
            elif current_color == 'YELLOW':
                self.ids.atmosphere_bedroom_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
                self.ids.atmosphere_bedroom_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
            elif current_color == 'PINK':
                self.ids.atmosphere_bedroom_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
                self.ids.atmosphere_bedroom_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
            elif current_color == 'BLUE':
                self.ids.atmosphere_bedroom_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
                self.ids.atmosphere_bedroom_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
            elif current_color == 'GREEN':
                self.ids.atmosphere_bedroom_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"
                self.ids.atmosphere_bedroom_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"

            self.ids.atmosphere_bedroom_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bedroom_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bedroom_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bedroom_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bedroom_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bedroom_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bedroom_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bedroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bedroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bedroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"

            if current_level == 'LEVEL_ONE':
                self.ids.atmosphere_bedroom_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bedroom_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif current_level == 'LEVEL_TWO':
                self.ids.atmosphere_bedroom_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bedroom_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif current_level == 'LEVEL_THREE':
                self.ids.atmosphere_bedroom_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bedroom_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif current_level == 'LEVEL_FOUR':
                self.ids.atmosphere_bedroom_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bedroom_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif current_level == 'LEVEL_FIVE':
                self.ids.atmosphere_bedroom_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bedroom_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
        elif self.profession_atmosphere_bedroom['switch'] == 'off':
            self.ids.atmosphere_bedroom_switch_button.background_normal = "data/icons/profession/atmosphere/off.png"
            self.ids.atmosphere_bedroom_switch_button.background_down = "data/icons/profession/atmosphere/off.png"
            self.ids.atmosphere_bedroom_FloatLayout.canvas.before.clear()
            with self.ids.atmosphere_bedroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/bedroom_background_off.jpg')
            self.ids.atmosphere_bedroom_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bedroom_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bedroom_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bedroom_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bedroom_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bedroom_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bedroom_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bedroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bedroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bedroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"

            self.ids.atmosphere_bedroom_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_bedroom_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_bedroom_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_bedroom_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_bedroom_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_bedroom_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_bedroom_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_bedroom_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_bedroom_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5_off.jpg"
            self.ids.atmosphere_bedroom_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5_off.jpg"

    def update_atmosphere_bashroom(self):
        if self.profession_atmosphere_bashroom['switch'] == 'on':
            self.ids.atmosphere_bashroom_switch_button.background_normal = "data/icons/profession/atmosphere/on.png"
            self.ids.atmosphere_bashroom_switch_button.background_down = "data/icons/profession/atmosphere/on.png"
            self.ids.atmosphere_bashroom_FloatLayout.canvas.before.clear()
            with self.ids.atmosphere_bashroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/bashroom_background_on.jpg')
            current_color = self.profession_atmosphere_bashroom['color']
            current_level = self.profession_atmosphere_bashroom['level']

            # if current_color != self.profession_atmosphere_bashroom['color']:
            #     self.profession_atmosphere_bashroom['color'] = current_color
            self.ids.atmosphere_bashroom_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_bashroom_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_bashroom_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_bashroom_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_bashroom_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_bashroom_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_bashroom_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_bashroom_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_bashroom_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5.jpg"
            self.ids.atmosphere_bashroom_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5.jpg"

            if current_color == 'WHITE':
                self.ids.atmosphere_bashroom_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
                self.ids.atmosphere_bashroom_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
            elif current_color == 'YELLOW':
                self.ids.atmosphere_bashroom_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
                self.ids.atmosphere_bashroom_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
            elif current_color == 'PINK':
                self.ids.atmosphere_bashroom_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
                self.ids.atmosphere_bashroom_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
            elif current_color == 'BLUE':
                self.ids.atmosphere_bashroom_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
                self.ids.atmosphere_bashroom_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
            elif current_color == 'GREEN':
                self.ids.atmosphere_bashroom_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"
                self.ids.atmosphere_bashroom_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"

            # if current_level != self.profession_atmosphere_bashroom['level']:
            #     self.profession_atmosphere_bashroom['level'] = current_level
            self.ids.atmosphere_bashroom_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bashroom_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bashroom_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bashroom_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bashroom_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bashroom_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bashroom_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bashroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bashroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_bashroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"

            if current_level == 'LEVEL_ONE':
                self.ids.atmosphere_bashroom_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bashroom_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif current_level == 'LEVEL_TWO':
                self.ids.atmosphere_bashroom_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bashroom_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif current_level == 'LEVEL_THREE':
                self.ids.atmosphere_bashroom_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bashroom_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif current_level == 'LEVEL_FOUR':
                self.ids.atmosphere_bashroom_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bashroom_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif current_level == 'LEVEL_FIVE':
                self.ids.atmosphere_bashroom_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_bashroom_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
        elif self.profession_atmosphere_bashroom['switch'] == 'off':
            self.ids.atmosphere_bashroom_switch_button.background_normal = "data/icons/profession/atmosphere/off.png"
            self.ids.atmosphere_bashroom_switch_button.background_down = "data/icons/profession/atmosphere/off.png"
            self.ids.atmosphere_bashroom_FloatLayout.canvas.before.clear()
            with self.ids.atmosphere_bashroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/bashroom_background_off.jpg')
            self.ids.atmosphere_bashroom_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bashroom_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bashroom_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bashroom_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bashroom_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bashroom_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bashroom_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bashroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bashroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_bashroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"

            self.ids.atmosphere_bashroom_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_bashroom_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_bashroom_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_bashroom_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_bashroom_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_bashroom_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_bashroom_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_bashroom_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_bashroom_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5_off.jpg"
            self.ids.atmosphere_bashroom_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5_off.jpg"

    def update_cover_left(self):
        postion = self.profession_cover_left['postion']
        self.ids.cover_left_postion_1_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_1_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_2_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_2_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_3_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_3_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_4_button.background_normal = \
            "data/icons/profession/floor_heating/switch.jpg"
        self.ids.cover_left_postion_4_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_5_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_5_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        if postion == 'ONE':
            self.ids.cover_left_postion_1_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_left_postion_1_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'TWO':
            self.ids.cover_left_postion_2_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_left_postion_2_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'THREE':
            self.ids.cover_left_postion_3_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_left_postion_3_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'FOUR':
            self.ids.cover_left_postion_4_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_left_postion_4_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'FIVE':
            self.ids.cover_left_postion_5_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_left_postion_5_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"

    def update_cover_right(self):
        postion = self.profession_cover_right['postion']
        self.ids.cover_right_postion_1_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_1_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_2_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_2_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_3_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_3_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_4_button.background_normal = \
            "data/icons/profession/floor_heating/switch.jpg"
        self.ids.cover_right_postion_4_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_5_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_5_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        if postion == 'ONE':
            self.ids.cover_right_postion_1_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_right_postion_1_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'TWO':
            self.ids.cover_right_postion_2_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_right_postion_2_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'THREE':
            self.ids.cover_right_postion_3_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_right_postion_3_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'FOUR':
            self.ids.cover_right_postion_4_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_right_postion_4_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'FIVE':
            self.ids.cover_right_postion_5_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_right_postion_5_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"

    def update_cover_mid(self):
        postion = self.profession_cover_mid['postion']
        self.ids.cover_mid_postion_1_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_1_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_2_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_2_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_3_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_3_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_4_button.background_normal = \
            "data/icons/profession/floor_heating/switch.jpg"
        self.ids.cover_mid_postion_4_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_5_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_5_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        if postion == 'ONE':
            self.ids.cover_mid_postion_1_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_mid_postion_1_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'TWO':
            self.ids.cover_mid_postion_2_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_mid_postion_2_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'THREE':
            self.ids.cover_mid_postion_3_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_mid_postion_3_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'FOUR':
            self.ids.cover_mid_postion_4_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_mid_postion_4_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'FIVE':
            self.ids.cover_mid_postion_5_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_mid_postion_5_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"

    def update_cover_bashroom(self):
        postion = self.profession_cover_bashroom['postion']
        self.ids.cover_bashroom_postion_1_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_1_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_2_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_2_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_3_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_3_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_4_button.background_normal = \
            "data/icons/profession/floor_heating/switch.jpg"
        self.ids.cover_bashroom_postion_4_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_5_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_5_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        if postion == 'ONE':
            self.ids.cover_bashroom_postion_1_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_bashroom_postion_1_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'TWO':
            self.ids.cover_bashroom_postion_2_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_bashroom_postion_2_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'THREE':
            self.ids.cover_bashroom_postion_3_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_bashroom_postion_3_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'FOUR':
            self.ids.cover_bashroom_postion_4_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_bashroom_postion_4_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
        elif postion == 'FIVE':
            self.ids.cover_bashroom_postion_5_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_bashroom_postion_5_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"

    def _update_clock(self, dt):
        #获取新风状态
        if self.ids.sm_profession.current == 'environment_air':
            pass
        #获取地暖状态
        elif self.ids.sm_profession.current == 'environment_floor_heating':
            self.update_floor_heat_screen()
        elif self.ids.sm_profession.current == 'environment_canopy':
            self.update_canopy_screen()
        #获取空调状态
        elif self.ids.sm_profession.current == 'environment_climate':
            self.update_climate_screen()
        #获取卧室灯状态
        elif self.ids.sm_profession.current == 'lights_bedroom':
            self.update_bedroom_light()
        #获取客厅灯状态
        elif self.ids.sm_profession.current == 'lights_livingroom':
            self.update_livingroom_light()
        #获取玄关灯状态
        elif self.ids.sm_profession.current == 'lights_vestibule':
            self.update_vestibule_light()
        #获取卫浴灯状态
        elif self.ids.sm_profession.current == 'lights_bashroom':
            self.update_bashroom_light()
        #获取卧室氛围灯状态
        elif self.ids.sm_profession.current == 'atmosphere_bedroom':
            self.update_atmosphere_bedroom()
        #获取卫浴氛围灯状态
        elif self.ids.sm_profession.current == 'atmosphere_bashroom':
            self.update_atmosphere_bashroom()
        # #获取左窗帘灯状态
        # elif self.ids.sm_profession.current == 'cover_left':
        #     self.update_cover_left()
        # #获取右窗帘灯状态
        # elif self.ids.sm_profession.current == 'cover_right':
        #     self.update_cover_right()
        # #获取中间窗帘灯状态
        # elif self.ids.sm_profession.current == 'cover_mid':
        #     self.update_cover_mid()
        # #获取卫浴窗帘灯状态
        # elif self.ids.sm_profession.current == 'cover_bashroom':
        #     self.update_cover_bashroom()

    def on_type_selected(self, *args):
        if self.profession_current_type != args[0]:
            if self.profession_current_type < args[0]:
                self.ids.sm_profession.transition.direction = 'left'
            else:
                self.ids.sm_profession.transition.direction = 'right'
            self.profession_current_type = args[0]
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            if args[0] == 1:
                self.ids.sm_profession.current = 'environment_air'
                self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
                self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
            elif args[0] == 2:
                self.ids.sm_profession.current = 'lights_bedroom'
                self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
                self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
            elif args[0] == 3:
                self.ids.sm_profession.current = 'atmosphere_bedroom'
                self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
                self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
            elif args[0] == 4:
                self.ids.sm_profession.current = 'cover_left'
                self.ids.cover_button.background_normal = "data/icons/profession/cover_h.jpg"
                self.ids.cover_button.background_down = "data/icons/profession/cover_h.jpg"

    # 页面切换
    def go_next_screen(self):
        self.ids.sm_profession.transition.direction = 'left'
        if self.ids.sm_profession.current == 'environment_air':
            self.ids.sm_profession.current = 'environment_floor_heating'
        elif self.ids.sm_profession.current == 'environment_floor_heating':
            self.ids.sm_profession.current = 'environment_canopy'
        elif self.ids.sm_profession.current == 'environment_canopy':
            self.ids.sm_profession.current = 'environment_climate'
        elif self.ids.sm_profession.current == 'environment_climate':
            self.profession_current_type = 2
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'lights_bedroom'
        elif self.ids.sm_profession.current == 'lights_bedroom':
            self.ids.sm_profession.current = 'lights_livingroom'
        elif self.ids.sm_profession.current == 'lights_livingroom':
            self.ids.sm_profession.current = 'lights_vestibule'
        elif self.ids.sm_profession.current == 'lights_vestibule':
            self.ids.sm_profession.current = 'lights_bashroom'
        elif self.ids.sm_profession.current == 'lights_bashroom':
            self.profession_current_type = 3
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'atmosphere_bedroom'
        # elif self.ids.sm_profession.current == 'atmosphere_bedroom':
        #     self.ids.sm_profession.current = 'atmosphere_livingroom'
        # elif self.ids.sm_profession.current == 'atmosphere_livingroom':
        #     self.ids.sm_profession.current = 'atmosphere_vestibule'
        # elif self.ids.sm_profession.current == 'atmosphere_vestibule':
        #     self.ids.sm_profession.current = 'atmosphere_bashroom'
        elif self.ids.sm_profession.current == 'atmosphere_bedroom':
            self.ids.sm_profession.current = 'atmosphere_bashroom'
        elif self.ids.sm_profession.current == 'atmosphere_bashroom':
            self.profession_current_type = 4
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover_h.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover_h.jpg"
            self.ids.sm_profession.current = 'cover_left'
        elif self.ids.sm_profession.current == 'cover_left':
            self.ids.sm_profession.current = 'cover_mid'
        elif self.ids.sm_profession.current == 'cover_mid':
            self.ids.sm_profession.current = 'cover_right'
        elif self.ids.sm_profession.current == 'cover_right':
            self.ids.sm_profession.current = 'cover_bashroom'
        elif self.ids.sm_profession.current == 'cover_bashroom':
            self.profession_current_type = 1
            self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'environment_air'

    def go_previous_screen(self):
        self.ids.sm_profession.transition.direction = 'right'
        if self.ids.sm_profession.current == 'environment_floor_heating':
            self.ids.sm_profession.current = 'environment_air'
        elif self.ids.sm_profession.current == 'environment_climate':
            self.ids.sm_profession.current = 'environment_canopy'
        elif self.ids.sm_profession.current == 'environment_canopy':
            self.ids.sm_profession.current = 'environment_floor_heating'
        elif self.ids.sm_profession.current == 'lights_bedroom':
            self.profession_current_type = 1
            self.ids.environment_button.background_normal = "data/icons/profession/environment_h.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment_h.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'environment_climate'
        elif self.ids.sm_profession.current == 'lights_livingroom':
            self.ids.sm_profession.current = 'lights_bedroom'
        elif self.ids.sm_profession.current == 'lights_vestibule':
            self.ids.sm_profession.current = 'lights_livingroom'
        elif self.ids.sm_profession.current == 'lights_bashroom':
            self.ids.sm_profession.current = 'lights_vestibule'
        elif self.ids.sm_profession.current == 'atmosphere_bedroom':
            self.profession_current_type = 2
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights_h.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights_h.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'lights_bashroom'
        # elif self.ids.sm_profession.current == 'atmosphere_livingroom':
        #     self.ids.sm_profession.current = 'atmosphere_bedroom'
        # elif self.ids.sm_profession.current == 'atmosphere_vestibule':
        #     self.ids.sm_profession.current = 'atmosphere_livingroom'
        # elif self.ids.sm_profession.current == 'atmosphere_bashroom':
        #     self.ids.sm_profession.current = 'atmosphere_vestibule'
        elif self.ids.sm_profession.current == 'atmosphere_bashroom':
            self.ids.sm_profession.current = 'atmosphere_bedroom'
        elif self.ids.sm_profession.current == 'cover_left':
            self.profession_current_type = 3
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere_h.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere_h.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover.jpg"
            self.ids.sm_profession.current = 'atmosphere_bashroom'
        elif self.ids.sm_profession.current == 'cover_right':
            self.ids.sm_profession.current = 'cover_mid'
        elif self.ids.sm_profession.current == 'cover_mid':
            self.ids.sm_profession.current = 'cover_left'
        elif self.ids.sm_profession.current == 'cover_bashroom':
            self.ids.sm_profession.current = 'cover_left'
        elif self.ids.sm_profession.current == 'environment_air':
            self.profession_current_type = 4
            self.ids.environment_button.background_normal = "data/icons/profession/environment.jpg"
            self.ids.environment_button.background_down = "data/icons/profession/environment.jpg"
            self.ids.lights_button.background_normal = "data/icons/profession/lights.jpg"
            self.ids.lights_button.background_down = "data/icons/profession/lights.jpg"
            self.ids.atmosphere_button.background_normal = "data/icons/profession/atmosphere.jpg"
            self.ids.atmosphere_button.background_down = "data/icons/profession/atmosphere.jpg"
            self.ids.cover_button.background_normal = "data/icons/profession/cover_h.jpg"
            self.ids.cover_button.background_down = "data/icons/profession/cover_h.jpg"
            self.ids.sm_profession.current = 'cover_bashroom'

    #新风快关
    def on_air_switch_selected(self):
        if self.profession_air_switch == 0:
            self.ids.air_FloatLayout.canvas.before.clear()
            with self.ids.air_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/air/background_on.jpg')
            self.ids.air_switch_button.background_normal = "data/icons/profession/air/on.png"
            self.ids.air_switch_button.background_down = "data/icons/profession/air/on.png"
            self.profession_air_switch = 1
        else:
            self.ids.air_FloatLayout.canvas.before.clear()
            with self.ids.air_FloatLayout.canvas.before:
                Rectangle(size=(self.width*0.7, self.height*0.58684), pos=(self.width*0.15, self.height*0.0815789),
                          source='data/icons/profession/air/background_off.jpg')
            self.ids.air_switch_button.background_normal = "data/icons/profession/air/off.png"
            self.ids.air_switch_button.background_down = "data/icons/profession/air/off.png"
            self.profession_air_switch = 0

    #地暖开关
    def on_floor_heating_switch_selected(self):
        if self.profession_floor_heating_switch == 'off':
            self.api.set_group_switch_on('floor_heat_switch')
        else:
            self.api.set_group_switch_off('floor_heat_switch')

    #地暖温度调节
    def on_floor_heating_level_selected(self, *args):
        if self.profession_floor_heating_switch == 'on':
            self.ids.floor_heating_level_1_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_1_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_2_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_2_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_3_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_3_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_4_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_5_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.floor_heating_level_5_button.background_down = \
                "data/icons/profession/floor_heating/switch.jpg"
            if args[0] == '1':
                self.ids.floor_heating_level_1_button.background_normal = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
                self.ids.floor_heating_level_1_button.background_down = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
            elif args[0] == '2':
                self.ids.floor_heating_level_2_button.background_normal = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
                self.ids.floor_heating_level_2_button.background_down = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
            elif args[0] == '3':
                self.ids.floor_heating_level_3_button.background_normal = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
                self.ids.floor_heating_level_3_button.background_down = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
            elif args[0] == '4':
                self.ids.floor_heating_level_4_button.background_normal = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
                self.ids.floor_heating_level_4_button.background_down = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
            elif args[0] == '5':
                self.ids.floor_heating_level_5_button.background_normal = \
                    "data/icons/profession/floor_heating/switch_h.jpg"
                self.ids.floor_heating_level_5_button.background_down = \
                    "data/icons/profession/floor_heating/switch_h.jpg"

    # 雨棚开关
    def on_canopy_switch_selected(self):
        if self.profession_canopy_switch == 'off':
            self.api.set_group_switch_on('canopy_switch')
        else:
            self.api.set_group_switch_off('canopy_switch')

    #空调开关
    def on_climate_switch_selected(self):
        if self.profession_climate_switch == 'off':
            self.profession_climate_switch = 'on'
            self.api.set_ac_mode('COOL')
        else:
            self.profession_climate_switch = 'off'
            self.api.set_ac_mode('False')
            self.profession_climate_mode = 'None'

    #空调模式选择
    def on_climate_mode_selected(self, *args):
        if self.profession_climate_switch == 'on':
            self.api.set_ac_mode(args[0])

    # 空调温度
    def on_climate_temp_selected(self, *args):
        temp = self.api.get_ac_temp()
        if args[0] is 'up':
            if temp < 30:
                temp = temp + 1
        elif args[0] is 'down':
            if temp > 18:
                temp = temp - 1
        self.api.set_ac_temp(temp)

    #卧室灯
    def on_lights_bedroom_switch_selected(self):
        if self.profession_lights_bedroom['switch'] == 'on':
            self.api.set_group_switch_off('bedroom_light_switch')
        else:
            self.api.set_group_switch_on('bedroom_light_switch')

    #卧室灯亮度选择
    def on_lights_bedroom_level_selected(self,*args):
        if self.profession_lights_bedroom['switch'] == 'on':
            self.ids.lights_bedroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bedroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            if args[0] == 1:
                self.ids.lights_bedroom_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bedroom_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 2:
                self.ids.lights_bedroom_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bedroom_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 3:
                self.ids.lights_bedroom_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bedroom_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 4:
                self.ids.lights_bedroom_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bedroom_level_4_button.background_down = \
                    "data/icons/profession/light  s/switch_h.jpg"
            elif args[0] == 5:
                self.ids.lights_bedroom_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bedroom_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"

    #客厅灯开关
    def on_lights_livingroom_switch_selected(self):
        if self.profession_lights_livingroom['switch'] == 'on':
            self.api.set_group_switch_off('livingroom_light_switch')
        else:
            self.api.set_group_switch_on('livingroom_light_switch')

    #客厅灯亮度选择
    def on_lights_livingroom_level_selected(self, *args):
        if self.profession_lights_livingroom['switch'] == 'on':
            self.ids.lights_livingroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_livingroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            if args[0] == 1:
                self.ids.lights_livingroom_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_livingroom_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 2:
                self.ids.lights_livingroom_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_livingroom_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 3:
                self.ids.lights_livingroom_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_livingroom_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 4:
                self.ids.lights_livingroom_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_livingroom_level_4_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 5:
                self.ids.lights_livingroom_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_livingroom_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"

    # 玄关灯开关
    def on_lights_vestibule_switch_selected(self):
        if self.profession_lights_vestibule['switch'] == 'on':
            self.api.set_group_switch_off('vestibule_light_switch')
        else:
            self.api.set_group_switch_on('vestibule_light_switch')

    # 玄关灯亮度选择
    def on_lights_vestibule_level_selected(self, *args):
        if self.profession_lights_vestibule['switch'] == 'on':
            self.ids.lights_vestibule_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_vestibule_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            if args[0] == 1:
                self.ids.lights_vestibule_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_vestibule_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 2:
                self.ids.lights_vestibule_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_vestibule_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 3:
                self.ids.lights_vestibule_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_vestibule_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 4:
                self.ids.lights_vestibule_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_vestibule_level_4_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 5:
                self.ids.lights_vestibule_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_vestibule_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"

    # 浴室灯开关
    def on_lights_bashroom_switch_selected(self):
        if self.profession_lights_bashroom['switch'] == 'on':
            self.api.set_group_switch_off('bashroom_light_switch')
        else:
            self.api.set_group_switch_on('bashroom_light_switch')

    # 浴室灯亮度选择
    def on_lights_bashroom_level_selected(self, *args):
        if self.profession_lights_bashroom['switch'] == 'on':
            self.ids.lights_bashroom_level_1_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_1_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_2_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_2_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_3_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_3_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_4_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_4_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_5_button.background_normal = \
                "data/icons/profession/lights/switch.jpg"
            self.ids.lights_bashroom_level_5_button.background_down = \
                "data/icons/profession/lights/switch.jpg"
            if args[0] == 1:
                self.ids.lights_bashroom_level_1_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bashroom_level_1_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 2:
                self.ids.lights_bashroom_level_2_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bashroom_level_2_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 3:
                self.ids.lights_bashroom_level_3_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bashroom_level_3_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 4:
                self.ids.lights_bashroom_level_4_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bashroom_level_4_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"
            elif args[0] == 5:
                self.ids.lights_bashroom_level_5_button.background_normal = \
                    "data/icons/profession/lights/switch_h.jpg"
                self.ids.lights_bashroom_level_5_button.background_down = \
                    "data/icons/profession/lights/switch_h.jpg"

    #卧室氛围灯开关
    def on_atmosphere_bedroom_switch_selected(self):
        if self.profession_atmosphere_bedroom['switch'] == 'off':
            self.api.set_group_light_switch_on('bedroom')
        else:
            self.api.set_group_light_off('bedroom')

    #卧室氛围灯亮度调节
    def on_atmosphere_bedroom_level_selected(self,*args):
        if self.profession_atmosphere_bedroom['switch'] == 'on':
            if args[0] == 1:
                self.api.set_light_brightness('bedroom', 'LEVEL_ONE')
            elif args[0] == 2:
                self.api.set_light_brightness('bedroom', 'LEVEL_TWO')
            elif args[0] == 3:
                self.api.set_light_brightness('bedroom', 'LEVEL_THREE')
            elif args[0] == 4:
                self.api.set_light_brightness('bedroom', 'LEVEL_FOUR')
            elif args[0] == 5:
                self.api.set_light_brightness('bedroom', 'LEVEL_FIVE')

    #卧室氛围灯颜色调节
    def on_atmosphere_bedroom_color_selected(self, *args):
        if self.profession_atmosphere_bedroom['switch'] == 'on':
            if args[0] == 1:
                self.api.set_light_color('bedroom', 'WHITE')
            elif args[0] == 2:
                self.api.set_light_color('bedroom', 'YELLOW')
            elif args[0] == 3:
                self.api.set_light_color('bedroom', 'PINK')
            elif args[0] == 4:
                self.api.set_light_color('bedroom', 'BLUE')
            elif args[0] == 5:
                self.api.set_light_color('bedroom', 'GREEN')

    #客厅氛围灯开关
    def on_atmosphere_livingroom_switch_selected(self):
        if self.profession_atmosphere_livingroom['switch'] == 'off':
            self.profession_atmosphere_livingroom['switch'] = 1
            self.ids.atmosphere_livingroom_switch_button.background_normal = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_livingroom_switch_button.background_down = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_livingroom_switch_button.canvas.before.clear()
            with self.ids.atmosphere_livingroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/livingroom_background_on.jpg')
            self.ids.atmosphere_livingroom_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"

            self.ids.atmosphere_livingroom_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_livingroom_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5.jpg"
        else:
            self.profession_atmosphere_livingroom['switch'] = 0
            self.ids.atmosphere_livingroom_switch_button.background_normal = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_livingroom_switch_button.background_down = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_livingroom_FloatLayout.canvas.before.clear()
            with self.ids.atmosphere_livingroom_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/livingroom_background_off.jpg')
            self.ids.atmosphere_livingroom_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"

            self.ids.atmosphere_livingroom_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_livingroom_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5_off.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5_off.jpg"

    #客厅氛围灯亮度调节
    def on_atmosphere_livingroom_level_selected(self, *args):
        if self.profession_atmosphere_livingroom['switch'] == 'on':
            self.ids.atmosphere_livingroom_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.atmosphere_livingroom_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_livingroom_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            if args[0] == 1:
                self.ids.atmosphere_livingroom_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_livingroom_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_livingroom_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_livingroom_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_livingroom_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_livingroom_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_livingroom_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_livingroom_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_livingroom_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_livingroom_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"

    #客厅氛围灯颜色调节
    def on_atmosphere_livingroom_color_selected(self, *args):
        if self.profession_atmosphere_livingroom['switch'] == 'on':
            self.ids.atmosphere_livingroom_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_livingroom_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_livingroom_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_livingroom_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_livingroom_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5.jpg"
            self.ids.atmosphere_livingroom_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5.jpg"
            if args[0] == 1:
                self.ids.atmosphere_livingroom_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
                self.ids.atmosphere_livingroom_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_livingroom_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
                self.ids.atmosphere_livingroom_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_livingroom_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
                self.ids.atmosphere_livingroom_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_livingroom_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
                self.ids.atmosphere_livingroom_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_livingroom_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"
                self.ids.atmosphere_livingroom_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"

    #玄关氛围灯开关
    def on_atmosphere_vestibule_switch_selected(self):
        if self.profession_atmosphere_vestibule['switch'] == 0:
            self.profession_atmosphere_vestibule['switch'] = 1
            self.ids.atmosphere_vestibule_switch_button.background_normal = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_vestibule_switch_button.background_down = "data/icons/profession/atmosphere/on.jpg"
            self.ids.atmosphere_vestibule_switch_button.canvas.before.clear()
            with self.ids.atmosphere_vestibule_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/vestibule_background_on.jpg')
            self.ids.atmosphere_vestibule_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"

            self.ids.atmosphere_vestibule_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_vestibule_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5.jpg"
        else:
            self.profession_atmosphere_vestibule['switch'] = 0
            self.ids.atmosphere_vestibule_switch_button.background_normal = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_vestibule_switch_button.background_down = "data/icons/profession/atmosphere/off.jpg"
            self.ids.atmosphere_vestibule_FloatLayout.canvas.before.clear()
            with self.ids.atmosphere_vestibule_FloatLayout.canvas.before:
                Rectangle(size=(self.width * 0.7, self.height * 0.74473684210526315789473684210526),
                          pos=(self.width * 0.15, self.height * 0.02894736842105263157894736842105),
                          source='data/icons/profession/atmosphere/vestibule_background_off.jpg')
            self.ids.atmosphere_vestibule_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch_disable.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch_disable.jpg"

            self.ids.atmosphere_vestibule_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_vestibule_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1_off.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2_off.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3_off.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4_off.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5_off.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5_off.jpg"

    #玄关氛围灯亮度调节
    def on_atmosphere_vestibule_level_selected(self, *args):
        if self.profession_atmosphere_vestibule['switch'] == 1:
            self.ids.atmosphere_vestibule_level_1_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_1_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_2_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_3_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_normal = \
                "data/icons/profession/floor_heating/switch.jpg"
            self.ids.atmosphere_vestibule_level_4_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_normal = \
                "data/icons/profession/atmosphere/switch.jpg"
            self.ids.atmosphere_vestibule_level_5_button.background_down = \
                "data/icons/profession/atmosphere/switch.jpg"
            if args[0] == 1:
                self.ids.atmosphere_vestibule_level_1_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_vestibule_level_1_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_vestibule_level_2_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_vestibule_level_2_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_vestibule_level_3_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_vestibule_level_3_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_vestibule_level_4_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_vestibule_level_4_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_vestibule_level_5_button.background_normal = \
                    "data/icons/profession/atmosphere/switch_h.jpg"
                self.ids.atmosphere_vestibule_level_5_button.background_down = \
                    "data/icons/profession/atmosphere/switch_h.jpg"

    #玄关氛围灯颜色调节
    def on_atmosphere_vestibule_color_selected(self, *args):
        if self.profession_atmosphere_vestibule['switch'] == 'on':
            self.ids.atmosphere_vestibule_color_1_button.background_normal = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_vestibule_color_1_button.background_down = \
                "data/icons/profession/atmosphere/color_1.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_normal = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_vestibule_color_2_button.background_down = \
                "data/icons/profession/atmosphere/color_2.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_normal = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_vestibule_color_3_button.background_down = \
                "data/icons/profession/atmosphere/color_3.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_normal = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_vestibule_color_4_button.background_down = \
                "data/icons/profession/atmosphere/color_4.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_normal = \
                "data/icons/profession/atmosphere/color_5.jpg"
            self.ids.atmosphere_vestibule_color_5_button.background_down = \
                "data/icons/profession/atmosphere/color_5.jpg"
            if args[0] == 1:
                self.ids.atmosphere_vestibule_color_1_button.background_normal = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
                self.ids.atmosphere_vestibule_color_1_button.background_down = \
                    "data/icons/profession/atmosphere/color_1_on.jpg"
            elif args[0] == 2:
                self.ids.atmosphere_vestibule_color_2_button.background_normal = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
                self.ids.atmosphere_vestibule_color_2_button.background_down = \
                    "data/icons/profession/atmosphere/color_2_on.jpg"
            elif args[0] == 3:
                self.ids.atmosphere_vestibule_color_3_button.background_normal = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
                self.ids.atmosphere_vestibule_color_3_button.background_down = \
                    "data/icons/profession/atmosphere/color_3_on.jpg"
            elif args[0] == 4:
                self.ids.atmosphere_vestibule_color_4_button.background_normal = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
                self.ids.atmosphere_vestibule_color_4_button.background_down = \
                    "data/icons/profession/atmosphere/color_4_on.jpg"
            elif args[0] == 5:
                self.ids.atmosphere_vestibule_color_5_button.background_normal = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"
                self.ids.atmosphere_vestibule_color_5_button.background_down = \
                    "data/icons/profession/atmosphere/color_5_on.jpg"

    #浴室氛围灯开关
    def on_atmosphere_bashroom_switch_selected(self):
        if self.profession_atmosphere_bashroom['switch'] == 'off':
            self.api.set_group_light_switch_on('bashroom')
        else:
            self.api.set_group_light_off('bashroom')

    #浴室氛围灯亮度调节
    def on_atmosphere_bashroom_level_selected(self, *args):
        if self.profession_atmosphere_bashroom['switch'] == 'on':
            if args[0] == 1:
                self.api.set_light_brightness('bashroom', 'LEVEL_ONE')
            elif args[0] == 2:
                self.api.set_light_brightness('bashroom', 'LEVEL_TWO')
            elif args[0] == 3:
                self.api.set_light_brightness('bashroom', 'LEVEL_THREE')
            elif args[0] == 4:
                self.api.set_light_brightness('bashroom', 'LEVEL_FOUR')
            elif args[0] == 5:
                self.api.set_light_brightness('bashroom', 'LEVEL_FIVE')

    #浴室氛围灯颜色调节
    def on_atmosphere_bashroom_color_selected(self, *args):
        if self.profession_atmosphere_bashroom['switch'] == 'on':
            if args[0] == 1:
                self.api.set_light_color('bashroom', 'WHITE')
            elif args[0] == 2:
                self.api.set_light_color('bashroom', 'YELLOW')
            elif args[0] == 3:
                self.api.set_light_color('bashroom', 'PINK')
            elif args[0] == 4:
                self.api.set_light_color('bashroom', 'BLUE')
            elif args[0] == 5:
                self.api.set_light_color('bashroom', 'GREEN')

    #窗帘
    def on_cover_left_action_button(self):
        if self.profession_cover_left['action'] == 0:
            self.profession_cover_left['action'] = 1
            self.ids.cover_left_action_button.background_normal = \
                "data/icons/profession/cover/action.jpg"
            self.ids.cover_left_action_button.background_down = \
                "data/icons/profession/cover/action.jpg"
        else:
            self.profession_cover_left['action'] = 0
            self.ids.cover_left_action_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_left_action_button.background_down = \
                "data/icons/profession/cover/switch.jpg"

    def on_cover_left_move_button(self, *args):
        if args[0] == 1:
            #升起
            self.api.set_cover_open('left_cover')
            if self.profession_cover_right['action'] == 1:
                self.api.set_cover_open('right_cover')
            if self.profession_cover_bashroom['action'] == 1:
                self.api.set_cover_open('bashroom_cover')
        elif args[0] == 2:
            #停止
            self.api.set_cover_stop('left_cover')
            if self.profession_cover_right['action'] == 1:
                self.api.set_cover_stop('right_cover')
            if self.profession_cover_bashroom['action'] == 1:
                self.api.set_cover_stop('bashroom_cover')
        elif args[0] == 3:
            #下降
            self.api.set_cover_close('left_cover')
            if self.profession_cover_right['action'] == 1:
                self.api.set_cover_close('right_cover')
            if self.profession_cover_bashroom['action'] == 1:
                self.api.set_cover_close('bashroom_cover')

    def on_cover_left_postion_button(self, *args):
        self.ids.cover_left_postion_1_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_1_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_2_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_2_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_3_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_3_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_4_button.background_normal = \
            "data/icons/profession/floor_heating/switch.jpg"
        self.ids.cover_left_postion_4_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_5_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_left_postion_5_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        if args[0] == 1:
            self.ids.cover_left_postion_1_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_left_postion_1_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('left_cover', 'ONE')
        elif args[0] == 2:
            self.ids.cover_left_postion_2_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_left_postion_2_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('left_cover', 'TWO')
        elif args[0] == 3:
            self.ids.cover_left_postion_3_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_left_postion_3_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('left_cover', 'THREE')
        elif args[0] == 4:
            self.ids.cover_left_postion_4_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_left_postion_4_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('left_cover', 'FOUR')
        elif args[0] == 5:
            self.ids.cover_left_postion_5_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_left_postion_5_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('left_cover', 'FIVE')

    def on_cover_mid_action_button(self):
        if self.profession_cover_mid['action'] == 0:
            self.profession_cover_mid['action'] = 1
            self.ids.cover_mid_action_button.background_normal = \
                "data/icons/profession/cover/action.jpg"
            self.ids.cover_mid_action_button.background_down = \
                "data/icons/profession/cover/action.jpg"
        else:
            self.profession_cover_mid['action'] = 0
            self.ids.cover_mid_action_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_mid_action_button.background_down = \
                "data/icons/profession/cover/switch.jpg"

    def on_cover_mid_move_button(self, *args):
        if args[0] == 1:
            #升起
            self.api.set_cover_open('mid_cover')
            if self.profession_cover_left['action'] == 1:
                self.api.set_cover_open('left_cover')
            if self.profession_cover_bashroom['action'] == 1:
                self.api.set_cover_open('bashroom_cover')
        elif args[0] == 2:
            #停止
            self.api.set_cover_stop('mid_cover')
            if self.profession_cover_left['action'] == 1:
                self.api.set_cover_stop('left_cover')
            if self.profession_cover_bashroom['action'] == 1:
                self.api.set_cover_stop('bashroom_cover')
        elif args[0] == 3:
            #下降
            self.api.set_cover_close('mid_cover')
            if self.profession_cover_left['action'] == 1:
                self.api.set_cover_close('left_cover')
            if self.profession_cover_bashroom['action'] == 1:
                self.api.set_cover_close('bashroom_cover')

    def on_cover_mid_postion_button(self, *args):
        self.ids.cover_mid_postion_1_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_1_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_2_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_2_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_3_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_3_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_4_button.background_normal = \
            "data/icons/profession/floor_heating/switch.jpg"
        self.ids.cover_mid_postion_4_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_5_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_mid_postion_5_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        if args[0] == 1:
            self.ids.cover_mid_postion_1_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_mid_postion_1_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('mid_cover', 'ONE')
        elif args[0] == 2:
            self.ids.cover_mid_postion_2_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_mid_postion_2_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('mid_cover', 'TWO')
        elif args[0] == 3:
            self.ids.cover_mid_postion_3_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_mid_postion_3_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('mid_cover', 'THREE')
        elif args[0] == 4:
            self.ids.cover_mid_postion_4_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_mid_postion_4_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('mid_cover', 'FOUR')
        elif args[0] == 5:
            self.ids.cover_mid_postion_5_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_mid_postion_5_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('mid_cover', 'FIVE')

    def on_cover_right_action_button(self):
        if self.profession_cover_right['action'] == 0:
            self.profession_cover_right['action'] = 1
            self.ids.cover_right_action_button.background_normal = \
                "data/icons/profession/cover/action.jpg"
            self.ids.cover_right_action_button.background_down = \
                "data/icons/profession/cover/action.jpg"
        else:
            self.profession_cover_right['action'] = 0
            self.ids.cover_right_action_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_right_action_button.background_down = \
                "data/icons/profession/cover/switch.jpg"

    def on_cover_right_move_button(self, *args):
        if args[0] == 1:
            #升起
            self.api.set_cover_open('right_cover')
            if self.profession_cover_left['action'] == 1:
                self.api.set_cover_open('left_cover')
            if self.profession_cover_bashroom['action'] == 1:
                self.api.set_cover_open('bashroom_cover')
        elif args[0] == 2:
            #停止
            self.api.set_cover_stop('right_cover')
            if self.profession_cover_left['action'] == 1:
                self.api.set_cover_stop('left_cover')
            if self.profession_cover_bashroom['action'] == 1:
                self.api.set_cover_stop('bashroom_cover')
        elif args[0] == 3:
            #下降
            self.api.set_cover_close('right_cover')
            if self.profession_cover_left['action'] == 1:
                self.api.set_cover_close('left_cover')
            if self.profession_cover_bashroom['action'] == 1:
                self.api.set_cover_close('bashroom_cover')

    def on_cover_right_postion_button(self, *args):
        self.ids.cover_right_postion_1_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_1_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_2_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_2_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_3_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_3_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_4_button.background_normal = \
            "data/icons/profession/floor_heating/switch.jpg"
        self.ids.cover_right_postion_4_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_5_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_right_postion_5_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        if args[0] == 1:
            self.ids.cover_right_postion_1_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_right_postion_1_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('right_cover', 'ONE')
        elif args[0] == 2:
            self.ids.cover_right_postion_2_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_right_postion_2_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('right_cover', 'TWO')
        elif args[0] == 3:
            self.ids.cover_right_postion_3_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_right_postion_3_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('right_cover', 'THREE')
        elif args[0] == 4:
            self.ids.cover_right_postion_4_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_right_postion_4_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('right_cover', 'FOUR')
        elif args[0] == 5:
            self.ids.cover_right_postion_5_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_right_postion_5_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('right_cover', 'FIVE')

    def on_cover_bashroom_action_button(self):
        if self.profession_cover_bashroom['action'] == 0:
            self.profession_cover_bashroom['action'] = 1
            self.ids.cover_bashroom_action_button.background_normal = \
                "data/icons/profession/cover/action.jpg"
            self.ids.cover_bashroom_action_button.background_down = \
                "data/icons/profession/cover/action.jpg"
        else:
            self.profession_cover_bashroom['action'] = 0
            self.ids.cover_bashroom_action_button.background_normal = \
                "data/icons/profession/cover/switch.jpg"
            self.ids.cover_bashroom_action_button.background_down = \
                "data/icons/profession/cover/switch.jpg"

    def on_cover_bashroom_move_button(self, *args):
        if args[0] == 1:
            #升起
            self.api.set_cover_open('bashroom_cover')
            if self.profession_cover_left['action'] == 1:
                self.api.set_cover_open('left_cover')
            if self.profession_cover_right['action'] == 1:
                self.api.set_cover_open('right_cover')
        elif args[0] == 2:
            #停止
            self.api.set_cover_stop('bashroom_cover')
            if self.profession_cover_left['action'] == 1:
                self.api.set_cover_stop('left_cover')
            if self.profession_cover_right['action'] == 1:
                self.api.set_cover_stop('right_cover')
        elif args[0] == 3:
            #下降
            self.api.set_cover_close('bashroom_cover')
            if self.profession_cover_left['action'] == 1:
                self.api.set_cover_close('left_cover')
            if self.profession_cover_right['action'] == 1:
                self.api.set_cover_close('right_cover')

    def on_cover_bashroom_postion_button(self, *args):
        self.ids.cover_bashroom_postion_1_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_1_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_2_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_2_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_3_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_3_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_4_button.background_normal = \
            "data/icons/profession/floor_heating/switch.jpg"
        self.ids.cover_bashroom_postion_4_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_5_button.background_normal = \
            "data/icons/profession/cover/switch.jpg"
        self.ids.cover_bashroom_postion_5_button.background_down = \
            "data/icons/profession/cover/switch.jpg"
        if args[0] == 1:
            self.ids.cover_bashroom_postion_1_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_bashroom_postion_1_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('bashroom_cover', 'ONE')
        elif args[0] == 2:
            self.ids.cover_bashroom_postion_2_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_bashroom_postion_2_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('bashroom_cover', 'TWO')
        elif args[0] == 3:
            self.ids.cover_bashroom_postion_3_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_bashroom_postion_3_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('bashroom_cover', 'THREE')
        elif args[0] == 4:
            self.ids.cover_bashroom_postion_4_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_bashroom_postion_4_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('bashroom_cover', 'FOUR')
        elif args[0] == 5:
            self.ids.cover_bashroom_postion_5_button.background_normal = \
                "data/icons/profession/cover/switch_h.jpg"
            self.ids.cover_bashroom_postion_5_button.background_down = \
                "data/icons/profession/cover/switch_h.jpg"
            self.api.set_cover_position('bashroom_cover', 'FIVE')
