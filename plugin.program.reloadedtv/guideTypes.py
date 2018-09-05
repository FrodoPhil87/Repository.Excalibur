# -*- coding: utf-8 -*-
#
# added reopen guide after selection and changed guides.ini to guide.cfg
# Copyright (C) 2015 Thomas Geppert [bluezed]
# bluezed.apps@gmail.com
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
import xbmc
import xbmcgui
import xbmcaddon
import os
import json
import ConfigParser
import xml.etree.ElementTree as ET
import sqlite3 as lite
import sys

from fileFetcher import *
from strings import *
from operator import itemgetter

ADDON = xbmcaddon.Addon(id='plugin.program.reloadedtv')
SOURCE_DB = 'source.db'
dex = 'dex'
reloaded = 'reloaded'
aftermathtv = 'aftermathtv'
ukturk = 'ukturk'
sanctuary = 'sanctuary'
OTTTV     = 'OTTTV'
suicide21 = 'suicid21e'
freeview  = 'freeview'
FTV = 'ftv'
uktvnow = 'uktvnow'
cluiptv = 'cluiptv'
suicide = 'suicide'
projectcypher = 'projectcypher'
notfilmon = 'filmnoton'
israelive = 'israelive'
adriansports = 'adriansports'
evolve = 'evolve'

dexAddon = 'plugin.video.dex'
reloadedAddon = 'plugin.video.reloadedtv'
OTTTVAddon  = 'plugin.video.ottalpha'
suicide21Addon = 'plugin.video.suicidetv21'
freeviewAddon  = 'plugin.video.freeview'
aftermathtvAddon = 'plugin.video.aftermathtv'
ukturkAddon = 'plugin.video.ukturk'
sanctuaryAddon = 'plugin.video.sanctuary'
FTVAddon = 'plugin.video.F.T.V'
uktvnowAddon = 'plugin.video.uktvnow'
cluiptvAddon = 'plugin.video.cluiptv'
suicideAddon = 'plugin.video.suicidetv'
projectcypherAddon = 'plugin.video.ProjectCypher'
notfilmonAddon = 'plugin.video.notfilmon'
israeliveAddon = 'plugin.video.israelive'
adriansportsAddon = 'plugin.video.adriansports'
evolveAddon = 'plugin.video.Evolve'

#profilePath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
#if not os.path.exists(profilePath):
#    os.makedirs(profilePath)
#    self.databasePath = os.path.join(profilePath, Database.SOURCE_DB)


class GuideTypes(object):
    GUIDE_ID = 0
    GUIDE_SORT = 1
    GUIDE_NAME = 2
    GUIDE_FILE = 3
    GUIDE_DEFAULT = 4

    CUSTOM_FILE_ID = 6

    guideTypes = []
    guideParser = ConfigParser.ConfigParser()
    filePath = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'plugin.program.reloadedtv', 'guide.cfg'))

    def __init__(self):
        try:
            if not os.path.exists(self.filePath):
                fetcher = FileFetcher('guide.cfg', ADDON)
                if fetcher.fetchFile() < 0:
                    xbmcgui.Dialog().ok(strings(FETCH_ERROR_TITLE), strings(FETCH_ERROR_LINE1), strings(FETCH_ERROR_LINE2))

            self.guideParser.read(self.filePath)
            guideTypes = []
            defaultGuideId = 0  # fallback to the first guide in case no default is actually set in the ini file
            for section in self.guideParser.sections():
                sectMap = self.SectionMap(section)
                id = int(sectMap['id'])
                fName = sectMap['file']
                sortOrder = int(sectMap['sort_order'])
                default = False
                if 'default' in sectMap and sectMap['default'] == 'true':
                    default = True
                    defaultGuideId = id
                guideTypes.append((id, sortOrder, section, fName, default))
            self.guideTypes = sorted(guideTypes, key=itemgetter(self.GUIDE_SORT))
            xbmc.log('[plugin.program.reloadedtv] GuideTypes collected: %s' % str(self.guideTypes), xbmc.LOGDEBUG)

            if str(ADDON.getSetting('xmltv.type')) == '':
                ADDON.setSetting('xmltv.type', str(defaultGuideId))
        except:
            print 'unable to parse guide.cfg'

    def SectionMap(self, section):
        dict1 = {}
        options = self.guideParser.options(section)
        for option in options:
            try:
                dict1[option] = self.guideParser.get(section, option)
                if dict1[option] == -1:
                    xbmc.log('[plugin.program.reloadedtv] skip: %s' % option, xbmc.LOGDEBUG)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1


    def getGuideDataItem(self, id, item):
        value = None
        guide = self.getGuideById(id)
        try:
            value = guide[item]
        except IndexError:
            xbmc.log('[plugin.program.reloadedtv] DataItem with index %s not found' % item, xbmc.LOGDEBUG)
        return value


    def getGuideById(self, id):
        xbmc.log('[plugin.program.reloadedtv] Finding Guide with ID: %s' % id, xbmc.LOGDEBUG)
        ret = []
        for guide in self.guideTypes:
            if guide[self.GUIDE_ID] == int(id):
                ret = guide
                xbmc.log('[plugin.program.reloadedtv] Found Guide with data: %s' % str(guide), xbmc.LOGDEBUG)
        return ret


def getKodiVersion():
    # retrieve current installed version
    jsonQuery = xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Application.GetProperties", "params": {"properties": ["version", "name"]}, "id": 1 }')
    jsonQuery = unicode(jsonQuery, 'utf-8', errors='ignore')
    jsonQuery = json.loads(jsonQuery)
    version = []
    if jsonQuery.has_key('result') and jsonQuery['result'].has_key('version'):
        version = jsonQuery['result']['version']
    return version['major']
    
def CheckHasThisAddon(FoundAddon):
    if xbmc.getCondVisibility('System.HasAddon(%s)' % FoundAddon) == 1:
        return True
    else:
        return False 
    
def updatecategories(typeName):
    con = None
    profilePath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
    if not os.path.exists(profilePath):
        os.makedirs(profilePath)
    databasePath = os.path.join(profilePath, SOURCE_DB)
    
    try:
        con = lite.connect(databasePath, detect_types=lite.PARSE_DECLTYPES)
            
        cur = con.cursor()
        if ADDON.getSetting('chnorder') == 'A-Z':
            cur.execute("CREATE TEMPORARY TABLE alphaTemp as WITH wtfIhateYou AS (select id, title, weight, (SELECT COUNT(*) - 1 FROM channels a WHERE a.title <= b.title COLLATE NOCASE) as rowNumber from Channels b Order By title COLLATE NOCASE ASC) select * from wtfIhateYou")
            con.commit()
            cur.execute("UPDATE Channels SET weight = (select rowNumber from alphaTemp where id = Channels.id)")
            con.commit()
            cur.execute("DROP TABLE alphaTemp")
            con.commit()
        if ADDON.getSetting('chnorder') == 'Default':
            cur.execute("UPDATE channels SET weight = rowid - 1")
            con.commit()
        cur.execute("UPDATE channels SET visible = 0")
        if ADDON.getSetting('dexter.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+dex+'%'])
            con.commit()
        if ADDON.getSetting('reloaded.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+reloaded+'%'])
            con.commit()
        if ADDON.getSetting('OTTTV.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+OTTTV+'%'])
            con.commit()
        if ADDON.getSetting('suicide21.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+suicide21+'%'])
            con.commit()
        if ADDON.getSetting('freeview.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+freeview+'%'])
            con.commit()
        if ADDON.getSetting('aftermathtv.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+aftermathtv+'%'])
            con.commit()
        if ADDON.getSetting('ukturk.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+ukturk+'%'])
            con.commit()
        if ADDON.getSetting('sanctuary.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+sanctuary+'%'])
            con.commit()
        if ADDON.getSetting('FTV.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+FTV+'%'])
            con.commit()
        if ADDON.getSetting('uktvnow.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+uktvnow+'%'])
            con.commit()
        if ADDON.getSetting('cluiptv.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+cluiptv+'%'])
            con.commit()
        if ADDON.getSetting('suicide.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+suicide+'%'])
            con.commit()
        if ADDON.getSetting('projectcypher.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+projectcypher+'%'])
            con.commit()
        if ADDON.getSetting('notfilmon.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+notfilmon+'%'])
            con.commit()
        if ADDON.getSetting('israelive.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+israelive+'%'])
            con.commit()
        if ADDON.getSetting('adriansports.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+adriansports+'%'])
            con.commit()
        if ADDON.getSetting('evolve.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%'+typeName+'%', '%'+evolve+'%'])
            con.commit()
        if ADDON.getSetting('allfreeaddons.enabled') == 'true':
            cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND (chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ?)",['%'+typeName+'%', '%'+ukturk+'%','%'+sanctuary+'%', '%'+FTV+'%', '%'+uktvnow+'%', '%'+cluiptv+'%', '%'+suicide+'%', '%'+projectcypher+'%', '%'+notfilmon+'%', '%'+israelive+'%', '%'+adriansports+'%', '%'+evolve+'%'])
            con.commit()
        ADDON.setSetting('last.category', typeName)
        cur.execute("SELECT id FROM channels WHERE visible = '1' LIMIT 1;")
        if not cur.fetchone():
            cur.execute("UPDATE channels SET visible = 0")
            if ADDON.getSetting('dexter.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+dex+'%'])
                con.commit()
            if ADDON.getSetting('reloaded.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+reloaded+'%'])
                con.commit()
            if ADDON.getSetting('OTTTV.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+OTTTV+'%'])
                con.commit()
            if ADDON.getSetting('suicide21.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+suicide21+'%'])
                con.commit()
            if ADDON.getSetting('freeview.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+freeview+'%'])
                con.commit()
            if ADDON.getSetting('aftermathtv.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+aftermathtv+'%'])
                con.commit()
            if ADDON.getSetting('ukturk.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+ukturk+'%'])
                con.commit()
            if ADDON.getSetting('sanctuary.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+sanctuary+'%'])
                con.commit()
            if ADDON.getSetting('FTV.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+FTV+'%'])
                con.commit()
            if ADDON.getSetting('uktvnow.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+uktvnow+'%'])
                con.commit()
            if ADDON.getSetting('cluiptv.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+cluiptv+'%'])
                con.commit()
            if ADDON.getSetting('suicide.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+suicide+'%'])
                con.commit()
            if ADDON.getSetting('projectcypher.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+projectcypher+'%'])
                con.commit()
            if ADDON.getSetting('notfilmon.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+notfilmon+'%'])
                con.commit()
            if ADDON.getSetting('israelive.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+israelive+'%'])
                con.commit()
            if ADDON.getSetting('adriansports.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+adriansports+'%'])
                con.commit()
            if ADDON.getSetting('evolve.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND chnaddon LIKE ?",['%All Channels%', '%'+evolve+'%'])
                con.commit()
            if ADDON.getSetting('allfreeaddons.enabled') == 'true':
                cur.execute("UPDATE channels SET visible = 1 WHERE chncategory LIKE ? AND (chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon LIKE ? OR chnaddon like ? OR chnaddon like ? OR chnaddon like ?)",['%All Channels%', '%'+ukturk+'%', '%'+sanctuary+'%','%'+FTV+'%', '%'+uktvnow+'%', '%'+cluiptv+'%', '%'+suicide+'%', '%'+projectcypher+'%', '%'+notfilmon+'%', '%'+israelive+'%', '%'+adriansports+'%', '%'+evolve+'%', '%'+freeview+'%'])
                con.commit()
            xbmcgui.Dialog().ok("Error!", "Enabled addons have no channels under this category..", "", "Defaulting back to All Channels!")
            ADDON.setSetting('last.category', "All Channels")
        
    except lite.Error, e:
            
        print "Error %s:" % e.args[0]
        sys.exit(1)
            
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    guideList = []
    gTypes = GuideTypes()
    for gType in gTypes.guideTypes:
        guideList.append(gType[gTypes.GUIDE_NAME])
    d = xbmcgui.Dialog()
    ret = d.select('Select channel category', guideList)
    if ret >= 0:
        guideId = gTypes.guideTypes[ret][gTypes.GUIDE_ID]
        typeId = str(guideId)
        typeName = gTypes.getGuideDataItem(guideId, gTypes.GUIDE_NAME)
        ver = getKodiVersion()
        if xbmc.getCondVisibility('system.platform.android') and int(ver) < 15:
            # This workaround is needed due to a Bug in the Kodi Android implementation
            # where setSetting() does not have any effect:
            #  #13913 - [android/python] addons can not save settings  [http://trac.kodi.tv/ticket/13913]
            xbmc.log('[plugin.program.reloadedtv] Running on ANDROID with Kodi v%s --> using workaround!' % str(ver), xbmc.LOGDEBUG)
            filePath = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'plugin.program.reloadedtv', 'settings.xml'))
            tree = ET.parse(filePath)
            root = tree.getroot()
            updated = False
            for item in root.findall('setting'):
                if item.attrib['id'] == '6':
                    if item.attrib['id'] == 'xmltv.type':
                        item.attrib['value'] = typeId
                        updated = True
                    elif item.attrib['id'] == 'xmltv.type_select':
                        item.attrib['value'] = typeName
                        updated = True
            if updated:
                tree.write(filePath)
                ADDON.openSettings()
        else:  # standard settings handling...
            if typeId == '6':
                ADDON.setSetting('xmltv.type', typeId)
                ADDON.setSetting('xmltv.type_select', typeName)
            else:
                pass
                #updatecategories(typeName)

            # Custom
            #xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
            #xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
            import gui
            w = gui.TVGuide()
            w.doModal()
            xbmc.sleep(350)
            del w       