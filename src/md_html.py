#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import markdown
from xml.dom.minidom import Document, parseString
from io import open
import os

from utils import get_output_name
from config import CSS_DIR
from config import CSS_PATH


def md_to_html(file_name, output_name=None):
    text = convert_md_html(file_name)
    html = fill_html(text)

    output_name = output_name if output_name else get_output_name(file_name, 'html')

    with open(output_name, 'w', encoding='utf-8') as f:
        f.write(html)

    return output_name


def convert_md_html(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    text_html = markdown.markdown(text)
    return text_html


def get_css_list(dir_path=CSS_DIR):
    if not os.path.isdir(dir_path):
        return []
    files = os.listdir(dir_path)
    files.sort()
    files = [
        '{0}/{1}'.format(dir_path, name)
        for name in files
        if name.endswith('.css')
    ]
    files.extend(CSS_PATH)
    return files


def fill_html(text):
    doc = Document()
    html = doc.createElement("html")
    doc.appendChild(html)
    head = doc.createElement("head")

    meta = doc.createElement("meta")
    meta.setAttribute('http-equiv', 'Content-Type')
    meta.setAttribute('content', 'text/html')
    meta.setAttribute('charset', 'utf-8')
    head.appendChild(meta)

    for css in get_css_list():
        link = doc.createElement("link")
        link.setAttribute('rel', 'stylesheet')
        link.setAttribute('type', r'text/css')
        link.setAttribute('href', css)
        head.appendChild(link)
    html.appendChild(head)

    body = doc.createElement("body")
    text = u'<article>{}</article>'.format(text)
    text = text.encode('utf-8')
    article_dom = parseString(text)
    article = article_dom.documentElement
    body.appendChild(article)
    html.appendChild(body)

    return doc.toprettyxml()
