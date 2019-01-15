import subprocess


__all__ = ['freeze', 'upgrade', 'upgradeable', 'install', 'mirror', 'file']

pypi = {'pip':'https://pypi.org/simple'
        'tsinghua': 'https://pypi.tuna.tsinghua.edu.cn/simple',
        'aliyun': 'https://mirrors.aliyun.com/pypi/simple',
        'ustc':'https://mirrors.ustc.edu.cn/pypi/web/simple'}

def freeze(name=None, py=3):
    """List all python libraries.
    
    Args:
        name: str or list. libraries name.
        py: python environment.one of [2, 3].
    Return:
        a dict of python libraries version.
    """
    assert name is None or isinstance(name, (str, list)), "`name` should be None or str or list."
    assert py in [2, 3], "`py` should be in one of [2, 3]."
    cmd = "pip3 freeze" if py==3 else "pip2 freeze"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = [i.split('==') for i in s.decode('utf-8').split('\r\n')[:-1]]
    s = {i[0]: i[1] for i in s}
    if name is not None:
        try:
            if isinstance(name, str):
                name = [name]
            s = {i:s[i] for i in name}
        except:
            raise ValueError("{} is not in local libraries".format(name))
    return s

def upgrade(name=None, version=None, py=3, mirror='pip'):
    """Upgrade python libraries.
    
    Args:
        name: str or list. libraries name.
        version: str or list. libraries version name.
        py: python environment.one of [2, 3].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
    Return:
        a dict of python libraries version.
    """
    assert py in [2, 3], "`py` should be in one of [2, 3]."
    assert version is None or isinstance(version, (str, list)), "`version` should be None or str or list."
    old_lib = freeze(name=name, py=py)
    if version is not None:
        if isinstance(version, str):
            version = [version]
        assert len(old_lib)==len(version), "`name` and `version` should be same number."
        for (dist, ver) in zip(name, version):
            if mirror in pypi:
                cmd = "pip" + str(py) +" install -i "+ pypi[mirror] + " --user --upgrade " + dist + "==" + ver
            else:
                cmd = "pip" + str(py) +" install -i "+ mirror + " --user --upgrade " + dist + "==" + ver
            subprocess.call(cmd, shell=True)
    else:
        for dist in old_lib:
            if mirror in pypi:
                cmd = "pip" + str(py) +" install -i "+ pypi[mirror] + " --user --upgrade " + dist
            else:
                cmd = "pip" + str(py) +" install -i "+ mirror + " --user --upgrade " + dist
            subprocess.call(cmd, shell=True)
    new_lib = freeze(name=name, py=py)
    lib = {i:{'old_version': old_lib[i], "new_version":new_lib[i]} for i in old_lib}
    return lib

def upgradeable(py=3):
    """Veiw upgradeable python libraries.
    
    Args:
        py: python environment.one of [2, 3].
    Return:
        a dict of python libraries version.
    """
    assert py in [2, 3], "`py` should be in one of [2, 3]."
    cmd = "pip" + str(py) +" list -o"
    a = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = [i.strip().split(' ') for i in a.decode('utf-8').split('\r\n')[2:-1]]
    s = [list(filter(lambda x:len(x)>0, i)) for i in s]
    s = {i[0]:{'version':i[1], 'latest':i[2], 'type':i[-1]} for i in s}
    return s

def install(name, version=None, py=3, mirror='pip'):
    """Install python libraries.
    
    Args:
        name: str or list. libraries name.
        version: str or list. libraries version name.
        py: python environment.one of [2, 3].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
    Return:
        a dict of python libraries version.
    """
    assert isinstance(name, str), "`name` should be str."
    assert version is None or isinstance(version, str), "`version` should be None or str."
    cmd = "pip" + str(py) +" install " + (name if vesion is None else name + "==" + version)
    if mirror in pypi:
        cmd = cmd + " -i "+ pypi[mirror]
    else:
        cmd = cmd + " -i "+ mirror
    subprocess.call(cmd, shell=True)
    return freeze(name=name, py=py)

def mirror(mirror='pip', py=3):
    """Set up pip mirrors on your machine.
    
    Args:
        py: python environment.one of [2, 3].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
    Return:
        pip cmd.
    """
    if mirror in pypi:
        upgrade(name='pip', py=py, mirror='pip')
        cmd = "pip" + str(py) +" config set global.index-url " + pypi[mirror]
    else:
        upgrade(name='pip', py=py, mirror='pip')
        cmd = "pip" + str(py) +" config set global.index-url " + mirror
    subprocess.call(cmd, shell=True)
    return cmd

def file(root, name, py=3, mirror='pip'):
    """Download python libraries to the specified folder.
    Args:
        root: str, dirs.
        name: str or list. libraries name.
        py: python environment.one of [2, 3].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
    Return:
        root: dirs.
    """
    assert isinstance(name, str), "`name` should be str."
    cmd = "pip" + str(py) +" download " + name + " -d " + root + " -i "+ (pypi[mirror] if mirror in pypi else mirror)
    subprocess.call(cmd, shell=True)
    return root
