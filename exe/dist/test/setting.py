#coding=utf-8

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics import Rectangle
from kivy.clock import Clock
from RsetAPI import RsetAPI
Builder.load_file('data/screens/setting.kv')


class SettingFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(SettingFloatLayout, self).__init__(**kwargs)
        self.setting_environment_switch = 0
        self.setting_power_switch = 0

    def environment_switch_pressed(self):
        if self.setting_environment_switch == 0:
            self.setting_environment_switch = 1
            self.ids.environment_switch.background_normal= "data/icons/setting/on.png"
            self.ids.environment_switch.background_down= "data/icons/setting/on.png"
        else:
            self.setting_environment_switch = 0
            self.ids.environment_switch.background_normal= "data/icons/setting/off.png"
            self.ids.environment_switch.background_down= "data/icons/setting/off.png"

    def power_switch_pressed(self):
        if self.setting_power_switch == 0:
            self.setting_power_switch = 1
            self.ids.power_switch.background_normal= "data/icons/setting/on.png"
            self.ids.power_switch.background_down= "data/icons/setting/on.png"
        else:
            self.setting_power_switch = 0
            self.ids.power_switch.background_normal= "data/icons/setting/off.png"
            self.ids.power_switch.background_down= "data/icons/setting/off.png"