import os
import xbmc
import xbmcgui
import xbmcaddon
import sqlite3

ADDON = xbmcaddon.Addon(id='plugin.program.reloadedtv')
profilePath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
SOURCE_DB = 'source.db'
databasePath = os.path.join(profilePath, SOURCE_DB)
removesuccess = False
dialog = xbmcgui.Dialog()

try:
	ret = dialog.yesno('[COLOR red]Reloaded TV Guide[/COLOR]','Are you sure you want to remove all saved stream selections for every channel?','','','No','Yes')
	if ret:
		conn = sqlite3.connect(databasePath, timeout = 10, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
		with conn:
			cur = conn.cursor()
			cur.execute('DELETE FROM custom_stream_url')
			removesuccess = True
	if not ret:
		removesuccess = False
except:
	dialog.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'Error removing all saved stream selections!','Please restart device!','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')

if removesuccess == True:
	dialog.ok('[COLOR red]Reloaded TV Guide[/COLOR]', 'All saved stream selections have been removed successfully!','','Thank you for using [COLOR red]Reloaded TV Guide[/COLOR]')