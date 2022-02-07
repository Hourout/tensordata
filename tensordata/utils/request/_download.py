import io
import json as jsons

import requests
import pandas as pd
from linora.utils import Progbar

__all__ = ['json', 'table', 'files']

def json(url, root_file):
    """Request url that file is json file.
    
    Args:
        url: str, request url.
        root_file: str, downloaded and saved file name.
    Return:
        root_file: str, downloaded and saved file name.
    """
    assert root_file[-5:]=='.json', '`root_file` should be `xxx.json`'
    s = requests.get(url)
    with open(root_file, 'w') as f:
        jsons.dump(s.json(), f, ensure_ascii=False)
    return root_file

def table(url, root_file, sep=',', names=None):
    """Request url that file is txt file.
    
    Args:
        url: str, request url.
        root_file: str, downloaded and saved file name.
        sep: str, field delimiter for the output file.
    Return:
        root_file: str, downloaded and saved file name.
    """
    s = requests.get(url).content
    data = pd.read_csv(io.StringIO(s.decode('utf-8')), names=names, dtype='str')
    data.to_csv(root_file, index=False, sep=sep)
    return root_file

def files(url, root_file, retries=3, verbose=1, chunk_size=1024):
    """Request url and download to root_file.
    
    Args:
        url: str, request url.
        root_file: str, downloaded and saved file name.
        retries: retry counts.
        verbose: Verbosity mode, 0 (silent), 1 (verbose)
        chunk_size: the number of bytes it should read into memory.
    Return:
        root_file: str, downloaded and saved file name.
    """
    for i in range(retries):
        try:
            r = requests.get(url, stream=True)
            content_type = r.headers.get('Content-Length')
            total_size = None if content_type is None else int(content_type.strip())
            p = Progbar(total_size, verbose=verbose)
            down_size = 0
            with open(root_file, 'wb') as f:
                for chunk in r.iter_content(chunk_size):
                    p.add(chunk_size)
                    f.write(chunk)
                    down_size += len(chunk)
            if down_size==total_size:
                break
            else:
                raise 'download failed'
        except:
            if i==retries-1:
                raise f'{url} download failed'
    return root_file
