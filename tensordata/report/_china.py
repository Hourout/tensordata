# -*- coding: utf-8 -*- 
import requests
import pandas as pd

__all__ = ['china_id_card', 'china_mobie', 'china_logistics']

company = {"申通":"shentong", "EMS":"ems", "顺丰":"shunfeng", "圆通":"yuantong",
           "中通":"zhongtong", "韵达":"yunda", "天天":"tiantian", "汇通":"huitongkuaidi",
           "全峰":"quanfengkuaidi", "德邦":"debangwuliu", "宅急送":"zhaijisong"}

def _get_id_card(card):
    return requests.get("https://www.fesugar.com/get_identitycards?id="+card).json()

def _get_mobie(mobile):
    return requests.get("http://mobsec-dianhua.baidu.com/dianhua_api/open/location?tel="+mobile).json()
              
def _get_logistics(com, card):
    return requests.get("http://www.kuaidi100.com/query?type="+company[com]+"&postid="+card).json()

def china_id_card(card):
    assert isinstance(card, str), "`card` should be str."
    s = _get_id_card(card)
    if 'code' in s:
        s = s['data']
        s['sex'] = '男' if s['sex']=='1' else '女'
        s['birth'] = str(pd.to_datetime(s['birth']))[:10]
    return s

def china_mobie(mobile):
    assert isinstance(mobile, str), "`mobile` should be str."
    s = _get_mobie(mobile)
    s = s['response']
    return s

def china_logistics(com, card):
    assert isinstance(com, str), "`com` should be str."
    assert isinstance(card, str), "`card` should be str."
    if com not in company:
        raise ValueError("`com` is error.")
    s = _get_logistics(com, card)
    if s['message']!='ok':
        s = s['message']
    else:
        s = pd.DataFrame(s['data'])
    return s
