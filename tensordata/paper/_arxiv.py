import time

import tensordata.gfile as gfile
import tensordata.utils.request as rq

__all__ = ['arxiv']

def arxiv(root, ids, new_name=None):
    """Download paper from https://arxiv.org, the file format is pdf.
    
    Data storage directory:
    root = `/user/.../mydata`
    `ids`.pdf data: 
    `root/arxiv/`ids`.pdf` or `root/arxiv/`new_name`.pdf`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/arxiv`,
              root should be `/user/.../mydata`.
        ids: str, arxiv paper id.
             example:ids = '1605.09782' mean you want get paper links https://arxiv.org/abs/1605.09782.
        new_name: str, default None. if not None, download file path is `root/arxiv/new_name.pdf`.
    Returns:
        Store the absolute path of the data directory, is `root/arxiv`.
    """
    start = time.time()
    assert gfile.isdir(root), '`root` should be directory.'
    assert isinstance(ids, str), '`ids` type should be str.'
    if new_name is None:
        task_path = gfile.path_join(root, 'arxiv', ids+'.pdf')
    else:
        task_path = gfile.path_join(root, 'arxiv', new_name+'.pdf')
    gfile.makedirs(gfile.path_join(root, 'arxiv'))
    gfile.remove(task_path)
    url = 'https://arxiv.org/pdf/'+str(ids)+'.pdf'
    rq.files(url, task_path)
    print('arxiv paper download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
