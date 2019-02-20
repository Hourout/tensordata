import os
import tensorflow as tf

def assert_dirs(root, root_dir=None, delete=True):
    assert tf.io.gfile.isdir(root), '{} should be directory.'.format(root)
    if root_dir is not None:
        assert isinstance(root_dir, str), '{} should be str.'.format(root_dir)
        task_path = os.path.join(root, root_dir)
        if tf.io.gfile.exists(task_path):
            if delete:
                tf.io.gfile.rmtree(task_path)
                tf.io.gfile.makedirs(task_path)
        else:
            tf.io.gfile.makedirs(task_path)
        return task_path
    else:
        if not tf.io.gfile.exists(root):
            tf.io.gfile.makedirs(root)
        return root
