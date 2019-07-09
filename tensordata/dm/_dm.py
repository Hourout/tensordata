import time
from tensordata.utils._utils import assert_dirs, path_join
import tensordata.utils.request as rq


__all__ = ['boston_housing', 'adult', 'wine', 'abalone', 'arrhythmia']

def boston_housing(root):
    """Housing Values in Suburbs of Boston
    
    Harrison, D. and Rubinfeld, D.L. (1978) Hedonic prices and the demand for 
    clean air. J. Environ. Economics and Management 5, 81–102.
    
    Belsley D.A., Kuh, E. and Welsch, R.E. (1980) Regression Diagnostics. 
    Identifying Influential Data and Sources of Collinearity. New York: Wiley.
    
    Data storage directory:
    root = `/user/.../mydata`
    boston_housing data: 
    `root/boston_housing/boston_housing.txt`
    `root/boston_housing/boston_housing.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/boston_housing`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/boston_housing`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'boston_housing')
    url_json = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/boston_house/boston_housing.json'
    url_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/boston_house/boston_housing.txt'
    rq.json(url_json, path_join(task_path, 'boston_housing.json'))
    rq.table(url_txt, path_join(task_path, 'boston_housing.txt'))
    print('boston_housing dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def adult(root):
    """This data was extracted from the census bureau database found at
    http://www.census.gov/ftp/pub/DES/www/welcome.html
    
    48842 instances, mix of continuous and discrete    (train=32561, test=16281)
    45222 if instances with unknown values are removed (train=30162, test=15060)
    Duplicate or conflicting instances : 6
    Class probabilities for adult.all file
    Probability for the label '>50K'  : 23.93% / 24.78% (without unknowns)
    Probability for the label '<=50K' : 76.07% / 75.22% (without unknowns)
    
    Data storage directory:
    root = `/user/.../mydata`
    adult data: 
    `root/adult/adult.txt`
    `root/adult/adult.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/adult`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/adult`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'adult')
    url_json = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/adult/adult.json'
    url_txt = 'https://raw.githubusercontent.com/Hourout/datasets/master/dm/adult/adult.txt'
    rq.json(url_json, path_join(task_path, 'adult.json'))
    rq.table(url_txt, path_join(task_path, 'adult.txt'))
    print('adult dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def wine(root):
    """Title of Database: Wine recognition data
    Updated Sept 21, 1998 by C.Blake : Added attribute information
    
    These data are the results of a chemical analysis of
    wines grown in the same region in Italy but derived from three
    different cultivars.
    The analysis determined the quantities of 13 constituents
    found in each of the three types of wines. 
    
    Number of Instances
    class 1 59
    class 2 71
    class 3 48
    
    Data storage directory:
    root = `/user/.../mydata`
    wine data: 
    `root/wine/wine.txt`
    `root/wine/wine.json`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/wine`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/wine`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'wine')
    url_introduce = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.names'
    url_txt = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
    rq.files(url_introduce, path_join(task_path, 'introduce.txt'), verbose=0)
    rq.table(url_txt, path_join(task_path, 'wine.txt'),
             names=['label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium',
                    'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                    'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline'])
    print('wine dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def abalone(root):
    """Predicting the age of abalone from physical measurements.
    
    The age of abalone is determined by cutting the shell through the cone, 
    staining it, and counting the number of rings through a microscope -- a boring and
    time-consuming task.  Other measurements, which are easier to obtain, are
    used to predict the age.  Further information, such as weather patterns
    and location (hence food availability) may be required to solve the problem.
    
    Data storage directory:
    root = `/user/.../mydata`
    abalone data: 
    `root/abalone/abalone.txt`
    `root/abalone/introduce.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/abalone`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/abalone`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'abalone')
    url_introduce = 'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.names'
    url_txt = 'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
    rq.files(url_introduce, path_join(task_path, 'introduce.txt'), verbose=0)
    rq.table(url_txt, path_join(task_path, 'abalone.txt'),
             names=['Sex', 'Length', 'Diameter', 'Height' 'Whole_weight', 
                    'Shucked_weight', 'Viscera_weight', 'Shell_weight', 'label'])
    print('abalone dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def arrhythmia(root):
    """Aarrhythmia datasets from http://archive.ics.uci.edu/ml/datasets/Arrhythmia.
    
    This database contains 279 attributes, 206 of which are linear
    valued and the rest are nominal. 
    
    Data storage directory:
    root = `/user/.../mydata`
    arrhythmia data: 
    `root/abalone/arrhythmia.txt`
    `root/abalone/introduce.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/arrhythmia`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/arrhythmia`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'arrhythmia')
    url_introduce = 'http://archive.ics.uci.edu/ml/machine-learning-databases/arrhythmia/arrhythmia.names'
    url_txt = 'http://archive.ics.uci.edu/ml/machine-learning-databases/arrhythmia/arrhythmia.data'
    rq.files(url_introduce, path_join(task_path, 'introduce.txt'), verbose=0)
    rq.table(url_txt, path_join(task_path, 'arrhythmia.txt'))
    print('arrhythmia dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
