import time
from tensordata.utils._utils import get_paper


__all__ = ['CVPR2018', 'CVPR2017', 'CVPR2016', 'CVPR2015', 'CVPR2014', 'CVPR2013',
           'CVPR2019',
          ]

def CVPR2019(root):
    """CVPR2018 datasets from http://openaccess.thecvf.com/CVPR2019.py.
        
    CVPR2019 datasets includes 1915 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2019 data: 
    `root/CVPR2019/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2019`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2019`.
    """
    start = time.time()
    task_path = get_paper('CVPR2019', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2019.txt')
    print('CVPR2019 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def CVPR2018(root):
    """CVPR2018 datasets from http://openaccess.thecvf.com/CVPR2018.py.
        
    CVPR2018 datasets includes 979 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2018 data: 
    `root/CVPR2018/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2018`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2018`.
    """
    start = time.time()
    task_path = get_paper('CVPR2018', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2018.txt')
    print('CVPR2018 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def CVPR2017(root):
    """CVPR2017 datasets from http://openaccess.thecvf.com/CVPR2017.py.
        
    CVPR2017 datasets includes 783 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2017 data: 
    `root/CVPR2017/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2017`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2017`.
    """
    start = time.time()
    task_path = get_paper('CVPR2017', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2017.txt')
    print('CVPR2017 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def CVPR2016(root):
    """CVPR2016 datasets from http://openaccess.thecvf.com/CVPR2016.py.
        
    CVPR2016 datasets includes 643 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2016 data: 
    `root/CVPR2016/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2016`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2016`.
    """
    start = time.time()
    task_path = get_paper('CVPR2016', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2016.txt')
    print('CVPR2016 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def CVPR2015(root):
    """CVPR2015 datasets from http://openaccess.thecvf.com/CVPR2015.py.
        
    CVPR2015 datasets includes 602 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2015 data: 
    `root/CVPR2015/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2015`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2015`.
    """
    start = time.time()
    task_path = get_paper('CVPR2015', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2015.txt')
    print('CVPR2015 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def CVPR2014(root):
    """CVPR2014 datasets from http://openaccess.thecvf.com/CVPR2014.py.
        
    CVPR2014 datasets includes 540 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2014 data: 
    `root/CVPR2014/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2014`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2014`.
    """
    start = time.time()
    task_path = get_paper('CVPR2014', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2014.txt')
    print('CVPR2014 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def CVPR2013(root):
    """CVPR2013 datasets from http://openaccess.thecvf.com/CVPR2013.py.
        
    CVPR2013 datasets includes 471 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2013 data: 
    `root/CVPR2013/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2013`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2013`.
    """
    start = time.time()
    task_path = get_paper('CVPR2013', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2013.txt')
    print('CVPR2013 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
