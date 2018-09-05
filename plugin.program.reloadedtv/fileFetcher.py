# -*- coding: utf-8 -*-
#
# FTV Guide
# Copyright (C) 2015 Thomas Geppert [bluezed]
# bluezed.apps@gmail.com
#
# This Program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
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
import xbmc
import xbmcvfs
import os
import urllib2
import datetime
import zlib

# downloader
import xbmcgui
import urllib
import time
import sys
import base64
import requests
import pickle
import add
import cfscrape
import xbmcaddon
import json
import lolol

MAIN_URL = base64.b64decode('aHR0cDovL21heWZhaXJndWlkZXMuY29tL2d1aWRlLw==')
REPO  =  xbmc.translatePath(os.path.join('special://home/addons','repository.GearsTV'))
cookiefile = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'plugin.program.reloadedtv', 'cookie'))
ADDONID    = 'plugin.program.reloadedtv'
ADDON      =  xbmcaddon.Addon(ADDONID)
UA         = base64.b64decode('VXNlci1BZ2VudC1NYXlmYWlyUFJP') + "Reloaded TV"
addonbase  = base64.b64decode('cGx1Z2luLnByb2dyYW0ubXR2Z3VpZGVwcm8=')

if not os.path.exists(REPO):
        dialog = xbmcgui.Dialog()
        dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", "[B][COLOR lime]Sorry, you DO NOT have Reloaded TV's Repository installed![/COLOR][/B]","[COLOR yellow]Reloaded TV's Repository is needed for OFFICIAL updates.[/COLOR]","Get it at: [COLOR orangered]http://targetcreates.com/repo/[/COLOR]")
        sys.exit(1)

class FileFetcher(object):
    INTERVAL_ALWAYS = 0
    INTERVAL_12 = 1
    INTERVAL_24 = 2
    INTERVAL_48 = 3

    FETCH_ERROR = -1
    FETCH_NOT_NEEDED = 0
    FETCH_OK = 1

    TYPE_DEFAULT = 1
    TYPE_REMOTE = 2
    basePath = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'plugin.program.reloadedtv'))
    filePath = ''
    fileUrl = ''
    addon = None
    fileType = TYPE_DEFAULT

    def __init__(self, fileName, addon):
        self.addon = addon
        self.lolololol = self.get_reloaded()
        self.isrs = self.checkrs()

        if fileName.startswith("http://") or fileName.startswith("sftp://") or fileName.startswith("ftp://") or \
                fileName.startswith("https://") or fileName.startswith("ftps://") or fileName.startswith("smb://") or \
                fileName.startswith("nfs://"):
            self.fileType = self.TYPE_REMOTE
            self.fileUrl = fileName
            self.filePath = os.path.join(self.basePath, fileName.split('/')[-1])
        else:
            self.fileType = self.TYPE_DEFAULT
            self.filePath = os.path.join(self.basePath, fileName)
            if self.isrs:
                self.fileUrl = lolol.lolrs(fileName)
            else:
                self.fileUrl = lolol.lolf(fileName)

        # make sure the folder is actually there already!
        if not os.path.exists(self.basePath):
            os.makedirs(self.basePath)

    def fetchFile(self):
        retVal = self.FETCH_NOT_NEEDED
        fetch = False
        if not os.path.exists(os.path.join(self.basePath, 'guide.xml')):
            fetch = True
        if not os.path.exists(self.filePath):  # always fetch if file doesn't exist!
            fetch = True
        else:
            interval = int(self.addon.getSetting('xmltv.interval'))
            if interval != self.INTERVAL_ALWAYS:
                modTime = datetime.datetime.fromtimestamp(os.path.getmtime(self.filePath))
                td = datetime.datetime.now() - modTime
                # need to do it this way cause Android doesn't support .total_seconds() :(
                diff = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10 ** 6) / 10 ** 6
                if ((interval == self.INTERVAL_12 and diff >= 345600) or      
                        (interval == self.INTERVAL_24 and diff >= 86400) or
                        (interval == self.INTERVAL_48 and diff >= 172800)):
                    fetch = True
            else:
                fetch = True

        if fetch:
            tmpFile = os.path.join(self.basePath, 'tmp')
            if self.fileType == self.TYPE_REMOTE:
                xbmc.log('[plugin.program.reloadedtv] file is in remote location: %s' % self.fileUrl, xbmc.LOGDEBUG)
                if not xbmcvfs.copy(self.fileUrl, tmpFile):
                    xbmc.log('[plugin.program.reloadedtv] Remote file couldn\'t be copied: %s' % self.fileUrl, xbmc.LOGERROR)                 
            else:
                # Builtin               
                xbmc.log('[plugin.program.reloadedtv] file is on the internet: %s' % self.fileUrl, xbmc.LOGDEBUG)
                if ".zip" in self.fileUrl:
                    tmpData = lolol.loldd(self.fileUrl,tmpFile)         
                else:
                    f = open(tmpFile, 'wb')
                    tmpData = lolol.lold(self.fileUrl)
                    #if 'addons.ini' in self.fileUrl:
                    #    tmpData = tmpData.replace(addonbase, ADDONID)
                    f.write(tmpData)
                    f.close()

            if os.path.getsize(tmpFile) > 0:
                if os.path.exists(self.filePath):
                    os.remove(self.filePath)
                os.rename(tmpFile, self.filePath)
                retVal = self.FETCH_OK
                xbmc.log('[plugin.program.reloadedtv] file %s was downloaded' % self.filePath, xbmc.LOGDEBUG)          
                if ".zip" in self.fileUrl:
                    print self.fileUrl
                    try:
                        import zipfile                  
                        zin = zipfile.ZipFile(self.filePath, 'r')
                        zin.extractall(self.basePath)
                        zin.close()
                        add.StartCreate()
                    except: 
                        pass
            else:
                retVal = self.FETCH_ERROR 
        return retVal

    def get_reloaded(self):
        try:
            u = base64.b64decode("aHR0cDovL21heWZhaXJndWlkZXMuY29tL2d1aWRlL3JlbG9hZGVkLnR4dA==")
            uu = requests.get(u, headers={'User-Agent': (UA)}).content
            return uu
        except:
            dialog = xbmcgui.Dialog()
            dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", base64.b64decode("RXJyb3IhIENvdWxkIG5vdCBjb25uZWN0IHRvIHNlcnZlciBbMV0="),"", base64.b64decode("UGxlYXNlIHRyeSBhZ2FpbiBsYXRlci4="))

    def get_reloaded_account_info(self):
        try:
            lolol.show_busy_dialog()
            req = urllib2.Request(self.lolololol+base64.b64decode("L3BhbmVsX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXM=")%(urllib.quote_plus(ADDON.getSetting(base64.b64decode("cmVsb2FkZWQudXNlcg=="))),urllib.quote_plus(ADDON.getSetting(base64.b64decode("cmVsb2FkZWQucGFzcw==")))))
            req.add_header(base64.b64decode("VXNlci1BZ2VudA==") , base64.b64decode("TWF5ZmFpckd1aWRlLVVzZXJBZ2VudA=="))
            response = urllib2.urlopen(req)
            link=response.read()
            jdata = json.loads(link.decode('utf8'))
            response.close()
            lolol.hide_busy_dialog()
            return jdata
        except:
            lolol.hide_busy_dialog()
            try:
                lolol.show_busy_dialog()
                req = urllib2.Request(base64.b64decode("aHR0cDovL3JlbG9hZGVkbm93LmNvbToyMDg2L3BhbmVsX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXM=")%(urllib.quote_plus(ADDON.getSetting(base64.b64decode("cmVsb2FkZWQudXNlcg=="))),urllib.quote_plus(ADDON.getSetting(base64.b64decode("cmVsb2FkZWQucGFzcw==")))))
                req.add_header(base64.b64decode("VXNlci1BZ2VudA==") , base64.b64decode("TWF5ZmFpckd1aWRlLVVzZXJBZ2VudA=="))
                response = urllib2.urlopen(req)
                link=response.read()
                jdata = json.loads(link.decode('utf8'))
                response.close()
                lolol.hide_busy_dialog()
                return jdata
            except:
                lolol.hide_busy_dialog()
                dialog = xbmcgui.Dialog()
                dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]",base64.b64decode("RXJyb3Ih"),base64.b64decode("SXMg")+"Reloaded TV"+base64.b64decode("IGRvd24/"),"")

    def checkrs(self):
        rsdata = self.get_reloaded_account_info()
        rsinfo = rsdata[base64.b64decode("dXNlcl9pbmZv")]
        rsinfo = rsinfo[base64.b64decode("ZXhwX2RhdGU=")]
        if rsinfo:
            return True
        return False
        

def mayfairdownloader(url, dest):
    BUFFSIZE = 1024 * 4
    progress = xbmcgui.DialogProgress()
    progress.create("[COLOR red]Reloaded TV Guide[/COLOR]", "Downloading & Installing Files", ' ', ' ')
    #currenttime = time.time()
    #cookieexpire = currenttime - 870
    if os.path.exists(cookiefile):
        r = requests.get(url, headers={'User-Agent': (UA)}, cookies=load_cookies(cookiefile), stream=True)
    else:
        r = requests.get(url, headers={'User-Agent': (UA)}, stream=True)

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

            progress.update(int(completion) * 100, "Downloading & Installing Files", " ", *text)

            if progress.iscanceled():
                break

    outfile.close()
    progress.close()

def format_delta(s):
    s = int(s)

def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)

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
