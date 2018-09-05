# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Sean Poyser and Richard Dean (write2dixie@gmail.com)
#
#      Modified for FTV Guide (09/2014 onwards)
#      by Thomas Geppert [bluezed] - bluezed.apps@gmail.com
#
# This Program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This Program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with XBMC; see the file COPYING. If not, write to
# the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# http://www.gnu.org/copyleft/gpl.html
#

import time
import os
import xbmc
import xbmcgui
import xbmcaddon
import shutil



addon = 'plugin.program.reloadedtv';addon_name = addon;icon = xbmc.translatePath(os.path.join('special://home/addons', addon, 'icon.png'))
addonPath = xbmc.translatePath(os.path.join('special://home', 'addons', addon))
basePath = xbmc.translatePath(os.path.join('special://profile', 'addon_data', addon))
dbPath = xbmc.translatePath(xbmcaddon.Addon(addon).getAddonInfo('profile'))
dialog = xbmcgui.Dialog();dp = xbmcgui.DialogProgress()


mode='run_maintenance_delete_files'




def maintenance_delete_files():
        #######################################
        # Delete core Guide files
        #######################################

        choice = dialog.select('Perform general maintenance', ['Close',
                                                               'Delete Database (Linked Channels and EPG data)',
                                                               'Delete Linked addons file',                                                               
                                                               'Delete Category file',
                                                               'Delete Guide XML (EPG data file)',
                                                               'Delete Thumbnails',
                                                               'Delete textures (Database Textures13.db)'])
        if choice == 0:  sys.exit(0)
        #
        # Delete main database.db (Linked Channels)
        if choice == 1:
            deleteDB()                   
            #sys.exit()
        #
        
        # Delete ini files
        if choice == 2:
            deleteINI()
            sys.exit()
            
            
        # Delete guide.ini
        if choice == 3:
            deleteCFG()
            sys.exit()            
 

        # Delete Guide xmls
        if choice == 4:
            deleteXML()
            sys.exit()  

      
        #
        # Delete Thumbnails
        if choice == 5:
            path = xbmc.translatePath(os.path.join('special://home/userdata', 'Thumbnails'))
            dp.create(path,"Deleting...",path, 'Please Wait')
            if os.path.exists(path)==True:  
                for root, dirs, files in os.walk(path):
                    file_count = 0
                    file_count += len(files)
                    if file_count > 0:                
                        for f in files:
                            try:
                                os.unlink(os.path.join(root, f))
                            except:
                                pass
                xbmc.executebuiltin('Notification(%s, %s, %s)'%("SUCCESS! Thumbnails deleted.","", icon))
            else:
                xbmc.executebuiltin('Notification(%s, %s, %s)'%("ERROR! Failed to delete Thumbnails.","", icon))
            sys.exit()
        #
        # Delete textures (Database Textures13.db)
        if choice == 6:
            textures = xbmc.translatePath(os.path.join('special://home/userdata/Database', 'Textures13.db'))
            try:
                dbcon = database.connect(textures)
                dbcur = dbcon.cursor()
                dbcur.execute("DROP TABLE IF EXISTS path")
                dbcur.execute("VACUUM")
                dbcon.commit()
                dbcur.execute("DROP TABLE IF EXISTS sizes")
                dbcur.execute("VACUUM")
                dbcon.commit()
                dbcur.execute("DROP TABLE IF EXISTS texture")
                dbcur.execute("VACUUM")
                dbcon.commit()
                dbcur.execute("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""")
                dbcon.commit()
                dbcur.execute("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""")
                dbcon.commit()
                dbcur.execute("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""")
                dbcon.commit()
                xbmc.executebuiltin('Notification(%s, %s, %s)'%("SUCCESS! Textures deleted.","", icon))
            except:
                xbmc.executebuiltin('Notification(%s, %s, %s)'%("ERROR! Failed to delete Textures.","", icon))
            sys.exit()
        #






# Delete Guide xmls
def deleteXML():
    try:
        dbPath1 = xbmc.translatePath(xbmcaddon.Addon(id = 'plugin.program.reloadedtv').getAddonInfo('profile'))
        dbPath1 = os.path.join(dbPath1, 'guide.xml')
        dbPath2 = xbmc.translatePath(xbmcaddon.Addon(id = 'plugin.program.reloadedtv').getAddonInfo('profile'))
        dbPath2 = os.path.join(dbPath2, 'guide.zip')
        delete_file(dbPath1)
        delete_file(dbPath2)
        passed = not os.path.exists(dbPath1) and not os.path.exists(dbPath2)
        if passed:
            xbmc.executebuiltin('Notification(%s, %s, %s)'%("SUCCESS! Guide XML deleted.","", icon))
            xbmc.log("[plugin.program.reloadedtv] Deleting guide.xml...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.executebuiltin('Notification(%s, %s, %s)'%("ERROR! Failed to delete Guide XML.","", icon))
            xbmc.log("[plugin.program.reloadedtv] Deleting guide.xml...FAILED", xbmc.LOGDEBUG)
        return passed
    except Exception, e:
        xbmc.executebuiltin('Notification(%s, %s, %s)'%("EXCEPTION ERROR! Failed to delete Guide XML.","", icon))
        xbmc.log('[plugin.program.reloadedtv] Deleting guide.xml...EXCEPTION', xbmc.LOGDEBUG)
        return False





# Delete guide.cfg
def deleteCFG():
    try:
        xbmc.log("[plugin.program.reloadedtv] Deleting guide.cfg", xbmc.LOGDEBUG)
        dbPath = xbmc.translatePath(xbmcaddon.Addon(id = 'plugin.program.reloadedtv').getAddonInfo('profile'))
        dbPath = os.path.join(dbPath, 'guide.cfg')

        delete_file(dbPath)

        passed = not os.path.exists(dbPath)

        if passed:
            xbmc.executebuiltin('Notification(%s, %s, %s)'%("SUCCESS! guide.cfg deleted.","", icon))
            xbmc.log("[plugin.program.reloadedtv] Deleting guide.cfg...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.executebuiltin('Notification(%s, %s, %s)'%("ERROR! Failed to delete guide.cfg","", icon))
            xbmc.log("[plugin.program.reloadedtv] Deleting guide.cfg...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.executebuiltin('Notification(%s, %s, %s)'%("ERROR! Failed to delete guide.cfg","", icon))
        xbmc.log('[plugin.program.reloadedtv] Deleting Guide listing Choices...EXCEPTION', xbmc.LOGDEBUG)
        return False




# delete ini files
def deleteINI():
    try:
        xbmc.log("[plugin.program.reloadedtv] Deleting linked addons ini...", xbmc.LOGDEBUG)
        dbPath1 = xbmc.translatePath(xbmcaddon.Addon(id = 'plugin.program.reloadedtv').getAddonInfo('profile'))
        dbPath1 = os.path.join(dbPath1, 'addons.ini')
        delete_file(dbPath1)
        passed = not os.path.exists(dbPath1)
        if passed:
            xbmc.executebuiltin('Notification(%s, %s, %s)'%("SUCCESS! Linked addons file deleted.","", icon))
            xbmc.log("[plugin.program.reloadedtv] Deleting linked addons ini...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.executebuiltin('Notification(%s, %s, %s)'%("ERROR! Failed to delete linked addons file.","", icon))
            xbmc.log("[plugin.program.reloadedtv] Deleting linked addons ini...FAILED", xbmc.LOGDEBUG)
        return passed
    except Exception, e:
        xbmc.executebuiltin('Notification(%s, %s, %s)'%("ERROR! Failed to delete linked addons file.","", icon))
        xbmc.log('[plugin.program.reloadedtv] Deleting linked addons ini...EXCEPTION', xbmc.LOGDEBUG)
        return False



# Linked channels
def deleteDB():
    try:
        xbmc.log("[plugin.program.reloadedtv] Deleting database...", xbmc.LOGDEBUG)
        dbPath = xbmc.translatePath(xbmcaddon.Addon(id = 'plugin.program.reloadedtv').getAddonInfo('profile'))
        dbPath = os.path.join(dbPath, 'source.db')
        delete_file(dbPath)
        passed = not os.path.exists(dbPath)
        if passed:
            xbmc.executebuiltin('Notification(%s, %s, %s)'%("SUCCESS! Database deleted.","", icon))
            xbmc.log("[plugin.program.reloadedtv] Deleting database...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.executebuiltin('Notification(%s, %s, %s)'%("ERROR! Failed to delete Database.","", icon))
            xbmc.log("[plugin.program.reloadedtv] Deleting database...FAILED", xbmc.LOGDEBUG)
        return passed
    except Exception, e:
        xbmc.executebuiltin('Notification(%s, %s, %s)'%("ERROR! Failed to delete Database.","", icon))
        xbmc.log('[plugin.program.reloadedtv] Deleting database...EXCEPTION', xbmc.LOGDEBUG)
        return False
#
def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            break
        except:
            tries -= 1



if __name__ == '__main__':
    if maintenance_delete_files():
        maintenance_delete_files()

#if mode=='run_maintenance_delete_files' : maintenance_delete_files()
