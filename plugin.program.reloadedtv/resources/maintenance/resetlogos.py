import time
import os
import xbmc
import xbmcgui
import xbmcaddon
import shutil

databasePath = xbmc.translatePath('special://userdata/addon_data/plugin.program.reloadedtv')
LogosDir = xbmc.translatePath('special://userdata/addon_data/plugin.program.reloadedtv/resources/logos')
d = xbmcgui.Dialog()
deletesuccess = False
logodelete = False

for root, dirs, files in os.walk(databasePath,topdown=True):
    dirs[:] = [d for d in dirs]
    for name in files:
        if "guide.xml" in name:
            try:
                os.remove(os.path.join(root,name))
                deletesuccess = True
            except: 
                d = xbmcgui.Dialog()
                d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Error Removing ' + str(name),'Please restart device!','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')
                pass
        else:
            continue

for root, dirs, files in os.walk(databasePath,topdown=True):
    dirs[:] = [d for d in dirs]
    for name in files:
        if "guide.zip" in name:
            try:
                os.remove(os.path.join(root,name))
                deletesuccess = True
            except: 
                d = xbmcgui.Dialog()
                d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Error Removing ' + str(name),'Please restart device!','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')
                pass
        else:
            continue
try:
    shutil.rmtree(LogosDir, ignore_errors=True)
    logodelete = True
except:
    d = xbmcgui.Dialog()
    d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Error Removing logos!','Please restart device!','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')



if deletesuccess == True and logodelete == True:
    d = xbmcgui.Dialog()            
    d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Channel logos successfully deleted.','Please launch guide to download logos.','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')
else:
    d = xbmcgui.Dialog()
    d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Error! file(s) not found.. Try loading guide to download files!','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')