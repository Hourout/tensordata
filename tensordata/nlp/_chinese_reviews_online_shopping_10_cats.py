import os
import time
import json
import requests
import pandas as pd
import tensorflow as tf

def chinese_reviews_online_shopping_10_cats(root):
    """Chinese online shopping reviews datasets.
        
    Chinese online shopping reviews datasets contains 60,000+ samples, 
    about 10 categories (books, tablets, mobile phones, fruits, shampoos, 
    water heaters, Mengniu, clothes, computers, hotels),
    including more than 30,000 positive reviews 
    and more than 30,000 negative reviews
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_reviews_online_shopping_10_cats data: 
    `root/chinese_reviews_online_shopping_10_cats/chinese_reviews_online_shopping_10_cats.json`
    `root/chinese_reviews_online_shopping_10_cats/chinese_reviews_online_shopping_10_cats.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_reviews_online_shopping_10_cats`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_reviews_online_shopping_10_cats`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_reviews_online_shopping_10_cats')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url_json = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_reviews_online_shopping_10_cats/chinese_reviews_online_shopping_10_cats.json'
    url_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_reviews_online_shopping_10_cats/chinese_reviews_online_shopping_10_cats.csv'
    s = requests.get(url_json)
    with open(os.path.join(task_path, 'chinese_reviews_online_shopping_10_cats.json'), 'w') as outfile:
        json.dump(s.json(), outfile, ensure_ascii=False)
        outfile.write('\n')
    s = requests.get(url_txt).content
    data = pd.read_csv(io.StringIO(s.decode('utf-8')))
    data.to_csv(os.path.join(task_path, 'chinese_reviews_online_shopping_10_cats.txt'), index=False)
    print('chinese_reviews_online_shopping_10_cats dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
