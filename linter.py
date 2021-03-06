#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sergey Kulanov
# Copyright (c) 2015 Sergey Kulanov
#
# License: MIT
#

"""This module exports the Rpmlint plugin class."""

from SublimeLinter.lint import Linter, util


class Rpmlint(Linter):

    """Provides an interface to rpmlint."""

    syntax = 'rpm spec'
    cmd = 'rpmlint'
    executable = None
    regex = r'^.+?[:,\ ](?P<line>\d+):(?P<message>.+)'
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
