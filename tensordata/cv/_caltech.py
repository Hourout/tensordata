import time
import tensorflow as tf
from tensordata.utils.compress import un_gz, un_tar
from tensordata.utils._utils import assert_dirs, path_join
import tensordata.utils.request as rq

__all__  = ['caltech101', 'caltech256']

def caltech101(root):
    """Caltech101 dataset from http://www.vision.caltech.edu/Image_Datasets/Caltech101
    
    Pictures of objects belonging to 101 categories. 
    About 40 to 800 images per category.
    Most categories have about 50 images. 
    Collected in September 2003 by Fei-Fei Li, Marco Andreetto, 
    and Marc 'Aurelio Ranzato.  
    The size of each image is roughly 300 x 200 pixels.

    We have carefully clicked outlines of each object in these pictures, 
    these are included under the 'Annotations.tar'.
    There is also a matlab script to view the annotaitons, 'show_annotations.m'.
    
    Attention: if exist dirs `root/caltech101`, api will delete it and create it.
    Data storage directory:
    root = `/user/.../mydata`
    caltech101 data: 
    `root/caltech101/train/accordion/xx.jpg`
    `root/caltech101/train/brain/xx.ipg`
    `root/caltech101/train/panda/xx.jpg`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/caltech101`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/caltech101.
    """
    start = time.time()
    task_path = assert_dirs(root, 'caltech101', make_root_dir=False)
    url = 'http://www.vision.caltech.edu/Image_Datasets/Caltech101/101_ObjectCategories.tar.gz'
    rq.files(url, path_join(root, url.split('/')[-1]))
    un_tar(un_gz(path_join(root, url.split('/')[-1])), task_path)
    tf.io.gfile.rename(path_join(task_path, '101_ObjectCategories'), path_join(task_path, 'train'))
    for i in ['101_ObjectCategories.tar.gz', '101_ObjectCategories.tar']:
        tf.io.gfile.remove(path_join(root, i))
    print('caltech101 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def caltech256(root):
    """Caltech256 dataset from http://www.vision.caltech.edu/Image_Datasets/Caltech256
    
    Pictures of objects belonging to 256 categories. 
    About 80 to 800 images per category.
    Collected in September 2003 by Fei-Fei Li, Marco Andreetto, 
    and Marc 'Aurelio Ranzato.  
    The size of each image is roughly 300 x 200 pixels.

    We have carefully clicked outlines of each object in these pictures, 
    these are included under the 'Annotations.tar'.
    There is also a matlab script to view the annotaitons, 'show_annotations.m'.
    
    Attention: if exist dirs `root/caltech256`, api will delete it and create it.
    Data storage directory:
    root = `/user/.../mydata`
    caltech256 data: 
    `root/caltech256/train/007.bat/xx.jpg`
    `root/caltech256/train/010.beer-mug/xx.ipg`
    `root/caltech256/train/064.elephant-101/xx.jpg`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/caltech256`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/caltech256`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'caltech256', make_root_dir=False)
    url = "http://www.vision.caltech.edu/Image_Datasets/Caltech256/256_ObjectCategories.tar"
    rq.files(url, path_join(root, url.split('/')[-1]))
    un_tar(path_join(root, url.split('/')[-1]), task_path)
    tf.io.gfile.rename(path_join(task_path, '256_ObjectCategories'), path_join(task_path, 'train'))
    tf.io.gfile.remove(path_join(root, '256_ObjectCategories.tar'))
    print('caltech256 dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
