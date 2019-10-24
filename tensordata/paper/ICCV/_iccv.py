import time
from tensordata.utils._utils import get_paper


__all__ = ['ICCV2013', 'ICCV2015', 'ICCV2017', 'ICCV2019'
          ]

def ICCV2019(root):
    """ICCV2019 datasets from http://openaccess.thecvf.com/ICCV2019.py.
        
    ICCV2019 datasets includes 1619 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    ICCV2019 data: 
    `root/ICCV2019/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/ICCV2019`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/ICCV2019`.
    """
    start = time.time()
    task_path = get_paper('ICCV2019', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/ICCV/iccv2019.txt')
    print('ICCV2019 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def ICCV2017(root):
    """ICCV2017 datasets from http://openaccess.thecvf.com/ICCV2017.py.
        
    ICCV2017 datasets includes 621 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    ICCV2017 data: 
    `root/ICCV2017/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/ICCV2017`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/ICCV2017`.
    """
    start = time.time()
    task_path = get_paper('ICCV2017', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/ICCV/iccv2017.txt')
    print('ICCV2017 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def ICCV2015(root):
    """ICCV2015 datasets from http://openaccess.thecvf.com/ICCV2015.py.
        
    ICCV2015 datasets includes 526 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    ICCV2015 data: 
    `root/ICCV2015/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/ICCV2015`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/ICCV2015`.
    """
    start = time.time()
    task_path = get_paper('ICCV2015', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/ICCV/iccv2015.txt')
    print('ICCV2015 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def ICCV2013(root):
    """ICCV2013 datasets from http://openaccess.thecvf.com/ICCV2013.py.
        
    ICCV2013 datasets includes 455 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    ICCV2013 data: 
    `root/ICCV2013/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/ICCV2013`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/ICCV2013`.
    """
    start = time.time()
    task_path = get_paper('ICCV2013', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/ICCV/iccv2013.txt')
    print('ICCV2013 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
