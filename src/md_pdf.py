#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from md_html import md_to_html
from html_pdf import html_to_pdf

import sys


def md_to_pdf(file_name):
    html_file_name = md_to_html(file_name)
    return html_to_pdf(html_file_name)


if __name__ == '__main__':
    if not sys.argv[1]:
        print('File path required.')
        exit()
    md_to_pdf(sys.argv[1])
