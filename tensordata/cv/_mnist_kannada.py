import time

import pandas as pd
import tensordata.gfile as gfile
import tensordata.utils.request as rq
from tensordata.utils._utils import assert_dirs
from tensordata.utils.compress._un_compress import un_zip
from linora.image import save_image, array_to_image

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
    unzip_path = un_zip(task_path+'/kannada_MNIST.zip')
    train = pd.read_csv(gfile.path_join(task_path, 'kannada_MNIST/kannada_MNIST_train.csv'), header=None, dtype='uint8')
    test = pd.read_csv(gfile.path_join(task_path, 'kannada_MNIST/kannada_MNIST_test.csv'), header=None, dtype='uint8')
    for i in set(train[0]):
        gfile.makedirs(gfile.path_join(task_path, 'train', str(i)))
        gfile.makedirs(gfile.path_join(task_path, 'test', str(i)))
    for i in range(len(train)):
        save_image(gfile.path_join(task_path, 'train', str(train.iat[i, 0]), str(i)+'.png'),
                       array_to_image(train.iloc[i, 1:].values.reshape(28, 28, 1)))
    for i in range(len(test)):
        save_image(gfile.path_join(task_path, 'test', str(test.iat[i, 0]), str(i)+'.png'),
                       array_to_image(test.iloc[i, 1:].values.reshape(28, 28, 1)))
    gfile.remove(zip_path)
    gfile.remove(unzip_path)
    print('mnist_kannada dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
