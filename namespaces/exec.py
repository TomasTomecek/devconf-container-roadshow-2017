#!/usr/bin/python3
import os
import sys
import subprocess
from ctypes import CDLL
from os import open as os_open, O_RDONLY

import docker

libc = CDLL('libc.so.6')


def set_namespaces(pid, namespaces_list):
    fds = []
    # first we need to load all the FDs
    # then we need to setns
    for n in namespaces_list:
        fds.append(os_open('/proc/{}/ns/{}'.format(pid, n), O_RDONLY))
    for fd in fds:
        libc.setns(fd, 0)

try:
    container = sys.argv[1]
except IndexError:
    print("Usage: {} <CONTAINER>".format(sys.argv[0]))
    sys.exit(1)

try:
    d = docker.Client(version="auto")
except AttributeError:
    d = docker.APIClient(version="auto")

try:
    i = d.inspect_container(container)
    pid = i["State"]["Pid"]
except Exception as ex:
    print("Container does not exist, or is not running: {}".format(ex))
    sys.exit(2)

set_namespaces(pid, ["net", "mnt", "pid", "uts", "ipc"])

# child processes will join PID namespace

subprocess.call(["/bin/bash"])
# import pprint
# pprint.pprint(os.listdir("/"))
