import sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urllib2,re
import shutil
import time
import requests
import pickle
import base64
addon         = 'plugin.program.reloadedtv'
addonPath     = xbmc.translatePath(os.path.join('special://home/addons', addon))
sys.path.append(addonPath)
import cfscrape
import lolol

addon         = 'plugin.program.reloadedtv'
ADDONID       = addon
addon_name    = addon
icon = xbmc.translatePath(os.path.join('special://home/addons', addon, 'icon.png'))
addonPath = xbmc.translatePath(os.path.join('special://home', 'addons', addon))
basePath = xbmc.translatePath(os.path.join('special://profile', 'addon_data', addon))
dbPath = xbmc.translatePath(xbmcaddon.Addon(addon).getAddonInfo('profile'))
dialog = xbmcgui.Dialog();dp = xbmcgui.DialogProgress()

cookiefile = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'plugin.program.reloadedtv', 'cookie'))
UA         = base64.b64decode('VXNlci1BZ2VudC1NYXlmYWlyUFJP') + "Reloaded TV"

skin1 = 'Default'
skin2 = 'FTV_Blue'
skin3 = 'FTV_Dark'
skin4 = 'FTV_Default'
skin5 = 'FTV_MOD'
skin6 = 'FTV_Eminence'
skin7 = 'FTV_Touch'

mode='run_skinsDL_Menu'

def skinsDL_Menu():
#        choice = dialog.select('Choose skin to Download', ['Close',
#                                                           skin1,
#                                                           skin2,
#                                                          skin3,
#                                                           skin4,
#                                                           skin5,
#                                                           skin6,
#                                                           skin7])
#        if choice == 0: sys.exit(0)
#        if choice == 1:
#            skinDL(skin1)
#        if choice == 2:
#            skinDL(skin2)
#        if choice == 3:
#            skinDL(skin3)
#        if choice == 4:
#            skinDL(skin4)
#        if choice == 5:
#            skinDL(skin5)
#        if choice == 6:
#            skinDL(skin6)
#        if choice == 7:
#            skinDL(skin7)

    skinDL()

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
        currenttime = time.time()
        cookieexpire = currenttime - 870
        if os.path.exists(cookiefile):
            cookiemodifedtime = os.path.getmtime(cookiefile)
        if not os.path.exists(cookiefile) or cookiemodifedtime < cookieexpire:
            session = requests.session()
            scraper = cfscrape.create_scraper(sess=session)
            r = scraper.get(skins, headers={'User-Agent': (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False)
            save_cookies(scraper.cookies, cookiefile)
            session.close
        else:
            r = requests.get(skins, headers={'User-Agent': (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False, cookies=load_cookies(cookiefile))
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
            getSkin(label, id, item[1])
            notify('Skins',label + ' ' + ver + ' successfully Installed.',os.path.join('special://home/addons', addon, 'icon.png'))##NOTIFY##  
        SetSetting('skin', 'Default')
        d = xbmcgui.Dialog()            
        d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Reset successfully performed.','','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')
    except: 
        import sys
        import traceback as tb
        (etype, value, traceback) = sys.exc_info()
        tb.print_exception(etype, value, traceback)

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
    except:
        pass
#

def SetSetting(param, value):
    try:
        value = str(value)
        if GetSetting(param) == value:
            return
        xbmcaddon.Addon(ADDONID).setSetting(param, value)
    except:
        import sys
        import traceback as tb
        (etype, value, traceback) = sys.exc_info()
        tb.print_exception(etype, value, traceback)

def GetSetting(param):
    try:
        return xbmcaddon.Addon(ADDONID).getSetting(param)
    except:
        import sys
        import traceback as tb
        (etype, value, traceback) = sys.exc_info()
        tb.print_exception(etype, value, traceback)

def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)

def mayfairdownloader(url, dest):
    BUFFSIZE = 1024 * 4
    progress = xbmcgui.DialogProgress()
    progress.create("Skin","Downloading & Installing Skins", ' ', ' ')
    currenttime = time.time()
    cookieexpire = currenttime - 870
    if os.path.exists(cookiefile):
        cookiemodifedtime = os.path.getmtime(cookiefile)
    if not os.path.exists(cookiefile) or cookiemodifedtime < cookieexpire:
        session = requests.session()
        scraper = cfscrape.create_scraper(sess=session)
        r = scraper.get(url, auth=(lolol.lolu(), lolol.lolp()), verify=False, stream=True)
        save_cookies(scraper.cookies, cookiefile)
        session.close
    else:
        r = requests.get(url, auth=(lolol.lolu(), lolol.lolp()), verify=False, cookies=load_cookies(cookiefile), stream=True)

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
    
def format_delta(s):
    s = int(s)
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
            import sys
            import traceback as tb
            (etype, value, traceback) = sys.exc_info()
            tb.print_exception(etype, value, traceback)
        if dp.iscanceled(): 
            dp.close() 
#
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
#

if mode=='run_skinsDL_Menu' : skinsDL_Menu()
