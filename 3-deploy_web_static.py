#!/usr/bin/python3
""" uses the do_pack and do_deploy functions for full deployment """
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['34.204.186.164', '54.80.223.108']
env.user = 'ubuntu'


def do_pack():
    """ return the archive path if correctly gernerated. """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """ returns True if all operations are successful
        or False if file path doesn't exist
    """
    if not path.exists(archive_path):
        return False
    archive_name = archive_path[9:]
    remote_dir = '/data/web_static/releases/' + archive_name[:-4]
    put(archive_path, '/tmp')
    run('sudo mkdir -p {}'.format(remote_dir))
    with cd(remote_dir):
        run('sudo tar -xzf {}'.format('/tmp/' + archive_name))
    run('sudo rm /tmp/{}'.format(archive_name))
    run('sudo mv {}/web_static/* {}'.format(remote_dir, remote_dir))
    run('sudo rm -rf {}/web_static'.format(remote_dir))
    run('sudo rm /data/web_static/current')
    run('sudo ln -s {} /data/web_static/current'.format(remote_dir))
    print("New version deployed!")
    return True


def deploy():
    """ full deployment """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
