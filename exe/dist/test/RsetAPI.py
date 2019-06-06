from requests import get
from requests import post
import json
import time


class RsetAPI():
    def __init__(self):
        self.url = 'http://guoxi.mynatapp.cc/api/'
        self.headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTA2NzIzOTAsImlzcyI6ImVmYmU5YWFhMWZlYzQ4YTNhOGVkZTNjNTU2YWE4MTU1IiwiZXhwIjoxODY2MDMyMzkwfQ.GlA1Qb0LmIWqSvkTSgv_7bUyMxq5IfU1kPR9PBBCb5Y',
            'content-type': 'application/json'
        }

    def get_light_state(self, arg):
        response = get(self.url+'states/light.'+arg, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def get_switch_state(self, arg):
        response = get(self.url+'states/switch.'+arg, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def get_group_switch_state(self, arg):
        response = get(self.url+'states/group.'+arg, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def set_switch_on(self, arg):
        body = {"entity_id": "switch." + arg}
        response = post(self.url + 'services/switch/turn_on', data=json.dumps(body), headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def set_switch_off(self, arg):
        body = {"entity_id": "switch." + arg}
        response = post(self.url + 'services/switch/turn_off', data=json.dumps(body), headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def set_group_switch_on(self, arg):
        body = {"entity_id": "group." + arg}
        try:
            response = post(self.url + 'services/switch/turn_on', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def set_group_switch_off(self, arg):
        body = {"entity_id": "group." + arg}
        try:
            response = post(self.url + 'services/switch/turn_off', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def set_light_on(self, light, brightness, rgb_color):
        body = {"entity_id": "light." + light, "brightness": brightness, "rgb_color": rgb_color}
        response = post(self.url + 'services/light/turn_on', data=json.dumps(body), headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def set_light_off(self, light):
        body = {"entity_id": "light." + light}
        response = post(self.url + 'services/light/turn_off', data=json.dumps(body), headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def set_cover_open(self, cover):
        body = {"entity_id": "cover." + cover}
        try:
            response = post(self.url + 'services/cover/open_cover', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def set_cover_close(self, cover):
        body = {"entity_id": "cover." + cover}
        try:
            response = post(self.url + 'services/cover/close_cover', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def set_cover_stop(self, cover):
        body = {"entity_id": "cover." + cover}
        try:
            response = post(self.url + 'services/cover/stop_cover', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def set_cover_position(self, cover, position):
        body = {"entity_id": "input_select." + cover + '_position_setting', 'option': position}
        try:
            response = post(self.url + 'services/input_select/select_option', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def get_cover_position(self, cover):
        response = get(self.url + 'states/input_select.'+cover + '_position', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def get_temp(self):
        try:
            response = get(self.url + 'states/sensor.wen_du', headers=self.headers, timeout=2)
            if response.status_code == 200:
                return json.loads(response.text)['state']
            else:
                return u'unknown'
        except:
            return u'unknown'

    def get_hum(self):
        response = get(self.url + 'states/sensor.shi_du', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def get_PM25(self):
        response = get(self.url + 'states/sensor.pm2_5', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def get_jia_quan(self):
        response = get(self.url + 'states/sensor.jia_quan', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def get_liangdu(self,index):
        response = get(self.url + 'states/sensor.liang_du_' + index, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def get_PM25_level(self):
        response = get(self.url + 'states/input_select.pm2_5_level', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def get_hum_level(self):
        response = get(self.url + 'states/input_select.hum_level', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def set_group_light_on(self, light, brightness, rgb_color):
        body = {"entity_id": "light." + light + '_color_lights',
                "brightness": brightness,
                "rgb_color": rgb_color}
        response = post(self.url + 'services/light/turn_on', data=json.dumps(body), headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def set_group_light_switch_on(self, light):
        body = {"entity_id": "light." + light + '_color_lights'}
        try:
            response = post(self.url + 'services/light/turn_on', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def set_group_light_brightness(self, light, brightness):
        body = {"entity_id": "light." + light + '_color_lights',
                "brightness": brightness}
        response = post(self.url + 'services/light/turn_on', data=json.dumps(body), headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def set_group_light_color(self, light, rgb_color):
        body = {"entity_id": "light." + light + '_color_lights',
                "rgb_color": rgb_color}
        response = post(self.url + 'services/light/turn_on', data=json.dumps(body), headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def set_group_light_off(self, light):
        body = {"entity_id": "light." + light + '_color_lights'}
        try:
            response = post(self.url + 'services/light/turn_off', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def get_group_light_state(self, light):
        response = get(self.url + 'states/light.' + light + '_color_lights', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return False

    def get_light_color(self, light):
        response = get(self.url + 'states/input_select.' + light + '_color_light_rgb_setting', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return False

    def get_light_brightness(self, light):
        response = get(self.url + 'states/input_select.' + light + '_color_light_brightness_setting', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return False

    def set_light_color(self, light, arg):
        body = {"entity_id": "input_select." + light + '_color_light_rgb_setting', 'option': arg}
        try:
            response = post(self.url + 'services/input_select/select_option', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def set_light_brightness(self, light, arg):
        body = {"entity_id": "input_select." + light + '_color_light_brightness_setting', 'option': arg}
        try:
            response = post(self.url + 'services/input_select/select_option', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def get_environment_state(self):
        response = get(self.url + 'states/group.environment_setting', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None

    def get_ac_mode(self):
        response = get(self.url + 'states/input_select.ac_setting', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def set_ac_mode(self, arg):
        body = {"entity_id": "input_select.ac_setting", 'option': arg}
        try:
            response = post(self.url + 'services/input_select/select_option', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def get_ac_swing(self):
        response = get(self.url + 'states/input_select.swing_setting', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def set_ac_swing(self, arg):
        body = {"entity_id": "input_select.swing_setting", 'option': arg}
        response = post(self.url + 'services/input_select/select_option', data=json.dumps(body), headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def get_ac_fan(self):
        response = get(self.url + 'states/input_select.fan_setting', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['state']
        else:
            return None

    def set_ac_fan(self, arg):
        body = {"entity_id": "input_select.fan_setting", 'option': arg}
        response = post(self.url + 'services/input_select/select_option', data=json.dumps(body), headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def get_ac_temp(self):
        response = get(self.url + 'states/input_number.air_conditioner_temp', headers=self.headers)
        if response.status_code == 200:
            temp = json.loads(response.text)['state']
            return int(float(temp.encode("utf-8")))
        else:
            return None

    def set_ac_temp(self, arg):
        body = {"entity_id": "input_number.air_conditioner_temp", 'value': arg}
        try:
            response = post(self.url + 'services/input_number/set_value', data=json.dumps(body), headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def set_home_mode(self, arg):
        body = {"entity_id": "input_select.home_mode_setting", 'option': arg}
        response = post(self.url + 'services/input_select/select_option', data=json.dumps(body), headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def get_all_state(self):
        response = get(self.url + 'states', headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return False


if __name__ == '__main__':
    now = lambda: time.time()
    api = RsetAPI()
    start = now()
    states = api.get_all_state()
    print('TIME: ', now() - start)
    for state in states:
        print(state)
    print('TIME: ', now() - start)
