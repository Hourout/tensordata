# -*- coding: utf-8 -*-
import io
import time
import requests
import pandas as pd

__all__ =['rating', 'problem_platform']

def rating(date=None):
    """P2peye comprehensive rating and display results.
    
    from https://www.p2peye.com
    
    Args:
        date: if None, download latest data, if like '201812', that download month data.
    Returns:
        DataFrame
    """
    start = time.time()
    if date is None:
        date = str(pd.to_datetime(pd.datetime.now())-pd.DateOffset(months=1))[:7].replace('-', '')
    assert (isinstance(date, str) and len(date)==6), "`date` shoule format '201812' or None"
    url_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/report/p2peye/rating/p2peye_rating'+date+'.txt'
    s = requests.get(url_txt).content
    data = pd.read_csv(io.StringIO(s.decode('utf-8')))
    print('p2peye rating dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return data

def problem_platform(date=None, days=7):
    """P2peye problem platform and display results.
    
    from https://www.p2peye.com
    
    Args:
        date: if None, download latest data, if like '2018-12-01', that download month data.
        days: latest (date-days) day data.
    Returns:
        DataFrame
    """
    start = time.time()
    if date is None:
        date = str(pd.to_datetime(pd.datetime.now()).floor('d'))[:10]
    assert (isinstance(date, str) and len(date)==10), "`date` shoule format '2018-12-01' or None"
    date = pd.to_datetime(date)
    update = date-pd.DateOffset(days=days)
    url_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/report/p2peye/problem_platform/problem_platform.txt'
    s = requests.get(url_txt).content
    data = pd.read_csv(io.StringIO(s.decode('utf-8')), parse_dates=['问题发生时间'])
    data = data[(data['问题发生时间']<=date)&(data['问题发生时间']>update)].reset_index(drop=True)
    print('p2peye problem platform dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return data
