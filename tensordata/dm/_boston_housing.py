import os
import time
import json
import requests
import pandas as pd
import tensorflow as tf


def boston_housing(root):
    """Housing Values in Suburbs of Boston
    
    Harrison, D. and Rubinfeld, D.L. (1978) Hedonic prices and the demand for 
    clean air. J. Environ. Economics and Management 5, 81–102.
    
    Belsley D.A., Kuh, E. and Welsch, R.E. (1980) Regression Diagnostics. 
    Identifying Influential Data and Sources of Collinearity. New York: Wiley.
    
    Data storage directory:
    root = `/user/.../mydata`
    boston_housing data: 
    `root/boston_housing/boston_housing.txt`
    `root/boston_housing/boston_housing.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/boston_housing`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/boston_housing`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'boston_housing')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url_json = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/boston_house/boston_housing.json'
    url_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/boston_house/boston_housing.txt'
    s = requests.get(url_json)
    with open(os.path.join(task_path, 'boston_housing.json'), 'w') as outfile:
        json.dump(s.json(), outfile, ensure_ascii=False)
        outfile.write('\n')
    s = requests.get(url_txt).content
    data = pd.read_csv(io.StringIO(s.decode('utf-8')), dtype='float32')
    data.to_csv(os.path.join(task_path, 'boston_housing.txt'), index=False)
    print('boston_housing dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
