import tensorflow as tf

def assert_dirs(root, root_dir):
    assert tf.gfile.IsDirectory(root), '{} should be directory.'.format(root)
    assert isinstance(root_dir, str), '{} should be str.'.format(root_dir)
    task_path = os.path.join(root, root_dir)
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    return task_path
