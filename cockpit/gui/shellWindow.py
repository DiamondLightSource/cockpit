#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Copyright (C) 2020 David Miguel Susano Pinto <david.pinto@bioch.ox.ac.uk>
##
## This file is part of Cockpit.
##
## Cockpit is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## Cockpit is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Cockpit.  If not, see <http://www.gnu.org/licenses/>.

import wx.py.shell

window = None

def makeWindow(parent):
    global window
    # parent is None otherwise some keyboard keys are intercepted and
    # won't work (up/down arrows when selecting an auto-complete
    # choice).  Probably the keyboard intercepts should be changed.
    window = wx.py.shell.ShellFrame(None)
    # Default icon for the ShellFrame is the PyCrust, so replace it.
    window.SetIcon(parent.GetIcon())
