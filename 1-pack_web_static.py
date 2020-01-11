#!/usr/bin/python3
from fabric.api import local
import datetime


"""Fabric script that generates a
.tgz archive from the contents of the web_static"""


def do_pack():
    """
    compress a folder inside a .tgz
    :return:
    """
    now = datetime.datetime.now()
    file_name = "web_static_" + now.strftime("%Y%M%d%H%M%S")
    local("mkdir -p versions")
    status = local("tar -cvzf versions/{}.tgz web_static".format(file_name))
    if status:
        return "versions/{}.tgz".format(file_name)
    else:
        return None
