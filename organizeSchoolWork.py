from docx import Document
from datetime import date
from subprocess import Popen
import subprocess
import os
from pathlib import Path
import sys

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
    "Science"
]
(Path.home() / "Documents" / "SchoolWork").mkdir(exist_ok=True)
SUBJECTS.extend(os.listdir((Path.home() / "Documents" / "SchoolWork")))
if "template.docx" in SUBJECTS:
    SUBJECTS.remove("template.docx")
SUBJECTS = sorted(list(set(SUBJECTS)))


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
        env = os.environ
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
        ret["close_fds"] = True
    ret.update(
        {
            "stdin": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "startupinfo": si,
            "env": env,
        }
    )
    return ret


def new_doc(subject, name):
    subject = subject.title()
    template = (
        (Path.home() / "Documents" / "SchoolWork" / "template.docx")
        .absolute()
        .resolve()
    )
    loc = (Path.home() / "Documents" / "SchoolWork" / subject).absolute()
    loc.mkdir(exist_ok=True, parents=True)
    file = (loc / f"{date.today().isoformat()}-{name}.docx").absolute().resolve()
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
    if sys.platform == "darwin":
        utility = "open"
    elif sys.platform.startswith("win"):
        utility = "start"
    else:
        utility = "xdg-open"
    Popen([utility, os.fspath(file)], **subprocess_args())
