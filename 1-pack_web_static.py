#!/usr/bin/python3
""" Script Fabric that generates a .tgz from the contents of web_static """
from fabric.api import local
import time


def do_pack():
    """
        Return the archive path if archive has been correctly
        gernerated.
    """

    local('mkdir -p versions')
    archived_f_path = f'versions/web_static_{time.strftime("%Y%m%d%H%M%S")}.tgz'
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))
    if t_gzip_archive:
        return archived_f_path
    return None
