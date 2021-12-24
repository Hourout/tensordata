import subprocess

__all__ = ['view_env', 'create_env', 'remove_env']

def view_env():
    """Get virtual environment info."""
    cmd = f"conda info -e"
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = s.decode('utf-8').strip().split('\n')[2:]
    s = [i.split(' ') for i in s]
    return {i[0]:i[-1] for i in s}

def create_env(name, version):
    """Create virtual environment.
    
    Args:
        name: virtual environment.
        version: python version.
    Return:
        log info.
    """
    cmd = 'conda update -n base -c defaults conda'
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = view_env()
    if name in s:
        return 'Virtual environment already exists.'
    cmd = f"conda create -n {name} python={version} -y"
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = view_env()
    if name in s:
        return 'Virtual environment successfully created.'
    return 'Virtual environment failed created.'

def remove_env(name):
    """Remove virtual environment.
    
    Args:
        name: virtual environment.
    Return:
        log info.
    """
    s = view_env()
    if name not in s:
        return 'Virtual environment not exists.'
    cmd = f'conda remove -n {name} --all'
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    s = view_env()
    if name not in s:
        return 'Virtual environment successfully removed.'
    return 'Virtual environment failed removed.'