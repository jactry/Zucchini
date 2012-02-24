#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

command1 = "pyuic4 -o ui_login.py ui/ui_login.ui"
command2 = "pyrcc4 -o images_rc.py images.qrc"
print command1
print command2
os.system(command1)
os.system(command2)