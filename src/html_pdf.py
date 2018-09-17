#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import pdfkit

from config import Config
from utils import get_output_name


def html_to_pdf(file_name, output_name=None):
    output_name = output_name if output_name else get_output_name(file_name, 'pdf')
    configuration = pdfkit.configuration(wkhtmltopdf=Config["WKH2P_PATH"])
    pdfkit.from_file(file_name, output_name,
                     configuration=configuration,
                     options=Config["WKH2P_OPTION"]
                     )
    return output_name
