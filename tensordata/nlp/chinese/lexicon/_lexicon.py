import io
import os
import time
import requests
import pandas as pd
import tensorflow as tf

__all__ = ['it',
]

def it(root):
    """Chinese lexicon IT datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_it dataset contains 16000+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_reviews_ctrip_hotel data: 
    `root/chinese_lexicon_it/chinese_lexicon_it.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_it`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_it`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_it')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_it.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_it.txt'), index=False, header=None)
    print('chinese_lexicon_it dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
