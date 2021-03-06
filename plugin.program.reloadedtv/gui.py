# -*- coding: utf-8 -*-
#      Copyright (C) 2014 Tommy Winther
#      http://tommy.winther.nu
#
#      Modified for FTV Guide (09/2014 onwards)
#      by Thomas Geppert [bluezed] - bluezed.apps@gmail.com
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
import datetime
import threading
import time
import xbmc
import xbmcgui
import source as src
from notification import Notification
from strings import *
import os
import sys
import add
import json
import urllib2
import base64
import urllib
import xbmcaddon
import hashlib
import fileFetcher
import pickle
import requests
import kappa
from TriHard import lel
from TriHard import hm
from TriHard import okok
import inspect
import re
import guideTypes
import lolol

import streaming

DEBUG = False

MODE_EPG = 'EPG'
MODE_TV = 'TV'
MODE_OSD = 'OSD'

ACTION_LEFT = 1
ACTION_RIGHT = 2
ACTION_UP = 3
ACTION_DOWN = 4
ACTION_PAGE_UP = 5
ACTION_PAGE_DOWN = 6
ACTION_SELECT_ITEM = 7
ACTION_PARENT_DIR = 9
ACTION_PREVIOUS_MENU = 10
ACTION_SHOW_INFO = 11
ACTION_NEXT_ITEM = 14
ACTION_PREV_ITEM = 15

ACTION_MOUSE_WHEEL_UP = 104
ACTION_MOUSE_WHEEL_DOWN = 105
ACTION_MOUSE_MOVE = 107

KEY_NAV_BACK = 92
KEY_CONTEXT_MENU = 117
KEY_HOME = 159
KEY_ESC = 61467
KEY_ZERO = 58

CHANNELS_PER_PAGE = 8

HALF_HOUR = datetime.timedelta(minutes=30)

SAVESTREAM = ADDON.getSetting('save.stream') == 'true'

#for extras players
ADDONID     = 'plugin.program.reloadedtv'
ADDON       =  xbmcaddon.Addon(ADDONID)
HOME        =  ADDON.getAddonInfo('path')
ICON        =  os.path.join(HOME, 'icon.png')
ICON        =  xbmc.translatePath(ICON)
PROFILE     =  xbmc.translatePath(ADDON.getAddonInfo('profile'))
RESOURCES   =  os.path.join(HOME, 'resources')
SKIN        =  ADDON.getSetting('skin')

#SKINdir     =  os.path.join(HOME)# skin in resources
SKINdir     =  os.path.join(PROFILE)# skin in user settings folder
usrsetting  = os.path.join(PROFILE)
LOGOdir     = xbmc.translatePath(os.path.join(usrsetting, 'resources', 'logos'))
addonini    = xbmc.translatePath(os.path.join(usrsetting, 'addons.ini'))
cookiefile = xbmc.translatePath(os.path.join(usrsetting, 'cookie'))
maycustom = ADDON.getSetting('skincustomization.enabled') == 'true'
maywpfile = ''
UA        = base64.b64decode('VXNlci1BZ2VudC1NYXlmYWlyUFJP') + "Reloaded TV"

####################################################
# download skin first run
####################################################
#if not os.path.exists(xbmc.translatePath(os.path.join(SKINdir, 'resources', 'skins', 'Default'))):
#	add.skinDL()
#	ADDON.setSetting('skin', 'Default')
#	SKIN =  ADDON.getSetting('skin')
if not os.path.exists(xbmc.translatePath(os.path.join(SKINdir, 'resources', 'skins', ADDON.getSetting('skin')))):
	ADDON.setSetting('skin', 'Default')
	xbmcgui.Dialog().notification('Skins', 'Skin not found! Using Default Skin!', icon=os.path.join('special://home/addons', ADDONID, 'icon.png'), time=2000, sound=True)
SKINDL = add.skinDL()
#if SKINDL == 'Change':
#	ADDON.setSetting('skin', 'Default')
SKIN =  ADDON.getSetting('skin')
if ADDON.getSetting('skin.custom.wallpaper') != '' and maycustom:
	maysuccess, maywpfile = hm(None).cw(ADDON.getSetting('skin.custom.wallpaper'))
	if SKIN != 'Default':
		ADDON.setSetting('skin', 'Default')
		SKIN =  ADDON.getSetting('skin')
		xbmcgui.Dialog().notification('Skins', 'Using Default Skin for customization!', icon=os.path.join('special://home/addons', ADDONID, 'icon.png'), time=2000, sound=True)
for p, d, f in os.walk(xbmc.translatePath(os.path.join(SKINdir, 'resources', 'skins', 'Default')), topdown=False):
	if p == xbmc.translatePath(os.path.join(SKINdir, 'resources', 'skins', 'Default')):
		for name in f:
			if 'ver.txt' in name:
				continue
			if maywpfile != '' and maywpfile in name:
				continue
			else:
				os.remove(os.path.join(p, name))

# for unicode utf asci  maybe not needed
#reload(sys)
#sys.setdefaultencoding("utf-8")




# Below here needed for player
#
'''
def getLivemixChannels():
	import requests
	import re
	DecodeLivemixHex   =  getINIhex('https://app.uktvnow.net/v1/get_all_channels','goat')       
	headers =  {'User-Agent':'USER-AGENT-UKTVNOW-APP-V1', 
				'User-Agent':'application/x-www-form-urlencoded; charset=UTF-8',
				'gzip':'Accept-Encoding',
				'app-token':DecodeLivemixHex,
				'Keep-Alive':'Connection',                
				'app.uktvnow.net':'Host'}
	LMData = {'username':'goat'}
	requestthelivemixchannels = requests.post('https://app.uktvnow.net/v1/get_all_channels', data=LMData, headers=headers)   
	requestLMcontent =  requestthelivemixchannels.content
	requestLMcontent =  requestLMcontent.replace('\/','/')    
	decryptitems = '"channel_name":"(.+?)","img":"(.+?)","http_stream":"(.+?)","rtmp_stream":"(.+?)","cat_id":"(.+?)"'   
	items    = re.compile(decryptitems).findall(requestLMcontent)
	LMItems = []
	for item in items:
		link = {'label': item[0], 'url': item[2]}
		LMItems.append(link)
	return LMItems
#
def getINIhex(url, uktvnowUser):
	import base64
	import hashlib
	thetime   =  FigureOutTheTime()
	st   = "uktvnow-token-" + thetime + "-" + "_|_-" + url + "-" + uktvnowUser + "-" + "_|_" + "-" + base64.b64decode("MTIzNDU2IUAjJCVedWt0dm5vd14lJCNAITY1NDMyMQ==")
	return hashlib.md5(st).hexdigest()
#
def FigureOutTheTime():
	from datetime import datetime, timedelta
	rightnowtime = datetime.now() + timedelta(hours=5)
	return rightnowtime.strftime('%B-%d-%Y')
#
# Only needed for playing - used in gui.py #   
#def getLIVETV(url):
def playlivemix(url):
	TrytogetChannels = getLivemixChannels()
	stream   = url.split(':', 1)[-1].lower()
	for tempchan in TrytogetChannels:
		LivemixChanIDs = tempchan['label']
		url   = tempchan['url']
		if stream == LivemixChanIDs.lower():
			return url
	return None
#
'''







def debug(s):
	if DEBUG: xbmc.log(str(s), xbmc.LOGDEBUG)

class Point(object):
	def __init__(self):
		self.x = self.y = 0

	def __repr__(self):
		return 'Point(x=%d, y=%d)' % (self.x, self.y)


class EPGView(object):
	def __init__(self):
		self.top = self.left = self.right = self.bottom = self.width = self.cellHeight = 0


class ControlAndProgram(object):
	def __init__(self, control, program):
		self.control = control
		self.program = program


class TVGuide(xbmcgui.WindowXML):
	C_MAIN_DATE_LONG = 3999
	C_MAIN_DATE = 4000
	C_MAIN_TITLE = 4020
	C_MAIN_TIME = 4021
	C_MAIN_DESCRIPTION = 4022
	C_MAIN_IMAGE = 4023
	C_MAIN_LOGO = 4024
	C_MAIN_TIMEBAR = 4100
	C_MAIN_LOADING = 4200
	C_MAIN_LOADING_PROGRESS = 4201
	C_MAIN_LOADING_TIME_LEFT = 4202
	C_MAIN_LOADING_CANCEL = 4203
	C_MAIN_MOUSE_CONTROLS = 4300
	C_MAIN_MOUSE_HOME = 4301
	C_MAIN_MOUSE_LEFT = 4302
	C_MAIN_MOUSE_UP = 4303
	C_MAIN_MOUSE_DOWN = 4304
	C_MAIN_MOUSE_RIGHT = 4305
	C_MAIN_MOUSE_EXIT = 4306
	C_MAIN_BACKGROUND = 4600
	C_MAIN_EPG = 5000
	C_MAIN_EPG_VIEW_MARKER = 5001
	C_MAIN_OSD = 6000
	C_MAIN_OSD_TITLE = 6001
	C_MAIN_OSD_TIME = 6002
	C_MAIN_OSD_DESCRIPTION = 6003
	C_MAIN_OSD_CHANNEL_LOGO = 6004
	C_MAIN_OSD_CHANNEL_TITLE = 6005
	C_MAIN_OSD_CHANNEL_NUMBER = 6009
	C_MAIN_CPUINFO = 9889
	C_MAIN_MEMINFO = 9890
	C_MAIN_SETTING = 30450
	C_MAIN_CAT     = 8898
	C_MAIN_VERSION = 8899

		
	def __new__(cls):
		# Skin in resources
		#return super(TVGuide, cls).__new__(cls, 'script-tvguide-main.xml', ADDON.getAddonInfo('path'), SKIN)
		# Skin in user settings
		try:
			return super(TVGuide, cls).__new__(cls, 'script-tvguide-main.xml', SKINdir, SKIN)
		except:
			mayq = okok(None)
			if not mayq.loggedin:
				mayq.logout()
				sys.exit(1)
			mayq.logout()
			dialog = xbmcgui.Dialog()
			dialog.ok('[COLOR red]Reloaded TV Guide[/COLOR]','[COLOR red]Error with skin![/COLOR]','Something went wrong with loading your active skin..','Please go into settings and change your active skin!')
			ADDON.openSettings()

		
	def __init__(self):

		super(TVGuide, self).__init__()
		self.notification = None
		self.redrawingEPG = False
		self.isClosing = False
		self.init = False
		self.PlayBackStopped = False
		self.channelswitch = False
		self.previouschannel = None
		self.windowID = None
		#self.q = lolol.loll()
		self.controlAndProgramList = list()
		self.ignoreMissingControlIds = list()
		self.channelIdx = 0
		self.focusPoint = Point()
		self.epgView = EPGView()
		self.streamingService = streaming.StreamsService(ADDON)
		#self.player = xbmc.Player()
		self.player = self.CustomPlayer()
		self.database = None

		self.mode = MODE_EPG
		self.currentChannel = None

		self.osdEnabled = ADDON.getSetting('enable.osd') == 'true' and ADDON.getSetting(
			'alternative.playback') != 'true'
		self.osdShownumbers = ADDON.getSetting('osd.shownumbers') == 'true'
		self.osdShowlogos = ADDON.getSetting('osd.showlogos') == 'true'
		self.shownumbers = ADDON.getSetting('shownumbers') == 'true'
		self.showcat = ADDON.getSetting('showcat') == 'true'
		self.chnexit = ADDON.getSetting('chnexit') == 'true'
		self.showDebugInfo = ADDON.getSetting('debuginfo.enabled') == 'true'
		self.alternativePlayback = ADDON.getSetting('alternative.playback') == 'true'
		self.lolololol = self.get_reloaded()
		self.mayfaircustomwp = ADDON.getSetting('skin.custom.wallpaper') != '' and maycustom and maysuccess
		self.tvlistingprogramfocuscolor    = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('tvlisting.program.focus.color')).group(1)
		self.tvlistingprogramnonfocuscolor = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('tvlisting.program.nonfocus.color')).group(1)
		self.channelnamecolor              = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('channel.name.color')).group(1)
		self.channelnumbercolor            = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('channel.number.color')).group(1)
		self.guidedatecolor                = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('guide.date.color')).group(1)
		self.systemdatecolor               = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('system.date.color')).group(1)
		self.guidetimecolor                = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('guide.time.color')).group(1)
		self.catcolor                      = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('cat.color')).group(1)
		self.programdesccolor              = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('program.desc.color')).group(1)
		self.programstartendtimecolor      = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('program.start.end.color')).group(1)
		self.programtitlecolor             = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('program.title.color')).group(1)
		self.versioncolor                  = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('addon.version.color')).group(1)
		self.largetvlistingfont            = ADDON.getSetting('largetvlistingfont.enabled') == 'true'
		self.osdChannel = None
		self.osdProgram = None
		self.reloadedEnabled = ADDON.getSetting('reloaded.enabled')
		self.Kappa = None
		self.TriHard = None
		self.addonupdated = False
		self.dexAddon = 'plugin.video.dex'
		self.reloadedAddon = 'plugin.video.reloadedtv'
		self.aftermathtvAddon = 'plugin.video.aftermathtv'
		self.ukturkAddon = 'plugin.video.ukturk'
		self.sanctuaryAddon = 'plugin.video.sanctuary'
		self.OTTTVAddon     = 'plugin.video.ottalpha'
		self.suicide21Addon      = 'plugin.video.suicidetv21'
		self.freeviewAddon       = 'plugin.video.freeview'
		self.FTVAddon = 'plugin.video.F.T.V'
		self.uktvnowAddon = 'plugin.video.uktvnow'
		self.cluiptvAddon = 'plugin.video.cluiptv'
		self.suicideAddon = 'plugin.video.suicidetv'
		self.projectcypherAddon = 'plugin.video.ProjectCypher'
		self.notfilmonAddon = 'plugin.video.notfilmon'
		self.israeliveAddon = 'plugin.video.israelive'
		self.adriansportsAddon = 'plugin.video.adriansports'
		self.evolveAddon = 'plugin.video.Evolve'
		global instance
		instance = self
		self.kek = lel(instance)
		self.kekk = hm(instance)
		self.q = okok(instance)
		self.channelinput = False
		self.doneacclu = False

		# find nearest half hour
		self.viewStartDate = datetime.datetime.today()
		self.viewStartDate -= datetime.timedelta(minutes=self.viewStartDate.minute % 30,
												 seconds=self.viewStartDate.second)

		if not ADDON.getSetting('xmltv.interval') == '2':
			ADDON.setSetting('xmltv.interval', '2')
		if not ADDON.getSetting('cluiptv.enabled') == 'false':
			ADDON.setSetting('cluiptv.enabled', 'false')
		if self.q.isrs:
			ADDON.setSetting('acclu', 'false')

		if not self.q.loggedin:
			self.fc()
		self.q.donotice()
		if not os.path.exists(LOGOdir):
			add.logoDL()
			ADDON.setSetting('logos.folder', LOGOdir)
		if not os.path.exists(xbmc.translatePath(os.path.join(ADDON.getSetting('logos.folder')))):
			add.logoDL()
			ADDON.setSetting('logos.folder', LOGOdir)

		if ADDON.getSetting('systemsettingcheck') == 'false':
			if xbmc.getCondVisibility('system.platform.android'):
				systemsettingschanged = self.kekk.systemvideosettings()
				if systemsettingschanged:
					self.fc()

		if ADDON.getSetting('save.stream') == 'unset':
			dialog = xbmcgui.Dialog()
			ret = dialog.yesno('[COLOR red]Reloaded TV Guide[/COLOR]',self.DansGame('W0NPTE9SIHJlZF1bQl1GZWF0dXJlIG5vdCBjb25maWd1cmVkOiBbL0JdWy9DT0xPUl1TYXZlIHN0cmVhbSBzZWxlY3Rpb24='),self.DansGame('RG8geW91IHdpc2ggdG8gYXV0b21hdGljYWxseSByZW1lbWJlciBhbmQgc2F2ZSB5b3VyIHN0cmVhbSBzZWxlY3Rpb24gZm9yIGVhY2ggY2hhbm5lbCBzbyB5b3UgZG9udCBoYXZlIHRvIGNob29zZSBhZ2Fpbj8='),'','No','Yes')
			if ret:
				ADDON.setSetting('save.stream', "true")
				SAVESTREAM = ADDON.getSetting('save.stream') == 'true'
			if not ret:
				ADDON.setSetting('save.stream', "false")
				SAVESTREAM = ADDON.getSetting('save.stream') == 'true'

		if self.reloadedEnabled == "true":
			if ADDON.getSetting(self.DansGame("cmVsb2FkZWQudXNlcg==")) == '' or ADDON.getSetting(self.DansGame("cmVsb2FkZWQucGFzcw==")) == '':
				dialog = xbmcgui.Dialog()
				dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", self.DansGame("RXJyb3IhIE5vIA==")+"Reloaded TV"+self.DansGame("IFVzZXJuYW1lIG9yIHBhc3N3b3JkIQ=="), self.DansGame("UGxlYXNlIGVudGVyIHlvdXIgdXNlcm5hbWUgYW5kIHBhc3N3b3JkLg=="), "")
				lklklklklk = dialog.input(self.DansGame('RW50ZXIg')+"Reloaded TV"+self.DansGame('IFVzZXJuYW1l'), type=xbmcgui.INPUT_ALPHANUM)
				lklkllklklk = dialog.input(self.DansGame('RW50ZXIg')+"Reloaded TV"+self.DansGame("IFBhc3N3b3Jk"), type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
				ADDON.setSetting(self.DansGame('cmVsb2FkZWQudXNlcg=='), lklklklklk)
				ADDON.setSetting(self.DansGame('cmVsb2FkZWQucGFzcw=='), lklkllklklk)
				self.fc()
			else:
				getdata = self.get_reloaded_account_info()
				MingLee = getdata[base64.b64decode("dXNlcl9pbmZv")]
				self.Kappa = MingLee[base64.b64decode("YXV0aA==")]
				if self.Kappa == 1:
					self.TriHard = MingLee[base64.b64decode("c3RhdHVz")]
				if self.Kappa == 0:
					dialog = xbmcgui.Dialog()
					dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", self.DansGame("RXJyb3IhIA==")+"Reloaded TV"+self.DansGame("IEFjY291bnQgbm90IGZvdW5kIQ=="), self.DansGame("UGxlYXNlIGNoZWNrIHlvdXIgdXNlcm5hbWUgb3IgcGFzc3dvcmQgaW4gZ3VpZGUgc2V0dGluZ3M="), "")
					lklklklk = dialog.input(self.DansGame('RW50ZXIg')+"Reloaded TV"+self.DansGame("IFVzZXJuYW1l"), type=xbmcgui.INPUT_ALPHANUM)
					lklklkl = dialog.input(self.DansGame('RW50ZXIg')+"Reloaded TV"+self.DansGame("IFBhc3N3b3Jk"), type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
					ADDON.setSetting(self.DansGame('cmVsb2FkZWQudXNlcg=='), lklklklk)
					ADDON.setSetting(self.DansGame('cmVsb2FkZWQucGFzcw=='), lklklkl)
					self.fc()
				if self.TriHard == self.DansGame("QmFubmVk"):
					dialog = xbmcgui.Dialog()
					dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", self.DansGame("RXJyb3IhIA==")+"Reloaded TV"+self.DansGame("IEFjY291bnQgYmFubmVkIQ=="), self.DansGame("Q2Fubm90IGxvZ2luIQ=="), "")
					ADDON.openSettings()
					self.fc()
				if self.TriHard == self.DansGame("RGlzYWJsZWQ="):
					dialog = xbmcgui.Dialog()
					dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", self.DansGame("RXJyb3IhIA==")+"Reloaded TV"+self.DansGame("IEFjY291bnQgc3VzcGVuZGVkIQ=="), self.DansGame("UGxlYXNlIGNoZWNrIHlvdXIgaW52b2ljZXMh"), "")
					ADDON.openSettings()
					self.fc()
		if ADDON.getSetting('dexter.enabled') == 'true':
			if not self.CheckHasThisAddon(self.dexAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have DexterTV addon enabled but not installed...", "", "Please disable this addon in settings or install DexterTV!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('OTTTV.enabled') == 'true':
			if not self.CheckHasThisAddon(self.OTTTVAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have Over The Top TV addon enabled but not installed...", "", "Please disable this addon in settings or install Over The Top TV!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('suicide21.enabled') == 'true':
			if not self.CheckHasThisAddon(self.suicide21Addon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have Suicide TV 2.1 addon enabled but not installed...", "", "Please disable this addon in settings or install Suicide TV 2.1!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('aftermathtv.enabled') == 'true':
			if not self.CheckHasThisAddon(self.aftermathtvAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have AftermathTV addon enabled but not installed...", "", "Please disable this addon in settings or install AftermathTV!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('ukturk.enabled') == 'true':
			if not self.CheckHasThisAddon(self.ukturkAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have UK Turk addon enabled but not installed...", "", "Please disable this addon in settings or install UK Turk!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('sanctuary.enabled') == 'true':
			if not self.CheckHasThisAddon(self.sanctuaryAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have Sanctuary(Oblivion IPTV) addon enabled but not installed...", "", "Please disable this addon in settings or install Sanctuary!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('FTV.enabled') == 'true':
			if not self.CheckHasThisAddon(self.FTVAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have F.T.V addon enabled but not installed...", "", "Please disable this addon in settings or install F.T.V!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('uktvnow.enabled') == 'true':
			if not self.CheckHasThisAddon(self.uktvnowAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have UKTV Again addon enabled but not installed...", "", "Please disable this addon in settings or install UKTV Again!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('cluiptv.enabled') == 'true':
			if not self.CheckHasThisAddon(self.cluiptvAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have Clu IPTV addon enabled but not installed...", "", "Please disable this addon in settings or install Clu IPTV!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('suicide.enabled') == 'true':
			if not self.CheckHasThisAddon(self.suicideAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have Suicide TV addon enabled but not installed...", "", "Please disable this addon in settings or install Suicide TV!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('projectcypher.enabled') == 'true':
			if not self.CheckHasThisAddon(self.projectcypherAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have Project Cypher addon enabled but not installed...", "", "Please disable this addon in settings or install Project Cypher!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('notfilmon.enabled') == 'true':
			if not self.CheckHasThisAddon(self.notfilmonAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have NotFilmOn addon enabled but not installed...", "", "Please disable this addon in settings or install NotFilmOn!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('israelive.enabled') == 'true':
			if not self.CheckHasThisAddon(self.israeliveAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have IsraeLIVE addon enabled but not installed...", "", "Please disable this addon in settings or install IsraeLIVE!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('adriansports.enabled') == 'true':
			if not self.CheckHasThisAddon(self.adriansportsAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have AdrianSports addon enabled but not installed...", "", "Please disable this addon in settings or install AdrianSports!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('evolve.enabled') == 'true':
			if not self.CheckHasThisAddon(self.evolveAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have Evolve addon enabled but not installed...", "", "Please disable this addon in settings or install Evolve!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('freeview.enabled') == 'true':
			if not self.CheckHasThisAddon(self.freeviewAddon):
				xbmcgui.Dialog().ok("Enabled addon not installed!", "You have Freeview addon enabled but not installed...", "", "Please disable this addon in settings or install Freeview!")
				ADDON.openSettings()
				self.fc()
		if ADDON.getSetting('allfreeaddons.enabled') == 'true':
			TheseAddons   =  [self.ukturkAddon,self.sanctuaryAddon,self.FTVAddon,self.uktvnowAddon,self.suicideAddon,self.projectcypherAddon,self.notfilmonAddon,self.israeliveAddon,self.adriansportsAddon,self.evolveAddon,self.freeviewAddon]#self.cluiptvAddon
			for FoundAddon in TheseAddons:
				if not self.CheckHasThisAddon(FoundAddon):
					xbmcgui.Dialog().ok("Enabled addon not installed!", "All Free Addons enabled but " +FoundAddon+ " not installed...", "Please only enable addons you have installed or install " +FoundAddon+ "!")
					ADDON.openSettings()
					self.fc()
		if ADDON.getSetting('allfreeaddons.enabled') == 'false' and ADDON.getSetting('dexter.enabled') == 'false' and ADDON.getSetting('reloaded.enabled') == 'false' and ADDON.getSetting('OTTTV.enabled') == 'false' and  ADDON.getSetting('suicide21.enabled') == 'false' and ADDON.getSetting('aftermathtv.enabled') == 'false' and ADDON.getSetting('ukturk.enabled') == 'false' and ADDON.getSetting('sanctuary.enabled') == 'false' and ADDON.getSetting('FTV.enabled') == 'false' and ADDON.getSetting('uktvnow.enabled') == 'false' and ADDON.getSetting('cluiptv.enabled') == 'false' and ADDON.getSetting('suicide.enabled') == 'false' and ADDON.getSetting('projectcypher.enabled') == 'false' and ADDON.getSetting('notfilmon.enabled') == 'false' and ADDON.getSetting('israelive.enabled') == 'false' and ADDON.getSetting('adriansports.enabled') == 'false' and ADDON.getSetting('evolve.enabled') == 'false' and ADDON.getSetting('freeview.enabled') == 'false' and ADDON.getSetting('allchannels.enabled') == 'false':
			xbmcgui.Dialog().ok("No addons enabled!", "You have no addons enabled..", "", "Please go to addon settings and enable some addons for the guide to use!")
			ADDON.openSettings()
			self.fc()

		self.check_addons_data_updated()

	def DansGame(self,KappaPride):
		gachiGASM = base64.b64decode(KappaPride)
		return gachiGASM

	def get_reloaded(self):
		try:
			u = self.DansGame("aHR0cDovL21heWZhaXJndWlkZXMuY29tL2d1aWRlL3JlbG9hZGVkLnR4dA==")
			uu = requests.get(u, headers={'User-Agent': (UA)}).content
			return uu
		except:
			dialog = xbmcgui.Dialog()
			dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", self.DansGame("RXJyb3IhIENvdWxkIG5vdCBjb25uZWN0IHRvIHNlcnZlciBbMV0="),"", self.DansGame("UGxlYXNlIHRyeSBhZ2FpbiBsYXRlci4="))
			self.fc()

	def get_reloaded_account_info(self):
			try:
				self.show_busy_dialog()
				req = urllib2.Request(self.lolololol+self.DansGame("L3BhbmVsX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXM=")%(urllib.quote_plus(ADDON.getSetting(self.DansGame("cmVsb2FkZWQudXNlcg=="))),urllib.quote_plus(ADDON.getSetting(self.DansGame("cmVsb2FkZWQucGFzcw==")))))
				req.add_header(self.DansGame("VXNlci1BZ2VudA==") , self.DansGame("TWF5ZmFpckd1aWRlLVVzZXJBZ2VudA=="))
				response = urllib2.urlopen(req)
				link=response.read()
				jdata = json.loads(link.decode('utf8'))
				response.close()
				self.hide_busy_dialog()
				return jdata
			except:
				self.hide_busy_dialog()
				try:
					self.show_busy_dialog()
					req = urllib2.Request(self.DansGame("aHR0cDovL3JlbG9hZGVkbm93LmNvbToyMDg2L3BhbmVsX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXM=")%(urllib.quote_plus(ADDON.getSetting(self.DansGame("cmVsb2FkZWQudXNlcg=="))),urllib.quote_plus(ADDON.getSetting(self.DansGame("cmVsb2FkZWQucGFzcw==")))))
					req.add_header(self.DansGame("VXNlci1BZ2VudA==") , self.DansGame("TWF5ZmFpckd1aWRlLVVzZXJBZ2VudA=="))
					response = urllib2.urlopen(req)
					link=response.read()
					jdata = json.loads(link.decode('utf8'))
					response.close()
					self.hide_busy_dialog()
					return jdata
				except:
					self.hide_busy_dialog()
					dialog = xbmcgui.Dialog()
					dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]",self.DansGame("RXJyb3Ih"),self.DansGame("SXMg")+"Reloaded TV"+self.DansGame("IGRvd24/"),"")
					self.fc()

	def show_busy_dialog(self):
		xbmc.executebuiltin('ActivateWindow(10138)')

	def hide_busy_dialog(self):
		xbmc.executebuiltin('Dialog.Close(10138)')
		while xbmc.getCondVisibility('Window.IsActive(10138)'):
			xbmc.sleep(100)

	def check_addons_data_updated(self):
		if self.q.isrs:
			if lolol.cars():
				del self.streamingService
				self.streamingService = streaming.StreamsService(ADDON)
		else:
			if lolol.ca():
				del self.streamingService
				self.streamingService = streaming.StreamsService(ADDON)

	def CheckHasThisAddon(self,FoundAddon):
		if xbmc.getCondVisibility('System.HasAddon(%s)' % FoundAddon) == 1:
			return True
		else:
			return False 

	def getControl(self, controlId):
		try:
			return super(TVGuide, self).getControl(controlId)
		except:
			if controlId in self.ignoreMissingControlIds:
				return None
			if not self.isClosing:
				self.close()
			return None

	def fc(self):
		try:
			self.q.logout(True)
		except:
			pass
		self.kek.close()
		sys.exit(1)

	def close(self):
		if not self.isClosing:
			self.isClosing = True
			if self.chnexit:
				if self.player.isPlaying():
					self.player.stop()
			if self.database:
				try:
					self.q.logout()
				except:
					pass
				self.kek.close()
				self.database.close(super(TVGuide, self).close)
			else:
				try:
					self.q.logout()
				except:
					pass
				self.kek.close()
				super(TVGuide, self).close()

	def onInit(self):
		if self.init:
			return
		if not self.q:
			xbmcgui.Dialog().ok(lolkek('52584a796233496849466c7664534268636d5567626d39304947463164476876636d6c365a575175'), lolkek('57573931494746795a5342756233516759585630614739796158706c5a4377676347786c59584e6c49474e6f5a574e7249486c766458496764584e6c636d3568625755766347467a63336476636d5175'), lolkek('52584a79623349675932396b5a546f67')+str(self.w), '')
		self.windowID = xbmcgui.getCurrentWindowId()
		xbmcgui.Window(10000).setProperty('MAIN_WINDOW', str(self.windowID))
		if self.mayfaircustomwp:
			self.setControlImage(self.C_MAIN_BACKGROUND, xbmc.translatePath(os.path.join(SKINdir, 'resources', 'skins', 'Default', maywpfile)))
		self._hideControl(self.C_MAIN_MOUSE_CONTROLS, self.C_MAIN_OSD)
		self._showControl(self.C_MAIN_EPG, self.C_MAIN_LOADING)
		self.setControlLabel(self.C_MAIN_LOADING_TIME_LEFT, strings(BACKGROUND_UPDATE_IN_PROGRESS))
		self.setFocusId(self.C_MAIN_LOADING_CANCEL)
		if maycustom:
			self.setControlLabel(self.C_MAIN_VERSION, "[COLOR %s]%s[/COLOR]" % (self.versioncolor, "v"+ADDON.getAddonInfo('version')))
		else:
			self.setControlLabel(self.C_MAIN_VERSION, "v"+ADDON.getAddonInfo('version'))

		control = self.getControl(self.C_MAIN_EPG_VIEW_MARKER)
		if control:
			left, top = control.getPosition()
			self.focusPoint.x = left
			self.focusPoint.y = top
			self.epgView.left = left
			self.epgView.top = top
			self.epgView.right = left + control.getWidth()
			self.epgView.bottom = top + control.getHeight()
			self.epgView.width = control.getWidth()
			self.epgView.cellHeight = control.getHeight() / CHANNELS_PER_PAGE

		if self.database:
			self.onRedrawEPG(self.channelIdx, self.viewStartDate)
		else:
			try:
				self.database = src.Database(instance)
			except src.SourceNotConfiguredException:
				self.onSourceNotConfigured()
				self.close()
				return
			self.database.initialize(self.onSourceInitialized, self.isSourceInitializationCancelled)
		
		self.updateTimebar()
		self.init = True

	def onAction(self, action):
		debug('Mode is: %s' % self.mode)

		if self.mode == MODE_TV:
			self.onActionTVMode(action)
		elif self.mode == MODE_OSD:
			self.onActionOSDMode(action)
		elif self.mode == MODE_EPG:
			self.onActionEPGMode(action)

	def onActionTVMode(self, action):
		if action.getId() == ACTION_UP:
			if not self.channelswitch:
				self.kekk._channelUp()

		elif action.getId() == ACTION_DOWN:
			if not self.channelswitch:
				self.kekk._channelDown()

		elif action.getId() == ACTION_LEFT:
			if not self.channelswitch:
				self.kekk._previouschannel()

		elif action.getId() in range(KEY_ZERO, KEY_ZERO+10):
			if not self.channelinput:
				self.kekk.inputnumber(str(action.getId() - KEY_ZERO), 'TV')

		elif not self.osdEnabled and action.getId() in [ACTION_PARENT_DIR, KEY_NAV_BACK, KEY_CONTEXT_MENU, ACTION_PREVIOUS_MENU]:
			self.player.stop()
			#pass  # skip the rest of the actions

		elif action.getId() in [ACTION_PARENT_DIR, KEY_NAV_BACK, KEY_CONTEXT_MENU, ACTION_PREVIOUS_MENU]:
			self.viewStartDate = datetime.datetime.today()
			self.viewStartDate -= datetime.timedelta(minutes = self.viewStartDate.minute % 30, seconds = self.viewStartDate.second)
			self.focusPoint.y = self.epgView.top
			self.currentcategory = ADDON.getSetting('last.category')
			self.channelIdx = self.kek.getCurrentChannel(self.currentChannel, category=self.currentcategory)
			self.onRedrawEPG(self.channelIdx, self.viewStartDate)

		elif action.getId() == ACTION_SELECT_ITEM:
			if self.player.isPlaying():
				self.kekk._showOsd()

	def onActionOSDMode(self, action):
		if action.getId() in [ACTION_PARENT_DIR, KEY_NAV_BACK, KEY_CONTEXT_MENU, ACTION_PREVIOUS_MENU]:
			if action.getId() in [KEY_CONTEXT_MENU]:
				selection = xbmcgui.Dialog().select("[COLOR red]Reloaded TV Guide[/COLOR]",["Audio Settings", "Video Settings", "Exit OSD Mini EPG"])
				if selection == 0:
					xbmc.executebuiltin('ActivateWindow(osdaudiosettings)')
				elif selection == 1:
					xbmc.executebuiltin('ActivateWindow(osdvideosettings)')
				elif selection == 2:
					self._hideOsd()
				elif selection == -1:
					self._hideOsd()
			else:	
				self._hideOsd()

		elif action.getId() == ACTION_SELECT_ITEM:
			self.kekk.p1()

		elif action.getId() == ACTION_PAGE_UP:
			if not self.channelswitch:
				self.kekk._channelUp()
				self.kekk._showOsd()

		elif action.getId() == ACTION_PAGE_DOWN:
			if not self.channelswitch:
				self.kekk._channelDown()
				self.kekk._showOsd()

		elif action.getId() == ACTION_DOWN:
			self.osdChannel = self.kek.getPreviousChannel(self.osdChannel)
			self.osdProgram = self.kek.getCurrentProgram(self.osdChannel)
			self.kekk._showOsd()

		elif action.getId() == ACTION_UP:
			self.osdChannel = self.kek.getNextChannel(self.osdChannel)
			self.osdProgram = self.kek.getCurrentProgram(self.osdChannel)
			self.kekk._showOsd()

		elif action.getId() == ACTION_LEFT:
			previousProgram = self.kek.getPreviousProgram(self.osdProgram)
			if previousProgram:
				self.osdProgram = previousProgram
				self.kekk._showOsd()

		elif action.getId() == ACTION_RIGHT:
			nextProgram = self.kek.getNextProgram(self.osdProgram)
			if nextProgram:
				self.osdProgram = nextProgram
				self.kekk._showOsd()

		elif action.getId() in range(KEY_ZERO, KEY_ZERO+10):
			if not self.channelinput:
				self.kekk.inputnumber(str(action.getId() - KEY_ZERO), 'OSD')

	def onActionEPGMode(self, action):
		if action.getId() in [ACTION_PARENT_DIR, KEY_NAV_BACK]:
			if self.player.isPlaying():
				dialog = xbmcgui.Dialog()
				ret = dialog.yesno('[COLOR red]Reloaded TV Guide[/COLOR]','Detected you have a channel playing..','Do you wish to exit the guide or channel?','','Exit channel','Exit TV Guide')
				if ret:
					self.close()
					return
				if not ret:
					self.player.stop()
					return
			else:
				self.close()
				return

		# catch the ESC key
		elif action.getId() == ACTION_PREVIOUS_MENU and action.getButtonCode() == KEY_ESC:
			if self.player.isPlaying():
				dialog = xbmcgui.Dialog()
				ret = dialog.yesno('[COLOR red]Reloaded TV Guide[/COLOR]','Detected you have a channel playing..','Do you wish to exit the guide or channel?','','Exit channel','Exit TV Guide')
				if ret:
					self.close()
					return
				if not ret:
					self.player.stop()
					return
			else:
				self.close()
				return

		elif action.getId() == ACTION_MOUSE_MOVE:
			self._showControl(self.C_MAIN_MOUSE_CONTROLS)
			return

		#elif action.getId() in [KEY_CONTEXT_MENU, ACTION_PREVIOUS_MENU]:
		#	if self.player.isPlaying():
		#		self._hideEpg()

		controlInFocus = None
		currentFocus = self.focusPoint
		try:
			controlInFocus = self.getFocus()
			if controlInFocus in [elem.control for elem in self.controlAndProgramList]:
				(left, top) = controlInFocus.getPosition()
				currentFocus = Point()
				currentFocus.x = left + (controlInFocus.getWidth() / 2)
				currentFocus.y = top + (controlInFocus.getHeight() / 2)
		except Exception:
			control = self._findControlAt(self.focusPoint)
			if control is None and len(self.controlAndProgramList) > 0:
				control = self.controlAndProgramList[0].control
			if control is not None:
				self.setFocus(control)
				return

		if action.getId() == ACTION_LEFT:
			self._left(currentFocus)
		elif action.getId() == ACTION_RIGHT:
			self._right(currentFocus)
		elif action.getId() == ACTION_UP:
			self._up(currentFocus)
		elif action.getId() == ACTION_DOWN:
			self._down(currentFocus)
		elif action.getId() == ACTION_NEXT_ITEM:
			self._nextDay()
		elif action.getId() == ACTION_PREV_ITEM:
			self._previousDay()
		elif action.getId() == ACTION_PAGE_UP:
			self._moveUp(CHANNELS_PER_PAGE)
		elif action.getId() == ACTION_PAGE_DOWN:
			self._moveDown(CHANNELS_PER_PAGE)
		elif action.getId() == ACTION_MOUSE_WHEEL_UP:
			self._moveUp(scrollEvent=True)
		elif action.getId() == ACTION_MOUSE_WHEEL_DOWN:
			self._moveDown(scrollEvent=True)
		elif action.getId() == KEY_HOME:
			self.viewStartDate = datetime.datetime.today()
			self.viewStartDate -= datetime.timedelta(minutes=self.viewStartDate.minute % 30,
													 seconds=self.viewStartDate.second)
			self.onRedrawEPG(self.channelIdx, self.viewStartDate)
		elif action.getId() in [KEY_CONTEXT_MENU, ACTION_PREVIOUS_MENU] and controlInFocus is not None:
			program = self._getProgramFromControl(controlInFocus)
			if program is not None:
				self._showContextMenu(program)
		elif action.getId() in range(KEY_ZERO, KEY_ZERO+10):
			if not self.channelinput:
				self.kekk.inputnumber(str(action.getId() - KEY_ZERO), 'EPG')
		else:
			xbmc.log('[plugin.program.reloadedtv] Unhandled ActionId: ' + str(action.getId()), xbmc.LOGDEBUG)


	def onClick(self, controlId):
		if controlId in [self.C_MAIN_LOADING_CANCEL, self.C_MAIN_MOUSE_EXIT, self.C_MAIN_SETTING]:
			self.close()
			return

		if self.isClosing:
			return

		if controlId == self.C_MAIN_MOUSE_HOME:
			self.viewStartDate = datetime.datetime.today()
			self.viewStartDate -= datetime.timedelta(minutes=self.viewStartDate.minute % 30, seconds=self.viewStartDate.second)
			self.onRedrawEPG(self.channelIdx, self.viewStartDate)
			return
		elif controlId == self.C_MAIN_MOUSE_LEFT:
			self.viewStartDate -= datetime.timedelta(hours=2)
			self.onRedrawEPG(self.channelIdx, self.viewStartDate)
			return
		elif controlId == self.C_MAIN_MOUSE_UP:
			self._moveUp(count=CHANNELS_PER_PAGE)
			return
		elif controlId == self.C_MAIN_MOUSE_DOWN:
			self._moveDown(count=CHANNELS_PER_PAGE)
			return
		elif controlId == self.C_MAIN_MOUSE_RIGHT:
			self.viewStartDate += datetime.timedelta(hours=2)
			self.onRedrawEPG(self.channelIdx, self.viewStartDate)
			return

		program = self._getProgramFromControl(self.getControl(controlId))
		if program is None:
			return

		self.kekk.p2(program)


	def _showContextMenu(self, program):
		self._hideControl(self.C_MAIN_MOUSE_CONTROLS)
		d = PopupMenu(self.database, program, not program.notificationScheduled, instance)
		d.doModal()
		buttonClicked = d.buttonClicked
		del d

		if buttonClicked == PopupMenu.C_POPUP_REMIND:
			if program.notificationScheduled:
				self.notification.removeNotification(program)
			else:
				self.notification.addNotification(program)

			self.onRedrawEPG(self.channelIdx, self.viewStartDate)

		elif buttonClicked == PopupMenu.C_POPUP_CHOOSE_STREAM:
			d = StreamSetupDialog(self.database, program.channel)
			d.doModal()
			del d

		elif buttonClicked == PopupMenu.C_POPUP_SETTINGS:
			xbmc.executebuiltin('Dialog.Close(10140)')
			self.close()
			xbmc.sleep(100)
			ADDON.openSettings()

		elif buttonClicked == PopupMenu.C_POPUP_CATEGORIES:
			self.close()

		elif buttonClicked == PopupMenu.C_POPUP_PLAY:
			self.kekk.playChannel(program.channel, program)

		elif buttonClicked == PopupMenu.C_POPUP_CHANNELS:
			d = ChannelsMenu(self.database)
			d.doModal()
			del d
			self.onRedrawEPG(self.channelIdx, self.viewStartDate)

		elif buttonClicked == PopupMenu.C_POPUP_QUIT:
			self.close()

		elif buttonClicked == PopupMenu.C_POPUP_LIBMOV:
			xbmc.executebuiltin('ActivateWindow(Videos,videodb://movies/titles/)')

		elif buttonClicked == PopupMenu.C_POPUP_LIBTV:
			xbmc.executebuiltin('ActivateWindow(Videos,videodb://tvshows/titles/)')
			
		elif buttonClicked == PopupMenu.C_POPUP_VIDEOADDONS:
			xbmc.executebuiltin('ActivateWindow(Videos,addons://sources/video/)')

		# Custom addons1 to menu tab
		elif buttonClicked == PopupMenu.C_POPUP_ADDON1:
			addon1 = ADDON.getSetting('CustomAddon1')
			xbmc.executebuiltin('XBMC.RunAddon(' + addon1 + ')')  			
		# Custom addons2 to menu tab						
		elif buttonClicked == PopupMenu.C_POPUP_ADDON2:
			addon2 = ADDON.getSetting('CustomAddon2')
			xbmc.executebuiltin('XBMC.RunAddon(' + addon2 + ')') 			
		# Custom addons3 to menu tab			
		elif buttonClicked == PopupMenu.C_POPUP_ADDON3:
			addon3 = ADDON.getSetting('CustomAddon3')
			xbmc.executebuiltin('XBMC.RunAddon(' + addon3 + ')') 				
			
		#mayfair tv search
		elif buttonClicked == PopupMenu.C_POPUP_MTVSHOW:
			metalliqdir = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'plugin.video.metalliq'))
			metalliqplayerdir = xbmc.translatePath(os.path.join(metalliqdir, 'players'))
			qrepo = xbmc.translatePath(os.path.join('special://home/addons','repository.q'))
			try:
				if self.CheckHasThisAddon('plugin.video.metalliq'):
					metalliqaddon = xbmcaddon.Addon('plugin.video.metalliq')
					if metalliqaddon.getSetting('total_setup_done') == 'false':
						xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
						metalliqaddon.setSetting('total_setup_done', 'true')
						ADDON.setSetting('metalliqsetup', 'true')
					if ADDON.getSetting('metalliqsetup') == 'false':
						xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
						ADDON.setSetting('metalliqsetup', 'true')
					else:
						if os.path.exists(metalliqdir):
							if os.path.exists(metalliqplayerdir):
								if not os.listdir(metalliqplayerdir):
									xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
									ADDON.setSetting('metalliqsetup', 'true')
							else:
								xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
								ADDON.setSetting('metalliqsetup', 'true')
						else:
							xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
							ADDON.setSetting('metalliqsetup', 'true')
					if 'explore.youtube_nl.q' in metalliqaddon.getSetting('movies_enabled_players') or 'explore.youtube.q' in metalliqaddon.getSetting('movies_enabled_players') or 'explore.movieflix.q' in metalliqaddon.getSetting('movies_enabled_players') or 'explore.youtube_nl.q' in metalliqaddon.getSetting('tv_enabled_players') or 'explore.youtube.q' in metalliqaddon.getSetting('tv_enabled_players') or 'explore.movieflix.q' in metalliqaddon.getSetting('tv_enabled_players'):
						movieplayers = metalliqaddon.getSetting('movies_enabled_players').replace('"explore.youtube_nl.q", ','').replace(', "explore.youtube_nl.q"','').replace('"explore.youtube.q", ','').replace(', "explore.youtube.q"','').replace('"explore.movieflix.q", ','').replace(', "explore.movieflix.q"','')
						tvplayers    = metalliqaddon.getSetting('tv_enabled_players').replace('"explore.youtube_nl.q", ','').replace(', "explore.youtube_nl.q"','').replace('"explore.youtube.q", ','').replace(', "explore.youtube.q"','').replace('"explore.movieflix.q", ','').replace(', "explore.movieflix.q"','')
						metalliqaddon.setSetting('movies_enabled_players', movieplayers)
						metalliqaddon.setSetting('tv_enabled_players', tvplayers)
				selection = xbmcgui.Dialog().select("TV Shows",["Popular", "Genres", "Top rated", "Search.."])
				if selection == 0:
					xbmc.executebuiltin("ActivateWindow(Videos, plugin://plugin.video.metalliq/tv/tmdb/most_popular/<1>)")
				elif selection == 1:
					xbmc.executebuiltin("ActivateWindow(Videos, plugin://plugin.video.metalliq/tv/tmdb/genres)")
				elif selection == 2:
					xbmc.executebuiltin("ActivateWindow(Videos, plugin://plugin.video.metalliq/tv/tmdb/top_rated/<1>)")
				elif selection == 3:
					dialog = xbmcgui.Dialog()
					lklklklklklklklk = dialog.input(self.DansGame('U2VhcmNoIGZvciBUViBTaG93cw=='), type=xbmcgui.INPUT_ALPHANUM)
					xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/tv/play_by_name_only/%s/%s)" % (lklklklklklklklk, 'en'))
				if not os.path.exists(qrepo):
					dialog = xbmcgui.Dialog()
					dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", "[B][COLOR lime]You DO NOT have [COLOR FF8ABEE2]Q[/COLOR]'s Repository installed![/COLOR][/B]","[COLOR ff0084ff]M[/COLOR]etalli[COLOR ff0084ff]Q[/COLOR] addon required for this feature!","Get it at: [COLOR orangered]https://archive.org/download/OpenELEQ/[/COLOR]\nand install repository.q and [COLOR ff0084ff]M[/COLOR]etalli[COLOR ff0084ff]Q[/COLOR] video addon.")
			except:
				pass
		#mayfair movie search
		elif buttonClicked == PopupMenu.C_POPUP_MMOVIE:
			metalliqdir = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'plugin.video.metalliq'))
			metalliqplayerdir = xbmc.translatePath(os.path.join(metalliqdir, 'players'))
			qrepo = xbmc.translatePath(os.path.join('special://home/addons','repository.q'))
			try:
				if self.CheckHasThisAddon('plugin.video.metalliq'):
					metalliqaddon = xbmcaddon.Addon('plugin.video.metalliq')
					if metalliqaddon.getSetting('total_setup_done') == 'false':
						xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
						metalliqaddon.setSetting('total_setup_done', 'true')
						ADDON.setSetting('metalliqsetup', 'true')
					if ADDON.getSetting('metalliqsetup') == 'false':
						xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
						ADDON.setSetting('metalliqsetup', 'true')
					else:
						if os.path.exists(metalliqdir):
							if os.path.exists(metalliqplayerdir):
								if not os.listdir(metalliqplayerdir):
									xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
									ADDON.setSetting('metalliqsetup', 'true')
							else:
								xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
								ADDON.setSetting('metalliqsetup', 'true')
						else:
							xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
							ADDON.setSetting('metalliqsetup', 'true')
					if 'explore.youtube_nl.q' in metalliqaddon.getSetting('movies_enabled_players') or 'explore.youtube.q' in metalliqaddon.getSetting('movies_enabled_players') or 'explore.movieflix.q' in metalliqaddon.getSetting('movies_enabled_players') or 'explore.youtube_nl.q' in metalliqaddon.getSetting('tv_enabled_players') or 'explore.youtube.q' in metalliqaddon.getSetting('tv_enabled_players') or 'explore.movieflix.q' in metalliqaddon.getSetting('tv_enabled_players'):
						movieplayers = metalliqaddon.getSetting('movies_enabled_players').replace('"explore.youtube_nl.q", ','').replace(', "explore.youtube_nl.q"','').replace('"explore.youtube.q", ','').replace(', "explore.youtube.q"','').replace('"explore.movieflix.q", ','').replace(', "explore.movieflix.q"','')
						tvplayers    = metalliqaddon.getSetting('tv_enabled_players').replace('"explore.youtube_nl.q", ','').replace(', "explore.youtube_nl.q"','').replace('"explore.youtube.q", ','').replace(', "explore.youtube.q"','').replace('"explore.movieflix.q", ','').replace(', "explore.movieflix.q"','')
						metalliqaddon.setSetting('movies_enabled_players', movieplayers)
						metalliqaddon.setSetting('tv_enabled_players', tvplayers)
				selection = xbmcgui.Dialog().select("Movies",["Popular", "Genres", "Blockbusters", "Top rated", "Search.."])
				if selection == 0:
					xbmc.executebuiltin("ActivateWindow(Videos, plugin://plugin.video.metalliq/movies/tmdb/popular/<1>)")
				elif selection == 1:
					xbmc.executebuiltin("ActivateWindow(Videos, plugin://plugin.video.metalliq/movies/tmdb/genres)")
				elif selection == 2:
					xbmc.executebuiltin("ActivateWindow(Videos, plugin://plugin.video.metalliq/movies/tmdb/blockbusters/<1>)")
				elif selection == 3:
					xbmc.executebuiltin("ActivateWindow(Videos, plugin://plugin.video.metalliq/movies/tmdb/top_rated/<1>)")
				elif selection == 4:
					dialog = xbmcgui.Dialog()
					lklklklklklkllk = dialog.input(self.DansGame('U2VhcmNoIGZvciBNb3ZpZXM='), type=xbmcgui.INPUT_ALPHANUM)
					xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/movies/play_by_name/%s/%s)" % (lklklklklklkllk, 'en'))
				if not os.path.exists(qrepo):
					dialog = xbmcgui.Dialog()
					dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", "[B][COLOR lime]You DO NOT have [COLOR FF8ABEE2]Q[/COLOR]'s Repository installed![/COLOR][/B]","[COLOR ff0084ff]M[/COLOR]etalli[COLOR ff0084ff]Q[/COLOR] addon required for this feature!","Get it at: [COLOR orangered]https://archive.org/download/OpenELEQ/[/COLOR]\nand install repository.q and [COLOR ff0084ff]M[/COLOR]etalli[COLOR ff0084ff]Q[/COLOR] video addon.")
			except:
				pass

		elif buttonClicked == PopupMenu.C_POPUP_PLAY_BEGINNING:
			title = program.title.replace(" ", "%20").replace(",", "").replace(u"\u2013", "-")
			title = unicode.encode(title, "ascii", "ignore")
			metalliqdir = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'plugin.video.metalliq'))
			metalliqplayerdir = xbmc.translatePath(os.path.join(metalliqdir, 'players'))
			qrepo = xbmc.translatePath(os.path.join('special://home/addons','repository.q'))
			try:
				if self.CheckHasThisAddon('plugin.video.metalliq'):
					metalliqaddon = xbmcaddon.Addon('plugin.video.metalliq')
					if metalliqaddon.getSetting('total_setup_done') == 'false':
						xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
						metalliqaddon.setSetting('total_setup_done', 'true')
						ADDON.setSetting('metalliqsetup', 'true')
					if ADDON.getSetting('metalliqsetup') == 'false':
						xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
						ADDON.setSetting('metalliqsetup', 'true')
					else:
						if os.path.exists(metalliqdir):
							if os.path.exists(metalliqplayerdir):
								if not os.listdir(metalliqplayerdir):
									xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
									ADDON.setSetting('metalliqsetup', 'true')
							else:
								xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
								ADDON.setSetting('metalliqsetup', 'true')
						else:
							xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/setup/total)")
							ADDON.setSetting('metalliqsetup', 'true')
					if 'explore.youtube_nl.q' in metalliqaddon.getSetting('movies_enabled_players') or 'explore.youtube.q' in metalliqaddon.getSetting('movies_enabled_players') or 'explore.movieflix.q' in metalliqaddon.getSetting('movies_enabled_players') or 'explore.youtube_nl.q' in metalliqaddon.getSetting('tv_enabled_players') or 'explore.youtube.q' in metalliqaddon.getSetting('tv_enabled_players') or 'explore.movieflix.q' in metalliqaddon.getSetting('tv_enabled_players'):
						movieplayers = metalliqaddon.getSetting('movies_enabled_players').replace('"explore.youtube_nl.q", ','').replace(', "explore.youtube_nl.q"','').replace('"explore.youtube.q", ','').replace(', "explore.youtube.q"','').replace('"explore.movieflix.q", ','').replace(', "explore.movieflix.q"','')
						tvplayers    = metalliqaddon.getSetting('tv_enabled_players').replace('"explore.youtube_nl.q", ','').replace(', "explore.youtube_nl.q"','').replace('"explore.youtube.q", ','').replace(', "explore.youtube.q"','').replace('"explore.movieflix.q", ','').replace(', "explore.movieflix.q"','')
						metalliqaddon.setSetting('movies_enabled_players', movieplayers)
						metalliqaddon.setSetting('tv_enabled_players', tvplayers)
				if program.is_movie == "Movie":
					selection = 0
				elif program.season is not None:
					selection = 1
				else:
					selection = xbmcgui.Dialog().select("Choose media type",["Search as Movie", "Search as TV Show"])
				if selection == 0:
					xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/movies/play_by_name/%s/%s)" % (
						title, program.language))
				elif selection == 1:
					if program.season and program.episode:
						xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/tv/play_by_name/%s/%s/%s/%s)" % (
							title, program.season, program.episode, program.language))
					else:
						xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/tv/play_by_name_only/%s/%s)" % (
							title, program.language))
				if not os.path.exists(qrepo):
					dialog = xbmcgui.Dialog()
					dialog.ok("[COLOR red]Reloaded TV Guide[/COLOR]", "[B][COLOR lime]You DO NOT have [COLOR FF8ABEE2]Q[/COLOR]'s Repository installed![/COLOR][/B]","[COLOR ff0084ff]M[/COLOR]etalli[COLOR ff0084ff]Q[/COLOR] addon required for this feature!","Get it at: [COLOR orangered]https://archive.org/download/OpenELEQ/[/COLOR]\nand install repository.q and [COLOR ff0084ff]M[/COLOR]etalli[COLOR ff0084ff]Q[/COLOR] video addon.")
			except:
				pass



	def setFocusId(self, controlId):
		control = self.getControl(controlId)
		if control:
			self.setFocus(control)

	def setFocus(self, control):
		debug('setFocus %d' % control.getId())
		if control in [elem.control for elem in self.controlAndProgramList]:
			debug('Focus before %s' % self.focusPoint)
			(left, top) = control.getPosition()
			if left > self.focusPoint.x or left + control.getWidth() < self.focusPoint.x:
				self.focusPoint.x = left
			self.focusPoint.y = top + (control.getHeight() / 2)
			debug('New focus at %s' % self.focusPoint)

		super(TVGuide, self).setFocus(control)

	def onFocus(self, controlId):
		try:
			controlInFocus = self.getControl(controlId)
		except Exception:
			return

		program = self._getProgramFromControl(controlInFocus)
		if program is None:
			return
		title = '[B]%s[/B]' % program.title
		if program.season is not None and program.episode is not None:
			title += " [B]S%sE%s[/B]" % (program.season, program.episode)
		if program.is_movie == "Movie":
			title += " [B](Movie)[/B]"
		if maycustom:
			self.setControlLabel(self.C_MAIN_TITLE, '[COLOR %s]%s[/COLOR]' % (self.programtitlecolor, title))
		else:
			self.setControlLabel(self.C_MAIN_TITLE, title)
		if program.startDate or program.endDate:
			if maycustom:
				self.setControlLabel(self.C_MAIN_TIME,
									 '[COLOR %s][B]%s - %s[/B][/COLOR]' % (self.programstartendtimecolor, self.formatTime(program.startDate), self.formatTime(program.endDate)))
			else:
				self.setControlLabel(self.C_MAIN_TIME,
									 '[B]%s - %s[/B]' % (self.formatTime(program.startDate), self.formatTime(program.endDate)))
		else:
			self.setControlLabel(self.C_MAIN_TIME, '')
		if program.description:
			description = program.description
		else:
			description = strings(NO_DESCRIPTION)
		if maycustom:
			self.setControlText(self.C_MAIN_DESCRIPTION,'[COLOR %s]%s[/COLOR]' % (self.programdesccolor, description))
		else:
			self.setControlText(self.C_MAIN_DESCRIPTION, description)

		if program.channel.logo is not None:
			self.setControlImage(self.C_MAIN_LOGO, program.channel.logo)
		else:
			self.setControlImage(self.C_MAIN_LOGO, '')

		if program.imageSmall is not None:
			self.setControlImage(self.C_MAIN_IMAGE, program.imageSmall)
		else:
			self.setControlImage(self.C_MAIN_IMAGE, 'tvguide-logo-epg.png')

		if ADDON.getSetting('program.background.enabled') == 'true' and program.imageLarge is not None:
			self.setControlImage(self.C_MAIN_BACKGROUND, program.imageLarge)

		if not self.osdEnabled and self.player.isPlaying():
			#Custom
			#self.player.stop()
			print ''

	def _left(self, currentFocus):
		control = self._findControlOnLeft(currentFocus)
		if control is not None:
			self.setFocus(control)
		elif control is None:
			self.viewStartDate -= datetime.timedelta(hours=2)
			self.focusPoint.x = self.epgView.right
			self.onRedrawEPG(self.channelIdx, self.viewStartDate, focusFunction=self._findControlOnLeft)

	def _right(self, currentFocus):
		control = self._findControlOnRight(currentFocus)
		if control is not None:
			self.setFocus(control)
		elif control is None:
			self.viewStartDate += datetime.timedelta(hours=2)
			self.focusPoint.x = self.epgView.left
			self.onRedrawEPG(self.channelIdx, self.viewStartDate, focusFunction=self._findControlOnRight)

	def _up(self, currentFocus):
		currentFocus.x = self.focusPoint.x
		control = self._findControlAbove(currentFocus)
		if control is not None:
			self.setFocus(control)
		elif control is None:
			self.focusPoint.y = self.epgView.bottom
			self.onRedrawEPG(self.channelIdx - CHANNELS_PER_PAGE, self.viewStartDate,
							 focusFunction=self._findControlAbove)

	def _down(self, currentFocus):
		currentFocus.x = self.focusPoint.x
		control = self._findControlBelow(currentFocus)
		if control is not None:
			self.setFocus(control)
		elif control is None:
			self.focusPoint.y = self.epgView.top
			self.onRedrawEPG(self.channelIdx + CHANNELS_PER_PAGE, self.viewStartDate,
							 focusFunction=self._findControlBelow)

	def _nextDay(self):
		self.viewStartDate += datetime.timedelta(days=1)
		self.onRedrawEPG(self.channelIdx, self.viewStartDate)

	def _previousDay(self):
		self.viewStartDate -= datetime.timedelta(days=1)
		self.onRedrawEPG(self.channelIdx, self.viewStartDate)

	def _moveUp(self, count=1, scrollEvent=False):
		if scrollEvent:
			self.onRedrawEPG(self.channelIdx - count, self.viewStartDate)
		else:
			self.focusPoint.y = self.epgView.bottom
			self.onRedrawEPG(self.channelIdx - count, self.viewStartDate, focusFunction=self._findControlAbove)

	def _moveDown(self, count=1, scrollEvent=False):
		if scrollEvent:
			self.onRedrawEPG(self.channelIdx + count, self.viewStartDate)
		else:
			self.focusPoint.y = self.epgView.top
			self.onRedrawEPG(self.channelIdx + count, self.viewStartDate, focusFunction=self._findControlBelow)

	'''
	def playChannel(self, channel, program = None):
		self.currentChannel = channel
		wasPlaying = self.player.isPlaying()
		url = self.database.getStreamUrl(channel)
		if url:
			if str.startswith(url,"plugin://plugin.video.meta") and program is not None:
				import urllib
				title = urllib.quote(program.title)
				url += "/%s/%s" % (title, program.language)
			if url[0:9] == 'plugin://':
				if self.alternativePlayback:
					xbmc.executebuiltin('XBMC.RunPlugin(%s)' % url)
				elif self.osdEnabled:
					xbmc.executebuiltin('PlayMedia(%s,1)' % url)
				else:
					xbmc.executebuiltin('PlayMedia(%s)' % url)
			else:
				self.player.play(item=url, windowed=self.osdEnabled)

			if not wasPlaying:
				self._hideEpg()

		threading.Timer(1, self.waitForPlayBackStopped).start()
		self.osdProgram = self.database.getCurrentProgram(self.currentChannel)

		return url is not None
	'''

	class CustomPlayer(xbmc.Player):

		def __init__ (self, *args):
			self.isplaying = False

		def onPlayBackStarted(self):
			self.isplaying = True
			instance._hideEpg()
			instance.channelswitch = False
			if instance.osdEnabled:
				windowID = xbmcgui.Window(10000).getProperty('MAIN_WINDOW')
				try:
					xbmc.sleep(1000)
					windowID = int(windowID)
					xbmc.executebuiltin('ActivateWindow(%d)' % windowID)
				except:
					pass
				xbmc.sleep(100)
				instance.kekk._showOsd(True)
				xbmc.sleep(1700)
				instance._hideOsd(True)
				
		def onPlayBackEnded(self):
			dialog = xbmcgui.Dialog()
			dialog.ok('[COLOR red]Reloaded TV Guide[/COLOR]',instance.DansGame('W0NPTE9SIHJlZF1bQl1FcnJvciB3aXRoIHN0cmVhbSFbL0JdWy9DT0xPUl0='),instance.DansGame('Q29ubmVjdGlvbiB0byB0aGUgc3RyZWFtIHNlZW1zIHRvIGhhdmUgYmVlbiBsb3N0Lg=='),instance.DansGame('U3RyZWFtIGNvdWxkIG9mIGdvbmUgZG93biBvciB0cnkgY2xlYXIgeW91ciBjYWNoZSwgcmVzdGFydCB5b3VyIGRldmljZSBhbmQgY2hlY2sgeW91ciBjb25uZWN0aW9uLi4='))
			self.onPlayBackStopped()
				
		def onPlayBackStopped(self):
			if self.isplaying == False or self.isplaying == True and instance.channelswitch == True:
				self.isplaying = False
				instance.channelswitch = False
				instance.onPlayBackStopped()
				instance.kekk.StreamDown()
			else:
				self.isplaying = False
				instance.channelswitch = False
				instance.onPlayBackStopped()
				
		def onPlayBackPaused(self):
			if xbmc.Player().isPlaying():
				pass

		def onPlayBackResumed(self):
			if xbmc.Player().isPlaying():
				pass


	'''
	def playChannel(self, channel, program = None):
		self.currentChannel = channel
		wasPlaying = self.player.isPlaying()
		url = self.database.getStreamUrl(channel)
		if url:

			# pvr
			if url.isdigit():
				command = ('{"jsonrpc": "2.0", "id":"1", "method": "Player.Open","params":{"item":{"channelid":%s}}}' % url)
				xbmc.executeJSONRPC(command)
				return   
   
   
			# livemix
			if url.startswith('LIVETV'):
				import add;stream = add.playlivemix(url)
				# or
				#stream = playlivemix(url)
				
				delay=0
				delay=100
				playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
				playlist.clear()
				playlist.add(stream, xbmcgui.ListItem(''))
				try:
					xbmc.Player().play(playlist)
				except: pass
				return        


			# Playlist
			if url.lower().startswith('dsf'):
				import add
				if add.playPlaylist(url, windowed):
					#wait(maxIdle)
					print 'Playlist'
				return


			# meta or metalq
			if str.startswith(url,"plugin://plugin.video.meta") and program is not None:
				import urllib
				title = urllib.quote(program.title)
				url += "/%s/%s" % (title, program.language)

			# Addons                 
			if url[0:9] == 'plugin://':
				if self.alternativePlayback:
					xbmc.executebuiltin('XBMC.RunPlugin(%s)' % url)
				elif self.osdEnabled:
					xbmc.executebuiltin('PlayMedia(%s,1)' % url)
				else:
					xbmc.executebuiltin('PlayMedia(%s)' % url)
			else:
				self.player.play(item=url, windowed=self.osdEnabled)

			if not wasPlaying:
				self._hideEpg()

		threading.Timer(1, self.waitForPlayBackStopped).start()
		self.osdProgram = self.database.getCurrentProgram(self.currentChannel)

		return url is not None
	 '''      
		
		
  

	#def waitForPlayBackStopped(self):
	#	for retry in range(0, 100):
	#		xbmc.sleep(300)
	#		if self.player.isPlaying():
	#			break
#
#		while self.player.isPlaying() and not xbmc.abortRequested and not self.isClosing:
#			xbmc.sleep(500)
#
#		xbmc.Player().stop()
#		self.onPlayBackStopped()


	def waitForPlayBackStopped(self):
		for retry in range(0, 100):
			xbmc.sleep(200)
			if self.player.isPlaying():
				break

		while self.player.isPlaying() and not xbmc.abortRequested and not self.isClosing:
			xbmc.sleep(500)

		self.onPlayBackStopped()

	def _hideOsd(self, onplayback=False):
		if not onplayback:
			self.mode = MODE_TV
		self._hideControl(self.C_MAIN_OSD)

	def _hideEpg(self):
		self._hideControl(self.C_MAIN_EPG)
		self.mode = MODE_TV
		self._clearEpg()

	def onRedrawEPG(self, channelStart, startTime, focusFunction=None):
		if self.redrawingEPG or (self.database is not None and self.database.updateInProgress) or self.isClosing:
			debug('onRedrawEPG - already redrawing')
			xbmc.sleep(300)
			return  # ignore redraw request while redrawing
		debug('onRedrawEPG')

		self.redrawingEPG = True
		self.currentcategory = ADDON.getSetting('last.category')
		if self.mode == MODE_OSD:
			self._hideOsd()
		self.mode = MODE_EPG
		self._showControl(self.C_MAIN_EPG)
		self.updateTimebar(scheduleTimer=False)

		# show Loading screen
		self.setControlLabel(self.C_MAIN_LOADING_TIME_LEFT, strings(CALCULATING_REMAINING_TIME))
		self._showControl(self.C_MAIN_LOADING)
		self.setFocusId(self.C_MAIN_LOADING_CANCEL)


		# remove existing controls
		self._clearEpg()

		try:
			if inspect.stack()[1][3] == 'onPlayBackStopped':
				xbmc.sleep(250)
			self.channelIdx, channels, programs = self.database.getEPGView(channelStart, startTime, self.onSourceProgressUpdate, clearExistingProgramList=False, category=self.currentcategory)
			if len(channels) == 0:
				dialog = xbmcgui.Dialog()
				dialog.notification('', 'No channels found for this category!\nDefaulting back to All Channels', xbmcgui.NOTIFICATION_WARNING, 3500)
				ADDON.setSetting('last.category', "All Channels")
				self.currentcategory = ADDON.getSetting('last.category')
				self.channelIdx, channels, programs = self.database.getEPGView(channelStart, startTime, self.onSourceProgressUpdate, clearExistingProgramList=False, category=self.currentcategory)
		except src.SourceException:
			self.onEPGLoadError()
			return

		channelsWithoutPrograms = list(channels)

		# date and time row
		if maycustom:
			self.setControlLabel(self.C_MAIN_DATE, '[COLOR %s]%s[/COLOR]' % (self.guidedatecolor, self.formatDate(self.viewStartDate, False)))
		else:
			self.setControlLabel(self.C_MAIN_DATE, self.formatDate(self.viewStartDate, False))
		if maycustom:
			self.setControlLabel(self.C_MAIN_DATE_LONG, '[COLOR %s]%s[/COLOR]' % (self.systemdatecolor, self.formatDate(self.viewStartDate, True)))
		else:
			self.setControlLabel(self.C_MAIN_DATE_LONG, self.formatDate(self.viewStartDate, True))
		for col in range(1, 5):
			if maycustom:
				self.setControlLabel(4000 + col, '[COLOR %s]%s[/COLOR]' % (self.guidetimecolor, self.formatTime(startTime)))
			else:
				self.setControlLabel(4000 + col, self.formatTime(startTime))
			startTime += HALF_HOUR

		if programs is None:
			self.onEPGLoadError()
			return

		if self.kek.channels is None or not self.kek.channels:
			self.kek.updatechnlist()

		# set channel logo or text
		showLogo = ADDON.getSetting('logos.enabled') == 'true'
		for idx in range(0, CHANNELS_PER_PAGE):
			if idx >= len(channels):
				self.setControlImage(4110 + idx, ' ')
				self.setControlLabel(4010 + idx, ' ')
			else:
				channel = channels[idx]
				if maycustom:
					self.setControlLabel(4010 + idx, '[COLOR %s]%s[/COLOR]' % (self.channelnamecolor, channel.title))
				else:
					self.setControlLabel(4010 + idx, channel.title)
				if (channel.logo is not None and showLogo == True):
					self.setControlImage(4110 + idx, channel.logo)
				else:
					self.setControlImage(4110 + idx, ' ')
		#display chn numbers
		if self.shownumbers:
			for idx in range(CHANNELS_PER_PAGE):
				if idx >= len(channels):
					self.setControlLabel(7001 + idx, ' ')
				else:
					channel = channels[idx]
					try:
						if maycustom:
							self.setControlLabel(7001 + idx, '[COLOR %s]%s[/COLOR]' % (self.channelnumbercolor, str(self.kek.getCurrentChannel(channel)+1)))
						else:
							self.setControlLabel(7001 + idx, str(self.kek.getCurrentChannel(channel)+1))
					except:
						self.setControlLabel(7001 + idx, ' ')

		#display cat
		if self.showcat:
			if maycustom:
				self.setControlLabel(self.C_MAIN_CAT, '[COLOR %s]%s[/COLOR]' % (self.catcolor, self.currentcategory))
			else:
				self.setControlLabel(self.C_MAIN_CAT, self.currentcategory)
					
		# enable or disable cpu/mem info          
		if self.showDebugInfo == True:
			self._hideControl(self.C_MAIN_CPUINFO)
			self._hideControl(self.C_MAIN_MEMINFO)
		else:
			self._showControl(self.C_MAIN_CPUINFO)
			self._showControl(self.C_MAIN_MEMINFO)


		for program in programs:
			idx = channels.index(program.channel)
			if program.channel in channelsWithoutPrograms:
				channelsWithoutPrograms.remove(program.channel)

			startDelta = program.startDate - self.viewStartDate
			stopDelta = program.endDate - self.viewStartDate

			cellStart = self._secondsToXposition(startDelta.seconds)
			if startDelta.days < 0:
				cellStart = self.epgView.left
			cellWidth = self._secondsToXposition(stopDelta.seconds) - cellStart
			if cellStart + cellWidth > self.epgView.right:
				cellWidth = self.epgView.right - cellStart

			if cellWidth > 1:
				if program.notificationScheduled:
					noFocusTexture = 'tvguide-program-red.png'
					focusTexture = 'tvguide-program-red-focus.png'
				else:
					noFocusTexture = 'tvguide-program-grey.png'
					focusTexture = 'tvguide-program-grey-focus.png'

				if cellWidth < 25:
					title = ''  # Text will overflow outside the button if it is too narrow
				else:
					title = program.title

				if maycustom and self.largetvlistingfont:
					control = xbmcgui.ControlButton(
						cellStart,
						self.epgView.top + self.epgView.cellHeight * idx,
						cellWidth - 2,
						self.epgView.cellHeight - 2,
						title,
						focusedColor=self.tvlistingprogramfocuscolor,
						textColor=self.tvlistingprogramnonfocuscolor,
						noFocusTexture=noFocusTexture,
						focusTexture=focusTexture,
						font='font30'
					)
				elif maycustom:
					control = xbmcgui.ControlButton(
						cellStart,
						self.epgView.top + self.epgView.cellHeight * idx,
						cellWidth - 2,
						self.epgView.cellHeight - 2,
						title,
						focusedColor=self.tvlistingprogramfocuscolor,
						textColor=self.tvlistingprogramnonfocuscolor,
						noFocusTexture=noFocusTexture,
						focusTexture=focusTexture,
					)
				elif self.largetvlistingfont:
					control = xbmcgui.ControlButton(
						cellStart,
						self.epgView.top + self.epgView.cellHeight * idx,
						cellWidth - 2,
						self.epgView.cellHeight - 2,
						title,
						focusedColor='ff000000',
						textColor='ff000000',
						noFocusTexture=noFocusTexture,
						focusTexture=focusTexture,
						font='font30'
					)
				else:
					control = xbmcgui.ControlButton(
						cellStart,
						self.epgView.top + self.epgView.cellHeight * idx,
						cellWidth - 2,
						self.epgView.cellHeight - 2,
						title,
						focusedColor='ff000000',
						textColor='ff000000',
						noFocusTexture=noFocusTexture,
						focusTexture=focusTexture
					)

				self.controlAndProgramList.append(ControlAndProgram(control, program))

		for channel in channelsWithoutPrograms:
			idx = channels.index(channel)
			if maycustom:
				control = xbmcgui.ControlButton(
					self.epgView.left,
					self.epgView.top + self.epgView.cellHeight * idx,
					(self.epgView.right - self.epgView.left) - 2,
					self.epgView.cellHeight - 2,
					strings(NO_PROGRAM_AVAILABLE),
					focusedColor=self.tvlistingprogramfocuscolor,
					textColor=self.tvlistingprogramnonfocuscolor,
					noFocusTexture='tvguide-program-grey.png',
					focusTexture='tvguide-program-grey-focus.png'
				)
			else:
				control = xbmcgui.ControlButton(
					self.epgView.left,
					self.epgView.top + self.epgView.cellHeight * idx,
					(self.epgView.right - self.epgView.left) - 2,
					self.epgView.cellHeight - 2,
					strings(NO_PROGRAM_AVAILABLE),
					focusedColor='ff000000',
					textColor='ff000000',
					noFocusTexture='tvguide-program-grey.png',
					focusTexture='tvguide-program-grey-focus.png'
				)

			program = src.Program(channel, strings(NO_PROGRAM_AVAILABLE), None, None, None)
			self.controlAndProgramList.append(ControlAndProgram(control, program))

		# add program controls
		if focusFunction is None:
			focusFunction = self._findControlAt
		focusControl = focusFunction(self.focusPoint)
		controls = [elem.control for elem in self.controlAndProgramList]
		try:
			self.addControls(controls)
		except:
			xbmc.sleep(50)
			return

		if focusControl is not None:
			debug('onRedrawEPG - setFocus %d' % focusControl.getId())
			self.setFocus(focusControl)

		self.ignoreMissingControlIds.extend([elem.control.getId() for elem in self.controlAndProgramList])

		if focusControl is None and len(self.controlAndProgramList) > 0:
			self.setFocus(self.controlAndProgramList[0].control)

		self._hideControl(self.C_MAIN_LOADING)
		self.redrawingEPG = False

	def _clearEpg(self):
		controls = [elem.control for elem in self.controlAndProgramList]
		try:
			xbmc.sleep(50)
			self.removeControls(controls)
		except:
			for elem in self.controlAndProgramList:
				try:
					xbmc.sleep(50)
					self.removeControl(elem.control)
				except:
					xbmc.sleep(50)
					#pass  # happens if we try to remove a control that doesn't exist
		del self.controlAndProgramList[:]

	def onEPGLoadError(self):
		self.redrawingEPG = False
		self._hideControl(self.C_MAIN_LOADING)
		xbmcgui.Dialog().ok(strings(LOAD_ERROR_TITLE), strings(LOAD_ERROR_LINE1), strings(LOAD_ERROR_LINE2))
		self.close()

	def onSourceNotConfigured(self):
		self.redrawingEPG = False
		self._hideControl(self.C_MAIN_LOADING)
		xbmcgui.Dialog().ok(strings(LOAD_ERROR_TITLE), strings(LOAD_ERROR_LINE1), strings(CONFIGURATION_ERROR_LINE2))
		self.close()

	def isSourceInitializationCancelled(self):
		return xbmc.abortRequested or self.isClosing

	def onSourceInitialized(self, success):
		if success:
			self.notification = Notification(self.database, ADDON.getAddonInfo('path'))
			self.onRedrawEPG(0, self.viewStartDate)

	def onSourceProgressUpdate(self, percentageComplete):
		control = self.getControl(self.C_MAIN_LOADING_PROGRESS)
		if percentageComplete < 1:
			if control:
				control.setPercent(1)
			self.progressStartTime = datetime.datetime.now()
			self.progressPreviousPercentage = percentageComplete
		elif percentageComplete != self.progressPreviousPercentage:
			if control:
				control.setPercent(percentageComplete)
			self.progressPreviousPercentage = percentageComplete
			delta = datetime.datetime.now() - self.progressStartTime

			if percentageComplete < 20:
				self.setControlLabel(self.C_MAIN_LOADING_TIME_LEFT, strings(CALCULATING_REMAINING_TIME))
			else:
				secondsLeft = int(delta.seconds) / float(percentageComplete) * (100.0 - percentageComplete)
				if secondsLeft > 30:
					secondsLeft -= secondsLeft % 10
				self.setControlLabel(self.C_MAIN_LOADING_TIME_LEFT, strings(TIME_LEFT) % secondsLeft)
		if self.database.updateInProgress == True:
			if self.addonupdated == False:
				del self.streamingService
				self.streamingService = streaming.StreamsService(ADDON)
				self.addonupdated = True
			else:
				pass

		return not xbmc.abortRequested and not self.isClosing

	def onPlayBackStopped(self):
		if not self.player.isPlaying() and not self.isClosing and not self.PlayBackStopped and not self.channelswitch:
			self.PlayBackStopped = True
			self._hideControl(self.C_MAIN_OSD)
			self.viewStartDate = datetime.datetime.today()
			self.viewStartDate -= datetime.timedelta(minutes = self.viewStartDate.minute % 30, seconds = self.viewStartDate.second)
			self.focusPoint.y = self.epgView.top
			self.currentcategory = ADDON.getSetting('last.category')
			self.channelIdx = self.kek.getCurrentChannel(self.currentChannel, category=self.currentcategory)
			xbmc.sleep(350)
			self.onRedrawEPG(self.channelIdx, self.viewStartDate)
			self.PlayBackStopped = False
			return

	def _secondsToXposition(self, seconds):
		return self.epgView.left + (seconds * self.epgView.width / 7200)

	def _findControlOnRight(self, point):
		distanceToNearest = 10000
		nearestControl = None

		for elem in self.controlAndProgramList:
			control = elem.control
			(left, top) = control.getPosition()
			x = left + (control.getWidth() / 2)
			y = top + (control.getHeight() / 2)

			if point.x < x and point.y == y:
				distance = abs(point.x - x)
				if distance < distanceToNearest:
					distanceToNearest = distance
					nearestControl = control

		return nearestControl

	def _findControlOnLeft(self, point):
		distanceToNearest = 10000
		nearestControl = None

		for elem in self.controlAndProgramList:
			control = elem.control
			(left, top) = control.getPosition()
			x = left + (control.getWidth() / 2)
			y = top + (control.getHeight() / 2)

			if point.x > x and point.y == y:
				distance = abs(point.x - x)
				if distance < distanceToNearest:
					distanceToNearest = distance
					nearestControl = control

		return nearestControl

	def _findControlBelow(self, point):
		nearestControl = None

		for elem in self.controlAndProgramList:
			control = elem.control
			(leftEdge, top) = control.getPosition()
			y = top + (control.getHeight() / 2)

			if point.y < y:
				rightEdge = leftEdge + control.getWidth()
				if leftEdge <= point.x < rightEdge and (nearestControl is None or nearestControl.getPosition()[1] > top):
					nearestControl = control

		return nearestControl

	def _findControlAbove(self, point):
		nearestControl = None
		for elem in self.controlAndProgramList:
			control = elem.control
			(leftEdge, top) = control.getPosition()
			y = top + (control.getHeight() / 2)

			if point.y > y:
				rightEdge = leftEdge + control.getWidth()
				if leftEdge <= point.x < rightEdge and (nearestControl is None or nearestControl.getPosition()[1] < top):
					nearestControl = control

		return nearestControl

	def _findControlAt(self, point):
		for elem in self.controlAndProgramList:
			control = elem.control
			(left, top) = control.getPosition()
			bottom = top + control.getHeight()
			right = left + control.getWidth()

			if left <= point.x <= right and top <= point.y <= bottom:
				return control

		return None

	def _getProgramFromControl(self, control):
		for elem in self.controlAndProgramList:
			if elem.control == control:
				return elem.program
		return None

	def _hideControl(self, *controlIds):
		"""
		Visibility is inverted in skin
		"""
		for controlId in controlIds:
			control = self.getControl(controlId)
			if control:
				control.setVisible(True)

	def _showControl(self, *controlIds):
		"""
		Visibility is inverted in skin
		"""
		for controlId in controlIds:
			control = self.getControl(controlId)
			if control:
				control.setVisible(False)

	def formatTime(self, timestamp):
		if timestamp:
			format = xbmc.getRegion('time').replace(':%S', '').replace('%H%H', '%H')
			return timestamp.strftime(format)
		else:
			return ''

	def formatDate(self, timestamp, longdate=False):
		if timestamp:
			if longdate == True:
				format = xbmc.getRegion('datelong')
			else:
				format = xbmc.getRegion('dateshort')
			return timestamp.strftime(format)
		else:
			return ''

	def setControlImage(self, controlId, image):
		control = self.getControl(controlId)
		if control:
			control.setImage(image.encode('utf-8'))

	def setControlLabel(self, controlId, label):
		control = self.getControl(controlId)
		if control and label:
			control.setLabel(label)

	def setControlText(self, controlId, text):
		control = self.getControl(controlId)
		if control:
			control.setText(text)

	def updateTimebar(self, scheduleTimer=True):
		# move timebar to current time
		timeDelta = datetime.datetime.today() - self.viewStartDate
		control = self.getControl(self.C_MAIN_TIMEBAR)
		if control:
			(x, y) = control.getPosition()
			try:
				# Sometimes raises:
				# exceptions.RuntimeError: Unknown exception thrown from the call "setVisible"
				control.setVisible(timeDelta.days == 0)
			except:
				pass
			control.setPosition(self._secondsToXposition(timeDelta.seconds), y)

		if scheduleTimer and not xbmc.abortRequested and not self.isClosing:
			threading.Timer(1, self.updateTimebar).start()


class PopupMenu(xbmcgui.WindowXMLDialog):
	C_POPUP_PLAY = 4000
	C_POPUP_CHOOSE_STREAM = 4001
	C_POPUP_REMIND = 4002
	C_POPUP_CHANNELS = 4003
	C_POPUP_QUIT = 4004
	C_POPUP_PLAY_BEGINNING = 4005
	C_POPUP_CHANNEL_LOGO = 4100
	C_POPUP_CHANNEL_TITLE = 4101
	C_POPUP_PROGRAM_TITLE = 4102
	C_POPUP_LIBMOV = 80000
	C_POPUP_LIBTV = 80001
	C_POPUP_VIDEOADDONS = 80002
	C_POPUP_SETTINGS = 30450
	C_POPUP_CATEGORIES = 30441
	C_POPUP_MTVSHOW = 99874
	C_POPUP_MMOVIE  = 99875
	C_POP_ADD_FAV   = 99872
	C_POP_DEL_FAV   = 99873

	# Custom addons in menu tab
	C_POPUP_ADDON1 = 30010
	C_POPUP_ADDON2 = 30011
	C_POPUP_ADDON3 = 30012	
	
	def __new__(cls, database, program, showRemind, i):
		# Skin in resources
		#return super(PopupMenu, cls).__new__(cls, 'script-tvguide-menu.xml', ADDON.getAddonInfo('path'), SKIN)
		# Skin in user settings
		return super(PopupMenu, cls).__new__(cls, 'script-tvguide-menu.xml', SKINdir, SKIN)

	def __init__(self, database, program, showRemind, i):
		"""

		@type database: source.Database
		@param program:
		@type program: source.Program
		@param showRemind:
		"""
		super(PopupMenu, self).__init__()
		self.database = database
		self.program = program
		self.showRemind = showRemind
		self.buttonClicked = None
		self.i = i
		self.menubuttonscolor = re.search(r"\[COLOR ([A-Za-z0-9_]+)\]", ADDON.getSetting('menu.buttons.color')).group(1)

	def onInit(self):
		categoriesControl = self.getControl(self.C_POPUP_CATEGORIES)
		programPlayBeginningControl = self.getControl(self.C_POPUP_PLAY_BEGINNING)
		remindControl = self.getControl(self.C_POPUP_REMIND)
		chooseStrmControl = self.getControl(self.C_POPUP_CHOOSE_STREAM)
		channelsControl = self.getControl(self.C_POPUP_CHANNELS)
		settingsControl = self.getControl(self.C_POPUP_SETTINGS)
		mtvshowsControl  = self.getControl(self.C_POPUP_MTVSHOW)
		mmovieControl = self.getControl(self.C_POPUP_MMOVIE)
		playControl = self.getControl(self.C_POPUP_PLAY)
		channelLogoControl = self.getControl(self.C_POPUP_CHANNEL_LOGO)
		channelTitleControl = self.getControl(self.C_POPUP_CHANNEL_TITLE)
		programTitleControl = self.getControl(self.C_POPUP_PROGRAM_TITLE)
		AddFavControl = self.getControl(self.C_POP_ADD_FAV)
		DelFavControl = self.getControl(self.C_POP_DEL_FAV)

		if 'Favourites' in self.database.getChannelFavs(self.program.channel):
			AddFavControl.setVisible(False)
		else:
			DelFavControl.setVisible(False)

		playControl.setLabel(strings(WATCH_CHANNEL, self.program.channel.title))
		if not self.program.channel.isPlayable():
			playControl.setEnabled(False)
			self.setFocusId(self.C_POPUP_CHOOSE_STREAM)
		if self.database.getCustomStreamUrl(self.program.channel):
			if maycustom:
				chooseStrmControl.setLabel("[COLOR %s]%s[/COLOR]" % (self.menubuttonscolor, strings(REMOVE_STRM_FILE)))
			else:
				chooseStrmControl.setLabel(strings(REMOVE_STRM_FILE))
		else:
			if maycustom:
				chooseStrmControl.setLabel("[COLOR %s]%s[/COLOR]" % (self.menubuttonscolor, strings(CHOOSE_STRM_FILE)))
			else:
				chooseStrmControl.setLabel(strings(CHOOSE_STRM_FILE))

		if self.program.channel.logo is not None:
			channelLogoControl.setImage(self.program.channel.logo)
			channelTitleControl.setVisible(False)
		else:
			channelTitleControl.setLabel(self.program.channel.title)
			channelLogoControl.setVisible(False)

		programTitleControl.setLabel(self.program.title)

		if self.program.startDate:
			remindControl.setEnabled(True)
			if self.showRemind:
				if maycustom:
					remindControl.setLabel("[COLOR %s]%s[/COLOR]" % (self.menubuttonscolor, strings(REMIND_PROGRAM)))
				else:
					remindControl.setLabel(strings(REMIND_PROGRAM))
			else:
				if maycustom:
					remindControl.setLabel("[COLOR %s]%s[/COLOR]" % (self.menubuttonscolor, strings(DONT_REMIND_PROGRAM)))
				else:
					remindControl.setLabel(strings(DONT_REMIND_PROGRAM))
		else:
			remindControl.setEnabled(False)

		if maycustom:
			categoriesControl.setLabel("[COLOR %s]%s[/COLOR]" % (self.menubuttonscolor, "Categories"))
			programPlayBeginningControl.setLabel("[COLOR %s]%s[/COLOR]" % (self.menubuttonscolor, "Watch from beginning"))
			channelsControl.setLabel("[COLOR %s]%s[/COLOR]" % (self.menubuttonscolor, strings(CHANNELS)))
			settingsControl.setLabel("[COLOR %s]%s[/COLOR]" % (self.menubuttonscolor, "Settings"))
			mtvshowsControl.setLabel("[COLOR %s]%s[/COLOR]" % (self.menubuttonscolor, "Search TV Shows"))
			mmovieControl.setLabel("[COLOR %s]%s[/COLOR]" % (self.menubuttonscolor, "Search Movies"))

	def onAction(self, action):
		if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK, KEY_CONTEXT_MENU]:
			if self.i.player.isPlaying():
				self.i._hideEpg()
			self.close()
			return

	def onClick(self, controlId):
		if controlId == self.C_POPUP_CHOOSE_STREAM and self.database.getCustomStreamUrl(self.program.channel):
			self.database.deleteCustomStreamUrl(self.program.channel)
			chooseStrmControl = self.getControl(self.C_POPUP_CHOOSE_STREAM)
			if maycustom:
				chooseStrmControl.setLabel("[COLOR %s]%s[/COLOR]" % (self.menubuttonscolor, strings(CHOOSE_STRM_FILE)))
			else:
				chooseStrmControl.setLabel(strings(CHOOSE_STRM_FILE))

			if not self.program.channel.isPlayable():
				playControl = self.getControl(self.C_POPUP_PLAY)
				playControl.setEnabled(False)

		elif controlId == self.C_POPUP_CATEGORIES:
			guideList = []
			gTypes = guideTypes.GuideTypes()
			for gType in gTypes.guideTypes:
				guideList.append(gType[gTypes.GUIDE_NAME])
			d = xbmcgui.Dialog()
			ret = d.select('Select channel category', guideList)
			if ret >= 0:
				guideId = gTypes.guideTypes[ret][gTypes.GUIDE_ID]
				typeId = str(guideId)
				typeName = gTypes.getGuideDataItem(guideId, gTypes.GUIDE_NAME)
				ver = guideTypes.getKodiVersion()
				if xbmc.getCondVisibility('system.platform.android') and int(ver) < 15:
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
				else:
					if typeId == '6':
						ADDON.setSetting('xmltv.type', typeId)
						ADDON.setSetting('xmltv.type_select', typeName)
					else:
						ADDON.setSetting('last.category', typeName)
						instance.currentcategory = ADDON.getSetting('last.category')
						instance.viewStartDate = datetime.datetime.today()
						instance.viewStartDate -= datetime.timedelta(minutes = instance.viewStartDate.minute % 30, seconds = instance.viewStartDate.second)
						instance.focusPoint.y = instance.epgView.top
						instance.channelIdx = 0
						instance.onRedrawEPG(instance.channelIdx, instance.viewStartDate)
			self.close()
		elif controlId == self.C_POP_ADD_FAV:
			self.database.addChannelFav(self.program.channel)
			xbmcgui.Dialog().notification('[COLOR red]Reloaded TV Guide[/COLOR]', '[COLOR limegreen]Added[/COLOR] [COLOR gold]%s[/COLOR] [COLOR white]to Favourites![/COLOR]' % self.program.channel.id, xbmcgui.NOTIFICATION_INFO, 3500)
			self.close()
		elif controlId == self.C_POP_DEL_FAV:
			self.database.delChannelFav(self.program.channel)
			xbmcgui.Dialog().notification('[COLOR red]Reloaded TV Guide[/COLOR]', '[COLOR red]Removed[/COLOR] [COLOR gold]%s[/COLOR] [COLOR white]from Favourites![/COLOR]' % self.program.channel.id, xbmcgui.NOTIFICATION_INFO, 3500)
			self.i.onRedrawEPG(self.i.channelIdx, self.i.viewStartDate)
			self.close()
		else:
			self.buttonClicked = controlId
			self.close()

	def onFocus(self, controlId):
		pass


class ChannelsMenu(xbmcgui.WindowXMLDialog):
	C_CHANNELS_LIST = 6000
	C_CHANNELS_SELECTION_VISIBLE = 6001
	C_CHANNELS_SELECTION = 6002
	C_CHANNELS_SAVE = 6003
	C_CHANNELS_CANCEL = 6004

	def __new__(cls, database):
		# Skin in resources
		#return super(ChannelsMenu, cls).__new__(cls, 'script-tvguide-channels.xml', ADDON.getAddonInfo('path'), SKIN)
		# Skin in user settings
		return super(ChannelsMenu, cls).__new__(cls, 'script-tvguide-channels.xml', SKINdir, SKIN)
	def __init__(self, database):
		"""

		@type database: source.Database
		"""
		super(ChannelsMenu, self).__init__()
		self.database = database
		self.channelList = database.getChannelList(onlyVisible=False)
		self.swapInProgress = False
		
		self.selectedChannel = 0

	def onInit(self):
		self.updateChannelList()
		self.setFocusId(self.C_CHANNELS_LIST)

	def onAction(self, action):
		if action.getId() in [ACTION_PARENT_DIR, KEY_NAV_BACK]:
			self.close()
			return

		if self.getFocusId() == self.C_CHANNELS_LIST and action.getId() in [ACTION_PREVIOUS_MENU, KEY_CONTEXT_MENU, ACTION_LEFT]:
			listControl = self.getControl(self.C_CHANNELS_LIST)
			idx = listControl.getSelectedPosition()
			self.selectedChannel = idx
			buttonControl = self.getControl(self.C_CHANNELS_SELECTION)
			buttonControl.setLabel('[B]%s[/B]' % self.channelList[idx].title)

			self.getControl(self.C_CHANNELS_SELECTION_VISIBLE).setVisible(False)
			self.setFocusId(self.C_CHANNELS_SELECTION)

		elif self.getFocusId() == self.C_CHANNELS_SELECTION and action.getId() in [ACTION_RIGHT, ACTION_SELECT_ITEM]:
			self.getControl(self.C_CHANNELS_SELECTION_VISIBLE).setVisible(True)
			xbmc.sleep(350)
			self.setFocusId(self.C_CHANNELS_LIST)
			
		elif self.getFocusId() == self.C_CHANNELS_SELECTION and action.getId() in [ACTION_PREVIOUS_MENU, KEY_CONTEXT_MENU]:
			listControl = self.getControl(self.C_CHANNELS_LIST)
			idx = listControl.getSelectedPosition()
			self.swapChannels(self.selectedChannel, idx)
			self.getControl(self.C_CHANNELS_SELECTION_VISIBLE).setVisible(True)
			xbmc.sleep(350)
			self.setFocusId(self.C_CHANNELS_LIST)

		elif self.getFocusId() == self.C_CHANNELS_SELECTION and action.getId() == ACTION_UP:
			listControl = self.getControl(self.C_CHANNELS_LIST)
			idx = listControl.getSelectedPosition()
			if idx > 0:
				self.swapChannels(idx, idx - 1)

		elif self.getFocusId() == self.C_CHANNELS_SELECTION and action.getId() == ACTION_DOWN:
			listControl = self.getControl(self.C_CHANNELS_LIST)
			idx = listControl.getSelectedPosition()
			if idx < listControl.size() - 1:
				self.swapChannels(idx, idx + 1)

	def onClick(self, controlId):
		if controlId == self.C_CHANNELS_LIST:
			listControl = self.getControl(self.C_CHANNELS_LIST)
			item = listControl.getSelectedItem()
			channel = self.channelList[int(item.getProperty('idx'))]
			channel.visible = not channel.visible

			if channel.visible:
				iconImage = 'tvguide-channel-visible.png'
			else:
				iconImage = 'tvguide-channel-hidden.png'
			item.setIconImage(iconImage)

		elif controlId == self.C_CHANNELS_SAVE:
			self.database.saveChannelList(self.close, self.channelList)

		elif controlId == self.C_CHANNELS_CANCEL:
			self.close()

	def onFocus(self, controlId):
		pass

	def updateChannelList(self):
		listControl = self.getControl(self.C_CHANNELS_LIST)
		listControl.reset()
		for idx, channel in enumerate(self.channelList):
			if channel.visible:
				iconImage = 'tvguide-channel-visible.png'
			else:
				iconImage = 'tvguide-channel-hidden.png'

			item = xbmcgui.ListItem('%3d. %s' % (idx + 1, channel.title), iconImage=iconImage)
			item.setProperty('idx', str(idx))
			listControl.addItem(item)

	def updateListItem(self, idx, item):
		channel = self.channelList[idx]
		item.setLabel('%3d. %s' % (idx + 1, channel.title))

		if channel.visible:
			iconImage = 'tvguide-channel-visible.png'
		else:
			iconImage = 'tvguide-channel-hidden.png'
		item.setIconImage(iconImage)
		item.setProperty('idx', str(idx))

	def swapChannels(self, fromIdx, toIdx):
		if self.swapInProgress:
			return
		self.swapInProgress = True

		c = self.channelList[fromIdx]
		self.channelList[fromIdx] = self.channelList[toIdx]
		self.channelList[toIdx] = c

		# recalculate weight
		for idx, channel in enumerate(self.channelList):
			channel.weight = idx

		listControl = self.getControl(self.C_CHANNELS_LIST)
		self.updateListItem(fromIdx, listControl.getListItem(fromIdx))
		self.updateListItem(toIdx, listControl.getListItem(toIdx))

		listControl.selectItem(toIdx)
		xbmc.sleep(50)
		self.swapInProgress = False

class StreamSetupDialog(xbmcgui.WindowXMLDialog):
	C_STREAM_STRM_TAB = 101
	C_STREAM_FAVOURITES_TAB = 102
	C_STREAM_ADDONS_TAB = 103
	C_STREAM_STRM_BROWSE = 1001
	C_STREAM_STRM_FILE_LABEL = 1005
	C_STREAM_STRM_PREVIEW = 1002
	C_STREAM_STRM_OK = 1003
	C_STREAM_STRM_CANCEL = 1004
	C_STREAM_FAVOURITES = 2001
	C_STREAM_FAVOURITES_PREVIEW = 2002
	C_STREAM_FAVOURITES_OK = 2003
	C_STREAM_FAVOURITES_CANCEL = 2004
	C_STREAM_ADDONS = 3001
	C_STREAM_ADDONS_STREAMS = 3002
	C_STREAM_ADDONS_NAME = 3003
	C_STREAM_ADDONS_DESCRIPTION = 3004
	C_STREAM_ADDONS_PREVIEW = 3005
	C_STREAM_ADDONS_OK = 3006
	C_STREAM_ADDONS_CANCEL = 3007

	C_STREAM_VISIBILITY_MARKER = 100

	VISIBLE_STRM = 'strm'
	VISIBLE_FAVOURITES = 'favourites'
	VISIBLE_ADDONS = 'addons'

	def __new__(cls, database, channel):
		# Skin in resources
		#return super(StreamSetupDialog, cls).__new__(cls, 'script-tvguide-streamsetup.xml', ADDON.getAddonInfo('path'), SKIN)
		# Skin in user settings
		return super(StreamSetupDialog, cls).__new__(cls, 'script-tvguide-streamsetup.xml', SKINdir, SKIN)
		
	def __init__(self, database, channel):
		"""
		@type database: source.Database
		@type channel:source.Channel
		"""
		super(StreamSetupDialog, self).__init__()
		self.database = database
		self.channel = channel

		self.player = xbmc.Player()
		self.previousAddonId = None
		self.strmFile = None
		self.streamingService = streaming.StreamsService(ADDON)

	def close(self):
		if self.player.isPlaying():
			# Custom
			self.player.stop()
			print ''
		super(StreamSetupDialog, self).close()

	def onInit(self):
		self.getControl(self.C_STREAM_VISIBILITY_MARKER).setLabel(self.VISIBLE_STRM)

		favourites = self.streamingService.loadFavourites()
		items = list()
		for label, value in favourites:
			item = xbmcgui.ListItem(label)
			item.setProperty('stream', value)
			items.append(item)

		listControl = self.getControl(StreamSetupDialog.C_STREAM_FAVOURITES)
		items = sorted(items, key=lambda x: x.getLabel())
		listControl.addItems(items)

		items = list()
		for id in self.streamingService.getAddons():
			try:
				addon = xbmcaddon.Addon(id) # raises Exception if addon is not installed
				if id == base64.b64decode('cGx1Z2luLnByb2dyYW0ubXR2Z3VpZGVwcm8='):
					item = xbmcgui.ListItem('[COLOR white]Reloaded[COLOR red] TV[/COLOR]', iconImage=os.path.join(RESOURCES, 'png', 'Reloaded TV.png'))
				else:
					item = xbmcgui.ListItem(addon.getAddonInfo('name'), iconImage=addon.getAddonInfo('icon'))
				item.setProperty('addon_id', id)
				items.append(item)
			except Exception:
				pass
		listControl = self.getControl(StreamSetupDialog.C_STREAM_ADDONS)
		listControl.addItems(items)
		self.updateAddonInfo()

	def onAction(self, action):
		if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK, KEY_CONTEXT_MENU]:
			self.close()
			return

		elif self.getFocusId() == self.C_STREAM_ADDONS:
			self.updateAddonInfo()

	def onClick(self, controlId):
		if controlId == self.C_STREAM_STRM_BROWSE:
			stream = xbmcgui.Dialog().browse(1, ADDON.getLocalizedString(30304), 'video', '.strm')
			if stream:
				self.database.setCustomStreamUrl(self.channel, stream)
				self.getControl(self.C_STREAM_STRM_FILE_LABEL).setText(stream)
				self.strmFile = stream

		elif controlId == self.C_STREAM_ADDONS_OK:
			listControl = self.getControl(self.C_STREAM_ADDONS_STREAMS)
			item = listControl.getSelectedItem()
			if item:
				stream = item.getProperty('stream')
				addon_id = item.getProperty('addon_id')
				if addon_id == 'plugin.program.reloadedtv':
					stream = stream.replace('reloadedemail@email.com', urllib.quote_plus(ADDON.getSetting('reloaded.user')))
					stream = stream.replace('reloadedpass', urllib.quote_plus(ADDON.getSetting('reloaded.pass')))
				if addon_id == 'plugin.video.dex':
					dexaddon = xbmcaddon.Addon('plugin.video.dex')
					stream = stream.replace(urllib.quote_plus('dexter@email.com'), urllib.quote_plus(dexaddon.getSetting('kasutajanimi')))
					stream = stream.replace(urllib.quote_plus('dexterpassword'), urllib.quote_plus(dexaddon.getSetting('salasona')))
				if addon_id == 'plugin.video.ottalpha':
					OTTTVaddon = xbmcaddon.Addon('plugin.video.ottalpha')
					stream = stream.replace(urllib.quote_plus('otttv@email.com'), urllib.quote_plus(OTTTVaddon.getSetting('Username')))
					stream = stream.replace(urllib.quote_plus('otttvpassword'), urllib.quote_plus(OTTTVaddon.getSetting('Password')))
					if ADDON.getSetting('OTTTV.format') == 'ts':
						if not OTTTVaddon.getSetting('extend') == 'ts':
							OTTTVaddon.setSetting(id = 'extend', value = 'ts')
						stream = stream.replace('.m3u8','.ts')
					elif ADDON.getSetting('OTTTV.format') == 'rtmp':
						if not OTTTVaddon.getSetting('extend') == 'rtmp':
							OTTTVaddon.setSetting(id = 'extend', value = 'rtmp')
						stream = stream.replace('.m3u8','.rtmp')
					else:
						if not OTTTVaddon.getSetting('extend') == 'm3u8':
							OTTTVaddon.setSetting(id = 'extend', value = 'm3u8')
				if addon_id == 'plugin.video.suicidetv21':
					suicide21addon = xbmcaddon.Addon('plugin.video.suicidetv21')
					stream = stream.replace(urllib.quote_plus('suicide@email.com'), urllib.quote_plus(suicide21addon.getSetting('Username')))
					stream = stream.replace(urllib.quote_plus('suicidepassword'), urllib.quote_plus(suicide21addon.getSetting('Password')))
					if ADDON.getSetting('suicide21.format') == 'ts':
						if not suicide21addon.getSetting('extend') == 'ts':
							suicide21addon.setSetting(id = 'extend', value = 'ts')
						stream = stream.replace('.m3u8','.ts')
					elif ADDON.getSetting('suicide21.format') == 'rtmp':
						if not suicide21addon.getSetting('extend') == 'rtmp':
							suicide21addon.setSetting(id = 'extend', value = 'rtmp')
						stream = stream.replace('.m3u8','.rtmp')
					else:
						if not suicide21addon.getSetting('extend') == 'm3u8':
							suicide21addon.setSetting(id = 'extend', value = 'm3u8')
				self.database.setCustomStreamUrl(self.channel, stream)
			self.close()

		elif controlId == self.C_STREAM_FAVOURITES_OK:
			listControl = self.getControl(self.C_STREAM_FAVOURITES)
			item = listControl.getSelectedItem()
			if item:
				stream = item.getProperty('stream')
				self.database.setCustomStreamUrl(self.channel, stream)
			self.close()

		elif controlId == self.C_STREAM_STRM_OK:
			self.database.setCustomStreamUrl(self.channel, self.strmFile)
			self.close()

		elif controlId in [self.C_STREAM_ADDONS_CANCEL, self.C_STREAM_FAVOURITES_CANCEL, self.C_STREAM_STRM_CANCEL]:
			self.close()

		elif controlId in [self.C_STREAM_ADDONS_PREVIEW, self.C_STREAM_FAVOURITES_PREVIEW, self.C_STREAM_STRM_PREVIEW]:
			if self.player.isPlaying():
				# Custom no stop
				self.player.stop()
				self.getControl(self.C_STREAM_ADDONS_PREVIEW).setLabel(strings(PREVIEW_STREAM))
				self.getControl(self.C_STREAM_FAVOURITES_PREVIEW).setLabel(strings(PREVIEW_STREAM))
				self.getControl(self.C_STREAM_STRM_PREVIEW).setLabel(strings(PREVIEW_STREAM))
				return

			stream = None
			visible = self.getControl(self.C_STREAM_VISIBILITY_MARKER).getLabel()
			if visible == self.VISIBLE_ADDONS:
				listControl = self.getControl(self.C_STREAM_ADDONS_STREAMS)
				item = listControl.getSelectedItem()
				if item:
					stream = item.getProperty('stream')
			elif visible == self.VISIBLE_FAVOURITES:
				listControl = self.getControl(self.C_STREAM_FAVOURITES)
				item = listControl.getSelectedItem()
				if item:
					stream = item.getProperty('stream')
			elif visible == self.VISIBLE_STRM:
				stream = self.strmFile

			if stream is not None:
				self.player.play(item=stream, windowed=True)
				if self.player.isPlaying():
					self.getControl(self.C_STREAM_ADDONS_PREVIEW).setLabel(strings(STOP_PREVIEW))
					self.getControl(self.C_STREAM_FAVOURITES_PREVIEW).setLabel(strings(STOP_PREVIEW))
					self.getControl(self.C_STREAM_STRM_PREVIEW).setLabel(strings(STOP_PREVIEW))

	def onFocus(self, controlId):
		if controlId == self.C_STREAM_STRM_TAB:
			self.getControl(self.C_STREAM_VISIBILITY_MARKER).setLabel(self.VISIBLE_STRM)
		elif controlId == self.C_STREAM_FAVOURITES_TAB:
			self.getControl(self.C_STREAM_VISIBILITY_MARKER).setLabel(self.VISIBLE_FAVOURITES)
		elif controlId == self.C_STREAM_ADDONS_TAB:
			self.getControl(self.C_STREAM_VISIBILITY_MARKER).setLabel(self.VISIBLE_ADDONS)

	def updateAddonInfo(self):
		listControl = self.getControl(self.C_STREAM_ADDONS)
		item = listControl.getSelectedItem()
		if item is None:
			return

		if item.getProperty('addon_id') == self.previousAddonId:
			return

		self.previousAddonId = item.getProperty('addon_id')
		addon = xbmcaddon.Addon(id=item.getProperty('addon_id'))
		self.getControl(self.C_STREAM_ADDONS_NAME).setLabel('[B]%s[/B]' % addon.getAddonInfo('name'))
		self.getControl(self.C_STREAM_ADDONS_DESCRIPTION).setText(addon.getAddonInfo('description'))

		streams = self.streamingService.getAddonStreams(item.getProperty('addon_id'))
		items = list()
		for (label, stream) in streams:
			label = label.decode("hex")
			label = base64.b64decode(label)
			stream = stream.decode("hex")
			stream = base64.b64decode(stream)
			addon_id = item.getProperty('addon_id')
			if item.getProperty('addon_id') == "plugin.video.meta":
				label = self.channel.title
				stream = stream.replace("<channel>", self.channel.title.replace(" ","%20"))
			item = xbmcgui.ListItem(label)
			item.setProperty('stream', stream)
			item.setProperty('addon_id', addon_id)
			items.append(item)
		listControl = self.getControl(StreamSetupDialog.C_STREAM_ADDONS_STREAMS)
		listControl.reset()
		items = sorted(items, key=lambda x: x.getLabel())
		listControl.addItems(items)


class ChooseStreamAddonDialog(xbmcgui.WindowXMLDialog):
	C_SELECTION_LIST = 1000

	def __new__(cls, addons):
		# Skin in resources
		#return super(ChooseStreamAddonDialog, cls).__new__(cls, 'script-tvguide-streamaddon.xml', ADDON.getAddonInfo('path'), SKIN)
		# Skin in user settings
		return super(ChooseStreamAddonDialog, cls).__new__(cls, 'script-tvguide-streamaddon.xml', SKINdir, SKIN)
		
	def __init__(self, addons):
		super(ChooseStreamAddonDialog, self).__init__()
		self.addons = addons
		self.stream = None

	'''
	def onInit(self):
		items = list()
		for id, label, url in self.addons:
			addon = xbmcaddon.Addon(id)

			item = xbmcgui.ListItem(label, addon.getAddonInfo('name'), addon.getAddonInfo('icon'))
			item.setProperty('stream', url)
			items.append(item)

		listControl = self.getControl(ChooseStreamAddonDialog.C_SELECTION_LIST)
		listControl.addItems(items)

		self.setFocus(listControl)
	'''

	# Custom Players
	def onInit(self):    
 
		items = list()
		for id, label, url in self.addons:
			'''
			addon = xbmcaddon.Addon(id)
			item = xbmcgui.ListItem(label, addon.getAddonInfo('name'), addon.getAddonInfo('icon'))
			item.setProperty('stream', url)
			items.append(item)
			'''
			try:

				#elif id == 'kodi-favourite':
				if id == 'kodi-favourite':
					icon = os.path.join(RESOURCES, 'png', 'favourite.png')
					name = ''

				elif id == 'iptv-playlist':
					icon = os.path.join(RESOURCES, 'png', 'playlist.png')
					name = ''

				elif id == 'pvr.iptvsimple':
					#icon = os.path.join(RESOURCES, 'png', 'pvrsimple.png')
					icon = os.path.join(RESOURCES, 'png', 'pvr.png')
					name = ''

				elif id == base64.b64decode('cGx1Z2luLnByb2dyYW0ubXR2Z3VpZGVwcm8='):
					#icon = os.path.join(RESOURCES, 'png', 'pvrsimple.png')
					icon = os.path.join(RESOURCES, 'png', base64.b64decode('UmVsb2FkZWQgVFYucG5n'))
					name = ''

				else:
					addon = xbmcaddon.Addon(id)
					icon  = addon.getAddonInfo('icon')
					name  = addon.getAddonInfo('name')

				if not name:
					name = label
				if not icon:
					icon = ''
				
				#addon = xbmcaddon.Addon(id)
				item = xbmcgui.ListItem(label, name, icon)
				item.setProperty('stream', url)
				items.append(item)

			except:
				pass

				#addon = xbmcaddon.Addon(id)
				item = xbmcgui.ListItem(label, '', id)
				item.setProperty('stream', url)
				items.append(item) 

		listControl = self.getControl(ChooseStreamAddonDialog.C_SELECTION_LIST)
		listControl.addItems(items)

		self.setFocus(listControl)





	def onAction(self, action):
		if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK]:
			self.close()

	def onClick(self, controlId):
		if controlId == ChooseStreamAddonDialog.C_SELECTION_LIST:
			listControl = self.getControl(ChooseStreamAddonDialog.C_SELECTION_LIST)
			self.stream = listControl.getSelectedItem().getProperty('stream')
			self.close()

	def onFocus(self, controlId):
		pass
