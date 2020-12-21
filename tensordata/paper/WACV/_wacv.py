import time
from tensordata.utils._utils import get_paper


__all__ = ['WACV2020']

def WACV2020(root):
    """WACV2020 datasets from http://openaccess.thecvf.com/WACV2020.py.
        
    WACV2020 datasets includes 527 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    WACV2020 data: 
    `root/WACV2020/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/WACV2020`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/WACV2020`.
    """
    start = time.time()
    task_path = get_paper('WACV2020', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/wacv/wacv2020.txt')
    print('WACV2020 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
