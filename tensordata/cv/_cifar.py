import time
import tarfile
import imageio
import numpy as np
import tensorflow as tf
from tensordata.utils._utils import assert_dirs, path_join
import tensordata.utils.request as rq

__all__ = ['cifar10', 'cifar100']

def cifar10(root):
    """CIFAR10 image classification dataset from https://www.cs.toronto.edu/~kriz/cifar.html
    
    Each sample is an image (in 3D NDArray) with shape (32, 32, 3).
    
    Attention: if exist dirs `root/cifar10`, api will delete it and create it.
    Data storage directory:
    root = `/user/.../mydata`
    cifar10 data: 
    `root/cifar10/train/0/xx.png`
    `root/cifar10/train/2/xx.png`
    `root/cifar10/train/6/xx.png`
    `root/cifar10/test/0/xx.png`
    `root/cifar10/test/2/xx.png`
    `root/cifar10/test/6/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/cifar10`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/cifar10`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'cifar10')
    url = 'https://apache-mxnet.s3-accelerate.dualstack.amazonaws.com/gluon/dataset/cifar10/cifar-10-binary.tar.gz'
    rq.files(url, path_join(task_path, url.split('/')[-1]))
    with tarfile.open(path_join(task_path, url.split('/')[-1])) as t:
        t.extractall(task_path)
    noise_flie = tf.io.gfile.listdir(task_path)
    for file in ['data_batch_1.bin', 'data_batch_2.bin', 'data_batch_3.bin', 'data_batch_4.bin', 'data_batch_5.bin']:
        with open(path_join(task_path, file), 'rb') as fin:
            data = np.frombuffer(fin.read(), dtype=np.uint8).reshape(-1, 3072+1)
            train = data[:, 1:].reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)
            train_label = data[:, 0].astype(np.int32)
        for i in set(train_label):
            tf.io.gfile.makedirs(path_join(task_path, 'train', str(i)))
        for idx in range(train.shape[0]):
            imageio.imsave(path_join(task_path, 'train', str(train_label[idx]), str(idx)+'.png'), train[idx])
    for file in ['test_batch.bin']:
        with open(path_join(task_path, file), 'rb') as fin:
            data = np.frombuffer(fin.read(), dtype=np.uint8).reshape(-1, 3072+1)
            test = data[:, 1:].reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)
            test_label = data[:, 0].astype(np.int32)
        for i in set(test_label):
            tf.io.gfile.makedirs(path_join(task_path, 'test', str(i)))
        for idx in range(test.shape[0]):
            imageio.imsave(path_join(task_path, 'test', str(test_label[idx]), str(idx)+'.png'), test[idx])
    for file in noise_flie:
        tf.io.gfile.remove(path_join(task_path, file))
    print('cifar10 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def cifar100(root, fine_label=True):
    """CIFAR100 image classification dataset from https://www.cs.toronto.edu/~kriz/cifar.html
    
    Each sample is an image (in 3D NDArray) with shape (32, 32, 3).
    
    Attention: if exist dirs `root/cifar100`, api will delete it and create it.
    Data storage directory:
    root = `/user/.../mydata`
    cifar100 data: 
    `root/cifar100/train/0/xx.png`
    `root/cifar100/train/2/xx.png`
    `root/cifar100/train/6/xx.png`
    `root/cifar100/test/0/xx.png`
    `root/cifar100/test/2/xx.png`
    `root/cifar100/test/6/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/cifar100`,
              root should be `/user/.../mydata`.
        fine_label: bool, default False.
                    Whether to load the fine-grained (100 classes) or 
                    coarse-grained (20 super-classes) labels.
    Returns:
        Store the absolute path of the data directory, is `root/cifar100`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'cifar100')
    url = 'https://apache-mxnet.s3-accelerate.dualstack.amazonaws.com/gluon/dataset/cifar100/cifar-100-binary.tar.gz'
    rq.files(url, path_join(task_path, url.split('/')[-1]))
    with tarfile.open(path_join(task_path, url.split('/')[-1])) as t:
        t.extractall(task_path)
    noise_flie = tf.io.gfile.listdir(task_path)
    with open(path_join(task_path, 'train.bin'), 'rb') as fin:
        data = np.frombuffer(fin.read(), dtype=np.uint8).reshape(-1, 3072+2)
        train = data[:, 2:].reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)
        train_label = data[:, 0+fine_label].astype(np.int32)
    for i in set(train_label):
        tf.io.gfile.makedirs(path_join(task_path, 'train', str(i)))
    for idx in range(train.shape[0]):
        imageio.imsave(path_join(task_path, 'train', str(train_label[idx]), str(idx)+'.png'), train[idx])
    with open(path_join(task_path, 'test.bin'), 'rb') as fin:
        data = np.frombuffer(fin.read(), dtype=np.uint8).reshape(-1, 3072+2)
        test = data[:, 2:].reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)
        test_label = data[:, 0+fine_label].astype(np.int32)
    for i in set(test_label):
        tf.io.gfile.makedirs(path_join(task_path, 'test', str(i)))
    for idx in range(test.shape[0]):
        imageio.imsave(path_join(task_path, 'test', str(test_label[idx]), str(idx)+'.png'), test[idx])
    for file in noise_flie:
        tf.io.gfile.remove(path_join(task_path, file))
    print('cifar100 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
