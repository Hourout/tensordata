import io
import requests
import subprocess
import tensorflow as tf


__all__ = ['library_list', 'library_update', 'library_get']

def library_list(name=None, py=3):
    assert name is None or isinstance(name, str) or isinstance(name, list), "`name` should be None or str or list."
    assert py in [2, 3], "`py` should be in one of [2, 3]."
    
    cmd = "pip3 list" if py==3 else "pip2 list"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = [i.strip().split(' ') for i in s.decode('utf-8').split('\r\n')[2:-1]]
    s = {i[0]: i[-1] for i in s}
    if name is not None:
        try:
            if isinstance(name, str):
                name = [name]
            s = {i:s[i] for i in name}
        except:
            raise ValueError("{} is not in local libraries".format(name))
    return s

def library_update(name=None, version=None, py=3):
    assert py in [2, 3], "`py` should be in one of [2, 3]."
    old_lib = library_list(name=name)
    if version is not None:
        if isinstance(version, str):
            version = [version]
        elif isinstance(version, list):
            pass
        else:
            raise ValueError("`version` should be None or str or list.")
        assert len(old_lib)==len(version)
        for (dist, ver) in zip(name, version):
            if py==3:
                subprocess.call("pip3 install --user --upgrade " + dist + "==" + ver, shell=True)
            else:
                subprocess.call("pip2 install --user --upgrade " + dist + "==" + ver, shell=True)
    else:
        for dist in old_lib:
            if py==3:
                subprocess.call("pip3 install --user --upgrade " + dist, shell=True)
            else:
                subprocess.call("pip2 install --user --upgrade " + dist, shell=True)
    new_lib = library_list(name=name)
    lib = {i:{'old_version': old_lib[i], "new_version":new_lib[i]} for i in old_lib}
    return lib

def library_get(root, lib=None, name=None, version=None):
    if lib is None and name is None:
        raise ValueError("`lib` and `name` at least one is not None.")
    assert lib is None or isinstance(lib, str), "`lib` should be None or str."
    assert name is None or isinstance(name, str), "`name` should be None or str."
    assert version is None or isinstance(version, str), "`version` should be None or str."
    qinghua = "https://pypi.tuna.tsinghua.edu.cn"
    if lib is not None:
        s = requests.get(qinghua+'/simple/'+lib.split('-')[0]).content
        s = list(io.StringIO(s.decode('utf-8')))
        s = [(qinghua+'/'+i[i.find('packages'):]).split('"')[0] for i in s if lib in i]
    else:
        s = requests.get(qinghua+'/simple/'+name).content
        s = list(io.StringIO(s.decode('utf-8')))
        if version is None:
            s = [(qinghua+'/'+i[i.find('packages'):]).split('"')[0] for i in s if name in i]
        else:
            s = [(qinghua+'/'+i[i.find('packages'):]).split('"')[0] for i in s if name in i and version in i]
    for i in s:
        local_file = i.split('/')[-1]
        local_file = root+'/'+local_file[:local_file.find('#')]
        tf.keras.utils.get_file(local_file, i)
    return root
