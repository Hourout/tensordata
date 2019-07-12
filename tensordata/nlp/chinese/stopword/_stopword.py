import io
import time
import requests
import pandas as pd
from tensordata.utils._utils import assert_dirs, path_join
import tensordata.utils.request as rq

__all__ = ['standard', 'baidu', 'SCU', 'HIT']

def standard(root):
    """Chinese stop word datasets.
        
    Chinese stop word datasets Includes 746 stop word.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_stop_word data: 
    `root/chinese_stop_word/chinese_stop_word`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_stop_word`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_stop_word`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_stop_word')
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_stop_word/chinese_stop_word.txt'
    rq.table(url, path_join(task_path, 'chinese_stop_word.txt'))
    print('chinese_stop_word dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def baidu(root):
    """Chinese stop word of baidu datasets.
        
    Chinese stop word of baidu datasets Includes 1395 stop word.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_stop_word_baidu data: 
    `root/chinese_stop_word_baidu/chinese_stop_word_baidu`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_stop_word_baidu`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_stop_word_baidu`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_stop_word_baidu')
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_stop_word/chinese_stop_word_baidu.txt'
    rq.table(url, path_join(task_path, 'chinese_stop_word_baidu.txt'))
    print('chinese_stop_word_baidu dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def SCU(root):
    """Chinese stop word of Sichuan University datasets.
        
    Chinese stop word of Sichuan University datasets Includes 976 stop word.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_stop_word_SCU data: 
    `root/chinese_stop_word_SCU/chinese_stop_word_SCU`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_stop_word_SCU`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_stop_word_SCU`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_stop_word_SCU')
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_stop_word/chinese_stop_word_SCU.txt'
    rq.table(url, path_join(task_path, 'chinese_stop_word_SCU.txt'))
    print('chinese_stop_word_SCU dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def HIT(root):
    """Chinese stop word of Harbin Institute of Technology datasets.
        
    Chinese stop word of Harbin Institute of Technology datasets Includes 767 stop word.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_stop_word_HIT data: 
    `root/chinese_stop_word_HIT/chinese_stop_word_HIT`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_stop_word_HIT`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_stop_word_HIT`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_stop_word_HIT')
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_stop_word/chinese_stop_word_HIT.txt'
    data = pd.DataFrame(list(map(lambda x:x.replace('\n', ''), io.StringIO(requests.get(url).content.decode('utf-8')))))
    data.to_csv(path_join(task_path, 'chinese_stop_word_HIT.txt'), index=False, header=None)
    print('chinese_stop_word_HIT dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
