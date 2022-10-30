#!/usr/bin/python3
""" uses the do_pack and do_deploy functions for full deployment """


def deploy():
    """ full deployment """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
