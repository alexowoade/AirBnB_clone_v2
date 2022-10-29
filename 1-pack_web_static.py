#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder"""
from fabric.api import local
import time


def do_pack():
    """ returns generated archive else None """
    local('mkdir -p versions')
    arch_path = f'versions/web_static_{time.strftime("%Y%m%d%H%M%S")}.tgz'
    if local(f'tar -cvzf {arch_path} web_static'):
        return arch_path
    return None
