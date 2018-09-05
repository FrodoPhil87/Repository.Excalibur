# -*- coding: utf-8 -*-

# Deleting this file cripples the entire addon

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
# http://kodi.wiki/view/How-to:Write_Python_Scripts
################################################
'''
 mettaliq redo and work
 look into database
 scrape common plugins
 other m3us from www
 add stuff to settings
 imdb info
 skin color
 reyua
'''

from __future__ import unicode_literals
from collections import namedtuple
import codecs
import sys,os,json,urllib2
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,re
import shutil
import base64
import xbmcvfs
import urllib
import random
import hashlib
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import cookielib
import pickle
import time
import datetime
import cfscrape
import lolol

def GetSetting(param):
    try:
        return xbmcaddon.Addon(ADDONID).getSetting(param)
    except:
        pass

addon         = 'plugin.program.reloadedtv'
ADDONID       = addon
addon_name    = addon
addonPath     = xbmc.translatePath(os.path.join('special://home/addons', addon))
basePath      = xbmc.translatePath(os.path.join('special://profile', 'addon_data', addon))
tmp_File      = os.path.join(basePath, 'tmp.ini')
icon          = xbmc.translatePath(os.path.join('special://home/addons', addon, 'icon.png'))
dbPath        = xbmc.translatePath(xbmcaddon.Addon(addon).getAddonInfo('profile'))
dialog        = xbmcgui.Dialog();dp = xbmcgui.DialogProgress()

inipath       = xbmc.translatePath(os.path.join(basePath, 'resources', 'ini'))
skinpath      = xbmc.translatePath(os.path.join(basePath, 'resources', 'skins'))
m3upath       = xbmc.translatePath(os.path.join(basePath, 'resources', 'm3u'))
LOGOdir       = xbmc.translatePath(os.path.join(basePath, 'resources', 'logos'))
SKIN          = GetSetting('skin')

dex           = 'plugin.video.dex'
spinz 		  = 'plugin.video.spinz'
reboot        = 'plugin.video.reboot'
UA            = base64.b64decode('VXNlci1BZ2VudC1NYXlmYWlyUFJP') + "Reloaded TV"
addonbase     = base64.b64decode('cGx1Z2luLnByb2dyYW0ubXR2Z3VpZGVwcm8=')

cookiefile = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'plugin.program.reloadedtv', 'cookie'))

# make sure the folder is actually there already!
if not os.path.exists(basePath):
    os.makedirs(basePath)
    
# Create Resources dir        
if not os.path.exists(os.path.join(basePath, 'resources')):
    os.makedirs(os.path.join(basePath, 'resources'))

################################################# 
# Run #
#################################################
def StartCreate():
    # del playlist.m3u  
    if os.path.exists(basePath + '/playlist.m3u'):
        os.remove(basePath + '/playlist.m3u')

    # Start fresh with ini
    if os.path.exists(inipath):
        shutil.rmtree(inipath)
    if not os.path.exists(inipath):
        os.makedirs(inipath)
        
    # Create m3u dir      
    if not os.path.exists(m3upath):
        os.makedirs(m3upath)

    # check if have all skins
    skinDL()
        
    # Create Skin dir
    if not os.path.exists(os.path.join(skinpath, 'Default')):
        skinDL()
    if not os.path.exists(os.path.join(skinpath, GetSetting('skin'))):
        skinDL()
    #if missing_skin == True:
    #    skinDL()

    if not os.path.exists(LOGOdir):
        logoDL()
        SetSetting('logos.folder', LOGOdir)
    if not os.path.exists(xbmc.translatePath(os.path.join(GetSetting('logos.folder')))):
        logoDL()
        SetSetting('logos.folder', LOGOdir)
        
    #external_addon_ini(lolol.lolf('addons.ini'), os.path.join(basePath, 'addons.ini'), 'wb') # Grab addons.ini
     
    #add_Spinz()
    #add_ccloudm3u()             # Not Needed   create ccloud m3u
    #add_playlistm3u()           # Built in Ccloud playlist
    #add_pvr()                   # Add pvr.  The Flux Capacitor should go 88 miles per hour and create ini if m3u is already loaded.  Maybe adjust speeds or load at boot m3u creation
    #update_dex_info()
    #update_reboot_info()
    Copy_SupFavs_ini(xbmc.translatePath('special://profile/addon_data/plugin.program.super.favourites/Super Favourites/TV Guide/favourites.xml'),os.path.join(inipath,'plugin.program.super.favourites.ini'),'w')# Add Super Favorites to ini

    return
################################################# 
# Run END #
#################################################

def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)

################################################# 
# Default skin in settings dir -  run in gui.py
#################################################
def skinDL():
    # make sure the folder is actually there already!
    isrs = lolol.checkrs()
    try:
        if not os.path.exists(basePath):
            os.makedirs(basePath)
        if not os.path.exists(os.path.join(basePath, 'resources')):
            os.makedirs(os.path.join(basePath, 'resources'))
        if not os.path.exists(os.path.join(basePath, 'resources', 'skins')):
            os.makedirs(os.path.join(basePath, 'resources', 'skins'))
 
        path    = os.path.join(basePath, 'resources', 'skins')
        if isrs:
            url   =  lolol.lolrs('skins/')
            skins = lolol.lolrs('skins/skins.ini')
        else:
            url   =  lolol.lolf('skins/')
            skins = lolol.lolf('skins/skins.ini')
        progress = xbmcgui.DialogProgress()
        progress.create("[COLOR red]Reloaded TV Guide[/COLOR]", "Checking skins...", ' ', ' ')
        #currenttime = time.time()
        #cookieexpire = currenttime - 870
        if os.path.exists(cookiefile):
            r = requests.get(skins, headers={'User-Agent': (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False, cookies=load_cookies(cookiefile))
        else:
            r = requests.get(skins, headers={'User-Agent': (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False)
        match = re.compile('skin name="(.+?)" url="(.+?)" description="(.+?)" version="(.+?)"').findall(r.content)
        progress.close()
        for item in match:
            label  = item[0]
            if isrs:
                id     = lolol.lolrs('skins/'+item[1])
            else:
                id     = lolol.lolf('skins/'+item[1])
            desc   = item[2]       
            ver    = item[3]
            if label == 'Default':
                if not os.path.exists(os.path.join(skinpath, label)) or not os.path.exists(os.path.join(skinpath, label, 'ver.txt')):
                    getSkin(label, id, item[1])
                    notify('Skins',label + ' ' + ver + ' successfully Installed.',os.path.join('special://home/addons', addon, 'icon.png'))##NOTIFY##
                else:
                    curver = open(os.path.join(skinpath, label, 'ver.txt')).read()
                    if curver != ver:
                        getSkin(label, id, item[1])
                        notify('Skins',label + ' ' + ver + ' successfully Updated.',os.path.join('special://home/addons', addon, 'icon.png'))##NOTIFY##
            if label == SKIN:
                if not os.path.exists(os.path.join(skinpath, label)) or not os.path.exists(os.path.join(skinpath, label, 'ver.txt')):
                    getSkin(label, id, item[1])
                    notify('Skins',label + ' ' + ver + ' successfully Installed.',os.path.join('special://home/addons', addon, 'icon.png'))##NOTIFY##
                else:
                    curver = open(os.path.join(skinpath, label, 'ver.txt')).read()
                    if curver != ver:
                        getSkin(label, id, item[1])
                        notify('Skins',label + ' ' + ver + ' successfully Updated.',os.path.join('special://home/addons', addon, 'icon.png'))##NOTIFY##
        #if not os.path.exists(os.path.join(skinpath, SKIN)):
        #    notify('Skins','Skin not found! Using Default Skin!',os.path.join('special://home/addons', addon, 'icon.png'))##NOTIFY##
        #    return 'Change'
    except: 
        pass

def logoDL():
    isrs = lolol.checkrs()
    try:
        if not os.path.exists(basePath):
            os.makedirs(basePath)
        if not os.path.exists(os.path.join(basePath, 'resources')):
            os.makedirs(os.path.join(basePath, 'resources'))
        if not os.path.exists(os.path.join(basePath, 'resources', 'logos')):
            os.makedirs(os.path.join(basePath, 'resources', 'logos'))

        path  = os.path.join(basePath, 'resources', 'logos', 'logos.zip')
        tmpFile = os.path.join(basePath, 'resources', 'logos', 'tmp')
        if isrs:
            url   =  lolol.lolrs('logos/')
            logos = lolol.lolrs('logos/logos.zip')
        else:
            url   =  lolol.lolf('logos/')
            logos = lolol.lolf('logos/logos.zip')
        tmpData = mayfairdownloaderlogos(logos,tmpFile)         
        if os.path.getsize(tmpFile) > 0:
            os.rename(tmpFile, path)
            import zipfile
            zin = zipfile.ZipFile(path, 'r')
            zin.extractall(os.path.join(basePath, 'resources', 'logos'))
            zin.close()
            os.remove(path)
    except:
        pass

def getSkin(label, url, filename):
    try:
        path    = os.path.join(basePath, 'resources', 'skins', filename)
        tmpFile = os.path.join(basePath, 'resources', 'skins', 'tmp')
        tmpData = mayfairdownloader(url,tmpFile)         
        if os.path.getsize(tmpFile) > 0:
            os.rename(tmpFile, path)
            import zipfile                  
            zin = zipfile.ZipFile(path, 'r')
            zin.extractall(os.path.join(basePath, 'resources', 'skins'))   
            zin.close()
            os.remove(path)
            ReplaceText(os.path.join(path.replace('.zip',''), '720p', 'script-tvguide-channels.xml'), tmp_File, addonbase, addon, '', '', '','', '','')
            ReplaceText(os.path.join(path.replace('.zip',''), '720p', 'script-tvguide-main.xml'), tmp_File, addonbase, addon, '', '', '','', '','')
            ReplaceText(os.path.join(path.replace('.zip',''), '720p', 'script-tvguide-menu.xml'), tmp_File, addonbase, addon, '', '', '','', '','')
            ReplaceText(os.path.join(path.replace('.zip',''), '720p', 'script-tvguide-streamaddon.xml'), tmp_File, addonbase, addon, '', '', '','', '','')
            ReplaceText(os.path.join(path.replace('.zip',''), '720p', 'script-tvguide-streamsetup.xml'), tmp_File, addonbase, addon, '', '', '','', '','')
    except:
        pass

def SetSetting(param, value):
    try:
        value = str(value)
        if GetSetting(param) == value:
            return
        xbmcaddon.Addon(ADDONID).setSetting(param, value)
    except:
        pass


def download(url, path, tempzipfile):
    mayfairdownloader(url, tempzipfile)
    try:
        import zipfile                  
        zin = zipfile.ZipFile(tempzipfile, 'r')
        zin.extractall(path)
        zin.close()
        os.remove(tempzipfile)
    except: pass 
#
# skin
def mayfairdownloader(url, dest):
    BUFFSIZE = 1024 * 4
    progress = xbmcgui.DialogProgress()
    progress.create("Skin","Downloading & Installing Skins", ' ', ' ')
    #currenttime = time.time()
    #cookieexpire = currenttime - 870
    if os.path.exists(cookiefile):
        r = requests.get(url, headers={'User-Agent': (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False, cookies=load_cookies(cookiefile), stream=True)
    else:
        r = requests.get(url, headers={'User-Agent': (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False, stream=True)

    downloaded = 0
    total = r.headers['content-length']\
        if 'content-length' in r.headers else None

    with open(dest, 'wb') as outfile:
        start_time = time.time()
        for chunk in r.iter_content(chunk_size=BUFFSIZE):
            outfile.write(chunk)
            downloaded += len(chunk)

            text = ['Downloaded %.2f M' % (downloaded / 1024.0 / 1024.0)]
            completion = 0

            if total:
                elapsed = time.time() - start_time
                completion = downloaded / float(total)

                if completion > 0:
                    remaining = elapsed / completion - elapsed
                    text.append('Time remaining: %s' %
                                format_delta(remaining))

            progress.update(int(completion) * 100, "Downloading & Installing Skins", *text)

            if progress.iscanceled():
                break

    outfile.close()
    progress.close()

def mayfairdownloaderlogos(url, dest):
    BUFFSIZE = 1024 * 4
    progress = xbmcgui.DialogProgress()
    progress.create("Logos","Downloading & Installing Logos", ' ', ' ')
    #currenttime = time.time()
    #cookieexpire = currenttime - 870
    if os.path.exists(cookiefile):
        r = requests.get(url, headers={'User-Agent': (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False, cookies=load_cookies(cookiefile), stream=True)
    else:
        r = requests.get(url, headers={'User-Agent': (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False, stream=True)

    downloaded = 0
    total = r.headers['content-length']\
        if 'content-length' in r.headers else None

    with open(dest, 'wb') as outfile:
        start_time = time.time()
        for chunk in r.iter_content(chunk_size=BUFFSIZE):
            outfile.write(chunk)
            downloaded += len(chunk)

            text = ['Downloaded %.2f M' % (downloaded / 1024.0 / 1024.0)]
            completion = 0

            if total:
                elapsed = time.time() - start_time
                completion = downloaded / float(total)

                if completion > 0:
                    remaining = elapsed / completion - elapsed
                    text.append('Time remaining: %s' %
                                format_delta(remaining))

            progress.update(int(completion) * 100, "Downloading & Installing Logos", *text)

            if progress.iscanceled():
                break

    outfile.close()
    progress.close()
    
def format_delta(s):
    s = int(s)

def downloader(url, dest, dp = None):
    #import xbmcgui
    #import urllib
    #import time
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("Skin","Downloading & Installing Skins", ' ', ' ')
    dp.update(0)
    start_time=time.time()
    urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))   
#     
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Kb/s ' % kbps_speed 
            e += 'ETA: %02d:%02d' % divmod(eta, 60) 
            dp.update(percent, mbs, e)
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close() 
################################################# 
# Default skin in settings dir -  END
#################################################
################################################# 
# Notification #
#################################################
def notify(header,msg,icon_path):
    duration=2000
    #xbmc.executebuiltin("XBMC.Notification(%s,%s, %s, %s)" % (header, msg, duration, icon_path))
    xbmcgui.Dialog().notification(header, msg, icon=icon_path, time=duration, sound=False)
#
################################################# 
# Get Proper time in regards to device interpolation #
#################################################
def validTime(setting, maxAge):
    previousTime = getPreviousTime(setting)
    now          = datetime.datetime.today()
    delta        = now - previousTime
    nSeconds     = (delta.days * 86400) + delta.seconds
    return nSeconds <= maxAge
#
#################################################
# Set addon Setting
#################################################     
def SetSetting(param, value):
    value = str(value)
    if GetSetting(param) == value:
        return
    xbmcaddon.Addon(addon).setSetting(param, value)
#
#################################################
# This is a pop up box notification
#################################################
def DialogOK(line1, line2='', line3=''):
    d = xbmcgui.Dialog()
    d.ok('Subscriptions', line1, line2 , line3)     
#
#################################################
# LOG
#################################################
def log(text):
    try:
        output = '%s V%s : %s' % ("Log", 'Error?', str(text))
        if DEBUG:
            xbmc.log(output)
        else:
            xbmc.log(output, xbmc.LOGDEBUG)
    except: pass     
#
#################################################
# m3u8 to TS new file
#################################################
def M3U8_TS_New(Clean_Name,tmpFile):
    try:
        s=open(Clean_Name).read()
        s=s.replace('m3u8','ts')
        f=open(tmpFile,'w')
        f.write(s)
        f.close()
    except: pass        
# 
#################################################
# m3u8 to TS replace source file
#################################################
def M3U8_TS_Replace(Clean_Name,tmpFile):
    if os.path.exists(tmpFile):
        os.remove(tmpFile)
    os.rename(Clean_Name, tmpFile)
    s=open(tmpFile).read()
    #
    s=s.replace('m3u8','ts')
    #s=s.replace('.ts','.m3u8')
    #
    f=open(Clean_Name,'w')
    f.write(s)
    f.close()
    os.remove(tmpFile)   
#
#################################################
# Append source text to file
#################################################   
def AppendText(SourceFile, DestFile):
    try:
        s=open(SourceFile).read()
        f=open(DestFile,'a')
        f.write(s)
        f.close()
    except: pass
#
#################################################
# Replace Text in file
################################################# 
def ReplaceText(SourceFile, tmpFile, old1, new1, old2, new2, old3, new3, old4, new4):
    if os.path.exists(tmpFile):
        os.remove(tmpFile)
    os.rename(SourceFile, tmpFile)
    try:
        s=open(tmpFile).read()
        s=s.replace(old1, new1)
        s=s.replace(old2, new2)
        s=s.replace(old3, new3)
        s=s.replace(old4, new4)
        f=open(SourceFile,'a')
        f.write(s)
        f.close()
        os.remove(tmpFile)
    except: pass
#
#################################################
# Copy Super favs and superfavs to addon ini
#################################################
def Copy_SupFavs_ini(favourites,Dest_File,write_style):
    if os.path.exists(favourites):
        s=open(favourites).read()        
        s=s.replace('[/COLOR]', '')        
        s=s.replace('[COLOR yellow]', '')  
        s=s.replace('[COLOR white]', '') 
        s=s.replace('[COLOR red]', '') 
        s=s.replace('[COLOR green]', '') 
        s=s.replace('[COLOR blue]', '') 
        s=s.replace('[COLOR gold]', '')
        s=s.replace('[COLORornage]', '')
        s=s.replace('[COLOR whitee]', '')
        
        s=s.replace('[I]', '')
        s=s.replace('[/I]', '')   

        s=s.replace('quot;', '')      
        s=s.replace('amp;', '')
        s=s.replace('&plugin', 'plugin')     
        # Canada and UK English        
        s=s.replace('<favourites>', '')
        s=s.replace('</favourites>', '')        
        s=s.replace('	<favourite name="', '')
        s=s.replace('<favourite name="', '')            
        #s=s.replace(')</favourites>', '')         
        s=s.replace(')</favourite>', '')
        # USA English
        s=s.replace('<favorites>"', '')
        s=s.replace('</favorites>', '')
        s=s.replace('	<favorite name="', '')
        s=s.replace('<favorite name="', '') 
        #s=s.replace(')</favorites>', '')
        s=s.replace(')</favorites>', '')
        s=s.replace(')</favorite>', '')
        #
        for line in s:
          sp_line = line.rstrip(os.linesep).split("\n")
          s=re.sub('thumb.*PlayMedia','=',s)
          s=s.replace('" =(', '=')         
        #
        a=open(Dest_File,write_style)
        a.write('[plugin.program.super.favourites]\n') 
        a.write(s)
        a.close()
        #AppendText(Dest_File, xbmc.translatePath(os.path.join(basePath, 'addons.ini')))
#
#################################################
# External addon.ini # 
#################################################
def external_addon_ini(externalini, externaliniTemp, write_style):
    try:
        progress = xbmcgui.DialogProgress()
        progress.create("[COLOR red]Reloaded TV Guide[/COLOR]", "Downloading & Installing Files", ' ', ' ')
        f = open(externaliniTemp, write_style)
        #currenttime = time.time()
        #cookieexpire = currenttime - 870
        if os.path.exists(cookiefile):
            tmpData = requests.get(externalini, headers={'User-Agent': (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False, cookies=load_cookies(cookiefile)).content.replace(addonbase, addon)   
        else:
            tmpData = requests.get(externalini, headers={'User-Agent': (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False).content.replace(addonbase, addon)   
        f.write(tmpData)
        f.close()
        progress.close()
        #import gui
        #xbmc.executebuiltin('Dialog.Close(10140)')
        #xbmc.executebuiltin('XBMC.ActivateWindow(home)')
        #xbmc.sleep(350)
        #w = gui.TVGuide()
        #w.doModal()
        #xbmc.sleep(350)
        #del w       
    except:
        import sys
        import traceback as tb
        (etype, value, traceback) = sys.exc_info()
        tb.print_exception(etype, value, traceback)
###################################################################################################
################################################################################################### Subscriptions
###################################################################################################
#################################################
# Add Spinz .ini #                         Method 1
#################################################
def add_Spinz():
    tempaddonPath = xbmc.translatePath(os.path.join('special://profile', 'addon_data', spinz))
    addonDirPath = xbmc.translatePath(os.path.join('special://home', 'addons', spinz))
    addonDestFile = os.path.join(tempaddonPath, 'settings.xml')
    if os.path.exists(addonDirPath):    
        if os.path.exists(addonDestFile):
            try:
                notify('ini and m3u',spinz,os.path.join('special://home/addons', spinz, 'icon.png'))##NOTIFY##
                Name="dex";addon_name=spinz;addon=xbmcaddon.Addon(addon_name)
                urlpath2 = addon.getSetting('lehekylg');urlpath=urlpath2+':8000'
                username=addon.getSetting('kasutajanimi');password=addon.getSetting('salasona')
                groups = 'Sports,Kids,Cinema,Spanish,English,Adult'
                #write_style = 'a'
                Run_scraper(urlpath,addon_name,username,password,Name,groups)
            except: pass    
#################################################
# update dexter user/pass --mayfair
#################################################
def update_dex_info():
    TheseAddons   =  [dex]#Mayfair: only run for dexter!!
    for FoundAddon in TheseAddons:
        if CheckHasThisAddon(FoundAddon):
            notify('updating dexter info',FoundAddon,os.path.join('special://home/addons', FoundAddon, 'icon.png'))##NOTIFY##
            Addon    =  xbmcaddon.Addon(FoundAddon)
            user_name =  urllib.quote_plus(Addon.getSetting('kasutajanimi'))
            pass_word =  urllib.quote_plus(Addon.getSetting('salasona'))
            Source_File = xbmc.translatePath(os.path.join('special://profile', 'addon_data', addon,'addons.ini'))#Mayfair: addons.ini location with dexter channels all correct
            if os.path.exists(Source_File):
                pass_word_old='dexterpass'#Mayfair: default password in addons.ini to replace
                user_name_old='dexteremail@gmail.com'#Mayfair: default username in addons.ini to replace
                ReplaceText(Source_File, tmp_File, user_name_old, user_name, pass_word_old, pass_word, '','', '','')#Mayfair: replace default user/pass with correct info from dexter settings
##################################################
def update_reboot_info():
    TheseAddons   =  [reboot]#Mayfair: only run for reboot!!
    for FoundAddon in TheseAddons:
        if CheckHasThisAddon(FoundAddon):
            notify('updating Reloaded TV IPTV info',FoundAddon,os.path.join('special://home/addons', FoundAddon, 'icon.png'))##NOTIFY##
            Addon    =  xbmcaddon.Addon(FoundAddon)
            user_name =  urllib.quote_plus(Addon.getSetting('username'))
            pass_word =  urllib.quote_plus(Addon.getSetting('password'))
            Source_File = xbmc.translatePath(os.path.join('special://profile', 'addon_data', addon,'addons.ini'))
            if os.path.exists(Source_File):
                pass_word_old=urllib.quote_plus('rebootpassword')#Mayfair: default password in addons.ini to replace
                user_name_old=urllib.quote_plus('rebootemail@email.com')#Mayfair: default username in addons.ini to replace
                ReplaceText(Source_File, tmp_File, user_name_old, user_name, pass_word_old, pass_word, '','', '','')#Mayfair: replace default user/pass with correct info from reboot settings
#check addon######################################
def CheckHasThisAddon(FoundAddon):
    if xbmc.getCondVisibility('System.HasAddon(%s)' % FoundAddon) == 1:
        # This is a failsafe fix as this will error out if there is no pass set.  Should add check for pass is non existant in settings.xml too
        settingsFileCheck = xbmc.translatePath(os.path.join('special://home/userdata/addon_data',FoundAddon,'settings.xml'))
        if os.path.exists(settingsFileCheck):
            return True
    else:
        return False 
###################################################################################################
################################################################################################### M3U
###################################################################################################
# Play Playlist #
#def playDSF(url, windowed):
def playPlaylist(url, windowed):
    try:
        DSFID   =  ttTTtt(0,[112,13,108,120,117],[115,103,45,105,212,110,32,46,233,118,53,105,75,100,34,101,38,111,148,46,218,103,216,118,30,97,110,120])
        DSF     =  xbmcaddon.Addon(DSFID)
        DSFVER  =  DSF.getAddonInfo('version')
    except: pass     
    try:
        import urllib
        channel = urllib.quote_plus(url.split(':', 1)[-1])
        url = 'plugin://%s/?channel=%s' % (DSFID, channel)
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        playlist.add(url, xbmcgui.ListItem(''))
        xbmc.Player().play(playlist, windowed=windowed)
    except:
        return False
# Playlist End # 
#################################################
# CCloud #
#################################################
def add_ccloudm3u(): 
    www_fn = xbmc.translatePath(os.path.join(m3upath, 'ccloud.m3u'))   
    panel_url = "http://ccloudtv.org/lists/kodi.txt"
    req = urllib2.Request(panel_url)
    res = urllib2.urlopen(req)
    www_url = res.geturl()    
    response = urllib2.urlopen(www_url)
    wwwm3uFile = response.read()         
    www = open(www_fn, "wb")
    www.write(wwwm3uFile)
    www.close()
# CCloud End #
#################################################
# Playlist # ccloud
#################################################
def add_playlistm3u():
    # Create playlist.m3u
    import base64
    URL1 = base64.b64decode(b'aHR0cDovL2dvMmwuaW5rL2tvZGk=')#go2l
    URL2 = base64.b64decode(b'aHR0cDovL3guY28vZGJjaDAx')#x.co    
    URL3 = base64.b64decode(b'aHR0cDovL2Fpby5jY2xvdWR0di5vcmcva29kaQ==')#aio
    #URL4 = base64.b64decode(b'aHR0cDovL2tvZGkuY2NsZC5pbw==')#ccld
    #GrabUrls = [URL1, URL2, URL3, URL4]    
    GrabUrls = [URL1, URL2, URL3]    
    CheckIfM3u =  '#EXTM3U'
    for url in GrabUrls:
        request  = requests.get(url)
        M3uContents = request.text
        if CheckIfM3u in M3uContents:
            path = os.path.join(dbPath, 'playlist.m3u')
            with open(path, 'a') as f:
                f.write(M3uContents)
                break
#################################################
# PVR Start #
#################################################
def add_pvr():
    iniFle = 'pvr.ini';writestyle = 'w'
    iniPvrAddonName = 'plugin.program.reloadedtv'
    #iniPvrAddonName = 'pvr.iptvsimple'
    #
    PVRACTIVE   = (xbmc.getCondVisibility('Pvr.HasTVChannels')) or (xbmc.getCondVisibility('Pvr.HasRadioChannels')) == True    
    if not PVRACTIVE:
        return       
    pvrinipath  = os.path.join(inipath, iniFle)
    notify('PVR',iniFle,os.path.join(addonPath, 'resources', 'png', 'pvr.png'))##NOTIFY##
    # tv
    try:
        tryTvChannels  = _getPVRChannels('"tv"')
        tryTvChannelsCommand = tryTvChannels['result']          
    except: pass   
    # radio
    try:
        tryRadio  = _getPVRChannels('"radio"')
        tryRadioCommand = tryRadio['result']
    except: pass
    # Execute
    try:
        foundTvChannels  = tryTvChannelsCommand['channels']      
        foundRadioChannels  = tryRadioCommand['channels']
    except: pass    
    ThePVRini  = file(pvrinipath, writestyle)    
    ThePVRini.write('['+iniPvrAddonName+']\n')       
    try:
        for TryToFindStreams in foundTvChannels:
            WhatsTheGroupID  = TryToFindStreams['label']  
            stream = ('%s') % TryToFindStreams['channelid']
            ThePVRini.write('%s' % WhatsTheGroupID)
            ThePVRini.write("=")
            ThePVRini.write(('%s') % stream)            
            ThePVRini.write("\n")
    except: pass    
    try:
        for TryToFindStreams in foundRadioChannels:          
            WhatsTheGroupID  = TryToFindStreams['label']  
            stream = ('%s') % TryToFindStreams['channelid']
            ThePVRini.write('%s' % WhatsTheGroupID)
            ThePVRini.write("=")
            ThePVRini.write('%s' % stream)            
            ThePVRini.write("\n")
    except: pass   
    ThePVRini.write("\n")
    ThePVRini.close()
    #AppendText(pvrinipath, xbmc.translatePath(os.path.join(basePath, 'addons.ini')))
#
def _getPVRChannels(group):   
    method   = 'PVR.GetChannels'
    params   = 'channelgroupid'
    WhatAreGroupIDs  =  getGroupID(group)
    checkPVR =  sendJSONpvr(method, params, WhatAreGroupIDs)   
    return checkPVR
#
def getGroupID(group):
    method   = 'PVR.GetChannelGroups'
    params   = 'channeltype'   
    checkPVR = sendJSONpvr(method, params, group)
    result   = checkPVR['result']
    groups   = result['channelgroups']
    #
    for group in groups:
        WhatsTheGroupID = group['label']
        if WhatsTheGroupID == 'All channels':
            return group['channelgroupid']
#
def sendJSONpvr(method, params, value):
    JSONPVR  = ('{"jsonrpc":"2.0","method":"%s","params":{"%s":%s}, "id":"1"}' % (method, params, value))    
    checkPVR = xbmc.executeJSONRPC(JSONPVR)
    return json.loads(checkPVR.decode("utf-8"),"ignore")
# PVR End #
#################################################
# Create m3u and ini files #
#################################################
def Run_scraper(urlpath,addon_name,username,password,Name,groups):
    panel_url = urlpath+"/panel_api.php?username={}&password={}".format(username, password)  
    u = urllib2.urlopen(panel_url)
    j = json.loads(u.read())
    #
    # Channel ID Map
    my_map = {}    
    '''
    my_map = {"TREEHOUSE HD (NA)":"I80173.labs.zap2it.com",
              "FAMILY HD (NA)":"I70520.labs.zap2it.com",
              }
    '''          
    map_file =''
    if map_file:
      with open(map_file) as f:
        for line in f:
          sp_line = line.rstrip(os.linesep).split("\t")
          my_map[sp_line[0]] = sp_line[1]
    #
    # Renames channels as they are downloaded
    channelname_map = {"5*":"5Star", 
                       #"3E HD":"3e",
                       "5STAR MAX HD - NEW":"5StarMax",
                       "A+E HD":"A&E",
                       "5 Star":"5Star",
                       "ABC HD EAST":"ABC HD",                       
                       "ABC HD WEST - NEW":"ABC West",                      
                       "ABC NEWS":"ABC News",                       
                       "ACTION HD":"ACTION",
                       "ACTION MAX HD - NEW":"ActionMax",                       
                       "ALJAZEERA ENGLISH":"Aljazeera",                      
                       "AMAZING DISCOVERIES":"Amazing Discoveries",                       
                       "AMAZING FACTS":"Amazing Facts",    
                       "ANIMAL PLANET HD":"Animal Planet", 
                       "BBC AMERICA HD":"BBC America",
                       "BBC NEWS":"BBC News", 
                       "BBC One HD":"BBC1",
                       "BBC Two HD":"BBC2",
                       "BBC Three HD":"BBC3",
                       "BBC Four HD":"BBC4", 
                       "BC1 HD - NEW":"BC1", 
                       "BET HD":"BET",
                       "BLOOMBERG":"Bloomberg", 
                       "BNN HD - NEW":"BNN", 
                       "BOUNCE HD":"Bounce",
                       "BRAVO HD":"Bravo",
                       "CARTOON NETWORK HD (NA)":"Cartoon Network", 
                       "CBC EAST HD":"CBC", 
                       "CBC NEWS HD":"CBC News",
                       "CBC VANCOUVER HD- NEW":"CBC Vancouver", 
                       "CBS HD EAST":"CBS HD", 
                       "CBS HD WEST - NEW":"CBS West",
                       "CBS NEWS HD":"CBS News",
                       "CHCH HD":"CHCH",
                       "CINEMAX EAST HD - NEW":"Cinemax", 
                       "CITY TV HD":"City TV Toronto",
                       "CITY VANCOUVER HD - NEW":"City TV Vancouver", 
                       "CNBC HD":"CNBC", 
                       "CNN HD":"CNN",
                       #"COMEDY NETWORK HD":"Comedy Network",
                       "COMEDY NETWORK HD":"Comedy Central",
                       "CP24 HD":"CP24",
                       "CTV EAST HD":"CTV Toronto", 
                       "CTV NORTH":"CTV North",
                       "CTV VANCOUVER HD - NEW":"CTV Vancouver", 
                       "CW11 HD":"CW", 
                       "DISCOVERY HD":"Discovery",
                       "DISCOVERY SCIENCE HD":"Discovery Science",
                       "DISNEY HD EAST":"Disney",
                       "DISNEY XD HD (NA)":"Disney XD", 
                       "E! HD":"E!",
                       "ENCORE WESTERN HD - NEW":"Encore Western", 
                       "FAMILY HD (NA)":"FAMILY", 
                       "FOOD HD":"Food Network",
                       "FOX HD EAST":"FOX HD",
                       "FOX HD WEST - NEW":"FOX West",    
                       "FOX NEWS HD":"FOX News", 
                       "FX HD":"FX",
                       "FXX HD":"FXX", 
                       "GLOBAL BC HD - NEW":"Global Vancouver", 
                       "GLOBAL EAST HD":"Global Toronto",
                       "HALLMARK HD":"Hallmark",
                       "HBO COMEDY HD":"HBO Comedy", 
                       "HBO EAST HD":"HBO HD", 
                       "HBO SIGNATURE HD":"HBO Signature",
                       "HGTV HD":"HGTV", 
                       "HISTORY HD":"History", 
                       "HLN HD":"HLN",
                       "HSN 2":"HSN2",                       
                       "ID HD":"Discovery Investigation",
                       "IFC HD":"IFC",    
                       "LIFE HD":"Lifetime", 
                       "LIFETIME MOVIES HD":"LMN",
                       "MOREMAX HD - NEW":"MoreMax", 
                       "MOVIE TIME HD":"MovieTime", 
                       "MSNBC HD":"MSNBC",
                       "MTV HD":"MTV",
                       "NAT GEO HD":"National Geographic", 
                       "NAT GEO WILD HD":"Nat Geo Wild", 
                       "NBC HD EAST":"NBC HD",
                       "NBC HD WEST - NEW":"NBC West", 
                       "NICKELODEON HD (NA)":"Nickelodeon", 
                       "OMNI 1 HD":"OMNI 1",
                       "OMNI 2 HD":"OMNI 2",
                       "OWN HD":"OWN",    
                       "PBS HD":"PBS", 
                       "REV'N USA HD":"Rev USA",
                       "RT DOCUMENTARY HD":"RT Documentary", 
                       "RT NEWS HD":"RT News", 
                       "SHOWCASE HD":"SHOWCASE",
                       "SHOWTIME EAST":"Showtime HD",
                       "SHOWTIME SHOWCASE HD":"Showtime Showcase", 
                       "SKY CBBC HD":"CBBC", 
                       "SKY DISNEY JR (UK)":"Disney Jr UK",
                       "SKY DISNEY XD (UK)":"Disney XD UK", 
                       "SKY NEWS HD":"Sky News", 
                       "SKY NICK (UK)":"Nickelodeon UK",
                       "SKY NICK TOONS (UK)":"Nick Toons UK",
                       "SLICE HD":"SLICE",    
                       "SPIKE HD":"Spike", 
                       "STARZ BLACK HD":"Starz In Black",
                       "STARZ COMEDY HD - NEW":"Starz Comedy", 
                       "STARZ EDGE HD":"Starz Edge", 
                       "STARZ HD":"Starz",
                       "STARZ KIDZ HD - NEW":"Starz Kids",
                       "Sky 3E":"3E", 
                       "Sky Alibi":"Alibi", 
                       "Sky Animal Planet":"Animal Planet UK",
                       "Sky Channel 4":"Channel 4", 
                       "Sky Channel 5":"Channel 5", 
                       "Sky Comedy Network":"Comedy Central UK",
                       "Sky Crime and Investigation":"Crime and Investigation",
                       "Sky Dave":"Dave",    
                       "Sky Discovery":"Discovery UK", 
                       "Sky Discovery History":"Discovery History",
                       "Sky Discovery Science":"Discovery Science UK", 
                       "Sky Discovery Shed":"Discovery Shed", 
                       "Sky Discovery Turbo":"Discovery Turbo",
                       "Sky Discovery investigation":"Discovery Investigation UK",
                       "Sky Eden":"Eden", 
                       "Sky Film 4":"Film4", 
                       "Sky Food":"Food UK",
                       "Sky Gold":"Gold", 
                       "Sky Home":"Home", 
                       "Sky Movie Romance":"Sky Movies Drama",
                       "Sky Movies Atlantic":"Sky Atlantic",    
                       "Sky Movies Sci-Fi":"Sky Movies Scifi", 
                       "Sky Natgeo":"National Geographic UK",
                       "SKY News":"Sky News",
                       "Sky One":"Sky1", 
                       "Sky Quest":"Quest", 
                       "Sky RTE 1":"RTE1",
                       "Sky RTE 2":"RTE2",
                       "Sky Watch":"Watch",  
                       "Sky Yesterday":"Yesterday", 
                       "Sky itv1":"ITV1",
                       "Sky itv2":"ITV2", 
                       "Sky itv3":"ITV3",
                       "Sky itv4":"ITV4",
                       "SyFy HD":"Syfy",
                       "TBS HD":"TBS",    
                       "TCM EAST HD":"TCM", 
                       "TCM HD":"TCM",
                       "THRILLER MAX HD - NEW":"ThrillerMax", 
                       "TLC HD":"TLC", 
                       "TNT HD":"TNT",
                       "TRAVEL HD":"Travel",
                       "TREEHOUSE HD (NA)":"TREEHOUSE", 
                       "TRU TV HD":"truTV", 
                       "TV LAND HD":"TV Land",
                       "TVO HD (NA)":"TVO", 
                       "USA NETWORK HD":"USA Network", 
                       "VELOCITY HD":"VELOCITY",
                       "VEVO 1 HD":"VEVO1",
                       "VEVO 2 HD":"VEVO2",    
                       "VH1 HD":"VH1",    
                       "VICELAND HD":"Viceland", 
                       "W MOVIES HD":"W MOVIES",
                       "W NETWORK HD":"W NETWORK", 
                       "WE TV HD":"WE TV", 
                       "WEATHER CANADA HD":"Weather Canada",
                       "WEATHER USA HD":"Weather USA",
                       "WIN TV HD":"WIN TV",
                       "YTV HD (NA)":"YTV",
                       "Astro Supersports 1 HD":"Astro SuperSport 1", 
                       "Astro Supersports 2 HD":"Astro SuperSport 2", 
                       "Astro Supersports 3 HD":"Astro SuperSport 3",                        
                       "Astro Supersports 4 HD":"Astro SuperSport 4",                         
                       #"Astro Supersports 1 HD":"Astro Supersports 1", 
                       #"Astro Supersports 2 HD":"Astro Supersports 2", 
                       #"Astro Supersports 3 HD":"Astro Supersports 3",                        
                       #"Astro Supersports 4 HD":"Astro Supersports 4",                    
                       "BEIN HD":"BEINS1", 
                       "CBS SPORTS HD":"CBS Sports",
                       "ESPN HD":"ESPN",
                       "ESPN 2 HD":"ESPN2",    
                       "FOX SPORTS 1 HD":"Fox Sports 1 HD", 
                       "FOX SPORTS 2 HD":"Fox Sports 2 HD",
                       "GOLF HD":"Golf Channel", 
                       "MLB HD 01":"MLB1", 
                       "MLB HD 02":"MLB2", 
                       "MLB HD 03":"MLB3",                       
                       "MLB HD 04":"MLB4",                        
                       "MLB HD 05":"MLB5", 
                       "MLB HD 06":"MLB6",                        
                       "MLB HD 07":"MLB7",                        
                       "MLB HD 08":"MLB8",                       
                       "MLB HD 09":"MLB9",                        
                       "MLB HD 10":"MLB10",                       
                       "MLB HD 11":"MLB11",                       
                       "MLB HD 12":"MLB12",                      
                       "MLB NETWORK":"MLB Network",
                       "NBA HD":"NBA TV",
                       "NBC SPORTS":"NBCSN", 
                       "NFL NOW HD":"NFL NOW",
                       "NHL NETWORK HD":"NHL Network", 
                       "NHL ON VERSUS HD":"VERSUS", 
                       "SKY BOX NATION":"BoxNation",
                       "SKY BT 1":"BT Sport 1",
                       "SKY BT 2":"BT Sport 2",    
                       "SKY BT 1 HD":"BT Sport 1 HD",
                       "SKY BT 2 HD":"BT Sport 2 HD",
                       "Sky Sports News HD":"Sky Sports News", 
                       "SKY SPORTS 1":"Sky Sports 1 HD", 
                       "SKY SPORTS 2":"Sky Sports 2 HD", 
                       "SKY SPORTS 3":"Sky Sports 3 HD",                        
                       "SKY SPORTS 4":"Sky Sports 4 HD",                       
                       "SKY SPORTS 5":"Sky Sports 5 HD",                       
                       "SONY ESPN HD - LIVE EVENTS":"PPV",
                       #"SPORT TIME TV 1HD":"SPORT TIME TV 1HD", 
                       "SPORTSNET 360":"Sportsnet 360", 
                       "SPORTSNET ONE HD":"Sportsnet One",
                       "SPORTSNET ONT":"Sportsnet Ontario",
                       "SPORTSNET WORLD HD":"Sportsnet World", 
                       "Sky Sports News HD":"Sky Sports News HD",
                       "Sony Six HD":"Sony Six", 
                       "TEN CRICKET HD":"TEN Cricket", 
                       "TENNIS HD":"Tennis Channel",
                       "TSN 1 HD":"TSN1",
                       "TSN 2 HD":"TSN2",
                       "TSN 3 HD":"TSN3",                       
                       "TSN 4 HD":"TSN4",                       
                       "TSN 5 HD":"TSN5",                      
                       "WILLOW CRICKET HD":"WILLOW CRICKET",    
                       "WWE HD":"WWE Network", 
                       "W NETWORK":"W Network", 
                       "YANKEES HD - NEW":"YANKEES",
                       "HUSTLER HD":"HUSTLER", 
                       "PLAYBOY TV HD - NEW":"PLAYBOY", 
                       "VIVID TV - NEW":"VIVID"
                      }                      
    #channelname_map = {} 
    namemap_file = ''
    if namemap_file:
      with open(namemap_file) as f:
        for line in f:
          sp_line = line.rstrip(os.linesep).split("\t")
          channelname_map[sp_line[0]] = sp_line[1]
          
    #fuck
    #inv_map = {v: k for k, v in my_map.items()}
    
    Channel = namedtuple('Channel', ['tvg_id', 'tvg_name', 'tvg_logo', 'group_title', 'channel_url'])
    channels = []
    online_groups = set()

    #
    # Grab Channels
    for ts_id, info in j["available_channels"].iteritems():
      #channel_url = "http://2.welcm.tv:8000/live/{}/{}/{}.m3u8".format(username, password, ts_id)
      #channel_url = urlpath+":8000/live/{}/{}/{}.m3u8".format(username, password, ts_id)
      channel_url = urlpath+"/live/{}/{}/{}.m3u8".format(username, password, ts_id)
      tvg_id = ""
      tvg_name = info['name']
      if info['epg_channel_id'] and info['epg_channel_id'].endswith(".com"):
        tvg_id = info['epg_channel_id']
      if tvg_name in my_map:
        tvg_id = my_map[tvg_name]
      tvg_logo = ""
      #if info['stream_icon']:
      #  tvg_logo = info['stream_icon']
      group_title = info['category_name']
      online_groups.add(group_title)
      if tvg_name in channelname_map:
        tvg_name = channelname_map[tvg_name]
      channels.append(Channel(tvg_id, tvg_name, tvg_logo, group_title, channel_url))
    #
    # Grab Groups
    wanted_groups = sorted(online_groups)
    if groups:
      wanted_groups = groups.split(',')
      
      
    #fuck
    #group_idx = {group:idx for idx,group in enumerate(wanted_groups)}
    #  maybe
    group_idx = {}
    for idx,group in enumerate(wanted_groups):
        group_idx[group] = idx


    # Has error if channel listings is different 
    #sys.stderr.write("Channel groups: {}\n".format(",".join(wanted_groups)))
    wanted_channels = [c for c in channels if c.group_title in wanted_groups]
    wanted_channels.sort(key=lambda c: "{}-{}".format(group_idx[c.group_title], c.tvg_name))
    #
    # Sort Channels
    channel_fn = ''
    if channel_fn:
      #with open(channel_fn, 'w') as channel_f:
      with open(channel_fn, write_style) as channel_f:
        for c in wanted_channels:
          if c.tvg_id.endswith(".com"):
            if c.tvg_name in inv_map:
              channel_f.write("{}\n".format(inv_map[c.tvg_name]))
            else:
              channel_f.write("{}\n".format(c.tvg_id))
    #
    # Create m3u
    notify('m3u',addon_name + '.m3u',os.path.join('special://home/addons', addon_name, 'icon.png'))##NOTIFY##
    output_fn = addon_name + '.m3u'
    write_style = 'w'
    with codecs.open(m3upath + '/' + output_fn, write_style, 'utf-8') as f:     
      f.write('#EXTM3U\n#http://'+Name+'\n')
      for c in wanted_channels:
        #f.write('#EXTINF:-1 tvg-id="{0}" tvg-name="{1}" tvg-logo="{1}.png" group-title="{3}",{1}\n{4}\n'.format(c.tvg_id, c.tvg_name, c.tvg_logo, c.group_title, c.channel_url))
        #f.write('#EXTINF:-1 tvg-logo="{1}.png",{1}\n{4}\n'.format(c.tvg_id, c.tvg_name, c.tvg_logo, c.group_title, c.channel_url))
        f.write('#EXTINF:-1 tvg-id="{1}" tvg-name="{1}" tvg-logo="{1}.png" group-title="{3}",{1}\n{4}\n'.format(c.tvg_id, c.tvg_name, c.tvg_logo, c.group_title, c.channel_url))
    #
    Clean_Names(m3upath + '/' + output_fn, basePath+'/_iptvsubs.m3u') 
    #AppendText(m3upath + '/' + output_fn, dbPath + '/playlist.m3u')
    
      
    #
    # Create ini  
    #ini_file = addon_name + '.m3u.ini'
    ini_file = addon_name + '.ini'
    
    #notify('ini',ini_file,os.path.join('special://home/addons', addon_name, 'icon.png'))##NOTIFY##
    write_style = 'w'
    with open(inipath + '/' + ini_file, write_style) as f:
        f.write('['+addon_name+'] \n;'+Name+'\n')
        for c in wanted_channels:
            f.write('{1}={4}\n'.format(c.tvg_id, c.tvg_name, c.tvg_logo, c.group_title, c.channel_url))
    #
     
    # This will overwrite the json subscription method.  Its for the naming and ordering.              
    M3U8_TS_Replace(inipath + '/' + ini_file, tmp_File)
    #M3U8_TS_New( + '/' + , basePath+'/' + addon_name + '.ini') 
    #AppendText(inipath + '/' + ini_file, xbmc.translatePath(os.path.join(basePath, 'addons.ini')))
###################################################################################################
################################################################################################### CLEAN
###################################################################################################
#################################################
# Clean m3u and ini channel names #
#################################################
def Clean_Names(Clean_Name,tmpFile):
    #tmpFile = os.path.join(basePath, '_backup.ini')
    if os.path.exists(tmpFile):
        os.remove(tmpFile)
    os.rename(Clean_Name, tmpFile)
    s=open(tmpFile).read()
    # Clean these names in addons.ini #
    s=s.replace('ABC HD.png','ABC_HD.png')
    s=s.replace('ABC West.png','ABC_West.png')
    s=s.replace('ABC News.png','ABC_News.png')
    s=s.replace('AMC HD.png','AMC_HD.png')
    s=s.replace('Animal Planet.png','Animal_Planet.png')
    s=s.replace('BBC America.png','BBC_America.png')
    s=s.replace('BBC News.png','BBC_News.png')
    s=s.replace('CBC News.png','CBC_News.png')
    s=s.replace('CBC Vancouver.png','CBC_Vancouver.png')
    s=s.replace('CBS HD.png','CBS_HD.png')
    s=s.replace('CBS West.png','CBS_West.png')
    s=s.replace('CBS News.png','CBS_News.png')
    s=s.replace('CCTV News.png','CCTV_News.png')     
    s=s.replace('CEEN TV.png','CEEN_TV.png')      
    s=s.replace('City TV Vancouver.png','City_TV_Vancouver.png')
    s=s.replace('CTV Regina.png','CTV_Regina.png')
    s=s.replace('CTV Toronto.png','CTV_Toronto.png')
    s=s.replace('CTV Vancouver.png','CTV_Vancouver.png')
    s=s.replace('CTV North.png','CTV_North.png')
    s=s.replace('Cartoon Network.png','Cartoon_Network.png')
    s=s.replace('City TV Toronto.png','City_TV_Toronto.png')
    s=s.replace('Comedy Central.png','Comedy_Central.png')
    s=s.replace('Comedy Central UK.png','Comedy_Central_UK.png')
    s=s.replace('Crime and Investigation.png','Crime_and_Investigation.png')
    s=s.replace('Discovery Science.png','Discovery_Science.png')
    s=s.replace('Discovery Science UK.png','Discovery_Science_UK.png')
    s=s.replace('Discovery History.png','Discovery_History.png')
    s=s.replace('Discovery Investigation.png','Discovery_Investigation.png')
    s=s.replace('Discovery Investigation UK.png','Discovery_Investigation_UK.png')
    s=s.replace('Discovery Shed.png','Discovery_Shed.png')
    s=s.replace('Discovery Turbo.png','Discovery_Turbo.png')
    s=s.replace('Discovery UK.png','Discovery_UK.png')
    s=s.replace('Disney XD.png','Disney_XD.png')
    s=s.replace('Disney XD UK.png','Disney_XD_UK.png')
    s=s.replace('Disney Jr UK.png','Disney_Jr_UK.png')
    s=s.replace('Encore Western.png','Encore_Western.png')
    s=s.replace('FOX HD.png','FOX_HD.png')
    s=s.replace('FEVA TV.png','FEVA_TV.png')
    s=s.replace('FOX West.png','FOX_West.png')
    s=s.replace('FOX News.png','FOX_News.png')
    s=s.replace('Food Network.png','Food_Network.png')
    s=s.replace('Food UK.png','Food_UK.png')
    s=s.replace('Fox News.png','Fox_News.png')
    s=s.replace('Global Vancouver.png','Global_Vancouver.png')
    s=s.replace('Global Toronto.png','Global_Toronto.png')
    s=s.replace('HBO Comedy.png','HBO_Comedy.png')
    s=s.replace('HBO HD.png','HBO_HD.png')
    s=s.replace('HBO Signature.png','HBO_Signature.png')
    s=s.replace('Movie Time.png','Movie_Time.png')
    s=s.replace('NBC HD.png','NBC_HD.png')
    s=s.replace('NBC West.png','NBC_West.png')
    s=s.replace('Nat Geo Wild.png','Nat_Geo_Wild.png')
    s=s.replace('National Geographic.png','National_Geographic.png')
    s=s.replace('Nick Toons UK.png','Nick_Toons_UK.png')       
    s=s.replace('OMNI 1.png','OMNI_1.png')      
    s=s.replace('OMNI 2.png','OMNI_1.png')   
    s=s.replace('RT Documentary.png','RT_Documentary.png')     
    s=s.replace('RT News.png','RT_News.png')  
    s=s.replace('Rev USA.png','Rev_USA.png')
    s=s.replace('Sky News.png','Sky_News.png')
    s=s.replace('Starz In Black.png','Starz_In_Black.png')
    s=s.replace('Starz Comedy.png','Starz_Comedy.png')
    s=s.replace('Starz Edge.png','Starz_Edge.png')
    s=s.replace('Starz Kids & Family.png','Starz_Kids_&_Family.png')
    s=s.replace('Showtime HD.png','Showtime_HD.png')
    s=s.replace('Showtime Showcase.png','Showtime_Showcase.png')
    s=s.replace('Animal Planet UK.png','Animal_Planet_UK.png')
    s=s.replace('Channel 4.png','Channel_4.png')
    s=s.replace('Channel 5.png','Channel_5.png')
    s=s.replace('Discovery History UK.png','Discovery_History_UK.png')
    s=s.replace('Discovery Science.png','Discovery_Science.png')
    s=s.replace('Discovery Investigation.png','Discovery_Investigation.png')
    s=s.replace('Sky Atlantic.png','Sky_Atlantic.png')
    s=s.replace('Sky Movies Drama.png','Sky_Movies_Drama.png')
    s=s.replace('Sky Movies Action.png','Sky_Movies_Action.png')
    s=s.replace('Sky Movies Comedy.png','Sky_Movies_Comedy.png')
    s=s.replace('Sky Movies Disney.png','Sky_Movies_Disney.png')
    s=s.replace('Sky Movies Family.png','Sky_Movies_Family.png')
    s=s.replace('Sky Movies Premiere.png','Sky_Movies_Premiere.png')
    s=s.replace('Sky Movies Scifi.png','Sky_Movies_Scifi.png')
    s=s.replace('Sky Movies Select.png','Sky_Movies_Select.png')
    s=s.replace('Sky Movies Showcase.png','Sky_Movies_Showcase.png')
    s=s.replace('Starz Kids.png','Starz_Kids.png')
    s=s.replace('National Geographic UK.png','National_Geographic_UK.png')
    s=s.replace('TV Land.png','TV_Land.png')
    s=s.replace('TV JAMAICA.png','TV_JAMAICA.png')
    s=s.replace('Travel XP.png','Travel_XP.png')
    s=s.replace('USA Network.png','USA_Network.png')
    s=s.replace('W MOVIES.png','W_MOVIES.png')
    s=s.replace('WE TV.png','WE_TV.png')
    s=s.replace('WE NETWORK.png','WE_NETWORK.png')
    s=s.replace('Weather Canada.png','Weather_Canada.png')
    s=s.replace('Weather USA.png','Weather_USA.png')
    s=s.replace('WIN TV.png','WIN_TV.png')
    s=s.replace('ASTRO CRICKET HD.png','ASTRO_CRICKET_HD.png')
    s=s.replace('Arena Sports 1 HD.png','Arena_Sports_1_HD.png')     
    s=s.replace('Arena Sports 2 HD.png','Arena_Sports_2_HD.png')      
    s=s.replace('Arena Sports 3 HD.png','Arena_Sports_3_HD.png') 
    s=s.replace('Arena Sports 4 HD.png','Arena_Sports_4_HD.png')    
    s=s.replace('Astro SuperSport 1.png','Astro_SuperSport_1.png')
    s=s.replace('Astro SuperSport 2.png','Astro_SuperSport_2.png')
    s=s.replace('Astro SuperSport 3.png','Astro_SuperSport_3.png')
    s=s.replace('Astro SuperSport 4.png','Astro_SuperSport_4.png')
    s=s.replace('Fox Sports 1 HD.png','Fox_Sports_1_HD.png')
    s=s.replace('Fox Sports 2 HD.png','Fox_Sports_2_HD.png')
    s=s.replace('Golf Channel.png','Golf_Channel.png')
    s=s.replace('MLB Network.png','MLB_Network.png')
    s=s.replace('NBA TV.png','NBA_TV.png')
    s=s.replace('NFL Network.png','NFL_Network.png')
    s=s.replace('NHL Network.png','NHL_Network.png')
    s=s.replace('BT Sport 1.png','BT_Sport_1.png')
    s=s.replace('BT Sport 2.png','BT_Sport_2.png')
    s=s.replace('BT Sport 1 HD.png','BT_Sport_1_HD.png')
    s=s.replace('BT Sport 2 HD.png','BT_Sport_2_HD.png')
    s=s.replace('BT SPORTS ESPN.png','BT_SPORTS_ESPN.png')
    s=s.replace('BT SPORTS EUROPE.png','BT_SPORTS_EUROPE.png')
    s=s.replace('CBS Sports.png','CBS_Sports.png')
    s=s.replace('CTH 1 HD.png','CTH_1_HD.png') 
    s=s.replace('CTH 2 HD.png','CTH_2_HD.png')  
    s=s.replace('CTH 3 HD.png','CTH_3_HD.png')  
    s=s.replace('CTH 4 HD.png','CTH_4_HD.png') 
    s=s.replace('CTH 5 HD.png','CTH_5_HD.png')      
    s=s.replace('CTH XD HD.png','CTH_XD_HD.png')
    s=s.replace('FOX SPORTS 1 ASIA.png','FOX_SPORTS_1_ASIA.png')   
    s=s.replace('FOX SPORTS 2 ASIA.png','FOX_SPORTS_2_ASIA.png')
    s=s.replace('FOX SPORTS 3 ASIA.png','FOX_SPORTS_3_ASIA.png')
    s=s.replace('MOTO GP.png','MOTO_GP.png') 
    s=s.replace('NFL NOW.png','NFL_NOW.png') 
    s=s.replace('PREMIER SPORTS.png','PREMIER_SPORTS.png')                     
    s=s.replace('Setanta Asia HD.png','Setanta_Asia_HD.png')
    s=s.replace('Sky Sports News.png','Sky_Sports_News.png')
    s=s.replace('Sky Sports 1 HD.png','Sky_Sports_1_HD.png')
    s=s.replace('Sky Sports 2 HD.png','Sky_Sports_2_HD.png')
    s=s.replace('Sky Sports 2 HD.png','Sky_Sports_2_HD.png')
    s=s.replace('Sky Sports 3 HD.png','Sky_Sports_3_HD.png')
    s=s.replace('Sky Sports 4 HD.png','Sky_Sports_4_HD.png')
    s=s.replace('Sky Sports 5 HD.png','Sky_Sports_5_HD.png')
    s=s.replace('Sky Sports F1.png','Sky_Sports_F1.png')
    s=s.replace('Sky Sports News.png','Sky_Sports_News.png')
    s=s.replace('Sony Six.png','Sony_Six.png')
    s=s.replace('Sportsnet 360.png','Sportsnet_360.png')
    s=s.replace('Sportsnet One.png','Sportsnet_One.png')
    s=s.replace('Sportsnet Ontario.png','Sportsnet_Ontario.png')
    s=s.replace('Sportsnet World.png','Sportsnet_World.png')
    s=s.replace('Tennis Channel.png','Tennis_Channel.png')
    s=s.replace('TEN Cricket.png','TEN_Cricket.png')
    s=s.replace('WWE Network.png','WWE_Network.png')
    s=s.replace('WILLOW CRICKET.png','WILLOW_CRICKET.png')
    #
    
    
    
    s=s.replace('3E HD','3e')
    s=s.replace('5STAR MAX HD - NEW','5StarMax')
    s=s.replace('A+E HD','AE')
    s=s.replace('5 Star','5STAR')
    s=s.replace('ABC HD EAST','ABC HD')                       
    s=s.replace('ABC HD WEST - NEW','ABC West')                      
    s=s.replace('ABC NEWS','ABC News')                       
    s=s.replace('ACTION HD','ACTION')
    s=s.replace('ACTION MAX HD - NEW','ActionMax')                       
    s=s.replace('ALJAZEERA ENGLISH','Aljazeera')                      
    s=s.replace('AMAZING DISCOVERIES','Amazing Discoveries')                       
    s=s.replace('AMAZING FACTS','Amazing Facts')    
    s=s.replace('ANIMAL PLANET HD','Animal Planet') 
    s=s.replace('BBC AMERICA HD','BBC America')
    s=s.replace('BBC NEWS','BBC News') 
    s=s.replace('BBC One HD','BBC1')
    s=s.replace('BBC Two HD','BBC2')
    s=s.replace('BBC Three HD','BBC3')
    s=s.replace('BBC Four HD','BBC4') 
    s=s.replace('BC1 HD - NEW','BC1') 
    s=s.replace('BET HD','BET')
    s=s.replace('BLOOMBERG','Bloomberg') 
    s=s.replace('BNN HD - NEW','BNN') 
    s=s.replace('BOUNCE HD','Bounce')
    s=s.replace('BRAVO HD','Bravo')
    s=s.replace('CARTOON NETWORK HD (NA)','Cartoon Network') 
    s=s.replace('CBC EAST HD','CBC') 
    s=s.replace('CBC NEWS HD','CBC News')
    s=s.replace('CBC VANCOUVER HD- NEW','CBC Vancouver') 
    s=s.replace('CBS HD EAST','CBS HD') 
    s=s.replace('CBS HD WEST - NEW','CBS West')
    s=s.replace('CBS NEWS HD','CBS News')
    s=s.replace('CHCH HD','CHCH')
    s=s.replace('CINEMAX EAST HD - NEW','Cinemax') 
    s=s.replace('CITY TV HD','City TV Toronto')
    s=s.replace('CITY VANCOUVER HD - NEW','City TV Vancouver') 
    s=s.replace('CNBC HD','CNBC') 
    s=s.replace('CNN HD','CNN')
    #s=s.replace('COMEDY NETWORK HD','Comedy Network')
    s=s.replace('COMEDY NETWORK HD','Comedy Central')
    s=s.replace('CP24 HD','CP24')
    s=s.replace('CTV EAST HD','CTV Toronto') 
    s=s.replace('CTV NORTH','CTV North')
    s=s.replace('CTV VANCOUVER HD - NEW','CTV Vancouver') 
    s=s.replace('CW11 HD','CW') 
    s=s.replace('DISCOVERY HD','Discovery')
    s=s.replace('DISCOVERY SCIENCE HD','Discovery Science')
    s=s.replace('DISNEY HD EAST','Disney')
    s=s.replace('DISNEY XD HD (NA)','Disney XD') 
    s=s.replace('E! HD','E!')
    s=s.replace('ENCORE WESTERN HD - NEW','Encore Western') 
    s=s.replace('FAMILY HD (NA)','FAMILY') 
    s=s.replace('FOOD HD','Food Network')
    s=s.replace('FOX HD EAST','FOX HD')
    s=s.replace('FOX HD WEST - NEW','FOX West')    
    s=s.replace('FOX NEWS HD','FOX News') 
    s=s.replace('FX HD','FX')
    s=s.replace('FXX HD','FXX') 
    s=s.replace('GLOBAL BC HD - NEW','Global Vancouver') 
    s=s.replace('GLOBAL EAST HD','Global Toronto')
    s=s.replace('HALLMARK HD','Hallmark')
    s=s.replace('HBO COMEDY HD','HBO Comedy') 
    s=s.replace('HBO EAST HD','HBO HD') 
    s=s.replace('HBO SIGNATURE HD','HBO Signature')
    s=s.replace('HGTV HD','HGTV') 
    s=s.replace('HISTORY HD','History') 
    s=s.replace('HLN HD','HLN')
    s=s.replace('HSN 2','HSN2')                       
    s=s.replace('ID HD','Discovery Investigation')
    s=s.replace('IFC HD','IFC')    
    s=s.replace('LIFE HD','Lifetime') 
    s=s.replace('LIFETIME MOVIES HD','LMN')
    s=s.replace('MOREMAX HD - NEW','MoreMax') 
    s=s.replace('MOVIE TIME HD','MovieTime') 
    s=s.replace('MSNBC HD','MSNBC')
    s=s.replace('MTV HD','MTV')
    s=s.replace('NAT GEO HD','National Geographic') 
    s=s.replace('NAT GEO WILD HD','Nat Geo Wild') 
    s=s.replace('NBC HD EAST','NBC HD')
    s=s.replace('NBC HD WEST - NEW','NBC West') 
    s=s.replace('NICKELODEON HD (NA)','Nickelodeon') 
    s=s.replace('OMNI 1 HD','OMNI 1')
    s=s.replace('OMNI 2 HD','OMNI 2')
    s=s.replace('OWN HD','OWN')    
    s=s.replace('PBS HD','PBS') 
    #s=s.replace("REV'N USA HD",'Rev USA')
    s=s.replace('RT DOCUMENTARY HD','RT Documentary') 
    s=s.replace('RT NEWS HD','RT News') 
    s=s.replace('SHOWCASE HD','SHOWCASE')
    s=s.replace('SHOWTIME EAST','Showtime HD')
    s=s.replace('SHOWTIME SHOWCASE HD','Showtime Showcase') 
    s=s.replace('SKY CBBC HD','CBBC') 
    s=s.replace('SKY DISNEY JR (UK)','Disney Jr UK')
    s=s.replace('SKY DISNEY XD (UK)','Disney XD UK') 
    s=s.replace('SKY NEWS HD','Sky News') 
    s=s.replace('SKY NICK (UK)','Nickelodeon UK')
    s=s.replace('SKY NICK TOONS (UK)','Nick Toons UK')
    s=s.replace('SLICE HD','SLICE')    
    s=s.replace('SPIKE HD','Spike') 
    s=s.replace('STARZ BLACK HD','Starz In Black')
    s=s.replace('STARZ COMEDY HD - NEW','Starz Comedy') 
    s=s.replace('STARZ EDGE HD','Starz Edge') 
    s=s.replace('STARZ HD','Starz')
    s=s.replace('STARZ KIDZ HD - NEW','Starz Kids')
    s=s.replace('Sky 3E','3e') 
    s=s.replace('Sky Alibi','Alibi') 
    s=s.replace('Sky Animal Planet','Animal Planet UK')
    s=s.replace('Sky Channel 4','Channel 4') 
    s=s.replace('Sky Channel 5','Channel 5') 
    s=s.replace('Sky Comedy Network','Comedy Central UK')
    s=s.replace('Sky Crime and Investigation','Crime and Investigation')
    s=s.replace('Sky Dave','Dave')    
    s=s.replace('Sky Discovery','Discovery UK') 
    s=s.replace('Sky Discovery History','Discovery History')
    s=s.replace('Sky Discovery Science','Discovery Science UK') 
    s=s.replace('Sky Discovery Shed','Discovery Shed') 
    s=s.replace('Sky Discovery Turbo','Discovery Turbo')
    s=s.replace('Sky Discovery investigation','Discovery Investigation UK')
    s=s.replace('Sky Eden','Eden') 
    s=s.replace('Sky Film 4','Film4') 
    s=s.replace('Sky Food','Food UK')
    s=s.replace('Sky Gold','Gold') 
    s=s.replace('Sky Home','Home') 
    s=s.replace('Sky Movie Romance','Sky Movies Drama')
    s=s.replace('Sky Movies Atlantic','Sky Atlantic')    
    s=s.replace('Sky Movies Sci-Fi','Sky Movies Scifi') 
    s=s.replace('Sky Natgeo','National Geographic UK')
    s=s.replace('SKY News','Sky News')
    s=s.replace('Sky One','Sky1') 
    s=s.replace('Sky Quest','Quest') 
    s=s.replace('Sky RTE 1','RTE1')
    s=s.replace('Sky RTE 2','RTE2')
    s=s.replace('Sky Watch','Watch')  
    s=s.replace('Sky Yesterday','Yesterday') 
    s=s.replace('Sky itv1','ITV1')
    s=s.replace('Sky itv2','ITV2') 
    s=s.replace('Sky itv3','ITV3')
    s=s.replace('Sky itv4','ITV4')
    s=s.replace('SyFy HD','Syfy')
    s=s.replace('TBS HD','TBS')    
    s=s.replace('TCM EAST HD','TCM') 
    s=s.replace('TCM HD','TCM')
    s=s.replace('THRILLER MAX HD - NEW','ThrillerMax') 
    s=s.replace('TLC HD','TLC') 
    s=s.replace('TNT HD','TNT')
    s=s.replace('TRAVEL HD','Travel')
    s=s.replace('TREEHOUSE HD (NA)','TREEHOUSE') 
    s=s.replace('TRU TV HD','truTV') 
    s=s.replace('TV LAND HD','TV Land')
    s=s.replace('TVO HD (NA)','TVO') 
    s=s.replace('USA NETWORK HD','USA Network') 
    s=s.replace('VELOCITY HD','VELOCITY')
    s=s.replace('VEVO 1 HD','VEVO1')
    s=s.replace('VEVO 2 HD','VEVO2')    
    s=s.replace('VH1 HD','VH1')    
    s=s.replace('VICELAND HD','Viceland') 
    s=s.replace('W MOVIES HD','W MOVIES')
    s=s.replace('W NETWORK HD','W NETWORK') 
    s=s.replace('WE TV HD','WE TV') 
    s=s.replace('WEATHER CANADA HD','Weather Canada')
    s=s.replace('WEATHER USA HD','Weather USA')
    s=s.replace('WIN TV HD','WIN TV')
    s=s.replace('YTV HD (NA)','YTV')
    s=s.replace('Astro Supersports 1 HD','Astro SuperSport 1') 
    s=s.replace('Astro Supersports 2 HD','Astro SuperSport 2') 
    s=s.replace('Astro Supersports 3 HD','Astro SuperSport 3')                        
    s=s.replace('Astro Supersports 4 HD','Astro SuperSport 4')                         
    s=s.replace('Astro Supersports 1 HD','Astro Supersports 1') 
    s=s.replace('Astro Supersports 2 HD','Astro Supersports 2') 
    s=s.replace('Astro Supersports 3 HD','Astro Supersports 3')                        
    s=s.replace('Astro Supersports 4 HD','Astro Supersports 4')                    
    s=s.replace('BEIN HD','BEINS1') 
    s=s.replace('CBS SPORTS HD','CBS Sports')
    s=s.replace('ESPN HD','ESPN')
    s=s.replace('ESPN 2 HD','ESPN2')    
    s=s.replace('FOX SPORTS 1 HD','Fox Sports 1 HD') 
    s=s.replace('FOX SPORTS 2 HD','Fox Sports 2 HD')
    s=s.replace('GOLF HD','Golf Channel') 
    s=s.replace('MLB HD 01','MLB1') 
    s=s.replace('MLB HD 02','MLB2') 
    s=s.replace('MLB HD 03','MLB3')                       
    s=s.replace('MLB HD 04','MLB4')                        
    s=s.replace('MLB HD 05','MLB5') 
    s=s.replace('MLB HD 06','MLB6')                        
    s=s.replace('MLB HD 07','MLB7')                        
    s=s.replace('MLB HD 08','MLB8')                       
    s=s.replace('MLB HD 09','MLB9')                        
    s=s.replace('MLB HD 10','MLB10')                       
    s=s.replace('MLB HD 11','MLB11')                       
    s=s.replace('MLB HD 12','MLB12')                      
    s=s.replace('MLB NETWORK','MLB Network')
    s=s.replace('NBA HD','NBA TV')
    s=s.replace('NBC SPORTS','NBCSN') 
    s=s.replace('NFL NOW HD','NFL NOW')
    s=s.replace('NHL NETWORK HD','NHL Network') 
    s=s.replace('NHL ON VERSUS HD','VERSUS') 
    s=s.replace('SKY BOX NATION','BoxNation')
    s=s.replace('SKY BT 1','BT Sport 1')
    s=s.replace('SKY BT 2','BT Sport 2')    
    s=s.replace('SKY BT 1 HD','BT Sport 1 HD')
    s=s.replace('SKY BT 2 HD','BT Sport 2 HD')
    s=s.replace('Sky Sports News HD','Sky Sports News') 
    s=s.replace('SKY SPORTS 1','Sky Sports 1 HD') 
    s=s.replace('SKY SPORTS 2','Sky Sports 2 HD') 
    s=s.replace('SKY SPORTS 3','Sky Sports 3 HD')                        
    s=s.replace('SKY SPORTS 4','Sky Sports 4 HD')                       
    s=s.replace('SKY SPORTS 5','Sky Sports 5 HD')                       
    s=s.replace('SONY ESPN HD - LIVE EVENTS','PPV')
    #s=s.replace('SPORT TIME TV 1HD','SPORT TIME TV 1HD') 
    s=s.replace('SPORTSNET 360','Sportsnet 360') 
    s=s.replace('SPORTSNET ONE HD','Sportsnet One')
    s=s.replace('SPORTSNET ONT','Sportsnet Ontario')
    s=s.replace('SPORTSNET WORLD HD','Sportsnet World') 
    s=s.replace('Sky Sports News HD','Sky Sports News HD')
    s=s.replace('Sony Six HD','Sony Six') 
    s=s.replace('TEN CRICKET HD','TEN Cricket') 
    s=s.replace('TENNIS HD','Tennis Channel')
    s=s.replace('TSN 1 HD','TSN1')
    s=s.replace('TSN 2 HD','TSN2')
    s=s.replace('TSN 3 HD','TSN3')                       
    s=s.replace('TSN 4 HD','TSN4')                       
    s=s.replace('TSN 5 HD','TSN5')                      
    s=s.replace('WILLOW CRICKET HD','WILLOW CRICKET')    
    s=s.replace('WWE HD','WWE Network') 
    s=s.replace('W NETWORK','W Network') 
    s=s.replace('YANKEES HD - NEW','YANKEES')
    s=s.replace('HUSTLER HD','HUSTLER') 
    s=s.replace('PLAYBOY TV HD - NEW','PLAYBOY') 
    s=s.replace('VIVID TV - NEW','VIVID')    

    s=s.replace('东方财经浦东 ','') 
    s=s.replace('凤凰卫视 ','') 
    s=s.replace('凤凰美洲台 ','') 
    s=s.replace('凤凰香港台 ','')     
    s=s.replace('华夏电视 ','')     
    s=s.replace('厦门卫视 ','') 
    s=s.replace('台视美洲','(bonus)')     
    s=s.replace('四川国际 ','')         
    s=s.replace('国际频道 ','') 
    s=s.replace('天津卫视 ','')     
    s=s.replace('天津卫视 HD ','') 
    s=s.replace('央视 ','') 
    s=s.replace('安徽卫视 ','') 
    s=s.replace('山东卫视 HD ','')     
    s=s.replace('广东南方 ','')     
    s=s.replace('广东南方卫视 ','') 
    s=s.replace('旅游卫视 ','')     
    s=s.replace('时尚生活 ','')         
    s=s.replace('昆仑 HD ','') 
    s=s.replace('東森','(bonus)')    
    s=s.replace('河南卫视 ','')         
    s=s.replace('浙江卫视 HD ','') 
    s=s.replace('澳亞衛視','(bonus)') 



    #if args.ini_file:
    #    s=s.replace('m3u8','ts')
    f=open(Clean_Name,'a')
    f.write(s)
    f.close()
    os.remove(tmpFile)
    return


# Run #
if __name__ == '__main__':
    if StartCreate():
        StartCreate()
        print 'Subscriptions1'
    else:
        #StartCreate()
        print 'Subscriptions2'
