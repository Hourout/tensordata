import os
import time
import json
import requests
import pandas as pd
import tensorflow as tf

def chinese_reviews_takeaway(root):
    """Chinese takeaway reviews datasets.
    
    datasets url:`https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/waimai_10k/waimai_10k.csv`
    
    Chinese takeaway reviews datasets contains 12,000+ samples, 
    including more than 4,000 positive reviews 
    and more than 8,000 negative reviews
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_reviews_takeaway data: 
    `root/chinese_reviews_takeaway/chinese_reviews_takeaway.json`
    `root/chinese_reviews_takeaway/chinese_reviews_takeaway.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_reviews_takeaway`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_reviews_takeaway`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_reviews_takeaway')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url_json = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_reviews_takeaway/chinese_reviews_takeaway.json'
    url_txt = 'https://raw.githubusercontent.com/SophonPlus/ChineseNlpCorpus/master/datasets/waimai_10k/waimai_10k.csv'
    s = requests.get(url_json)
    with open(os.path.join(task_path, 'chinese_reviews_takeaway.json'), 'w') as outfile:
        json.dump(s.json(), outfile, ensure_ascii=False)
        outfile.write('\n')
    s = requests.get(url_txt).content
    data = pd.read_csv(io.StringIO(s.decode('utf-8')))
    data.to_csv(os.path.join(task_path, 'chinese_reviews_takeaway.txt'), index=False)
    print('chinese_reviews_takeaway dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
