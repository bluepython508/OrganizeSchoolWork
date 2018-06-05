#!/usr/bin/env bash
pyinstaller -w -F --add-binary template.docx:. -y -n OrganizeSchoolWork
