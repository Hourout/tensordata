import os
import io
import concurrent.futures

import requests
import pandas as pd
from tensordata.utils import request as rq

def assert_dirs(root, root_dir=None, delete=True, make_root_dir=True):
    assert os.path.isdir(root), '{} should be directory.'.format(root)
    if root_dir is not None:
        assert isinstance(root_dir, str), '{} should be str.'.format(root_dir)
        task_path = path_join(root, root_dir)
        if os.path.exists(task_path):
            if delete:
                os.rmdir(task_path)
                os.makedirs(task_path)
        else:
            if make_root_dir:
                os.makedirs(task_path)
        return task_path
    else:
        if not os.path.exists(root):
            os.makedirs(root)
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
