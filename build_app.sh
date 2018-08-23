#!/usr/bin/env bash
python templater.py
pyinstaller -w -F -y -n OrganizeSchoolWork gui.py
