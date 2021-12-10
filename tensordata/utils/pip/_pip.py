import subprocess


__all__ = ['freeze', 'upgrade', 'upgradeable', 'install', 'uninstall', 
           'mirror', 'download', 'show', 'set_mirror', 'get_mirror']

class pypi_mirror:
    pip = "https://pypi.org/simple"
    tsinghua = "https://pypi.tuna.tsinghua.edu.cn/simple"
    aliyun = "https://mirrors.aliyun.com/pypi/simple"
    ustc = "https://mirrors.ustc.edu.cn/pypi/web/simple"
    tencent = 'https://mirrors.cloud.tencent.com/pypi/simple'
    douban = 'https://pypi.doubanio.com/simple/'
    
mirror = pypi_mirror()

def libraries_name(name):
    for i in ['==', '>=', '<=', '>', '<']:
        if i in name:
            return name.split(i)+[i]
    for i,j in enumerate(name):
        if j=='-' and name[i+1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return [name[:i], name[i+1:], '-']
    return [name, '', '']

def freeze(name, py=''):
    """List all python libraries.
    
    Args:
        name: str or list. libraries name.
        py: python environment.one of ['', '3'].
    Return:
        a dict of python libraries version.
    """
    assert isinstance(name, (str, list)), "`name` should be None or str or list."
    cmd = f"pip{py} list"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = [i.split(' ') for i in s.decode('utf-8').split('\n')[2:-1]]
    s = {i[0]: i[-1] for i in s}
    if isinstance(name, str):
        name = [name]
    name = [libraries_name(i)[0] for i in name]
    s = {i:s.get(i, '') for i in name}
    return s

def upgrade(name, version=None, py='', mirror=mirror.pip, logger=False):
    """Upgrade python libraries.
    
    Args:
        name: str or list. libraries name.
        version: str or list. libraries version.
        py: python environment.one of ['', '3'].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
                or you can set eg. mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
                or eg. mirror=td.utils.pip.mirror.tsinghua
    Return:
        a dict of python libraries version.
    """
    assert version is None or isinstance(version, (str, list)), "`version` should be None or str or list."
    if isinstance(name, str):
        name = [name]
    old_lib = freeze(name=name, py=py)
    if version is not None:
        if isinstance(version, str):
            version = [version]
        assert len(name)==len(version), "`name` and `version` should be same number."
        for (dist, ver) in zip(name, version):
            if ver=='':
                cmd = f"pip{py} install --upgrade {dist} -i {mirror}"
            else:
                if len([i for i in ['==', '>', '<', '>=', '<='] if i in ver])==0:
                    ver = '=='+ver
                cmd = f"pip{py} install --upgrade {dist}{ver} -i {mirror}"
            if logger:
                subprocess.call(cmd, shell=True)
            else:
                subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    else:
        for dist in old_lib:
            cmd = f"pip{py} install --upgrade {dist} -i {mirror}"
            if logger:
                subprocess.call(cmd, shell=True)
            else:
                subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    new_lib = freeze(name=name, py=py)
    lib = {i:{'old_version': old_lib[i], "new_version":new_lib[i]} for i in new_lib}
    return lib

def upgradeable(py=''):
    """Veiw upgradeable python libraries.
    
    Args:
        py: python environment.one of ['', '3'].
    Return:
        a dict of python libraries version.
    """
    cmd = f"pip{py} list -o"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = [i.strip().split(' ') for i in s.decode('utf-8').split('\n')[2:-1]]
    s = [list(filter(lambda x:len(x)>0, i)) for i in s]
    s = {i[0]:{'version':i[1], 'latest':i[2], 'type':i[-1]} for i in s}
    return s

def install(name, py='', mirror=mirror.pip):
    """Install python libraries.
    
    Args:
        name: str or list. libraries name. 
              eg. name = 'numpy' or 'numpy==1.0.0' or ['numpy', 'pandas>1.0.0']
        py: python environment.one of ['', '3'].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
                or you can set mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
                or mirror=td.utils.pip.mirror.pip
    Return:
        a dict of python libraries version.
    """
    if isinstance(name, str):
        if name.startswith('https://github.com/'):
            cmd = f"pip{py} install git+git://github.com/{name.split('github.com/')[1]}.git"
            s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
            name = s.decode('utf-8').strip().split('\n')[-1].split(' ')[2:]
            return freeze(name=name, py=py)
        elif name.endswith('.whl'):
            cmd = f"pip{py} install {name}"
            s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
            name = s.decode('utf-8').strip().split('\n')[-1].split(' ')[2:]
            return freeze(name=name, py=py)
        elif name.endswith('.txt'):
            cmd = f"pip{py} install -r {name}"
            s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
            name = s.decode('utf-8').strip().split('\n')[-1].split(' ')[2:]
            return freeze(name=name, py=py)
        name = [name]
    name = [libraries_name(i) for i in name]
    name1 = [i[0] for i in name]
    name = [i[0] for i in name if i[2]=='']
    name = name + [i[0]+'=='+i[1] for i in name if i[2]=='-']
    name = name + [i[0]+i[2]+i[1] for i in name if i[2] not in ['', '-']]
    name = ['"'+i+'"' for i in name]
    cmd = f"pip{py} install {' '.join(name)} -i {mirror}"
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    return freeze(name=name1, py=py)

def uninstall(name, py=''):
    """Uinstall python libraries.
    
    Args:
        name: str or list. libraries name.
        py: python environment.one of ['', '3'].
    Return:
        uninstall log.
    """
    if isinstance(name, str):
        name = [name]
    name = [libraries_name(i)[0] for i in name]
    name = freeze(name, py)
    name1 = [f'Library not exist {i}' for i in name if name[i]=='']
    name = [i for i in name if name[i]!='']
    cmd = f"pip{py} uninstall {' '.join(name)} -y"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = [i.strip() for i in s.decode('utf-8').strip().split('\n') if 'Successfully uninstalled' in i]
    for i in name:
        if i not in ' '.join(s):
            s.append(f'Failed uninstall {i}')
    return s+name1

def get_mirror(py=''):
    """Get up pip mirrors on your machine.
    
    Args:
        py: python environment.one of ['', '3'].
    Return:
        mirror path.
    """
    cmd = f"pip{py} config list"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    return s.decode('utf-8').strip().split('global.index-url=')[1][1:-1]
    
def set_mirror(mirror=mirror.pip, py=''):
    """Set up pip mirrors on your machine.
    
    Args:
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
                or you can set mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
                or mirror=td.utils.pip.mirror.pip
        py: python environment.one of ['', '3'].
    Return:
        mirror file path.
    """
    subprocess.Popen(f"pip{py} install pip -U", stdout=subprocess.PIPE, shell=True).communicate()[0]
    cmd = f"pip{py} config set global.index-url {mirror}"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    return s.decode('utf-8').strip()

def download(root, name, py='', mirror=mirror.pip):
    """Download python libraries to the specified folder.
    Args:
        root: str, dirs.
        name: str or list. libraries name.
        py: python environment.one of ['', '3'].
        mirror: pip install libraries mirror,
                default official https://pypi.org/simple.
                or you can set mirror='https://pypi.tuna.tsinghua.edu.cn/simple'.
                mirror=td.utils.pip.mirror.pip
    Return:
        root: dirs.
    """
    if isinstance(name, str):
        name = [name]
    cmd = f"pip{py} download {' '.join(name)} -d {root} -i {mirror}"
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    return root

def show(name, py=''):
    """Show python libraries.
    
    Args:
        name: str or list. libraries name.
        py: python environment.one of ['', '3'].
    Return:
        a dict of python libraries version information.
    """
    if isinstance(name, str):
        name = [name]
    name = [libraries_name(i)[0] for i in name]
    name = freeze(name, py)
    t = {}
    for lib in name:
        if name[lib]=='':
            t[lib] = {}
        else:
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
        py: python environment.one of ['', '3'].
    Return:
        a dict of python libraries version information.
    """
    assert isinstance(name, str), "`name` should be str."
    cmd = f"pip{py} search {name}"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = [i.strip() for i in s.decode('utf-8').split('\n')[:-1]]
    s = {i[:i.find(')')+1]: i[i.find(')')+1:].strip() for i in s}
    return s