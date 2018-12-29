import os
import time
import tensorflow as tf

def get_arxiv(root, ids):
    """Download paper from https://arxiv.org, the file format is pdf.
    
    Data storage directory:
    root = `/user/.../mydata`
    `ids`.pdf data: 
    `root/arxiv/`ids`.pdf`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/arxiv`,
              root should be `/user/.../mydata`.
        ids: str, arxiv paper id.
             example:ids = '1605.09782' mean you want get paper links https://arxiv.org/abs/1605.09782.
    Returns:
        Store the absolute path of the data directory, is `root/arxiv`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'arxiv')
    if not tf.gfile.Exists(task_path):
        tf.gfile.MakeDirs(task_path)
    url = 'https://arxiv.org/pdf/'+str(ids)+'.pdf'
    tf.keras.utils.get_file(os.path.join(task_path, str(ids)+'.pdf'), url)
    print(str(ids)+'.pdf dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
