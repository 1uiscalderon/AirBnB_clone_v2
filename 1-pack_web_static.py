#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local
from datetime import datetime


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
