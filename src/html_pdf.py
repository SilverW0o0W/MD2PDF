#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import pdfkit

from utils import get_output_name


def html_to_pdf(file_name, output_name=None):
    output_name = output_name if output_name else get_output_name(file_name, 'pdf')
    config = pdfkit.configuration(wkhtmltopdf=WKH2P_PATH)
    pdfkit.from_file(file_name, output_name, configuration=config, options=config.WKH2P_OPTION)
    return output_name
