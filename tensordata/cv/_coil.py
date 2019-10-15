import os
import time
import pandas as pd
from tensordata.utils.compress import un_zip
from tensordata.utils._utils import assert_dirs, path_join
import tensordata.utils.request as rq
import tensorflow as tf
gfile = tf.io.gfile

__all__ = ['coil20', 'coil100']

def coil20(root):
    """COIL20 dataset from http://www.cs.columbia.edu/CAVE/software/softlib/coil-20.php
    
    "Columbia Object Image Library (COIL-20)," 
    S. A. Nene, S. K. Nayar and H. Murase,
    Technical Report CUCS-005-96, February 1996.
    
    Each sample is an gray image (in 3D NDArray) with shape (128, 128, 1).
    Attention: if exist dirs `root/coil20`, api will delete it and create it.
    Data storage directory:
    root = `/user/.../mydata`
    coil20 data: 
    `root/coil20/train/0/xx.png`
    `root/coil20/train/2/xx.png`
    `root/coil20/train/6/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/coil20`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/coil20`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'coil20')
    url = "http://www.cs.columbia.edu/CAVE/databases/SLAM_coil-20_coil-100/coil-20/coil-20-proc.zip"
    rq.files(url, path_join(task_path, 'coil20.zip'))
    un_zip(path_join(task_path, 'coil20.zip'))
    image = gfile.listdir(path_join(task_path, 'coil20', 'coil-20-proc'))
    t = pd.DataFrame(image, columns=['image'])
    t['label'] = t.image.map(lambda x:x.split('__')[0][3:])
    t['image_old_path'] = t.image.map(lambda x:path_join(task_path, 'coil20', 'coil-20-proc', x))
    t['image_new_path'] = (t.label+'/'+t.image).map(lambda x:path_join(task_path, 'train', x))
    for i in t.label.unique():
        gfile.makedirs(path_join(task_path, 'train', i))
    for i,j in zip(t.image_old_path, t.image_new_path):
        gfile.copy(i, j)
    gfile.remove(path_join(task_path, 'coil20.zip'))
    gfile.rmtree(path_join(task_path, 'coil20'))
    print('coil20 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def coil100(root):
    """COIL100 dataset from http://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php
    
    "Columbia Object Image Library (COIL-100),"
    S. A. Nene, S. K. Nayar and H. Murase,
    Technical Report CUCS-006-96, February 1996.
    
    Each sample is an gray image (in 3D NDArray) with shape (128, 128, 1).
    Attention: if exist dirs `root/coil100`, api will delete it and create it.
    Data storage directory:
    root = `/user/.../mydata`
    coil100 data: 
    `root/coil100/train/0/xx.png`
    `root/coil100/train/2/xx.png`
    `root/coil100/train/6/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/coil100`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/coil100`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'coil100')
    url = "http://www.cs.columbia.edu/CAVE/databases/SLAM_coil-20_coil-100/coil-100/coil-100.zip"
    rq.files(url, path_join(task_path, 'coil100.zip'))
    un_zip(path_join(task_path, 'coil100.zip'))
    image = gfile.listdir(path_join(task_path, 'coil100', 'coil-100'))
    t = pd.DataFrame(image, columns=['image'])
    t['label'] = t.image.map(lambda x:x.split('__')[0][3:])
    t['image_old_path'] = t.image.map(lambda x:path_join(task_path, 'coil100', 'coil-100', x))
    t['image_new_path'] = (t.label+'/'+t.image).map(lambda x:path_join(task_path, 'train', x))
    for i in t.label.unique():
        gfile.makedirs(path_join(task_path, 'train', i))
    for i,j in zip(t.image_old_path, t.image_new_path):
        gfile.copy(i, j)
    gfile.remove(path_join(task_path, 'coil100.zip'))
    gfile.rmtree(path_join(task_path, 'coil100'))
    if gfile.exists(path_join(task_path, 'train', 'vertGroupppm2png.pl')):
        gfile.remove(path_join(task_path, 'train', 'vertGroupppm2png.pl'))
    print('coil100 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
