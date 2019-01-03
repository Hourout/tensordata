import os
import time
import imageio
import numpy as np
import tensorflow as tf
from tensordata.utils.compress import un_gz, un_tar

__all__  = ['stl10']

def stl10(root):
    """Stl10 dataset from http://ai.stanford.edu/~acoates/stl10
    
    The STL-10 dataset is an image recognition dataset for developing 
    unsupervised feature learning, deep learning, self-taught learning algorithms.
    It is inspired by the CIFAR-10 dataset but with some modifications. 
    In particular, each class has fewer labeled training examples than in CIFAR-10, 
    but a very large set of unlabeled examples is provided to learn image models 
    prior to supervised training. The primary challenge is to make use of the 
    unlabeled data (which comes from a similar but different 
    distribution from the labeled data) to build a useful prior. 
    We also expect that the higher resolution of this dataset (96x96) 
    will make it a challenging benchmark for developing 
    more scalable unsupervised learning methods.
    
    Attention: if exist dirs `root/stl10`, api will delete it and create it.
    Data storage directory:
    root = `/user/.../mydata`
    stl10 data: 
    `root/stl10/train/1/xx.png`
    `root/stl10/train/4/xx.png`
    `root/stl10/train/8/xx.png`
    `root/stl10/test/1/xx.png`
    `root/stl10/test/4/xx.png`
    `root/stl10/test/8/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/stl10`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/stl10`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'stl10')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "http://ai.stanford.edu/~acoates/stl10/stl10_binary.tar.gz"
    tf.keras.utils.get_file(os.path.join(task_path, url.split('/')[-1]), url)
    un_tar(un_gz(os.path.join(task_path, url.split('/')[-1])))
    
    with tf.gfile.GFile(os.path.join(task_path, 'stl10_binary/stl10_binary/test_X.bin'), 'rb') as fin:
        data = np.frombuffer(fin.read(), dtype=np.uint8).reshape(-1, 3,96,96).transpose((0, 3, 2, 1))
    with tf.gfile.GFile(os.path.join(task_path, 'stl10_binary/stl10_binary/test_y.bin'), 'rb') as fin:
        data_label = np.frombuffer(fin.read(), dtype=np.uint8)
    for i in set(data_label):
        tf.gfile.MakeDirs(os.path.join(task_path, 'test', str(i)))
    for idx in range(data.shape[0]):
        imageio.imsave(os.path.join(task_path, 'test', str(data_label[idx]), str(idx)+'.png'), data[idx])
    
    with tf.gfile.GFile(os.path.join(task_path, 'stl10_binary/stl10_binary/train_X.bin'), 'rb') as fin:
        data = np.frombuffer(fin.read(), dtype=np.uint8).reshape(-1, 3,96,96).transpose((0, 3, 2, 1))
    with tf.gfile.GFile(os.path.join(task_path, 'stl10_binary/stl10_binary/train_y.bin'), 'rb') as fin:
        data_label = np.frombuffer(fin.read(), dtype=np.uint8)
    for i in set(data_label):
        tf.gfile.MakeDirs(os.path.join(task_path, 'train', str(i)))
    for idx in range(data.shape[0]):
        imageio.imsave(os.path.join(task_path, 'train', str(data_label[idx]), str(idx)+'.png'), data[idx])

    with tf.gfile.GFile(os.path.join(task_path, 'stl10_binary/stl10_binary/unlabeled_X.bin'), 'rb') as fin:
        data = np.frombuffer(fin.read(), dtype=np.uint8).reshape(-1, 3,96,96).transpose((0, 3, 2, 1))
    tf.gfile.MakeDirs(os.path.join(task_path, 'unlabeled'))
    for idx in range(data.shape[0]):
        imageio.imsave(os.path.join(task_path, 'unlabeled', str(idx)+'.png'), data[idx])
    
    tf.gfile.Remove(os.path.join(task_path, 'stl10_binary.tar.gz'))
    tf.gfile.Remove(os.path.join(task_path, 'stl10_binary.tar'))
    tf.gfile.DeleteRecursively(os.path.join(task_path, 'stl10_binary'))
    print('stl10 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
