#!/usr/bin/python3
"""Fabric script"""
from fabric.api import put, run, env
from os.path import exists
from fabric.api import local
from datetime import datetime
import os
env.user = 'ubuntu'
env.hosts = ['35.196.95.205', '34.73.121.54']


def do_pack():
    """Return the archive path if the archive has been correctly generated.
    Otherwise, it should return None"""
    local("mkdir -p versions")
    try:
        result = local("tar -czvf versions/web_static_{}.tgz web_static"
                       .format(datetime.now().strftime("%Y%m%d%H%M%S")))
        return result
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploy new static content"""
    if not os.path.exists(archive_path):
        return False
    try:
        upload = put(archive_path, "/tmp/")
        name = upload[0].split("/")[2].split(".")[0]
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{}.tgz -C "
            "/data/web_static/releases/{}".format(name, name))
        run("rm /tmp/{}.tgz".format(name))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} "
            "/data/web_static/current".format(name))
    except Exception:
        return False
    return True