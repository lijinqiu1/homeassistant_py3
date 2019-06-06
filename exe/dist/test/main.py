# -*-coding:utf-8-*-
import kivy
kivy.resources.resource_add_path('data/font/')
font = kivy.resources.resource_find('simhei.ttf')
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.clock import Clock
from RsetAPI import RsetAPI
Builder.load_file('data/screens/main.kv')

kivy.resources.resource_add_path("data/font")
simhei = kivy.resources.resource_find("simhei.ttf")
adobehtr = kivy.resources.resource_find("AdobeHeitiStd-Regular.otf")


class MainFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MainFloatLayout, self).__init__(**kwargs)
        Clock.schedule_interval(self._update_clock, 10.)
        self.api = RsetAPI()
        self.temp = 25
        self.hum_level = 'COMFORTABLE'
        self.hum = 0
        self.pm2_5_level = 'good'
        self.pm2_5 = 0
        temp = self.api.get_temp()
        if temp != u'unknown':
            self.temp = int(float(str(temp)))
            self.ids.main_label_temperature.font_name = adobehtr
            self.ids.main_label_temperature.text = '[color=#6E6E6E]'+str(self.temp)+'[/color]'
        self.ids.main_label_pm.font_name = adobehtr
        self.ids.main_label_pm.text = '[color=#6E6E6E]'+'优'+'[/color]'

        self.ids.main_label_water.font_name = adobehtr
        self.ids.main_label_water.text = '[color=#6E6E6E]' + '优' + '[/color]'

        self.ids.main_label_hum.font_name = adobehtr
        self.ids.main_label_hum.text = '[color=#6E6E6E]' + '舒适' + '[/color]'

    def set_temp(self, temp):
        self.temp = temp

    def set_hum(self, hum, hum_level):
        self.hum = hum
        self.hum_level = hum_level

    def set_pm2_5(self, pm2_5, pm2_5_level):
        self.pm2_5 = pm2_5
        self.pm2_5_level = pm2_5_level

    def _update_clock(self, dt):
        self.ids.main_label_temperature.text = '[color=#6E6E6E]'+str(self.temp)+'[/color]'
        if self.hum_level == 'COMFORTABLE':
            self.ids.main_label_hum.font_name = adobehtr
            self.ids.main_label_hum.text = '[color=#6E6E6E]' + '舒适' + '[/color]'
        elif self.hum_level == 'DAMP':
            self.ids.main_label_hum.font_name = adobehtr
            self.ids.main_label_hum.text = '[color=#6E6E6E]' + '潮湿' + '[/color]'
        elif self.hum_level == 'DRY':
            self.ids.main_label_hum.font_name = adobehtr
            self.ids.main_label_hum.text = '[color=#6E6E6E]' + '干燥' + '[/color]'
        if self.pm2_5_level == 'FINE':
            self.ids.main_label_hum.font_name = adobehtr
            self.ids.main_label_hum.text = '[color=#6E6E6E]' + '优' + '[/color]'
        elif self.pm2_5_level == 'GOOD':
            self.ids.main_label_hum.font_name = adobehtr
            self.ids.main_label_hum.text = '[color=#6E6E6E]' + '良' + '[/color]'
        elif self.pm2_5_level == 'NORMAL':
            self.ids.main_label_hum.font_name = adobehtr
            self.ids.main_label_hum.text = '[color=#6E6E6E]' + '一般' + '[/color]'
        elif self.pm2_5_level == 'BAD':
            self.ids.main_label_hum.font_name = adobehtr
            self.ids.main_label_hum.text = '[color=#6E6E6E]' + '恶劣' + '[/color]'

    def on_easy_screen(self, *l):
        pass

