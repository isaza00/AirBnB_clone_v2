#!/usr/bin/python3
"""generates a .tgz file from the contens of web_static using FABRIC"""
from fabric.api import *
import datetime


def do_pack():
    """ generarates .tgz archive from web_static folder """
    local("mkdir -p versions")
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    r = local("tar -cvzf versions/web_static_{}.tgz ./web_static".
              format(now), capture=True)
    if r.succeeded:
        return ("versions/web_static_{}.tgz".format(now))
    else:
        return
