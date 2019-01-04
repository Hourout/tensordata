import os
import bz2
import gzip
import zipfile
import tarfile
import rarfile
import tensorflow as tf

__all__ = ['files_zip', 'files_tar', 'files_bz2', 
           'folder_zip', 'folder_tar',
           'un_gz', 'un_tar', 'un_zip', 'un_rar', 'un_bz2']

def files_zip(files, zip_name):
    """Compression files to .zip.
    
    Args:
        files: str or list
               if str, files should be file path;
               if list, files should be file path list.
        zip_name: str, compression files name.
    Return:
        zip_name: str, compression files name.
    """
    assert isinstance(zip_name, str), '`zip_name` should be str.'
    if isinstance(files, str):
        assert not tf.gfile.IsDirectory(files), '`files` should be file path.'
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
            z.write(files)
    elif isinstance(files, list):
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
            for file in files:
                assert not tf.gfile.IsDirectory(file), 'Elements in the list should be file path.'
                z.write(file)
    else:
        raise ValueError('`files` should be type of str or list.')
    return zip_name

def files_tar(files, tar_name):
    """Compression files to .tar.
    
    Args:
        files: str or list
               if str, files should be file path;
               if list, files should be file path list.
        tar_name: str, compression files name.
    Return:
        tar_name: str, compression files name.
    """
    assert isinstance(tar_name, str), '`tar_name` should be str.'
    if isinstance(files, str):
        assert not tf.gfile.IsDirectory(files), '`files` should be file path.'
        with tarfile.TarFile(tar_name, 'w') as t:
            t.add(files)
    elif isinstance(files, list):
        with tarfile.TarFile(tar_name, 'w') as t:
            for file in files:
                assert not tf.gfile.IsDirectory(file), 'Elements in the list should be file path.'
                t.add(file)
    else:
        raise ValueError('`files` should be type of str or list.')
    return tar_name

def files_bz2(files, bz2_name):
    """Compression files to .bz2.
    
    Args:
        files: str or list
               if str, files should be file path;
               if list, files should be file path list.
        zip_name: str, compression files name.
    Return:
        zip_name: str, compression files name.
    """
    assert isinstance(bz2_name, str), '`bz2_name` should be str.'
    if isinstance(files, str):
        assert not tf.gfile.IsDirectory(files), '`files` should be file path.'
        with bz2.BZ2File(bz2_name, 'w') as b:
            with tf.gfile.GFile(files, 'rb') as f:
                b.write(f.read())
    elif isinstance(files, list):
        with bz2.BZ2File(bz2_name, 'w') as b:
            for file in files:
                assert not tf.gfile.IsDirectory(file), 'Elements in the list should be file path.'
                with tf.gfile.GFile(file, 'rb') as f:
                    b.write(f.read())
    else:
        raise ValueError('`files` should be type of str or list.')
    return bz2_name

def folder_zip(folder, zip_name):
    """Compress all files in the folder to .zip.
    
    Args:
        folder: str, folder should be folder path.
        zip_name: str, compression files name.
    Return:
        zip_name: str, compression files name.
    """
    assert tf.gfile.IsDirectory(folder), '`folder` should be folder path.'
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
        for dirpath, dirnames, filenames in tf.gfile.Walk(folder):
            fpath = dirpath.replace(startdir, '')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath+filename)
    return zip_name

def folder_tar(folder, tar_name):
    """Compress all files in the folder to .tar.
    
    Args:
        folder: str, folder should be folder path.
        zip_name: str, compression files name.
    Return:
        zip_name: str, compression files name.
    """
    assert tf.gfile.IsDirectory(folder), '`folder` should be folder path.'
    with tarfile.open(tar_name, 'w') as tar:
        for dirpath, dirnames, filenames in tf.gfile.Walk(tar_name):
            fpath = dirpath.replace(startdir, '')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                tar.add(os.path.join(dirpath, filename), fpath+filename)
    return tar_name

def un_gz(gz_file, ugz_name=None):
    """Uncompression .gz file.
    
    Args:
        gz_files: str, gz_file should be file path;
        ugz_name: str, uncompression files name.
    Return:
        ugz_name: str, uncompression files name.
    """
    assert gz_file[-3:]==".gz", '`gz_file` should be `xxx.gz`'
    if ugz_name is None:
        ugz_name = gz_file[:-3]
    with gzip.GzipFile(gz_file) as g_file:
        with tf.gfile.GFile(ugz_name, "w+") as f:
            f.write(g_file.read())
    return ugz_name

def un_tar(tar_file, utar_folder=None):
    """Uncompression .tar file
    
    Args:
        tar_files: str, tar_file should be file path;
        utar_folder: str, uncompression files name.
    Return:
        utar_folder: str, uncompression files name.
    """
    assert tar_file[-4:]==".tar", '`tar_file` should be `xxx.tar`'
    if utar_folder is None:
        utar_folder = tar_file[:-4]
    with tarfile.TarFile(tar_file, 'r') as tar:
        names = tar.getnames()
        for name in names:
            tar.extract(name, utar_folder)
    return utar_folder

def un_zip(zip_file, uzip_folder=None):
    """Uncompression .zip file
    
    Args:
        zip_files: str, zip_file should be file path;
        uzip_folder: str, uncompression files name.
    Return:
        uzip_folder: str, uncompression files name.
    """
    assert zip_file[-4:]==".zip", '`zip_file` should be `xxx.zip`'
    if uzip_folder is None:
        uzip_folder = zip_file[:-4]
    with zipfile.ZipFile(zip_file, 'r') as z:
        names = z.namelist()
        for name in names:
            z.extract(name, uzip_folder)
    return uzip_folder

def un_rar(rar_file, urar_folder=None):
    """Uncompression .rar file
    
    Args:
        rar_files: str, rar_file should be file path;
        urar_folder: str, uncompression files name.
    Return:
        urar_folder: str, uncompression files name.
    """
    assert rar_file[-4:]==".rar", '`rar_file` should be `xxx.rar`'
    if urar_folder is None:
        urar_folder = rar_file[:-4]
    with rarfile.RarFile(rar_file, 'r') as r:
        names = r.namelist()
        for name in names:
            r.extract(name, urar_folder)
    return urar_folder

def un_bz2(bz2_file, ubz2_folder=None):
    """Uncompression .bz2 file
    
    Args:
        rar_files: str, rar_file should be file path;
        urar_folder: str, uncompression files name.
    Return:
        urar_folder: str, uncompression files name.
    """
    assert bz2_file[-4:]==".bz2", '`bz2_file` should be `xxx.bz2`'
    if ubz2_folder is None:
        ubz2_folder = bz2_file[:-4]
    with bz2.BZ2File(bz2_file, 'r') as b:
        with tf.gfile.GFile(ubz2_folder, 'w') as f:
            f.write(b.readline())
    return ubz2_folder
