import requests
import pandas as pd

__all__ = ['china_id_card', 'china_mobie']

def _get_id_card(card):
    return requests.get("https://www.fesugar.com/get_identitycards?id="+card).json()

def _get_mobie(mobile):
    return requests.get("http://mobsec-dianhua.baidu.com/dianhua_api/open/location?tel="+mobile).json()

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
