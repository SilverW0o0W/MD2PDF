#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import pdfkit

from config import Config
from utils import get_output_name


def html_to_pdf(file_name, output_name=None):
    output_name = output_name if output_name else get_output_name(file_name, 'pdf')
    wk_path = Config.get('WKH2P_PATH', '')
    configuration = pdfkit.configuration(wkhtmltopdf=wk_path) if wk_path else None
    pdfkit.from_file(file_name, output_name,
                     configuration=configuration,
                     options=Config["WKH2P_OPTION"])
    return output_name
