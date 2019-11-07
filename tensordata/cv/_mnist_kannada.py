import time
import pandas as pd
import tensordata.utils.request as rq
from tensordata.utils._utils import assert_dirs, path_join
import tensorflow as tf
gfile = tf.io.gfile

__all__ = ['mnist_kannada']

def mnist_kannada(root):
    """kannada-MNIST from https://github.com/vinayprabhu/Kannada_MNIST.
    
    The Kannada-MNIST dataset was created an a drop-in substitute for the standard MNIST dataset.
    
    Each sample is an gray image (in 3D NDArray) with shape (28, 28, 1).
    
    Attention: if exist dirs `root/mnist_kannada`, api will delete it and create it.
    Data storage directory:
    root = `/user/.../mydata`
    mnist_kannada data: 
    `root/mnist_kannada/train/0/xx.png`
    `root/mnist_kannada/train/2/xx.png`
    `root/mnist_kannada/train/6/xx.png`
    `root/mnist_kannada/test/0/xx.png`
    `root/mnist_kannada/test/2/xx.png`
    `root/mnist_kannada/test/6/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/mnist_kannada`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/mnist_kannada`.
    """
    start = time.time()
    print('Downloading data from https://github.com/Hourout/datasets/releases/download/0.0.1/kannada_MNIST.zip')
    task_path = assert_dirs(root, 'mnist_kannada')
    zip_path = rq.files('https://github.com/Hourout/datasets/releases/download/0.0.1/kannada_MNIST.zip', task_path+'/kannada_MNIST.zip')
    unzip_path = td.utils.compress.un_zip(task_path+'/kannada_MNIST.zip')
    test = pd.read_csv('./data/kannada_MNIST/kannada_MNIST_train.csv', header=None, dtype='uint8')
    train = pd.read_csv('./data/kannada_MNIST/kannada_MNIST_test.csv', header=None, dtype='uint8')
    for i in set(train[0]):
        gfile.makedirs(path_join(task_path, 'train', str(i)))
        gfile.makedirs(path_join(task_path, 'test', str(i)))
    for i in range(len(train)):
        tf.io.write_file(path_join(task_path, 'train', str(train.iat[i, 0]), str(i)+'.png'),
                         tf.image.encode_png(train.iloc[i, 1:].values.reshape(28, 28, 1)))
    for i in range(len(test)):
        tf.io.write_file(path_join(task_path, 'test', str(test.iat[i, 0]), str(i)+'.png'),
                         tf.image.encode_png(test.iloc[i, 1:].values.reshape(28, 28, 1)))
    gfile.remove(zip_path)
    gfile.rmtree(unzip_path)
    print('mnist_kannada dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
