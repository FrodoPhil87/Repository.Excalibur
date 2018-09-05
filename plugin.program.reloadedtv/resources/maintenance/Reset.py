import time
import os
import xbmc
import xbmcgui
import xbmcaddon

databasePath = xbmc.translatePath('special://userdata/addon_data/plugin.program.reloadedtv')
d = xbmcgui.Dialog()
deletesuccess = False

for root, dirs, files in os.walk(databasePath,topdown=True):
	dirs[:] = [d for d in dirs]
	for name in files:
		if "guide.cfg" in name:
			try:
				os.remove(os.path.join(root,name))
				deletesuccess = True
			except: 
				d = xbmcgui.Dialog()
				d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Error Removing ' + str(name),'Please restart device!','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')
				pass
		else:
			continue
			
#for root, dirs, files in os.walk(databasePath,topdown=True):
#	dirs[:] = [d for d in dirs]
#	for name in files:
#		if "source.db" in name:
#			try:
#				os.remove(os.path.join(root,name))
#				deletesuccess = True
#			except: 
#				d = xbmcgui.Dialog()
#				d.ok('TV Guide', 'Error Removing ' + str(name),'Please restart device!','[COLOR yellow]Thank you for using M-TV Guide[/COLOR]')
#				pass
#		else:
#			continue
			
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

if deletesuccess == True:
	d = xbmcgui.Dialog()			
	d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Reset successfully performed.','','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')
else:
	d = xbmcgui.Dialog()
	d.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Error! file(s) not found.. Try loading guide to download data!','','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')
