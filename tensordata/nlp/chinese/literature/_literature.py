import tensorflow as tf

__all__ = ['shijing', 'youmengying']

def shijing(root):
    """Shijing dataset from Chinese classical literature.
    
    The earliest poetry collection in China, The Book of Songs, 
    is the earliest collection of poems in ancient Chinese poetry. 
    It collects poems from the early Western Zhou Dynasty to the 
    middle of spring and autumn (the first 11th century to the 
    first six centuries), including 311 articles, 
    of which 6 The article is a poem, that is, only the title, 
    no content, called the six poems of the poems 
    (Nan, Baihua, Huaying, Yukang, Chongwu, Yuyi),
    reflecting the period from the beginning of the week to 
    the late Zhou Dynasty for about five hundred years.
    
    Data storage directory:
    root = `/user/.../mydata`
    shijing data: 
    `root/shijing/shijing.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/shijing`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/shijing`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'shijing')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/shijing.json'
    tf.keras.utils.get_file(os.path.join(task_path, url.split('/')[-1]), url)
    print('shijing dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def youmengying(root):
    """Youmengying dataset from Chinese classical literature.
    
    "You Meng Ying" is an anthology of Zhang Chao's 
    creations by Qing Dynasty writers.
    
    Data storage directory:
    root = `/user/.../mydata`
    youmengying data: 
    `root/youmengying/youmengying.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/youmengying`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/youmengying`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'youmengying')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/youmengying.json"
    tf.keras.utils.get_file(os.path.join(task_path, url.split('/')[-1]), url)
    print('youmengying dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
