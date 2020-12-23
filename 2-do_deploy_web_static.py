#!/usr/bin/python3
"""Fabric script"""
from fabric.api import put, run, env
from os.path import exists
import os
env.user = 'ubuntu'
env.hosts = ['35.196.95.205', '34.73.121.54']


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
