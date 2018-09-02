# coding=utf-8
import markdown
import pyh
import pdfkit

with open('resume.md', 'r') as f:
    text = f.read()

text = text.decode('utf-8')
html = markdown.markdown(text)
html = html.encode('utf-8')

page = pyh.PyH()
page.addCSS('Github.css', '1.css', '2.css')
setattr(pyh.thisModule, 'article', pyh.TagFactory('article'))
page << pyh.article(html, cl='markdown-body entry-content')
page.printOut('test.html')

options = {
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'disable-smart-shrinking': '',
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    # 'cookie': [
    #     ('cookie-name1', 'cookie-value1'),
    #     ('cookie-name2', 'cookie-value2'),
    # ],
    'outline-depth': 10,
}

path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wk)
css = ['Github.css', '1.css', '2.css']
pdfkit.from_file('test.html', 'test.pdf', configuration=config, options=options)
