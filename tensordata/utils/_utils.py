import os
import io
import requests
import concurrent.futures
import pandas as pd
import tensorflow as tf
from tensordata.utils import request as rq

def assert_dirs(root, root_dir=None, delete=True, make_root_dir=True):
    assert tf.io.gfile.isdir(root), '{} should be directory.'.format(root)
    if root_dir is not None:
        assert isinstance(root_dir, str), '{} should be str.'.format(root_dir)
        task_path = path_join(root, root_dir)
        if tf.io.gfile.exists(task_path):
            if delete:
                tf.io.gfile.rmtree(task_path)
                tf.io.gfile.makedirs(task_path)
        else:
            if make_root_dir:
                tf.io.gfile.makedirs(task_path)
        return task_path
    else:
        if not tf.io.gfile.exists(root):
            tf.io.gfile.makedirs(root)
        return root

def path_join(path, *paths):
    return eval(repr(os.path.join(path, *paths)).replace("\\", '/').replace("//", '/'))

def _download(path):
    rq.files(path.split('|')[1], path_join(path.split('|')[0], path.split('|')[1].split('/')[-1]))
    
def get_paper(name, root, url):
    task_path = assert_dirs(root, name)
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)[0].tolist()
    data = [task_path+'|'+i for i in data]
    with concurrent.futures.ProcessPoolExecutor() as excutor:
        excutor.map(_download, data)
    return task_path
