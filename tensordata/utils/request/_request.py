import io
import json
import requests
import pandas as pd
import tensorflow as tf

__all__ ['json', 'txt']

def json(url, root_file):
    """Request url that file is json file.
    
    Args:
        url: str, request url.
        root_file: str, downloaded and saved file name.
    Return:
        root_file: str, downloaded and saved file name.
    """
    assert root_file[-5:]=='.json', '`root_file` should be `xxx.json`'
    s = requests.get(url)
    with tf.gfile.GFile(root_file, 'w') as f:
        json.dump(s.json(), f, ensure_ascii=False)
    return root_file

def request_txt(url, root_file, sep=','):
    """Request url that file is txt file.
    
    Args:
        url: str, request url.
        root_file: str, downloaded and saved file name.
        sep: str, field delimiter for the output file.
    Return:
        root_file: str, downloaded and saved file name.
    """
    s = requests.get(url).content
    data = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None, low_memory=False)
    data.to_csv(root_file, index=False, sep=sep, header=None)
    return root_file
