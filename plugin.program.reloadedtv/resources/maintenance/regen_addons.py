import time
import os
import xbmc
import xbmcgui
import xbmcaddon
import sys
addon         = 'plugin.program.reloadedtv'
addonPath     = xbmc.translatePath(os.path.join('special://home/addons', addon))
sys.path.append(addonPath)
import add

d = xbmcgui.Dialog()

try:
	add.StartCreate()
except:
	d = xbmcgui.Dialog()
	d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Error! Please try restarting','your device and try again..','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')
	notify('[COLOR red]Reloaded TV Guide[/COLOR]','Error! Please try restarting your device and try again..',os.path.join('special://home/addons', addon, 'icon.png'))

def notify(header,msg,icon_path):
    try:
        duration=1500
    #xbmc.executebuiltin("XBMC.Notification(%s,%s, %s, %s)" % (header, msg, duration, icon_path))
        xbmcgui.Dialog().notification(header, msg, icon=icon_path, time=duration, sound=False)
    except:
        import sys
        import traceback as tb
        (etype, value, traceback) = sys.exc_info()
        tb.print_exception(etype, value, traceback)