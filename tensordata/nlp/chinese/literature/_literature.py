import time
import tensorflow as tf
from tensordata.utils.compress import un_bz2
from tensordata.utils._utils import assert_dirs, path_join
import tensordata.utils.request as rq

__all__ = ['shijing', 'youmengying', 'huajianji', 'poetry_SouthernTang', 'lunyu',
           'poet_tang', 'poet_song', 'ci_song'
          ]

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
    task_path = assert_dirs(root, 'shijing')
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/shijing.json'
    rq.files(url, path_join(task_path, url.split('/')[-1]))
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
    task_path = assert_dirs(root, 'youmengying')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/youmengying.json"
    rq.files(url, path_join(task_path, url.split('/')[-1]))
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
    task_path = assert_dirs(root, 'huajianji')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/huajianji.json"
    rq.files(url, path_join(task_path, url.split('/')[-1]))
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
    task_path = assert_dirs(root, 'poetry_SouthernTang')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/nantang_erzhu_poetry.json"
    rq.files(url, path_join(task_path, 'poetry_SouthernTang.json'))
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
    task_path = assert_dirs(root, 'lunyu')
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/lunyu.json'
    rq.files(url, path_join(task_path, url.split('/')[-1]))
    print('lunyu dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def poet_tang(root):
    """Tang_poet dataset from Chinese classical literature.
    
    "Full Tang Poetry" is the 44th year of Qing Emperor Kangxi (1705), 
    Peng Dingqiu, Shen Sanzeng, Yang Zhongna, Wang Shizhen, Wang Wei, 
    Yu Mei, Xu Shuben, Che Dingjin, Pan Conglu, and Cha Yu 
    "There are more than 48,900 poems, more than 2,200 people,"
    a total of 900 volumes, 12 volumes of catalogues.
    
    Data storage directory:
    root = `/user/.../mydata`
    poet_tang data: 
    `root/poet_tang/poet_tang.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/poet_tang`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/poet_tang`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'poet_tang')
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/poetry_tang.json.bz2'
    rq.files(url, path_join(task_path, 'poet_tang.json.bz2'))
    un_bz2(path_join(task_path, 'poet_tang.json.bz2'))
    tf.io.gfile.remove(path_join(task_path, 'poet_tang.json.bz2'))
    print('poet_tang dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def poet_song(root):
    """Song_poet dataset from Chinese classical literature.
    
    "Full Song Poetry" After the high prosperity of Tang poetry, 
    Song poetry has new development and creation in ideological 
    content and artistic expression. 
    Many excellent writers have appeared, 
    and many schools have been formed, 
    which have produced poetry development in Yuan, 
    Ming and Qing. A far-reaching impact.
    
    Data storage directory:
    root = `/user/.../mydata`
    poetry_song data: 
    `root/poet_song/poet_song.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/poet_song`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/poet_song`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'poet_song')
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/poetry_song.json.bz2'
    rq.files(url, path_join(task_path, 'poet_song.json.bz2'))
    un_bz2(path_join(task_path, 'poet_song.json.bz2'))
    tf.io.gfile.remove(path_join(task_path, 'poet_song.json.bz2'))
    print('poet_song dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def ci_song(root):
    """Song_ci dataset from Chinese classical literature.
    
    "The Song of the Whole Song" is one of the most important 
    achievements of ancient books in China in the past 100 years. 
    Song poetry and Tang poetry are the artistic peaks of 
    Chinese classical poetry. The "Full Tang Poetry" edited in 
    the Qing Dynasty is a household name, and now it is newly 
    compiled "Full Song Ci", which is called the double shackles 
    of Chinese literature. The book has a total of five volumes, 
    a collection of words from the Song Dynasty for three hundred years.
    
    Data storage directory:
    root = `/user/.../mydata`
    ci_song data: 
    `root/ci_song/ci_song.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/ci_song`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/ci_song`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'ci_song')
    url = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/wenxue/ci_song.json'
    rq.files(url, path_join(task_path, url.split('/')[-1]))
    print('ci_song dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
