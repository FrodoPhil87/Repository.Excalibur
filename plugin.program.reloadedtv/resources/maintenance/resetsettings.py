import sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urllib2,re
import shutil
import time

addon         = 'plugin.program.reloadedtv'
ADDONID       = addon
addon_name    = addon
icon = xbmc.translatePath(os.path.join('special://home/addons', addon, 'icon.png'))
addonPath = xbmc.translatePath(os.path.join('special://home', 'addons', addon))
basePath = xbmc.translatePath(os.path.join('special://profile', 'addon_data', addon))
dbPath = xbmc.translatePath(xbmcaddon.Addon(addon).getAddonInfo('profile'))
dialog = xbmcgui.Dialog();dp = xbmcgui.DialogProgress()
ADDON = xbmcaddon.Addon(id='plugin.program.reloadedtv')

import base64

mode='run_reset'

def reset():

    AddonData = xbmc.translatePath('special://userdata/addon_data/plugin.program.reloadedtv')

    for root, dirs, files in os.walk(AddonData):
        file_count = 0
        file_count += len(files)
        if file_count > 0:            
            for f in files:
                try:
                    os.unlink(os.path.join(root, f))
                except: pass
            for d in dirs:
                try:
                    shutil.rmtree(os.path.join(root, d))
                except: pass
    if os.path.exists(AddonData):
        try:
            shutil.rmtree(AddonData)
        except: pass
    d = xbmcgui.Dialog()            
    d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Reset successfully performed.','','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')
    xbmc.executebuiltin('Dialog.Close(10140)')
    xbmc.sleep(100)
    ADDON.openSettings()
    sys.exit()  
#

def SetSetting(param, value):
    value = str(value)
    if GetSetting(param) == value:
        return
    xbmcaddon.Addon(ADDONID).setSetting(param, value)

def GetSetting(param):
    return xbmcaddon.Addon(ADDONID).getSetting(param)

#
def notify(header,msg,icon_path):
    duration=1500
    #xbmc.executebuiltin("XBMC.Notification(%s,%s, %s, %s)" % (header, msg, duration, icon_path))
    xbmcgui.Dialog().notification(header, msg, icon=icon_path, time=duration, sound=False)
#

if mode=='run_reset' : reset()
