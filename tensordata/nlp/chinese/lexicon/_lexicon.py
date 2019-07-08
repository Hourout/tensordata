import time
from tensordata.utils._utils import assert_dirs, path_join
import tensordata.utils.request as rq

__all__ = ['it', 'animal', 'medical', 'famous_person', 'placename', 'antonym', 
           'synonym', 'privative', 'idiom', 'pornography', 'car',
]

def it(root):
    """Chinese lexicon IT datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_it dataset contains 16000+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_lexicon_it data: 
    `root/chinese_lexicon_it/chinese_lexicon_it.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_it`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_it`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_lexicon_it')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_it.txt"
    rq.table(url, path_join(task_path, 'chinese_lexicon_it.txt'))
    print('chinese_lexicon_it dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def animal(root):
    """Chinese lexicon animal datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_animal dataset contains 17200+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_lexicon_animal data: 
    `root/chinese_lexicon_animal/chinese_lexicon_animal.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_animal`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_animal`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_lexicon_animal')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_animal.txt"
    rq.table(url, path_join(task_path, 'chinese_lexicon_animal.txt'))
    print('chinese_lexicon_animal dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def medical(root):
    """Chinese lexicon medical datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_medical dataset contains 18700+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_lexicon_medical data: 
    `root/chinese_lexicon_medical/chinese_lexicon_medical.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_medical`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_medical`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_lexicon_medical')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_medical.txt"
    rq.table(url, path_join(task_path, 'chinese_lexicon_medical.txt'))
    print('chinese_lexicon_medical dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def famous_person(root):
    """Chinese lexicon famous person datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_famous_person dataset contains 13600+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_lexicon_famous_person data: 
    `root/chinese_lexicon_famous_person/chinese_lexicon_famous_person.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_famous_person`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_famous_person`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_lexicon_famous_person')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_famous_person.txt"
    rq.table(url, path_join(task_path, 'chinese_lexicon_famous_person.txt'))
    print('chinese_lexicon_famous_person dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def placename(root):
    """Chinese lexicon placename datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_placename dataset contains 44800+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_lexicon_placename data: 
    `root/chinese_lexicon_placename/chinese_lexicon_placename.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_placename`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_placename`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_lexicon_placename')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_placename.txt"
    rq.table(url, path_join(task_path, 'chinese_lexicon_placename.txt'))
    print('chinese_lexicon_placename dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def antonym(root):
    """Chinese lexicon antonym datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_annonym dataset contains 18700+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_lexicon_antonym data: 
    `root/chinese_lexicon_antonym/chinese_lexicon_antonym.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_antonym`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_antonym`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_lexicon_antonym')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_antonym.txt"
    rq.table(url, path_join(task_path, 'chinese_lexicon_antonym.txt'))
    print('chinese_lexicon_antonym dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def synonym(root):
    """Chinese lexicon synonym datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_synonym dataset contains 17800+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_lexicon_synonym data: 
    `root/chinese_lexicon_synonym/chinese_lexicon_synonym.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_synonym`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_synonym`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_lexicon_synonym')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_synonym.txt"
    rq.table(url, path_join(task_path, 'chinese_lexicon_synonym.txt'))
    print('chinese_lexicon_synonym dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def privative(root):
    """Chinese lexicon privative datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_privative dataset contains 1500+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_lexicon_privative data: 
    `root/chinese_lexicon_privative/chinese_lexicon_privative.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_privative`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_privative`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_lexicon_privative')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_privative.txt"
    rq.table(url, path_join(task_path, 'chinese_lexicon_privative.txt'))
    print('chinese_lexicon_privative dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def idiom(root):
    """Chinese lexicon idiom datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_idiom dataset contains 8500+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_lexicon_idiom data: 
    `root/chinese_lexicon_idiom/chinese_lexicon_idiom.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_idiom`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_idiom`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_lexicon_idiom')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_idiom.txt"
    rq.table(url, path_join(task_path, 'chinese_lexicon_idiom.txt'))
    print('chinese_lexicon_idiom dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def pornography(root):
    """Chinese lexicon pornography datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_pornography dataset contains 930+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_lexicon_pornography data: 
    `root/chinese_lexicon_pornography/chinese_lexicon_pornography.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_pornography`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_pornography`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_lexicon_pornography')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_pornography.txt"
    rq.table(url, path_join(task_path, 'chinese_lexicon_pornography.txt'))
    print('chinese_lexicon_pornography dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path

def car(root):
    """Chinese lexicon car datasets.
    
    datasets url:`https://github.com/fighting41love/funNLP`
    
    chinese_lexicon_car dataset contains 3700+ samples.
    
    Data storage directory:
    root = `/user/.../mydata`
    chinese_lexicon_car data: 
    `root/chinese_lexicon_car/chinese_lexicon_car.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/chinese_lexicon_car`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/chinese_lexicon_car`.
    """
    start = time.time()
    task_path = assert_dirs(root, 'chinese_lexicon_car')
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_car.txt"
    rq.table(url, path_join(task_path, 'chinese_lexicon_car.txt'))
    print('chinese_lexicon_car dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
