import os
import time
import json
import requests
import pandas as pd
import tensorflow as tf

def chinese_reviews_ctrip_hotel(root):
    """Ctrip hotel reviews datasets.
    
    datasets url:`https://github.com/SophonPlus/ChineseNlpCorpus/blob/
    master/datasets/ChnSentiCorp_htl_all/ChnSentiCorp_htl_all.csv`
    
    Ctrip's review data set contains 7000+ samples, 
    including more than 5,000 positive reviews 
    and more than 2,000 negative reviews
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_reviews_ctrip_hotel data: 
    `root/chinese_reviews_ctrip_hotel/chinese_reviews_ctrip_hotel.txt`
    `root/chinese_reviews_ctrip_hotel/chinese_reviews_ctrip_hotel.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_reviews_ctrip_hotel`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_reviews_ctrip_hotel`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_reviews_ctrip_hotel')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url_json = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_reviews_ctrip_hotel/chinese_reviews_ctrip_hotel.json'
    url_txt = 'https://raw.githubusercontent.com/SophonPlus/ChineseNlpCorpus/master/datasets/ChnSentiCorp_htl_all/ChnSentiCorp_htl_all.csv'
    s = requests.get(url_json)
    with open(os.path.join(task_path, 'chinese_reviews_ctrip_hotel.json'), 'w') as outfile:
        json.dump(s.json(), outfile, ensure_ascii=False)
        outfile.write('\n')
    s = requests.get(url_txt).content
    data = pd.read_csv(io.StringIO(s.decode('utf-8')))
    data.to_csv(os.path.join(task_path, 'chinese_reviews_ctrip_hotel.txt'), index=False)
    print('chinese_reviews_ctrip_hotel dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
