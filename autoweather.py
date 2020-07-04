# Filename: autoweather.py
# Function：自动获取天气预报信息
import re
import datetime

import requests

# 城市代码参考https://gitee.com/wangjins/weather_api/edit/master/city.json
TIANQI_API = 'https://www.tianqiapi.com/api?version=v1&cityid=你的城市代码&appid=你的APPID&appsecret=你的APPSECRET'
now_time = datetime.datetime.today()

response = requests.get(TIANQI_API)
data = response.json()
update_time = data.get('update_time')
city = data.get('city')

pattern = re.compile(r'(.*)日(.*)时')

now_data = data.get('data')[0].get('hours')
weather_str = ''

for weather_data in now_data:
    day = weather_data.get('day')
    wea = weather_data.get('wea')
    tem = weather_data.get('tem')
    win = weather_data.get('win')
    win_speed = weather_data.get('win_speed')
    day_list = re.findall(pattern, day)
    day_data = int(day_list[0][0])
    hour_data = int(day_list[0][1])
    data_datetime = now_time.replace(day=day_data, hour=hour_data, minute=0)
    if data_datetime > now_time:
        weather_str += '|%s|%s|%s|%s %s|\n' % (
            day,
            wea,
            tem,
            win,
            win_speed,
        )

return_str = '- 现在时间：%s 天气数据更新时间：%s\n\n' \
             '| 日期     | 天气 | 温度 | 风向       |\n' \
             '| -------- | ---- | ---- | ---------- |\n' \
             '%s\n' % (now_time, update_time, weather_str)
print(return_str)
# result:
#
# - 现在时间：2020-07-04 16:54:18.193432 数据更新时间：2020-07-04 16:16:57
#
# | 日期     | 天气 | 温度 | 风向       |
# | -------- | ---- | ---- | ---------- |
# |04日17时|中雨|26℃|东南风 <3级|
# |04日20时|中雨|25℃|东南风 <3级|
# |04日23时|中雨|24℃|东南风 <3级|
# |05日02时|小雨|24℃|东南风 <3级|
# |05日05时|大雨|23℃|东南风 <3级|
