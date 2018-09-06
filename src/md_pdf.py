#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

from md_html import md_to_html
from html_pdf import html_to_pdf


def md_to_pdf(file_name):
    html_file_name = md_to_html(file_name)
    return html_to_pdf(html_file_name)


if __name__ == '__main__':
    # md_to_pdf('test.md')
    pass
