import os
import gzip
import time
import imageio
import numpy as np
import tensorflow as tf

def mnist(root):
    """MNIST handwritten digits dataset from http://yann.lecun.com/exdb/mnist
    Each sample is an gray image (in 3D NDArray) with shape (28, 28, 1).
    Data storage directory:
    root = `/user/.../mydata`
    mnist data: 
    `root/mnist/train/0/xx.png`
    `root/mnist/train/2/xx.png`
    `root/mnist/train/6/xx.png`
    `root/mnist/test/0/xx.png`
    `root/mnist/test/2/xx.png`
    `root/mnist/test/6/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/mnist`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/mnist`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'mnist')
    url_list = ['https://apache-mxnet.s3-accelerate.dualstack.amazonaws.com/gluon/dataset/mnist/train-labels-idx1-ubyte.gz',
                'https://apache-mxnet.s3-accelerate.dualstack.amazonaws.com/gluon/dataset/mnist/train-images-idx3-ubyte.gz',
                'https://apache-mxnet.s3-accelerate.dualstack.amazonaws.com/gluon/dataset/mnist/t10k-labels-idx1-ubyte.gz',
                'https://apache-mxnet.s3-accelerate.dualstack.amazonaws.com/gluon/dataset/mnist/t10k-images-idx3-ubyte.gz']
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    for url in url_list:
        tf.keras.utils.get_file(os.path.join(task_path, url.split('/')[-1]), url)
    with gzip.open(os.path.join(task_path, 'train-labels-idx1-ubyte.gz'), 'rb') as lbpath:
        train_label = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(os.path.join(task_path, 'train-images-idx3-ubyte.gz'), 'rb') as imgpath:
        train = np.frombuffer(imgpath.read(), np.uint8, offset=16).reshape(len(train_label), 28, 28)

    with gzip.open(os.path.join(task_path, 't10k-labels-idx1-ubyte.gz'), 'rb') as lbpath:
        test_label = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(os.path.join(task_path, 't10k-images-idx3-ubyte.gz'), 'rb') as imgpath:
        test = np.frombuffer(imgpath.read(), np.uint8, offset=16).reshape(len(test_label), 28, 28)
    
    for i in set(train_label):
        tf.gfile.MakeDirs(os.path.join(task_path, 'train', str(i)))
    for i in set(test_label):
        tf.gfile.MakeDirs(os.path.join(task_path, 'test', str(i)))
    for idx in range(train.shape[0]):
        imageio.imsave(os.path.join(task_path, 'train', str(train_label[idx]), str(idx)+'.png'), train[idx])
    for idx in range(test.shape[0]):
        imageio.imsave(os.path.join(task_path, 'test', str(test_label[idx]), str(idx)+'.png'), test[idx])
    for url in url_list:
        tf.gfile.Remove(os.path.join(task_path, url.split('/')[-1]))
    print('mnist dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def mnist_fashion(root):
    """A dataset of Zalando's article images consisting of fashion products.
    
    Fashion mnist datasets is a drop-in replacement of the original MNIST dataset
    from https://github.com/zalandoresearch/fashion-mnist.
    Each sample is an gray image (in 3D NDArray) with shape (28, 28, 1).
    
    Data storage directory:
    root = `/user/.../mydata`
    mnist data: 
    `root/mnist_fashion/train/0/xx.png`
    `root/mnist_fashion/train/2/xx.png`
    `root/mnist_fashion/train/6/xx.png`
    `root/mnist_fashion/test/0/xx.png`
    `root/mnist_fashion/test/2/xx.png`
    `root/mnist_fashion/test/6/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/mnist_fashion`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/mnist_fashion`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'mnist_fashion')
    url_list = ['http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz',
                'http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz',
                'http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz',
                'http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz']
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    for url in url_list:
        tf.keras.utils.get_file(os.path.join(task_path, url.split('/')[-1]), url)
    with gzip.open(os.path.join(task_path, 'train-labels-idx1-ubyte.gz'), 'rb') as lbpath:
        train_label = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(os.path.join(task_path, 'train-images-idx3-ubyte.gz'), 'rb') as imgpath:
        train = np.frombuffer(imgpath.read(), np.uint8, offset=16).reshape(len(train_label), 28, 28)

    with gzip.open(os.path.join(task_path, 't10k-labels-idx1-ubyte.gz'), 'rb') as lbpath:
        test_label = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(os.path.join(task_path, 't10k-images-idx3-ubyte.gz'), 'rb') as imgpath:
        test = np.frombuffer(imgpath.read(), np.uint8, offset=16).reshape(len(test_label), 28, 28)
    
    for i in set(train_label):
        tf.gfile.MakeDirs(os.path.join(task_path, 'train', str(i)))
    for i in set(test_label):
        tf.gfile.MakeDirs(os.path.join(task_path, 'test', str(i)))
    for idx in range(train.shape[0]):
        imageio.imsave(os.path.join(task_path, 'train', str(train_label[idx]), str(idx)+'.png'), train[idx])
    for idx in range(test.shape[0]):
        imageio.imsave(os.path.join(task_path, 'test', str(test_label[idx]), str(idx)+'.png'), test[idx])
    for url in url_list:
        tf.gfile.Remove(os.path.join(task_path, url.split('/')[-1]))
    print('mnist_fashion dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
