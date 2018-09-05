import urllib2
import xbmc
import xbmcgui
import sys
import json
import xbmcaddon
import base64
import urllib
import requests

ADDON = xbmcaddon.Addon(id='plugin.program.reloadedtv')
dialog      = xbmcgui.Dialog()
UA          = base64.b64decode('VXNlci1BZ2VudC1NYXlmYWlyUFJP') + "Reloaded TV"

def DansGame(KappaPride):
	gachiGASM = base64.b64decode(KappaPride)
	return gachiGASM

def show_busy_dialog():
		xbmc.executebuiltin('ActivateWindow(10138)')

def hide_busy_dialog():
	xbmc.executebuiltin('Dialog.Close(10138)')
	while xbmc.getCondVisibility('Window.IsActive(10138)'):
		xbmc.sleep(100)

def get_reloaded():
	try:
		u = DansGame("aHR0cDovL21heWZhaXJndWlkZXMuY29tL2d1aWRlL3JlbG9hZGVkLnR4dA==")
		uu = requests.get(u, headers={'User-Agent': (UA)}).content
		return uu
	except:
		dialog = xbmcgui.Dialog()
		dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", DansGame("RXJyb3IhIENvdWxkIG5vdCBjb25uZWN0IHRvIHNlcnZlciBbMV0="),"", DansGame("UGxlYXNlIHRyeSBhZ2FpbiBsYXRlci4="))
		sys.exit(1)

def get_reloaded_account_info():
	try:
		show_busy_dialog()
		req = urllib2.Request(get_reloaded()+DansGame("L3BhbmVsX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXM=")%(urllib.quote_plus(ADDON.getSetting(DansGame("cmVsb2FkZWQudXNlcg=="))),urllib.quote_plus(ADDON.getSetting(DansGame("cmVsb2FkZWQucGFzcw==")))))
		req.add_header(DansGame("VXNlci1BZ2VudA==") , DansGame("TWF5ZmFpckd1aWRlLVVzZXJBZ2VudA=="))
		response = urllib2.urlopen(req)
		link=response.read()
		jdata = json.loads(link.decode('utf8'))
		response.close()
		hide_busy_dialog()
		return jdata
	except:
		hide_busy_dialog()
		dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]",DansGame("RXJyb3IhIENvdWxkIG5vdCBjb25uZWN0Li4="),DansGame("SXMg")+"Reloaded TV"+DansGame("IGRvd24/"),"")
		sys.exit(1)

if ADDON.getSetting(DansGame("cmVsb2FkZWQudXNlcg==")) == '' or ADDON.getSetting(DansGame("cmVsb2FkZWQucGFzcw==")) == '':
	dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", DansGame("RXJyb3IhIE5vIA==")+"Reloaded TV"+DansGame("IFVzZXJuYW1lIG9yIHBhc3N3b3JkIQ=="), DansGame("UGxlYXNlIGVudGVyIHlvdXIgdXNlcm5hbWUgYW5kIHBhc3N3b3JkLg=="), "")
	xbmc.executebuiltin('Dialog.Close(10140)')
	lklklklklk = dialog.input(DansGame('RW50ZXIg')+"Reloaded TV"+DansGame('IFVzZXJuYW1l'), type=xbmcgui.INPUT_ALPHANUM)
	lklkllklklk = dialog.input(DansGame('RW50ZXIg')+"Reloaded TV"+DansGame("IFBhc3N3b3Jk"), type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
	ADDON.setSetting(DansGame('cmVsb2FkZWQudXNlcg=='), lklklklklk)
	ADDON.setSetting(DansGame('cmVsb2FkZWQucGFzcw=='), lklkllklklk)
	xbmc.sleep(100)
	ADDON.openSettings()
	sys.exit(1)
#if ADDON.getSetting(DansGame("cmVsb2FkZWQucGFzcw==")) == '':
#	dialog.ok("M-TV Guide", DansGame("RXJyb3IhIE5vIA==")+"Reloaded TV"+DansGame("IFBhc3N3b3JkIQ=="), DansGame("UGxlYXNlIGVudGVyIHlvdXIgcGFzc3dvcmQu"), "")
#	xbmc.executebuiltin('Dialog.Close(10140)')
#	lklkllklklk = dialog.input(DansGame('RW50ZXIg')+"Reloaded TV"+DansGame("IFBhc3N3b3Jk"), type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
#	ADDON.setSetting(DansGame('cmVsb2FkZWQucGFzcw=='), lklkllklklk)
#	xbmc.sleep(100)
#	ADDON.openSettings()
#	sys.exit(1)

getdata = get_reloaded_account_info()
MingLee = getdata[base64.b64decode("dXNlcl9pbmZv")]
Kappa = MingLee[base64.b64decode("YXV0aA==")]
if Kappa == 1:
	TriHard = MingLee[base64.b64decode("c3RhdHVz")]
	KreyGasm = MingLee[base64.b64decode("bWF4X2Nvbm5lY3Rpb25z")]
	sneakyGasm = MingLee[base64.b64decode("dXNlcm5hbWU=")]
	if TriHard == DansGame('QWN0aXZl'):
		dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", DansGame("VXNlcjog")+sneakyGasm, DansGame("QWNjb3VudCBTdGF0dXM6IA==")+DansGame("W0NPTE9SIGxpbWVd")+TriHard+DansGame("Wy9DT0xPUl0="), DansGame("TWF4IENvbm5lY3Rpb25zOiA=")+KreyGasm)
	else:
		dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", DansGame("VXNlcjog")+sneakyGasm, DansGame("QWNjb3VudCBTdGF0dXM6IA==")+DansGame("W0NPTE9SIHJlZF0=")+TriHard+DansGame("Wy9DT0xPUl0="), DansGame("TWF4IENvbm5lY3Rpb25zOiA=")+KreyGasm)
	sys.exit(1)

if Kappa == 0:
	dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", DansGame("RXJyb3IhIA==")+"Reloaded TV"+DansGame("IEFjY291bnQgbm90IGZvdW5kIQ=="), DansGame("UGxlYXNlIGNoZWNrIHlvdXIgdXNlcm5hbWUgb3IgcGFzc3dvcmQu"), "")
	xbmc.executebuiltin('Dialog.Close(10140)')
	lklklklk = dialog.input(DansGame('RW50ZXIg')+"Reloaded TV"+DansGame("IFVzZXJuYW1l"), type=xbmcgui.INPUT_ALPHANUM)
	lklklkl = dialog.input(DansGame('RW50ZXIg')+"Reloaded TV"+DansGame("IFBhc3N3b3Jk"), type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
	ADDON.setSetting(DansGame('cmVsb2FkZWQudXNlcg=='), lklklklk)
	ADDON.setSetting(DansGame('cmVsb2FkZWQucGFzcw=='), lklklkl)
	xbmc.sleep(100)
	ADDON.openSettings()
	sys.exit(1)