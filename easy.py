# -*-coding:utf-8-*-
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from RsetAPI import RsetAPI
from kivy.clock import Clock
import kivy

# Builder.load_file('data/screens/easy.kv')
with open('data/screens/easy.kv', encoding='utf8') as f:
    Builder.load_string(f.read())
kivy.resources.resource_add_path("data/font")
simhei = kivy.resources.resource_find("simhei.ttf")
adobehtr = kivy.resources.resource_find("AdobeHeitiStd-Regular.otf")


class EasyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(EasyFloatLayout, self).__init__(**kwargs)
        self.api = RsetAPI()
        self.ids.sm_easy.current = 'screen_mode'
        self.screen_index = 0
        self.current_mode = 'day'
        self.current_cover = 'open'

        self.ids.button_mode_day.background_normal = 'data/icons/easy/day_h.jpg'
        self.ids.button_mode_day.background_down = 'data/icons/easy/day_h.jpg'

        self.ids.button_cover_open.background_normal = 'data/icons/easy/selected.jpg'
        self.ids.button_cover_open.background_down = 'data/icons/easy/selected.jpg'

        Clock.schedule_interval(self._update_clock, 10.)
        self.temp = 25
        self.hum_level = 'COMFORTABLE'
        self.hum = 0
        self.pm2_5_level = 'good'
        self.pm2_5 = 0
        temp = self.api.get_temp()
        if temp != u'unknown':
            temp = int(float(str(temp)))
            self.ids.easy_label_temperature.font_name = adobehtr
            self.ids.easy_label_temperature.text = '[color=#6E6E6E]'+str(temp)+'[/color]'
        self.ids.easy_label_pm.font_name = adobehtr
        self.ids.easy_label_pm.text = '[color=#6E6E6E]'+'优'+'[/color]'

        self.ids.easy_label_water.font_name = adobehtr
        self.ids.easy_label_water.text = '[color=#6E6E6E]' + '优' + '[/color]'

        self.ids.easy_label_hum.font_name = adobehtr
        self.ids.easy_label_hum.text = '[color=#6E6E6E]' + '舒适' + '[/color]'

    def set_temp(self, temp):
        self.temp = temp

    def set_hum(self, hum, hum_level):
        self.hum = hum
        self.hum_level = hum_level

    def set_pm2_5(self, pm2_5, pm2_5_level):
        self.pm2_5 = pm2_5
        self.pm2_5_level = pm2_5_level

    def _update_clock(self,dt):
        self.ids.easy_label_temperature.text = '[color=#6E6E6E]' + str(self.temp) + '[/color]'
        if self.hum_level == 'COMFORTABLE':
            self.ids.easy_label_hum.font_name = adobehtr
            self.ids.easy_label_hum.text = '[color=#6E6E6E]' + '舒适' + '[/color]'
        elif self.hum_level == 'DAMP':
            self.ids.easy_label_hum.font_name = adobehtr
            self.ids.easy_label_hum.text = '[color=#6E6E6E]' + '潮湿' + '[/color]'
        elif self.hum_level == 'DRY':
            self.ids.easy_label_hum.font_name = adobehtr
            self.ids.easy_label_hum.text = '[color=#6E6E6E]' + '干燥' + '[/color]'
        if self.pm2_5_level == 'FINE':
            self.ids.easy_label_hum.font_name = adobehtr
            self.ids.easy_label_hum.text = '[color=#6E6E6E]' + '优' + '[/color]'
        elif self.pm2_5_level == 'GOOD':
            self.ids.easy_label_hum.font_name = adobehtr
            self.ids.easy_label_hum.text = '[color=#6E6E6E]' + '良' + '[/color]'
        elif self.pm2_5_level == 'NORMAL':
            self.ids.easy_label_hum.font_name = adobehtr
            self.ids.easy_label_hum.text = '[color=#6E6E6E]' + '一般' + '[/color]'
        elif self.pm2_5_level == 'BAD':
            self.ids.easy_label_hum.font_name = adobehtr
            self.ids.easy_label_hum.text = '[color=#6E6E6E]' + '恶劣' + '[/color]'


    def on_main_screen(self):
        pass

    def go_previous_screen(self):
        self.ids.sm_easy.transition.direction = 'right'
        if self.screen_index == 0:
            self.ids.sm_easy.current = 'screen_cover'
            self.screen_index = 1
        else:
            self.ids.sm_easy.current = 'screen_mode'
            self.screen_index = 0

    def go_next_screen(self):
        self.ids.sm_easy.transition.direction = 'left'
        if self.screen_index == 0:
            self.ids.sm_easy.current = 'screen_cover'
            self.screen_index = 1
        else:
            self.ids.sm_easy.current = 'screen_mode'
            self.screen_index = 0

    def on_mode_day_selected(self):
        self.current_mode = 'day'
        self.ids.button_mode_day.background_normal = 'data/icons/easy/day_h.jpg'
        self.ids.button_mode_day.background_down = 'data/icons/easy/day_h.jpg'

        self.ids.button_mode_night.background_normal = 'data/icons/easy/night.jpg'
        self.ids.button_mode_night.background_down = 'data/icons/easy/night.jpg'

        self.ids.button_mode_sleep.background_normal = 'data/icons/easy/sleep.jpg'
        self.ids.button_mode_sleep.background_down = 'data/icons/easy/sleep.jpg'

        self.ids.button_mode_romantic.background_normal = 'data/icons/easy/romantic.jpg'
        self.ids.button_mode_romantic.background_down = 'data/icons/easy/romantic.jpg'

        self.api.set_home_mode('DAY')

    def on_mode_night_selected(self):
        self.current_mode = 'night'
        self.ids.button_mode_day.background_normal = 'data/icons/easy/day.jpg'
        self.ids.button_mode_day.background_down = 'data/icons/easy/day.jpg'

        self.ids.button_mode_night.background_normal = 'data/icons/easy/night_h.jpg'
        self.ids.button_mode_night.background_down = 'data/icons/easy/night_h.jpg'

        self.ids.button_mode_sleep.background_normal = 'data/icons/easy/sleep.jpg'
        self.ids.button_mode_sleep.background_down = 'data/icons/easy/sleep.jpg'

        self.ids.button_mode_romantic.background_normal = 'data/icons/easy/romantic.jpg'
        self.ids.button_mode_romantic.background_down = 'data/icons/easy/romantic.jpg'
        self.api.set_home_mode('NIGHT')

    def on_mode_sleep_selected(self):
        self.current_mode = 'sleep'
        self.ids.button_mode_day.background_normal = 'data/icons/easy/day.jpg'
        self.ids.button_mode_day.background_down = 'data/icons/easy/day.jpg'

        self.ids.button_mode_night.background_normal = 'data/icons/easy/night.jpg'
        self.ids.button_mode_night.background_down = 'data/icons/easy/night.jpg'

        self.ids.button_mode_sleep.background_normal = 'data/icons/easy/sleep_h.jpg'
        self.ids.button_mode_sleep.background_down = 'data/icons/easy/sleep_h.jpg'

        self.ids.button_mode_romantic.background_normal = 'data/icons/easy/romantic.jpg'
        self.ids.button_mode_romantic.background_down = 'data/icons/easy/romantic.jpg'
        self.api.set_home_mode('SLEEP')

    def on_mode_romantic_selected(self):
        self.current_mode = 'romantic'
        self.ids.button_mode_day.background_normal = 'data/icons/easy/day.jpg'
        self.ids.button_mode_day.background_down = 'data/icons/easy/day.jpg'

        self.ids.button_mode_night.background_normal = 'data/icons/easy/night.jpg'
        self.ids.button_mode_night.background_down = 'data/icons/easy/night.jpg'

        self.ids.button_mode_sleep.background_normal = 'data/icons/easy/sleep.jpg'
        self.ids.button_mode_sleep.background_down = 'data/icons/easy/sleep.jpg'

        self.ids.button_mode_romantic.background_normal = 'data/icons/easy/romantic_h.jpg'
        self.ids.button_mode_romantic.background_down = 'data/icons/easy/romantic_h.jpg'
        self.api.set_home_mode('ROMANTIC')

    def on_cover_open_selected(self):
        self.current_cover = 'open'
        self.ids.button_cover_open.background_normal = 'data/icons/easy/selected.jpg'
        self.ids.button_cover_open.background_down = 'data/icons/easy/selected.jpg'

        self.ids.button_cover_half.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_half.background_down = 'data/icons/easy/select.jpg'

        self.ids.button_cover_close.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_close.background_down = 'data/icons/easy/select.jpg'

        self.api.set_cover_position('left_cover', 'ONE')
        self.api.set_cover_position('right_cover', 'ONE')
        self.api.set_cover_position('bashroom_cover', 'ONE')

    def on_cover_half_selected(self):
        self.current_cover = 'half'
        self.ids.button_cover_open.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_open.background_down = 'data/icons/easy/select.jpg'

        self.ids.button_cover_half.background_normal = 'data/icons/easy/selected.jpg'
        self.ids.button_cover_half.background_down = 'data/icons/easy/selected.jpg'

        self.ids.button_cover_close.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_close.background_down = 'data/icons/easy/select.jpg'

        self.api.set_cover_position('left_cover', 'THREE')
        self.api.set_cover_position('right_cover', 'THREE')
        self.api.set_cover_position('bashroom_cover', 'THREE')

    def on_cover_close_selected(self):
        self.current_cover = 'close'
        self.ids.button_cover_open.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_open.background_down = 'data/icons/easy/select.jpg'

        self.ids.button_cover_half.background_normal = 'data/icons/easy/select.jpg'
        self.ids.button_cover_half.background_down = 'data/icons/easy/select.jpg'

        self.ids.button_cover_close.background_normal = 'data/icons/easy/selected.jpg'
        self.ids.button_cover_close.background_down = 'data/icons/easy/selected.jpg'

        self.api.set_cover_position('left_cover', 'FIVE')
        self.api.set_cover_position('right_cover', 'FIVE')
        self.api.set_cover_position('bashroom_cover', 'FIVE')

