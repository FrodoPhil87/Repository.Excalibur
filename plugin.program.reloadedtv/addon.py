# -*- coding: utf-8 -*-
# untouched
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu
#
#      Modified for FTV Guide (01/2016 onwards)
#      by Andy [Halikus]
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import os
import xbmcgui 
import requests
import base64
import time
import urllib2
import hashlib
import cfscrape
import pickle
import lolol

addon_id = 'plugin.program.reloadedtv'
REPO  =  xbmc.translatePath(os.path.join('special://home/addons','repository.GearsTV'))
NOTICE     =  xbmc.translatePath(os.path.join('special://home/addons/' + addon_id,'NOTICE.txt'))
cookiefile = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'plugin.program.reloadedtv', 'cookie'))
basePath   = xbmc.translatePath(os.path.join('special://profile', 'addon_data', addon_id))

if not os.path.exists(REPO):
        dialog = xbmcgui.Dialog()
        dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", "[B][COLOR lime]Sorry, you DO NOT have Reloaded TV's Repository installed![/COLOR][/B]","[COLOR yellow]Reloaded TV's Repository is needed for OFFICIAL updates.[/COLOR]","Get it at: [COLOR orangered]http://targetcreates.com/repo/[/COLOR]")
        sys.exit(1)

if not os.path.exists(basePath):
    os.makedirs(basePath)

try:
    val = lolol.CheckForUpdates()
    if val:
        sys.exit(1)
    import gui
    w = gui.TVGuide()
    w.doModal()
    del w

except:
    import sys
    import traceback as tb
    (etype, value, traceback) = sys.exc_info()
    tb.print_exception(etype, value, traceback)