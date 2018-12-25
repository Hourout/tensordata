import os
import time
import json
import requests
import pandas as pd
import tensorflow as tf

def chinese_reviews_sina_weibo_emotion4(root):
    """Chinese Sina weibo 4 emotion reviews datasets.
        
    Chinese Sina weibo reviews datasets contains 360,000+ samples, 
    contains 4 emotions, including about 200,000 joys, 
    anger, disgust, and low, more than 50,000.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_reviews_sina_weibo_emotion4 data: 
    `root/chinese_reviews_sina_weibo_emotion4/chinese_reviews_sina_weibo_emotion4.json`
    `root/chinese_reviews_sina_weibo_emotion4/chinese_reviews_sina_weibo_emotion4.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_reviews_sina_weibo_emotion4`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_reviews_sina_weibo_emotion4`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_reviews_sina_weibo_emotion4')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url_json = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_reviews_sina_weibo_emotion4/chinese_reviews_sina_weibo_emotion4.json'
    url_txt = ['https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_reviews_sina_weibo_emotion4/chinese_reviews_sina_weibo_emotion4_01.txt',
               'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_reviews_sina_weibo_emotion4/chinese_reviews_sina_weibo_emotion4_02.txt',
               'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_reviews_sina_weibo_emotion4/chinese_reviews_sina_weibo_emotion4_03.txt',]
    s = requests.get(url_json)
    with open(os.path.join(task_path, 'chinese_reviews_sina_weibo_emotion4.json'), 'w') as outfile:
        json.dump(s.json(), outfile, ensure_ascii=False)
        outfile.write('\n')
    data = pd.DataFrame()
    for url in url_txt:
        s = requests.get(url).content
        data = pd.concat([data, pd.read_csv(io.StringIO(s.decode('utf-8')))])
    data.to_csv(os.path.join(task_path, 'chinese_reviews_sina_weibo_emotion4.txt'), index=False)
    print('chinese_reviews_sina_weibo_emotion4 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
