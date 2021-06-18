import subprocess


__all__ = ['freeze', 'upgrade', 'upgradeable', 'install', 'uninstall', 
           'mirror', 'file', 'show', 'search', 'set_mirror']

class pypi_mirror:
    pip = "https://pypi.org/simple"
    tsinghua = "https://pypi.tuna.tsinghua.edu.cn/simple"
    aliyun = "https://mirrors.aliyun.com/pypi/simple"
    ustc = "https://mirrors.ustc.edu.cn/pypi/web/simple"
    tencent = 'https://mirrors.cloud.tencent.com/pypi/simple'
    douban = 'https://pypi.doubanio.com/simple/'
    
mirror = pypi_mirror()

def freeze(name=None, py=''):
    """List all python libraries.
    
    Args:
        name: str or list. libraries name.
        py: python environment.one of ['', 2, 3].
    Return:
        a dict of python libraries version.
    """
    assert name is None or isinstance(name, (str, list)), "`name` should be None or str or list."
    cmd = f"pip{py} list"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = [i.split(' ') for i in s.decode('utf-8').split('\n')[2:-1]]
    s = {i[0]: i[-1] for i in s}
    if name is not None:
        try:
            if isinstance(name, str):
                name = [name]
            s = {i:s[i] for i in name}
        except:
            raise ValueError("{} is not in local libraries".format(name))
    return s

def upgrade(name=None, version=None, py='', mirror=mirror.pip):
    """Upgrade python libraries.
    
    Args:
        name: str or list. libraries name.
        version: str or list. libraries version name.
        py: python environment.one of ['', 2, 3].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
                options one of ['pip', 'tsinghua', 'aliyun', 'ustc'],
                or you can set mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
                or mirror=td.utils.pip.mirror.pip
    Return:
        a dict of python libraries version.
    """
    assert version is None or isinstance(version, (str, list)), "`version` should be None or str or list."
    old_lib = freeze(name=name, py=py)
    if version is not None:
        if isinstance(version, str):
            version = [version]
        assert len(old_lib)==len(version), "`name` and `version` should be same number."
        for (dist, ver) in zip(name, version):
            cmd = f"pip{py} install --upgrade {dist}=={ver} -i {mirror}"
            subprocess.call(cmd, shell=True)
    else:
        for dist in old_lib:
            cmd = f"pip{py} install --upgrade {dist} -i {mirror}"
            subprocess.call(cmd, shell=True)
    new_lib = freeze(name=name, py=py)
    lib = {i:{'old_version': old_lib[i], "new_version":new_lib[i]} for i in old_lib}
    return lib

def upgradeable(py=''):
    """Veiw upgradeable python libraries.
    
    Args:
        py: python environment.one of ['', 2, 3].
    Return:
        a dict of python libraries version.
    """
    cmd = f"pip{py} list -o"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = [i.strip().split(' ') for i in s.decode('utf-8').split('\n')[2:-1]]
    s = [list(filter(lambda x:len(x)>0, i)) for i in s]
    s = {i[0]:{'version':i[1], 'latest':i[2], 'type':i[-1]} for i in s}
    return s

def install(name, version=None, py='', mirror=mirror.pip):
    """Install python libraries.
    
    Args:
        name: str or list. libraries name.
        version: str or list. libraries version name.
        py: python environment.one of ['', 2, 3].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
                options one of ['pip', 'tsinghua', 'aliyun', 'ustc'],
                or you can set mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
                or mirror=td.utils.pip.mirror.pip
    Return:
        a dict of python libraries version.
    """
    assert isinstance(name, str), "`name` should be str."
    assert version is None or isinstance(version, str), "`version` should be None or str."
    cmd = f"pip{py} install {name if version is None else name + '==' + version} -i {mirror}"
    t = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    name = t.decode('utf-8').split('\n')[-3].split(' ')[-1]
    return freeze(name=name, py=py)

def uninstall(name, py=''):
    """Uinstall python libraries.
    
    Args:
        name: str. libraries name.
        py: python environment.one of [2, 3].
    Return:
        uninstall log.
    """
    assert isinstance(name, str), "`name` should be str."
    cmd = f"pip{py} uninstall {name} -y"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    return s

def set_mirror(mirror=mirror.pip, py=''):
    """Set up pip mirrors on your machine.
    
    Args:
        py: python environment.one of [2, 3].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
                options one of ['pip', 'tsinghua', 'aliyun', 'ustc'],
                or you can set mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
                or mirror=td.utils.pip.mirror.pip
    Return:
        mirror file path.
    """
    subprocess.call(f"pip{py} install pip -U", shell=True)
    cmd = f"pip{py} config set global.index-url {mirror}"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    return s

def file(root, name, py='', mirror=mirror.pip):
    """Download python libraries to the specified folder.
    Args:
        root: str, dirs.
        name: str or list. libraries name.
        py: python environment.one of ['', 2, 3].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
                options one of ['pip', 'tsinghua', 'aliyun', 'ustc'],
                or you can set mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
                mirror=td.utils.pip.mirror.pip
    Return:
        root: dirs.
    """
    assert isinstance(name, str), "`name` should be str."
    cmd = f"pip{py} download {name} -d {root} -i {mirror}"
    subprocess.call(cmd, shell=True)
    return root

def show(name, py=''):
    """Show python libraries.
    
    Args:
        name: str or list. libraries name.
        py: python environment.one of ['', 2, 3].
    Return:
        a dict of python libraries version information.
    """
    assert isinstance(name, (str, list)), "`name` should be str or list."
    if isinstance(name, str):
        name = [name]
    t = {}
    for lib in name:
        cmd = f"pip{py} show {lib}"
        s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
        s = [i.split(': ') for i in s.decode('utf-8').split('\n')[:-1]]
        s = {i[0]: i[1] for i in s}
        t[lib] = s
    return t

def search(name, py=''):
    """Show python libraries.
    
    Args:
        name: str. libraries name.
        py: python environment.one of ['', 2, 3].
    Return:
        a dict of python libraries version information.
    """
    assert isinstance(name, str), "`name` should be str."
    cmd = f"pip{py} search {name}"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = [i.strip() for i in s.decode('utf-8').split('\n')[:-1]]
    s = {i[:i.find(')')+1]: i[i.find(')')+1:].strip() for i in s}
    return s