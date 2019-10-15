import os
import time
import imageio
import numpy as np
from tensordata.utils.compress import un_tar
from tensordata.utils._utils import assert_dirs, path_join
import tensordata.utils.request as rq
import tensorflow as tf
gfile = tf.io.gfile

__all__ = ['mnist_kuzushiji10', 'mnist_kuzushiji49', 'mnist_kuzushiji_kanji']

def mnist_kuzushiji10(root):
    """Kuzushiji-MNIST from https://github.com/rois-codh/kmnist.
    
    Kuzushiji-MNIST is a drop-in replacement for the
    MNIST dataset (28x28 grayscale, 70,000 images), 
    provided in the original MNIST format as well as a NumPy format.
    Since MNIST restricts us to 10 classes, we chose one character to
    represent each of the 10 rows of Hiragana when creating Kuzushiji-MNIST.
    
    Each sample is an gray image (in 3D NDArray) with shape (28, 28, 1).
    
    Attention: if exist dirs `root/mnist_kuzushiji10`, api will delete it and create it.
    Data storage directory:
    root = `/user/.../mydata`
    mnist_kuzushiji10 data: 
    `root/mnist_kuzushiji10/train/0/xx.png`
    `root/mnist_kuzushiji10/train/2/xx.png`
    `root/mnist_kuzushiji10/train/6/xx.png`
    `root/mnist_kuzushiji10/test/0/xx.png`
    `root/mnist_kuzushiji10/test/2/xx.png`
    `root/mnist_kuzushiji10/test/6/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/mnist_kuzushiji10`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/mnist_kuzushiji10`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'mnist_kuzushiji10')
    url_list = ['http://codh.rois.ac.jp/kmnist/dataset/kmnist/kmnist-train-imgs.npz',
                'http://codh.rois.ac.jp/kmnist/dataset/kmnist/kmnist-train-labels.npz',
                'http://codh.rois.ac.jp/kmnist/dataset/kmnist/kmnist-test-imgs.npz',
                'http://codh.rois.ac.jp/kmnist/dataset/kmnist/kmnist-test-labels.npz']
    for url in url_list:
        rq.files(url, path_join(task_path, url.split('/')[-1]))
    train = np.load(path_join(task_path, 'kmnist-train-imgs.npz'))['arr_0']
    train_label = np.load(path_join(task_path, 'kmnist-train-labels.npz'))['arr_0']
    test = np.load(path_join(task_path, 'kmnist-test-imgs.npz'))['arr_0']
    test_label = np.load(path_join(task_path, 'kmnist-test-labels.npz'))['arr_0']
    for i in set(train_label):
        gfile.makedirs(path_join(task_path, 'train', str(i)))
    for i in set(test_label):
        gfile.makedirs(path_join(task_path, 'test', str(i)))
    for idx in range(train.shape[0]):
        imageio.imsave(path_join(task_path, 'train', str(train_label[idx]), str(idx)+'.png'), train[idx])
    for idx in range(test.shape[0]):
        imageio.imsave(path_join(task_path, 'test', str(test_label[idx]), str(idx)+'.png'), test[idx])
    for url in url_list:
        gfile.remove(path_join(task_path, url.split('/')[-1]))
    print('mnist_kuzushiji10 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def mnist_kuzushiji49(root):
    """Kuzushiji-49 from https://github.com/rois-codh/kmnist.
    
    Kuzushiji-49, as the name suggests, has 49 classes (28x28 grayscale, 270,912 images),
    is a much larger, but imbalanced dataset containing 48 Hiragana 
    characters and one Hiragana iteration mark.
    
    Each sample is an gray image (in 3D NDArray) with shape (28, 28, 1).
    
    Attention: if exist dirs `root/mnist_kuzushiji49`, api will delete it and create it.
    Data storage directory:
    root = `/user/.../mydata`
    mnist_kuzushiji49 data: 
    `root/mnist_kuzushiji49/train/0/xx.png`
    `root/mnist_kuzushiji49/train/2/xx.png`
    `root/mnist_kuzushiji49/train/6/xx.png`
    `root/mnist_kuzushiji49/test/0/xx.png`
    `root/mnist_kuzushiji49/test/2/xx.png`
    `root/mnist_kuzushiji49/test/6/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/mnist_kuzushiji49`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/mnist_kuzushiji49`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'mnist_kuzushiji49')
    url_list = ['http://codh.rois.ac.jp/kmnist/dataset/k49/k49-train-imgs.npz',
                'http://codh.rois.ac.jp/kmnist/dataset/k49/k49-train-labels.npz',
                'http://codh.rois.ac.jp/kmnist/dataset/k49/k49-test-imgs.npz',
                'http://codh.rois.ac.jp/kmnist/dataset/k49/k49-test-labels.npz']
    for url in url_list:
        rq.files(url, path_join(task_path, url.split('/')[-1]))
    train = np.load(path_join(task_path, 'k49-train-imgs.npz'))['arr_0']
    train_label = np.load(path_join(task_path, 'k49-train-labels.npz'))['arr_0']
    test = np.load(path_join(task_path, 'k49-test-imgs.npz'))['arr_0']
    test_label = np.load(path_join(task_path, 'k49-test-labels.npz'))['arr_0']
    for i in set(train_label):
        gfile.makedirs(path_join(task_path, 'train', str(i)))
    for i in set(test_label):
        gfile.makedirs(path_join(task_path, 'test', str(i)))
    for idx in range(train.shape[0]):
        imageio.imsave(path_join(task_path, 'train', str(train_label[idx]), str(idx)+'.png'), train[idx])
    for idx in range(test.shape[0]):
        imageio.imsave(path_join(task_path, 'test', str(test_label[idx]), str(idx)+'.png'), test[idx])
    for url in url_list:
        gfile.remove(path_join(task_path, url.split('/')[-1]))
    print('mnist_kuzushiji49 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def mnist_kuzushiji_kanji(root):
    """Kuzushiji-Kanji dataset from https://github.com/rois-codh/kmnist.
    
    Kuzushiji-Kanji is a large and highly imbalanced 64x64 dataset 
    of 3832 Kanji characters, containing 140,426 images 
    of both common and rare characters.
    
    Attention: if exist dirs `root/mnist_kuzushiji_kanji`, api will delete it and create it.
    Data storage directory:
    root = `/user/.../mydata`
    mnist_kuzushiji_kanji data: 
    `root/mnist_kuzushiji_kanji/train/U+55C7/xx.png`
    `root/mnist_kuzushiji_kanji/train/U+7F8E/xx.png`
    `root/mnist_kuzushiji_kanji/train/U+9593/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/mnist_kuzushiji_kanji`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/mnist_kuzushiji_kanji.
    """
    start = time.time()
    task_path = assert_dirs(root, 'mnist_kuzushiji_kanji', make_root_dir=False)
    url = "http://codh.rois.ac.jp/kmnist/dataset/kkanji/kkanji.tar"
    rq.files(url, path_join(root, url.split('/')[-1]))
    un_tar(path_join(root, url.split('/')[-1]), task_path)
    gfile.rename(path_join(task_path, 'kkanji2'), path_join(task_path, 'train'))
    gfile.remove(path_join(root, 'kkanji.tar'))
    print('mnist_kuzushiji_kanji dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
