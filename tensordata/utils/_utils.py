import tensorflow as tf

def assert_dirs(root, root_dir=None, delete=True):
    assert tf.gfile.IsDirectory(root), '{} should be directory.'.format(root)
    if root_dir is not None:
        assert isinstance(root_dir, str), '{} should be str.'.format(root_dir)
        task_path = os.path.join(root, root_dir)
        if tf.gfile.Exists(task_path):
            if delete:
                tf.gfile.DeleteRecursively(task_path)
                tf.gfile.MakeDirs(task_path)
        else:
            tf.gfile.MakeDirs(task_path)
        return task_path
    else:
        if not tf.gfile.Exists(root):
            tf.gfile.MakeDirs(root)
        return root
