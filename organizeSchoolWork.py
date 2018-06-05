from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as P_ALIGN
from datetime import date
from subprocess import Popen
import os
from pathlib import Path


def new_doc(subject, name):
    template = (Path.home() / "Documents"/ "SchoolWork" / "template.docx").absolute().resolve()
    loc = (Path.home() / "Documents" / "SchoolWork" / subject).absolute().resolve()
    file = (loc / f"{date.today().isoformat()}-{name}.docx").absolute().resolve()
    doc = Document(os.fspath(template))
    date_para = doc.add_paragraph(date.today().strftime("%a, %d %b %Y"), "Heading2")
    date_para.alignment = P_ALIGN.RIGHT
    head = doc.add_paragraph(name, "Title")
    head.alignment = P_ALIGN.CENTER
    body = doc.add_paragraph("This is the body...", "Body")
    doc.save(os.fspath(file))
    Popen(["start", file.path])
