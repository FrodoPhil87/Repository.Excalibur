import time
import os
import xbmc
import xbmcgui
import xbmcaddon
import shutil

cookiefile = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'plugin.program.reloadedtv', 'cookie'))
d = xbmcgui.Dialog()
deletesuccess = False

try:
	os.remove(cookiefile)
	deletesuccess = True
except: 
	d = xbmcgui.Dialog()
	d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Error Removing cookie file','Please restart device!','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')
	sys.exit(1)

if deletesuccess == True:
	d = xbmcgui.Dialog()
	d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Cookie file successfully deleted.','','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')