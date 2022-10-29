#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder
from fabric.api import local
import time


def do_pack():
    """ generates a .tgz archive """
    local('mkdir -p versions')
    arch_name = f'versions/web_static_{time.strftime("%Y%m%d%H%M%S")}.tgz'
    if local(f'tar -cvzf {arch_name} web_static'):
        return arch_name
    return None
