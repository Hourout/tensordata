import os
import time
import requests
import pandas as pd
import tensorflow as tf

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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_stop_word')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_stop_word/chinese_stop_word.txt'
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')))
    data.to_csv(os.path.join(task_path, 'chinese_stop_word.txt'), index=False)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_stop_word_baidu')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_stop_word/chinese_stop_word_baidu.txt'
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')))
    data.to_csv(os.path.join(task_path, 'chinese_stop_word_baidu.txt'), index=False)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_stop_word_SCU')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_stop_word/chinese_stop_word_SCU.txt'
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')))
    data.to_csv(os.path.join(task_path, 'chinese_stop_word_SCU.txt'), index=False)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_stop_word_HIT')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_stop_word/chinese_stop_word_HIT.txt'
    data = pd.DataFrame(list(map(lambda x:x.replace('\n', ''), io.StringIO(requests.get(url).content.decode('utf-8')))))
    data.to_csv(os.path.join(task_path, 'chinese_stop_word_HIT.txt'), index=False, header=None)
    print('chinese_stop_word_HIT dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
