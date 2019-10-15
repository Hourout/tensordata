import os
import bz2
import gzip
import zipfile
import tarfile
import rarfile
import tensorflow as tf
from tensordata.utils._utils import path_join

__all__ = ['folder_zip', 'folder_tar']

def folder_zip(folder, zip_name):
    """Compress all files in the folder to .zip.
    
    Args:
        folder: str, folder should be folder path.
        zip_name: str, compression files name.
    Return:
        zip_name: str, compression files name.
    """
    assert tf.io.gfile.isdir(folder), '`folder` should be folder path.'
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
        for dirpath, dirnames, filenames in tf.io.gfile.walk(folder):
            fpath = dirpath.replace(startdir, '')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                z.write(path_join(dirpath, filename), path_join(fpath, filename))
    return zip_name

def folder_tar(folder, tar_name):
    """Compress all files in the folder to .tar.
    
    Args:
        folder: str, folder should be folder path.
        zip_name: str, compression files name.
    Return:
        zip_name: str, compression files name.
    """
    assert tf.io.gfile.isdir(folder), '`folder` should be folder path.'
    with tarfile.open(tar_name, 'w') as tar:
        for dirpath, dirnames, filenames in tf.io.gfile.walk(tar_name):
            fpath = dirpath.replace(startdir, '')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                tar.add(path_join(dirpath, filename), path_join(fpath, filename))
    return tar_name
