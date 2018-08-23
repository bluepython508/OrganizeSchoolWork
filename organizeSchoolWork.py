import os
import re
from base64 import b64decode

from template import template as template_b64
import subprocess
import sys
from datetime import date
from pathlib import Path
from subprocess import Popen

from docx import Document

SCHOOLWORK = Path.home() / "Documents" / "SchoolWork"
SUBJECTS = [
    "English",
    "Irish",
    "Maths",
    "Home Economics",
    "Woodwork",
    "Resource",
    "Geography",
    "History",
    "Religion",
    "Cspe",
    "Sphe",
    "Pe",
    "Science",
]
SCHOOLWORK.mkdir(exist_ok=True)
SUBJECTS.extend(os.listdir(os.fspath(SCHOOLWORK)))
SUBJECTS = sorted(list(set(SUBJECTS)))
if "template.docx" in SUBJECTS:
    SUBJECTS.remove("template.docx")


def subprocess_args(include_stdout=True):
    # The following is true only on Windows.
    if hasattr(subprocess, "STARTUPINFO"):
        # On Windows, subprocess calls will pop up a command window by default
        # when run from Pyinstaller with the ``--noconsole`` option. Avoid this
        # distraction.
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        # Windows doesn't search the path by default. Pass it an environment so
        # it will.
        # env = os.environ
    else:
        si = None

    env = None
    # ``subprocess.check_output`` doesn't allow specifying ``stdout``::
    #
    #   Traceback (most recent call last):
    #     File "test_subprocess.py", line 58, in <module>
    #       **subprocess_args(stdout=None))
    #     File "C:\Python27\lib\subprocess.py", line 567, in check_output
    #       raise ValueError('stdout argument not allowed, it will be overridden.')
    #   ValueError: stdout argument not allowed, it will be overridden.
    #
    # So, add it only if it's needed.
    if include_stdout:
        ret = {"stdout": subprocess.PIPE}
    else:
        ret = {}

    # On Windows, running this from the binary produced by Pyinstaller
    # with the ``--noconsole`` option requires redirecting everything
    # (stdin, stdout, stderr) to avoid an OSError exception
    # "[Error 6] the handle is invalid."
    if sys.platform == "win32":
        ret["shell"] = True
        # pass
    ret.update(
        {
            "stdin": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "startupinfo": si,
            "env": env,
        }
    )
    return ret
    # return {}


def new_doc(subject, name):
    subject = subject.title()
    subject = re.sub("[^-A-Za-z0-9_ .,]*", "", subject)
    name = re.sub("[^-A-Za-z0-9_ .,]*", "", name)
    template = (SCHOOLWORK / "template.docx").resolve()
    if not template.exists():
        if not template.parent.exists():
            template.parent.mkdir(exist_ok=True, parents=True)
        with template.open('wb') as temp:
            temp.write(b64decode(template_b64))
        # print(b64encode(template.read_text()))
    # print(template.exists())
    loc = (SCHOOLWORK / subject).absolute()
    loc.mkdir(exist_ok=True, parents=True)
    file = (loc / f"{date.today().isoformat()}-{name}.docx").resolve()
    doc = Document(os.fspath(template))
    for para in doc.paragraphs:
        para.text = para.text.format(
            **{
                "date": date.today().strftime("%a, %d %b %Y"),
                "heading": name,
                "body": "Replace this...",
            }
        )
    doc.save(os.fspath(file))
    # print(sys.platform)
    if sys.platform == "darwin":
        utility = "open"
    elif sys.platform.startswith("win"):
        utility = "start"
    else:
        utility = "xdg-open"
    print(utility, os.fspath(file))
    # print(subprocess_args())
    # sh.Command(utility)(os.fspath(file))
    Popen([utility, os.fspath(file)], **subprocess_args())
