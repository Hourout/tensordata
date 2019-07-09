import io
import time
import requests
import concurrent
import pandas as pd
from tensordata.utils._utils import assert_dirs, path_join
import tensordata.utils.request as rq

def _request_txt(url):
    s = requests.get(url).content
    t = pd.read_csv(io.StringIO(s.decode('utf-8')))
    return t

def movielens(root):
    """Movielens movies datasets.
    
    This dataset (ml-latest) describes 5-star rating and free-text tagging 
    activity from [MovieLens](http://movielens.org), a movie recommendation service. 
    It contains 27753444 ratings and 1108997 tag applications across 58098 movies. 
    These data were created by 283228 users between January 09, 1995 and September 26, 2018. 
    This dataset was generated on September 26, 2018.

    Users were selected at random for inclusion. All selected users had rated at least 1 movies. 
    No demographic information is included. Each user is represented by an id, 
    and no other information is provided.

    The data are contained in the files `genome-scores.csv`, `genome-tags.csv`,
    `links.csv`, `movies.csv`, `ratings.csv` and `tags.csv`. 
    More details about the contents and use of all these files follows.

    This is a *development* dataset. As such, 
    it may change over time and is not an appropriate dataset for shared research results. 
    See available *benchmark* datasets if that is your intent.

    This and other GroupLens data sets are publicly available for download at <http://grouplens.org/datasets/>.
    
    Data storage directory:
    root = `/user/.../mydata`
    movielens data: 
    `root/movielens/movielens.json`
    `root/movielens/links.txt`
    `root/movielens/genome_tags.txt`
    `root/movielens/movies.txt`
    `root/movielens/genome_scores.txt`
    `root/movielens/ratings.txt`
    `root/movielens/tags.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/movielens`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/movielens`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'movielens')
    url_json = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/imdb/movielens.json'
    url_link_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/imdb/links.txt'
    url_genome_tags_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/imdb/genome_tags.txt'
    url_movies_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/imdb/movies.txt'
    url_genome_scores_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/imdb/genome_scores.txt'
    url_ratings_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/imdb/ratings.txt'
    url_tags_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/imdb/tags.txt'
    rq.json(url_json, path_join(task_path, 'movielens.json'))
    rq.table(url_link_txt, path_join(task_path, 'links.txt'))
    rq.table(url_movies_txt, path_join(task_path, 'movies.txt'))
    rq.table(url_genome_tags_txt, path_join(task_path, 'genome_tags.txt'))
    l = [url_genome_scores_txt[:-4]+str(i)+url_genome_scores_txt[-4:] for i in range(16)]
    with concurrent.futures.ProcessPoolExecutor() as excutor:
        data = pd.concat(excutor.map(_request_txt, l))
    data.to_csv(path_join(task_path, 'genome_scores.txt'), index=False)
    l = [url_ratings_txt[:-4]+str(i)+url_ratings_txt[-4:] for i in range(21)]
    with concurrent.futures.ProcessPoolExecutor() as excutor:
        data = pd.concat(excutor.map(_request_txt, l))
    data.to_csv(path_join(task_path, 'ratings.txt'), index=False)
    l = [url_tags_txt[:-4]+str(i)+url_tags_txt[-4:] for i in range(2)]
    with concurrent.futures.ProcessPoolExecutor() as excutor:
        data = pd.concat(excutor.map(_request_txt, l))
    data.to_csv(path_join(task_path, 'tags.txt'), index=False)
    print('movielens dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
