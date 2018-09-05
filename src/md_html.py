# coding=utf-8
import markdown
# import pdfkit
from xml.dom.minidom import Document
import HTMLParser

# import cgi

with open('resume.md', 'r') as f:
    text = f.read()

text = text.decode('utf-8')
text_html = markdown.markdown(text)
text_html = text_html.encode('utf-8')
# text_html = HTMLParser.HTMLParser().unescape(text_html)

doc = Document()
html = doc.createElement("html")
doc.appendChild(html)
head = doc.createElement("head")

for css_name in ['1.css', '2.css', 'Github.css']:
    link = doc.createElement("link")
    link.setAttribute('rel', 'stylesheet')
    link.setAttribute('type', r'text/css')
    link.setAttribute('href', css_name)
    head.appendChild(link)
html.appendChild(head)

body = doc.createElement("body")
article = doc.createElement("article")
article.data = text_html
content = doc.createTextNode(text_html)
article.appendChild(content)
body.appendChild(article)
html.appendChild(body)

with open('test.html', 'w') as f:
    f.write(doc.toprettyxml())

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
