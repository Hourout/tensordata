# -*- coding: utf-8 -*- 
import requests
import pandas as pd

__all__ = ['real_time', 'real_time_share', 'real_time_index', 
           'info_city', 'info_weather',
           'feature_time', 'feature_time_index']

def _get_tianqi_api(city):
    assert isinstance(city, str), "`city` should be str."
    return requests.get('https://www.tianqiapi.com/api/?version=v1&city='+city).json()

def real_time_share(city):
    a = _get_tianqi_api(city)
    for i in a['data']:
        if i['date']==str(pd.to_datetime(pd.datetime.now()))[:10]:
            break    
    s = pd.DataFrame(i['hours']).rename(columns={'day':'分时', 'tem':'温度', 'wea':'天气', 'win':'风向', 'win_speed':'风力'})
    s['更新时间'] = a['update_time']
    return s

def real_time(city):
    a = _get_tianqi_api(city)
    for i in a['data']:
        if i['date']==str(pd.to_datetime(pd.datetime.now()))[:10]:
            break
    s = {j:[i[j]] for j in ['date', 'tem', 'tem1', 'tem2', 'wea', 'week', 'win', 'win_speed', 'air', 'air_level']}
    s['city'] = [city]
    s = pd.DataFrame(s).reindex(
        columns=['city', 'date', 'air', 'air_level', 'tem', 'tem1', 'tem2', 'wea', 'week', 'win', 'win_speed']).rename(
        columns={'date':'日期', 'tem':'温度', 'wea':'天气', 'win':'风向',
                 'win_speed':'风力', 'air':'空气质量指数', 'air_level':'空气质量等级',
                 'tem1':'最高温度', 'tem2':'最低温度', 'week':'星期', 'city':'城市'})
    s['更新时间'] = a['update_time']
    return s

def real_time_index(city):
    a = _get_tianqi_api(city)
    for i in a['data']:
        if i['date']==str(pd.to_datetime(pd.datetime.now()))[:10]:
            break
    s = {'指数':['空气质量指数', '紫外线指数', '运动指数', '血糖指数', '穿衣指数', '洗车指数', '空气污染扩散指数']}
    s['等级'] = [i['air_level']]+[j['level'] for j in i['index']]
    s['建议'] = [i['air_tips']]+[j['desc'] for j in i['index']]
    s = pd.DataFrame(s).reindex(columns=['指数', '等级', '建议'])
    return s

def info_city():
    return pd.DataFrame(requests.get('https://cdn.huyahaha.com/tianqiapi/city.json').json())

def info_weather():
    return ["晴","阴","多云","雨夹雪","小雨","中雨","阵雨","小雪","中雪","大雪","大雨","雾",
            "暴雨","雷阵雨","阵雪","暴雪","扬沙","大暴雨","霾","浮尘","晴转多云","小雪转晴",
            "多云转晴","多云转阴","晴转阴","阴转多云","多云转小雪","阵雪转晴","晴转阵雪",
            "小雪转多云","小雨转多云","晴转小雪","多云转雨夹雪","多云转阵雪","阵雨转多云",
            "多云转小雨","多云转阵雨","阵雪转小雪","阴转小雪","小雪转阴","阵雪转多云",
            "阴转晴","阴转阵雪","阵雪转阴","扬沙转多云","扬沙转晴","浮尘转晴","晴转雨夹雪",
            "多云转中雪","晴转中雪","阴转小雨","小雨转中雨","小雨转阴","中雨转多云",
            "中雨转小雨","阴转中雨","多云转中雨","小雨转大雨","阵雨转中雨","阵雨转大雨",
            "阴转大雨","雾转多云","阵雨转小雨","中雨转阴","晴转小雨","多云转大雨",
            "小雨转暴雨","阵雨转晴","小雨转晴","阵雨转中到大雨","小雨转阵雨","阵雨转阴",
            "雨夹雪转晴","雨夹雪转多云","小雨转小雪","小雪转雨夹雪","阴转阵雨",
            "小雨转小到中雨","小到中雨转小雨","小到中雨转阴","晴转阵雨","中雨转阵雨",
            "阵雨转雷阵雨","多云转大雪","阴转中雪","阴转大雪","雨夹雪转阴","雨夹雪转小雪",
            "小雨转大雪","雨夹雪转大雪","雨夹雪转中雪","中雨转小雪","中雨转中雪","晴转大雪",
            "小雨转雨夹雪","阴转雨夹雪","多云转雾","小雪转阵雪","小雪转中雪","多云转小到中雪",
            "中雪转多云","中雪转小雪","大雪转小雪","中雨转大雨","阵雨转雨夹雪","多云转小到中雨",
            "小到中雨","小到中雨转阵雨","小雨转阵雪","雷阵雨转多云","雷阵雨转阵雨","多云转扬沙",
            "晴转扬沙","扬沙转阴","浮尘转霾","晴转霾","霾转阴","霾转多云","霾转晴","小到中雪转多云",
            "大雪转多云","雨夹雪转小雨","大雨转阴","浮尘转多云","多云转霾","晴转雾","小雨转中雪",
            "阵雨转小雪","晴转雷阵雨","阴转雾"]

def feature_time(city):
    a = _get_tianqi_api(city)
    s = {}
    name = ['日期', '温度', '最高温度', '最低温度', '天气', '风向', '风力', '星期']
    name_en = ['date', 'tem', 'tem1', 'tem2', 'wea', 'win', 'win_speed', 'week']
    for i, j in zip(name, name_en):
        s[i] = [k[j] for k in a['data']]
    s = pd.DataFrame(s).reindex(columns=name)
    s['更新时间'] = a['update_time']
    return s

def feature_time_index(city):
    a = _get_tianqi_api(city)
    s = {}
    s['日期'] = [i['date'] for i in a['data']]
    name = ['紫外线指数', '运动指数', '血糖指数', '穿衣指数', '洗车指数', '空气污染扩散指数']
    for i, j in enumerate(name):
        s[j] = [k['index'][i]['level'] for k in a['data']]
    s = pd.DataFrame(s).drop(['运动指数'], axis=1)
    s['更新时间'] = a['update_time']
    return s
