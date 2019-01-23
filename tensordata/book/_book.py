import os
import time
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
    Returns:
        Store the absolute path of the data directory, is `root/...(pdf or epub or mobi)`.
    """
    start = time.time()
    assert mode in ['pdf', 'epub', 'mobi'], "`mode` should be one of ['pdf', 'epub', 'mobi']."
    task_path = assert_dirs(root)
    url = 'https://github.com/nailperry-zd/The-Economist/raw/master/'+date+'/The_Economist_-_'+date+'.'+mode
    task_path = os.path.join(task_path, url.split('/')[-1])
    rq.files(url, task_path, verbose=1)
    print('economist dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
