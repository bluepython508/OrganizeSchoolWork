from docx import Document
from datetime import date
from subprocess import Popen
import os
from pathlib import Path
import sys
import shutil


def new_doc(subject, name):
    template = (Path.home() / "Documents" / "SchoolWork" / "template.docx").absolute().resolve()
    if not template.exists():
        template.parent.mkdir(exist_ok=True)
        shutil.copy('template.docx', os.fspath(template))
    loc = (Path.home() / "Documents" / "SchoolWork" / subject).absolute()
    loc.mkdir(exist_ok=True)
    file = (loc / f"{date.today().isoformat()}-{name}.docx").absolute().resolve()
    doc = Document(os.fspath(template))
    for para in doc.paragraphs:
        para.text = para.text.format(**{'date': date.today().strftime("%a, %d %b %Y"), 'heading': name,
                                        'body': 'Replace this...'})
    doc.save(os.fspath(file))
    if sys.platform == 'darwin':
        utility = 'open'
    elif sys.platform.startswith('win'):
        utility = 'start'
    else:
        utility = 'xdg-open'
    Popen([utility, os.fspath(file)])
