#!/usr/bin/python3
""" uses the do_pack and do_deploy functions for full deployment """
from fabric.api import *
import time
import os


env.hosts = ['34.204.186.164', '54.80.223.108']
env.user = 'ubuntu'


def do_pack():
    """ returns .tgz archive if generated else None """
    local('mkdir -p versions')
    time_created = time.strftime("%Y%m%d%H%M%S")
    arch_path = 'versions/web_static_{}.tgz'.format(time_created)
    if local('tar -cvzf {} web_static'.format(arch_path)):
        return arch_path
    return None


def do_deploy(archive_path):
    """
    a Fabric script that distributes an archive to your web servers
    """

    if not os.path.exists(archive_path):
        return False

    archived_file = archive_path[9:]
    newest_version = "/data/web_static/releases/" + archive_path[:-4]
    archived_file = "/tmp/" + archived_file

    put(archive_path, "/tmp/")
    run("sudo mkdir -p {}".format(newest_version))
    run("sudo tar -xzf {} -C {}/".format(archived_file, newest_version))
    run("sudo rm {}".format(archived_file))
    run("sudo mv {}/web_static/* {}".format(newest_version,
                                            newest_version))
    run("sudo rm -rf {}/web_static".format(newest_version))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(newest_version))

    print("New version deployed!")
    return True


def deploy():
    """ full deployment """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
