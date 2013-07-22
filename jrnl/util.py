#!/usr/bin/env python
# encoding: utf-8
import sys
import os
from tzlocal import get_localzone
PY3 = sys.version_info[0] == 3
PY2 = sys.version_info[0] == 2

def u(s):
    """Mock unicode function for python 2 and 3 compatibility."""
    return s if PY3 else unicode(s, "unicode_escape")

STDIN = sys.stdin
STDERR = sys.stderr
STDOUT = sys.stdout
__cached_tz = None

def prompt(msg):
    """Prints a message to the std err stream defined in util."""
    print(msg, file=STDERR)

def py23_input(msg):
    STDOUT.write(msg)
    return STDIN.readline().strip()

def get_local_timezone():
    """Returns the Olson identifier of the local timezone.
    In a happy world, tzlocal.get_localzone would do this, but there's a bug on OS X
    that prevents that right now: https://github.com/regebro/tzlocal/issues/6"""
    global __cached_tz
    if not __cached_tz and "darwin" in sys.platform:
        __cached_tz = os.popen("systemsetup -gettimezone").read().replace("Time Zone: ", "").strip()
    elif not __cached_tz:
        __cached_tz = str(get_localzone())
    return __cached_tz
