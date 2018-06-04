from ostools import FilePath
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as P_ALIGN
from datetime import date
from subprocess import Popen


def new_doc(subject, name):
    template = FilePath("%HomeDrive%%HomePath%", ensure="dir")["Documents"][
        "SchoolWork"
    ].getChild("template.docx", ensure="file")
    loc = FilePath("%HomeDrive%%HomePath%", ensure="dir")["Documents"]["SchoolWork"][
        subject
    ]
    file = FilePath(loc, ensure="file").child(f"{date.today().isoformat()}-{name}.docx")
    doc = Document(template.path)
    date_para = doc.add_paragraph(date.today().strftime("%a, %d %b %Y"), "Heading2")
    date_para.alignment = P_ALIGN.RIGHT
    head = doc.add_paragraph(name, "Title")
    head.alignment = P_ALIGN.CENTER
    body = doc.add_paragraph("This is the body...", "Body")
    doc.save(file.path)
    Popen(["start", file.path])
