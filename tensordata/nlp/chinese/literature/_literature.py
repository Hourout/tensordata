import os
import time
import tensorflow as tf
from tensordata.utils.compress import un_bz2

__all__ = ['shijing', 'youmengying', 'huajianji', 'poetry_nantang_erzhu', 'lunyu']

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

def huajianji(root):
    """Huajianji dataset from Chinese classical literature.
    
    "Hua Jian Ji" is a collection of Chinese poetry 
    compiled during the Five Dynasties and Ten Kingdoms period. 
    It is also the first collection of literati in the history of literature. 
    It was edited by Zhao Chongxi, a later monk. 
    The book contains 18 classic works of poetry by Wen Tingjun and Wei Zhuang. 
    It concentrates and typically reflects the subject orientation, 
    aesthetic taste, physical style and artistic achievement 
    of the human creation in the early word history.
    
    Data storage directory:
    root = `/user/.../mydata`
    huajianji data: 
    `root/huajianji/huajianji.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/huajianji`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/huajianji`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'huajianji')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/huajianji.json"
    tf.keras.utils.get_file(os.path.join(task_path, url.split('/')[-1]), url)
    print('huajianji dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def poetry_SouthernTang(root):
    """poetry_SouthernTang dataset from Chinese classical literature.
    
    "The Southern Tang Dynasty's two main words", 
    is the Southern Tang Dynasty master Li Jing, the latter master Li Yu. 
    The book was written in the Southern Song Dynasty, 
    and later generations have been compiled, 
    and later generations have written various versions.
    
    Data storage directory:
    root = `/user/.../mydata`
    poetry_SouthernTang data: 
    `root/poetry_SouthernTang/poetry_SouthernTang.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/poetry_SouthernTang`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/poetry_SouthernTang`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'poetry_SouthernTang')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/nantang_erzhu_poetry.json"
    tf.keras.utils.get_file(os.path.join(task_path, 'poetry_SouthernTang.json'), url)
    print('poetry_SouthernTang dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def lunyu(root):
    """Lunyu dataset from Chinese classical literature.
    
    The Chinese Confucian classics, "The Analects of Confucius" is 
    a collection of quotations of Confucius and his disciples. 
    It was written by Confucius disciples and re-transmission disciples, 
    and was written in the early period of the Warring States Period. 
    The book consists of 20 chapters and 492 chapters. 
    It is mainly composed of quotations and supplemented by narratives. 
    It mainly records the words and deeds of Confucius and his disciples, 
    and more concentratedly reflects Confucius' political opinions, 
    ethical thoughts, moral concepts and educational principles. 
    This book is one of the classic works of Confucianism. 
    It is also called "Four Books" with "University", 
    "The Doctrine of the Mean" and "Mencius",
    plus "The Book of Songs", "Shangshu", "Book of Rites", 
    "Zhou Yi", "Spring and Autumn", collectively called "four books". Five Classics."
    
    Data storage directory:
    root = `/user/.../mydata`
    lunyu data: 
    `root/lunyu/lunyu.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/lunyu`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/lunyu`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'lunyu')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/lunyu.json'
    tf.keras.utils.get_file(os.path.join(task_path, url.split('/')[-1]), url)
    print('lunyu dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path