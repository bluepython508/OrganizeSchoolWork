import base64

with open('template.docx', 'rb') as tpo, open('template.py', 'wb') as tp:
    tp.write(b'template = """')
    tp.write(base64.b64encode(tpo.read()))
    tp.write(b'"""')
