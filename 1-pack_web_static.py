#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder
from fabric.api import local
import time


def do_pack():
    """ returns .tgz archive if generated else None """
    local('mkdir -p versions')
    arch_path = 'web_static_{}.tgz'.format(time.strftime("%Y%m%d%H%M%S"))
    if local('tar -cvzf {} web_static'.arch_path):
        return arch_path
    return None
