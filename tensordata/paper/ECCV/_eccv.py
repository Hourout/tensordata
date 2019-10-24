import time
from tensordata.utils._utils import get_paper


__all__ = ['ECCV2018'
          ]

def ECCV2018(root):
    """ECCV2018 datasets from http://openaccess.thecvf.com/ECCV2018.py.
        
    ECCV2018 datasets includes 776 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    ECCV2018 data: 
    `root/ECCV2018/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/ECCV2018`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/ECCV2018`.
    """
    start = time.time()
    task_path = get_paper('ECCV2018', root, 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/eccv/eccv2018.txt')
    print('ECCV2018 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
