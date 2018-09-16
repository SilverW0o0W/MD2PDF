#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

import os

PWD = os.path.dirname(os.path.realpath(__file__))


def split_name(file_name):
    path, temp_name = os.path.split(file_name)
    name, ext = os.path.splitext(temp_name)
    return path, name, ext


def get_output_name(file_name, ext):
    path, name, old_ext = split_name(file_name)
    path = PWD if not path else path
    return '{0}/{1}.{2}'.format(path, name, ext)
