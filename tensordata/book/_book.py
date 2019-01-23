import os
import time
import pandas as pd
from tensordata.utils._utils import assert_dirs
import tensordata.utils.request as rq

__all__ = ['economist']

def economist(root, date, mode='pdf'):
    """The Economist from https://github.com/nailperry-zd/The-Economist.
    
    Data storage directory:
    root = `/user/.../mydata`
    economist data: 
    `root/...(pdf or epub or mobi)`
    Args:
        root: str, Store the absolute path of the data directory.
        date: str, eg:'2019-01-01'.
        mode: str, one of ['pdf', 'epub', 'mobi'].
    Returns:
        Store the absolute path of the data directory, is `root/...(pdf or epub or mobi)`.
    """
    start = time.time()
    assert mode in ['pdf', 'epub', 'mobi'], "`mode` should be one of ['pdf', 'epub', 'mobi']."
    t = divmod((pd.to_datetime(date)-pd.to_datetime('2017-05-06')).days, 7)
    if t[0]<0 or t[1]>0:
        raise ValueError("No book that meets the date.") 
    task_path = assert_dirs(root)
    url = 'https://github.com/nailperry-zd/The-Economist/raw/master/'+date+'/The_Economist_-_'+date+'.'+mode
    task_path = os.path.join(task_path, url.split('/')[-1])
    rq.files(url, task_path, verbose=1)
    print('economist dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
