import zipfile
import tensorflow as tf

def zip_files(files, zip_name):
    """Compression files
    
    Args:
        files: str or list
               if str, files should be file path;
               if list, files should be file path list.
        zip_name: str, compression files name.
    Return:
        zip_name: str, compression files name.
    """
    assert isinstance(zip_name, str), 'zip_name should be str.'
    if isinstance(files, str):
        assert not tf.gfile.IsDirectory(files), 'Files should be file path.'
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
            z.write(files)
    elif isinstance(files, list):
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
            for file in files:
                assert not tf.gfile.IsDirectory(file), 'Elements in the list should be file path.'
                z.write(file)
    else:
        raise ValueError('Files should be type of str or list.')
    return zip_name
