import subprocess


__all__ = ['freeze', 'upgrade', 'upgradeable', 'install', 'uninstall', 
           'mirror', 'file', 'show', 'search']

pypi = {'pip':"https://pypi.org/simple",
        'tsinghua': "https://pypi.tuna.tsinghua.edu.cn/simple",
        'aliyun': "https://mirrors.aliyun.com/pypi/simple",
        'ustc':"https://mirrors.ustc.edu.cn/pypi/web/simple"}

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
    cmd = "pip" + str(py) +" freeze"
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
                options one of ['pip', 'tsinghua', 'aliyun', 'ustc'],
                or you can set mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
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
            cmd = "pip" + str(py) +" install "+ " --user --upgrade " + dist + "==" + ver
            cmd = cmd + " -i "+ (pypi[mirror] if mirror in pypi else mirror)
            subprocess.call(cmd, shell=True)
    else:
        for dist in old_lib:
            cmd = "pip" + str(py) +" install "+ " --user --upgrade " + dist
            cmd = cmd + " -i "+ (pypi[mirror] if mirror in pypi else mirror)
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
                options one of ['pip', 'tsinghua', 'aliyun', 'ustc'],
                or you can set mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
    Return:
        a dict of python libraries version.
    """
    assert isinstance(name, str), "`name` should be str."
    assert version is None or isinstance(version, str), "`version` should be None or str."
    cmd = "pip" + str(py) +" install " + (name if version is None else name + "==" + version)
    cmd = cmd + " -i "+ (pypi[mirror] if mirror in pypi else mirror)
    subprocess.call(cmd, shell=True)
    return freeze(name=name, py=py)

def uninstall(name, py=3):
    """Uinstall python libraries.
    
    Args:
        name: str. libraries name.
        py: python environment.one of [2, 3].
    Return:
        uninstall log.
    """
    assert isinstance(name, str), "`name` should be str."
    assert py in [2, 3], "`py` should be in one of [2, 3]."
    cmd = "pip" + str(py) +" uninstall " + name + " -y"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    return s

def mirror(mirror='pip', py=3):
    """Set up pip mirrors on your machine.
    
    Args:
        py: python environment.one of [2, 3].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
                options one of ['pip', 'tsinghua', 'aliyun', 'ustc'],
                or you can set mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
    Return:
        mirror file path.
    """
    subprocess.call("pip" + str(py) +" install pip -U", shell=True)
    cmd = "pip" + str(py) +" config set global.index-url " + (pypi[mirror] if mirror in pypi else mirror)
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    return s

def file(root, name, py=3, mirror='pip'):
    """Download python libraries to the specified folder.
    Args:
        root: str, dirs.
        name: str or list. libraries name.
        py: python environment.one of [2, 3].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
                options one of ['pip', 'tsinghua', 'aliyun', 'ustc'],
                or you can set mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
    Return:
        root: dirs.
    """
    assert isinstance(name, str), "`name` should be str."
    cmd = "pip" + str(py) +" download " + name + " -d " + root + " -i "+ (pypi[mirror] if mirror in pypi else mirror)
    subprocess.call(cmd, shell=True)
    return root

def show(name, py=3):
    """Show python libraries.
    
    Args:
        name: str or list. libraries name.
        py: python environment.one of [2, 3].
    Return:
        a dict of python libraries version information.
    """
    assert isinstance(name, (str, list)), "`name` should be str or list."
    assert py in [2, 3], "`py` should be in one of [2, 3]."
    if isinstance(name, str):
        name = [name]
    t = {}
    for lib in name:
        cmd = "pip" + str(py) +" show " + lib
        s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
        s = [i.split(': ') for i in s.decode('utf-8').split('\r\n')[:-1]]
        s = {i[0]: i[1] for i in s}
        t[lib] = s
    return t

def search(name, py=3):
    """Show python libraries.
    
    Args:
        name: str. libraries name.
        py: python environment.one of [2, 3].
    Return:
        a dict of python libraries version information.
    """
    assert isinstance(name, str), "`name` should be str."
    assert py in [2, 3], "`py` should be in one of [2, 3]."
    cmd = "pip" + str(py) +" search " + name
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = [i.strip() for i in s.decode('utf-8').split('\r\n')[:-1]]
    s = {i[:i.find(')')+1]: i[i.find(')')+1:].strip() for i in s}
    return s
