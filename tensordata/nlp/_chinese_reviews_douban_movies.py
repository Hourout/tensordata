import os
import time
import requests
import concurrent
import pandas as pd
import tensorflow as tf

def _request_txt(url):
    s = requests.get(url).content
    t = pd.read_csv(io.StringIO(s.decode('utf-8')))
    return t

def chinese_reviews_douban_movies(root):
    """Chinese douban movies reviews datasets.
        
    Chinese douban movies reviews datasets Includes 28 movies, 
    over 700,000 users, over 2 million ratings.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_reviews_douban_movies data: 
    `root/chinese_reviews_douban_movies/chinese_reviews_douban_movies.json`
    `root/chinese_reviews_douban_movies/ratings.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_reviews_douban_movies`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_reviews_douban_movies`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_reviews_douban_movies')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url_json = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_reviews_douban_movies/chinese_reviews_douban_movies.json'
    url_movies = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_reviews_douban_movies/movies.txt'
    url_ratings = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_reviews_douban_movies/ratings.txt'
    with open(os.path.join(task_path, 'chinese_reviews_douban_movies.json'), 'w') as outfile:
        json.dump(requests.get(url_json).json(), outfile, ensure_ascii=False)
        outfile.write('\n')
    data = pd.read_csv(io.StringIO(requests.get(url_movies).content.decode('utf-8')))
    data.to_csv(os.path.join(task_path, 'movies.txt'), index=False)
    l = [url_ratings[:-4]+str(i)+url_ratings[-4:] for i in range(13)]
    with concurrent.futures.ProcessPoolExecutor() as excutor:
        data = pd.concat(excutor.map(_request_txt, l))
    data.to_csv(os.path.join(task_path, 'ratings.txt'), index=False)
    print('chinese_reviews_douban_movies dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
