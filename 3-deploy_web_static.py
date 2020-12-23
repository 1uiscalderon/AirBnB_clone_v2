#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local, put, run, env
from datetime import datetime
from os.path import exists
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
        run("sudo mkdir -p /data/web_static/releases/{}".format(name))
        run("sudo tar -xzf /tmp/{}.tgz -C "
            "/data/web_static/releases/{}".format(name, name))
        run("sudo rm -f /tmp/{}.tgz".format(name))
        run("sudo mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} "
            "/data/web_static/current".format(name))
    except Exception:
        return False
    return True


def deploy():
    """Creates and distributes an archive to your web servers, using the
    function deploy"""
    archive_path = do_pack()
    if path is None:
        return False
    return do_deploy(archive_path)
