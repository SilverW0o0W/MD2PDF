#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import toml

with open('config.toml', 'r') as f:
    Config = toml.load(f)

PWD = os.path.dirname(os.path.realpath(__file__))
