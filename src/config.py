#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import toml

config_content = ''
with open('config.toml', 'r') as f:
    config_content = f.read()
conf = toml.loads(config_content)
