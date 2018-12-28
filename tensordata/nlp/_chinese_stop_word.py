import os
import time
import requests
import pandas as pd
import tensorflow as tf

def chinese_stop_word(root):
    """Chinese stop word datasets.
        
    Chinese douban stop word datasets Includes 746 stop word.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_reviews_douban_movies data: 
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
