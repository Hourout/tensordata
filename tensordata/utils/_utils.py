from tensorflow.io import gfile

def assert_dirs(root, root_dir=None, delete=True, make_root_dir=True):
    assert gfile.isdir(root), '{} should be directory.'.format(root)
    if root_dir is not None:
        assert isinstance(root_dir, str), '{} should be str.'.format(root_dir)
        task_path = root+'/'+root_dir
        if gfile.exists(task_path):
            if delete:
                gfile.rmtree(task_path)
                gfile.makedirs(task_path)
        else:
            if make_root_dir:
                gfile.makedirs(task_path)
        return task_path
    else:
        if not gfile.exists(root):
            gfile.makedirs(root)
        return root

def path_join(path, *paths):
    return eval(repr(os.path.join(path, *paths)).replace("\\", '/').replace("//", '/'))
