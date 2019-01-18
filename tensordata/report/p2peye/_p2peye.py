import io
import time
import requests
import pandas as pd

__all__ =['rating']

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
