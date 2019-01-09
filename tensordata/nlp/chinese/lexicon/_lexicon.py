import io
import os
import time
import requests
import pandas as pd
import tensorflow as tf

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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_it')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_it.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_it.txt'), index=False, header=None)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_animal')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_animal.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_animal.txt'), index=False, header=None)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_medical')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_medical.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_medical.txt'), index=False, header=None)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_famous_person')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_famous_person.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None, sep='\t')[0]
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_famous_person.txt'), index=False, header=None)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_placename')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_placename.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_placename.txt'), index=False, header=None)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_antonym')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_antonym.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_antonym.txt'), index=False, header=None)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_synonym')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_synonym.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None, sep='\n')
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_synonym.txt'), index=False, header=None)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_privative')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_privative.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_privative.txt'), index=False, header=None)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_idiom')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_idiom.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_idiom.txt'), index=False, header=None)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_pornography')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_pornography.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_pornography.txt'), index=False, header=None)
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
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'chinese_lexicon_car')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url = "https://raw.githubusercontent.com/Hourout/datasets/master/nlp/chinese_lexicon/chinese_lexicon_car.txt"
    data = pd.read_csv(io.StringIO(requests.get(url).content.decode('utf-8')), header=None)
    data.to_csv(os.path.join(task_path, 'chinese_lexicon_car.txt'), index=False, header=None)
    print('chinese_lexicon_car dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
