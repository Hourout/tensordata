import os
import io
import time
import requests
import concurrent
import pandas as pd
import tensorflow as tf


__all__ = ['CVPR2018', 'CVPR2017', 'CVPR2016', 'CVPR2015', 'CVPR2014', 'CVPR2013',
          ]

def _download(path):
    tf.keras.utils.get_file(os.path.join(path.split('|')[0], path.split('|')[1].split('/')[-1]), path.split('|')[1])

def arxiv(root, ids, new_name=None):
    """Download paper from https://arxiv.org, the file format is pdf.
    
    Data storage directory:
    root = `/user/.../mydata`
    `ids`.pdf data: 
    `root/arxiv/`ids`.pdf` or `root/arxiv/`new_name`.pdf`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/arxiv`,
              root should be `/user/.../mydata`.
        ids: str, arxiv paper id.
             example:ids = '1605.09782' mean you want get paper links https://arxiv.org/abs/1605.09782.
        new_name: str, default None. if not None, download file path is `root/arxiv/new_name.pdf`.
    Returns:
        Store the absolute path of the data directory, is `root/arxiv`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    assert isinstance(ids, str), '`ids` type should be str.'
    assert isinstance(new_name, str), '`new_name` type should be str.'
    if new_name is None:
        task_path = os.path.join(root, 'arxiv', ids+'.pdf')
    else:
        task_path = os.path.join(root, 'arxiv', new_name+'.pdf')
    if not tf.gfile.Exists(task_path):
        tf.gfile.MakeDirs(task_path)
    tf.gfile.DeleteRecursively(task_path)
    url = 'https://arxiv.org/pdf/'+str(ids)+'.pdf'
    tf.keras.utils.get_file(task_path, url)
    print('arxiv paper download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def _get_paper(name, root, url):
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, name)
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)[0].tolist()
    data = [task_path+'|'+i for i in data]
    with concurrent.futures.ProcessPoolExecutor() as excutor:
        excutor.map(_download, data)
    return task_path

def CVPR2018(root):
    """CVPR2018 datasets from http://openaccess.thecvf.com/CVPR2018.py.
        
    CVPR2018 datasets includes 979 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2018 data: 
    `root/CVPR2018/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2018`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2018`.
    """
    start = time.time()
    _get_paper('CVPR2018', root,
               url='https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2018.txt')
#     assert tf.gfile.IsDirectory(root), '`root` should be directory.'
#     task_path = os.path.join(root, 'cvpr2018')
#     if tf.gfile.Exists(task_path):
#         tf.gfile.DeleteRecursively(task_path)
#     tf.gfile.MakeDirs(task_path)
#     url = 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2018.txt'
#     data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)[0].tolist()
#     with concurrent.futures.ProcessPoolExecutor() as excutor:
#         excutor.map(_download, [task_path+'|'+i for i in data])
    print('CVPR2018 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def CVPR2017(root):
    """CVPR2017 datasets from http://openaccess.thecvf.com/CVPR2017.py.
        
    CVPR2017 datasets includes 783 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2017 data: 
    `root/CVPR2017/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2017`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2017`.
    """
    start = time.time()
    _get_paper('CVPR2017', root,
               url='https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2017.txt')
#     assert tf.gfile.IsDirectory(root), '`root` should be directory.'
#     task_path = os.path.join(root, 'cvpr2017')
#     if tf.gfile.Exists(task_path):
#         tf.gfile.DeleteRecursively(task_path)
#     tf.gfile.MakeDirs(task_path)
#     url = 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2017.txt'
#     data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)[0].tolist()
#     with concurrent.futures.ProcessPoolExecutor() as excutor:
#         excutor.map(_download, [task_path+'|'+i for i in data])
    print('CVPR2017 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def CVPR2016(root):
    """CVPR2016 datasets from http://openaccess.thecvf.com/CVPR2016.py.
        
    CVPR2016 datasets includes 643 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2016 data: 
    `root/CVPR2016/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2016`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2016`.
    """
    start = time.time()
    _get_paper('CVPR2016', root,
               url='https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2016.txt')
#     assert tf.gfile.IsDirectory(root), '`root` should be directory.'
#     task_path = os.path.join(root, 'cvpr2017')
#     if tf.gfile.Exists(task_path):
#         tf.gfile.DeleteRecursively(task_path)
#     tf.gfile.MakeDirs(task_path)
#     url = 'https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2017.txt'
#     data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)[0].tolist()
#     with concurrent.futures.ProcessPoolExecutor() as excutor:
#         excutor.map(_download, [task_path+'|'+i for i in data])
    print('CVPR2016 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def CVPR2015(root):
    """CVPR2015 datasets from http://openaccess.thecvf.com/CVPR2015.py.
        
    CVPR2015 datasets includes 602 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2015 data: 
    `root/CVPR2015/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2015`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2015`.
    """
    start = time.time()
    _get_paper('CVPR2015', root,
               url='https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2015.txt')
    print('CVPR2015 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def CVPR2014(root):
    """CVPR2014 datasets from http://openaccess.thecvf.com/CVPR2014.py.
        
    CVPR2014 datasets includes 540 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2014 data: 
    `root/CVPR2014/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2014`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2014`.
    """
    start = time.time()
    _get_paper('CVPR2014', root,
               url='https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2014.txt')
    print('CVPR2014 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def CVPR2013(root):
    """CVPR2013 datasets from http://openaccess.thecvf.com/CVPR2013.py.
        
    CVPR2013 datasets includes 471 papers.
    
    Data storage directory:
    root = `/user/.../mydata`
    CVPR2013 data: 
    `root/CVPR2013/...`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/CVPR2013`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/CVPR2013`.
    """
    start = time.time()
    _get_paper('CVPR2013', root,
               url='https://raw.githubusercontent.com/Hourout/datasets/master/paper/cvpr/cvpr2013.txt')
    print('CVPR2013 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
