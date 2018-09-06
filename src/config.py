#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

import os

PWD = os.path.dirname(os.path.realpath(__file__))

WKH2P_OPTION = {
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'disable-smart-shrinking': '',
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'outline-depth': 10,
}

WKH2P_PATH = r'/usr/local/bin/wkhtmltopdf'

CSS_DIR = 'CSS/GitHub'
CSS_PATH = []
