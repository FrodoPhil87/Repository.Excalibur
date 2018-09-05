# coding: UTF-8
import sys
l111l_opy_ = sys.version_info [0] == 2
l1lll1_opy_ = 2048
l1lll_opy_ = 7
def l11l1_opy_ (ll_opy_):
	global l1111_opy_
	l1l111_opy_ = ord (ll_opy_ [-1])
	l11ll_opy_ = ll_opy_ [:-1]
	l1ll_opy_ = l1l111_opy_ % len (l11ll_opy_)
	l1l1_opy_ = l11ll_opy_ [:l1ll_opy_] + l11ll_opy_ [l1ll_opy_:]
	if l111l_opy_:
		l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - l1lll1_opy_ - (l1l11_opy_ + l1l111_opy_) % l1lll_opy_) for l1l11_opy_, char in enumerate (l1l1_opy_)])
	else:
		l1ll1l_opy_ = str () .join ([chr (ord (char) - l1lll1_opy_ - (l1l11_opy_ + l1l111_opy_) % l1lll_opy_) for l1l11_opy_, char in enumerate (l1l1_opy_)])
	return eval (l1ll1l_opy_)
import datetime
import time
import sqlite3
import os
import xbmcaddon
import xbmc
import xbmcgui
from source import Program
from source import Channel
import gui
import kappa
import urllib
import re
import urlparse
import base64
import lolol
import threading
import requests
import hashlib
import cfscrape
import sys
import json
ADDON = xbmcaddon.Addon(id=l11l1_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡲࡵࡳ࡬ࡸࡡ࡮࠰ࡵࡩࡱࡵࡡࡥࡧࡧࡸࡻ࠭৙"))
addon_id = l11l1_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡳࡶࡴ࡭ࡲࡢ࡯࠱ࡶࡪࡲ࡯ࡢࡦࡨࡨࡹࡼࠧ৚")
profilePath = xbmc.translatePath(ADDON.getAddonInfo(l11l1_opy_ (u"ࠪࡴࡷࡵࡦࡪ࡮ࡨࠫ৛")))
HOME        =  ADDON.getAddonInfo(l11l1_opy_ (u"ࠫࡵࡧࡴࡩࠩড়"))
ICON        =  os.path.join(HOME, l11l1_opy_ (u"ࠬ࡯ࡣࡰࡰ࠱ࡴࡳ࡭ࠧঢ়"))
ICON        =  xbmc.translatePath(ICON)
usrsetting  = os.path.join(profilePath)
addonini    = xbmc.translatePath(os.path.join(usrsetting, l11l1_opy_ (u"࠭ࡡࡥࡦࡲࡲࡸ࠴ࡩ࡯࡫ࠪ৞")))
UA          = base64.b64decode(l11l1_opy_ (u"ࠧࡗ࡚ࡑࡰࡨ࡯࠱ࡃ࡜࠵࡚ࡺࡪࡃ࠲ࡐ࡜࡜ࡱࡳ࡙ࡘ࡮ࡼ࡙ࡋࡐࡐࠨয়")) + l11l1_opy_ (u"ࠣࡔࡨࡰࡴࡧࡤࡦࡦࠣࡘ࡛ࠨৠ")
SOURCE_DB = l11l1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦ࠰ࡧࡦࠬৡ")
l1l111l11_opy_ = os.path.join(profilePath, l11l1_opy_ (u"ࠪࡸࡪࡳࡰ࠯ࡦࡥࠫৢ"))
l11lll111_opy_ = os.path.join(profilePath, l11l1_opy_ (u"ࠫ࡬ࡻࡩࡥࡧ࠱ࡼࡲࡲࠧৣ"))
KEY = l11l1_opy_ (u"ࠬࡾ࡭࡭ࡶࡹࠫ৤")
dex = l11l1_opy_ (u"࠭ࡤࡦࡺࠪ৥")
reloaded = l11l1_opy_ (u"ࠧࡳࡧ࡯ࡳࡦࡪࡥࡥࠩ০")
aftermathtv = l11l1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡭ࡢࡶ࡫ࡸࡻ࠭১")
ukturk = l11l1_opy_ (u"ࠩࡸ࡯ࡹࡻࡲ࡬ࠩ২")
sanctuary = l11l1_opy_ (u"ࠪࡷࡦࡴࡣࡵࡷࡤࡶࡾ࠭৩")
OTTTV     = l11l1_opy_ (u"ࠫࡔ࡚ࡔࡕࡘࠪ৪")
suicide21 = l11l1_opy_ (u"ࠬࡹࡵࡪࡥ࡬ࡨ࠷࠷ࡥࠨ৫")
freeview  = l11l1_opy_ (u"࠭ࡦࡳࡧࡨࡺ࡮࡫ࡷࠨ৬")
FTV = l11l1_opy_ (u"ࠧࡧࡶࡹࠫ৭")
uktvnow = l11l1_opy_ (u"ࠨࡷ࡮ࡸࡻࡴ࡯ࡸࠩ৮")
cluiptv = l11l1_opy_ (u"ࠩࡦࡰࡺ࡯ࡰࡵࡸࠪ৯")
suicide = l11l1_opy_ (u"ࠪࡷࡺ࡯ࡣࡪࡦࡨࠫৰ")
projectcypher = l11l1_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡨࡿࡰࡩࡧࡵࠫৱ")
notfilmon = l11l1_opy_ (u"ࠬ࡬ࡩ࡭࡯ࡱࡳࡹࡵ࡮ࠨ৲")
israelive = l11l1_opy_ (u"࠭ࡩࡴࡴࡤࡩࡱ࡯ࡶࡦࠩ৳")
adriansports = l11l1_opy_ (u"ࠧࡢࡦࡵ࡭ࡦࡴࡳࡱࡱࡵࡸࡸ࠭৴")
evolve = l11l1_opy_ (u"ࠨࡧࡹࡳࡱࡼࡥࠨ৵")
dialog = xbmcgui.Dialog()
class URLopener(urllib.FancyURLopener):
    version = l11l1_opy_ (u"ࠤࡐࡳࡿ࡯࡬࡭ࡣ࠲࠹࠳࠶࡙ࠠࠩ࡬ࡲࡩࡵࡷࡴࠢࡑࡘࠥ࠷࠰࠯࠲࠾ࠤ࡜࡯࡮࠷࠶࠾ࠤࡽ࠼࠴ࠪࠢࡄࡴࡵࡲࡥࡘࡧࡥࡏ࡮ࡺ࠯࠶࠵࠺࠲࠸࠼ࠠࠩࡍࡋࡘࡒࡒࠬࠡ࡮࡬࡯ࡪࠦࡇࡦࡥ࡮ࡳ࠮ࠦࡃࡩࡴࡲࡱࡪ࠵࠵࠷࠰࠳࠲࠷࠿࠲࠵࠰࠻࠻࡙ࠥࡡࡧࡣࡵ࡭࠴࠻࠳࠸࠰࠶࠺ࠧ৶")
class lel(object):
    def __init__(self, i):
        sqlite3.register_adapter(datetime.datetime, self.adapt_datetime)
        sqlite3.register_converter(l11l1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭৷"),     self.convert_datetime)
        databasePath = os.path.join(profilePath, SOURCE_DB)
        self.conn = sqlite3.connect(databasePath, timeout = 10, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.i = i
        self.channels = None
    def convert_datetime(self, ts):
        try:
            return datetime.datetime.fromtimestamp(float(ts))
        except ValueError:
            return None
    def adapt_datetime(self, ts):
        return time.mktime(ts.timetuple())
    def getCurrentProgram(self, channel):
        l11l1_opy_ (u"ࠦࠧࠨࠍࠋࠏࠍࠤࠥࠦࠠࠡࠢࠣࠤࡅࡶࡡࡳࡣࡰࠤࡨ࡮ࡡ࡯ࡰࡨࡰ࠿ࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࡂࡷࡽࡵ࡫ࠠࡤࡪࡤࡲࡳ࡫࡬࠻ࠢࡶࡳࡺࡸࡣࡦ࠰ࡆ࡬ࡦࡴ࡮ࡦ࡮ࠐࠎࠥࠦࠠࠡࠢࠣࠤࠥࡆࡲࡦࡶࡸࡶࡳࡀࠍࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ৸")
        program = None
        now = datetime.datetime.now()
        c = self.conn.cursor()
        try:
            c.execute(l11l1_opy_ (u"࡙ࠬࡅࡍࡇࡆࡘࠥ࠰ࠠࡇࡔࡒࡑࠥࡶࡲࡰࡩࡵࡥࡲࡹࠠࡘࡊࡈࡖࡊࠦࡣࡩࡣࡱࡲࡪࡲ࠽ࡀࠢࡄࡒࡉࠦࡳࡰࡷࡵࡧࡪࡃ࠿ࠡࡃࡑࡈࠥࡹࡴࡢࡴࡷࡣࡩࡧࡴࡦࠢ࠿ࡁࠥࡅࠠࡂࡐࡇࠤࡪࡴࡤࡠࡦࡤࡸࡪࠦ࠾࠾ࠢࡂࠫ৹"),
                    [channel.id, KEY, now, now])
            row = c.fetchone()
            if row:
                program = Program(channel, row[l11l1_opy_ (u"࠭ࡴࡪࡶ࡯ࡩࠬ৺")], row[l11l1_opy_ (u"ࠧࡴࡶࡤࡶࡹࡥࡤࡢࡶࡨࠫ৻")], row[l11l1_opy_ (u"ࠨࡧࡱࡨࡤࡪࡡࡵࡧࠪৼ")], row[l11l1_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ৽")],
                                row[l11l1_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࡡ࡯ࡥࡷ࡭ࡥࠨ৾")], row[l11l1_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࡢࡷࡲࡧ࡬࡭ࠩ৿")], None, row[l11l1_opy_ (u"ࠬࡹࡥࡢࡵࡲࡲࠬ਀")], row[l11l1_opy_ (u"࠭ࡥࡱ࡫ࡶࡳࡩ࡫ࠧਁ")],
                                row[l11l1_opy_ (u"ࠧࡪࡵࡢࡱࡴࡼࡩࡦࠩਂ")], row[l11l1_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪਃ")])
            c.close()
        except:
            pass
        return program
    def getNextProgram(self, program):
        nextProgram = None
        c = self.conn.cursor()
        c.execute(
            l11l1_opy_ (u"ࠩࡖࡉࡑࡋࡃࡕࠢ࠭ࠤࡋࡘࡏࡎࠢࡳࡶࡴ࡭ࡲࡢ࡯ࡶࠤ࡜ࡎࡅࡓࡇࠣࡧ࡭ࡧ࡮࡯ࡧ࡯ࡁࡄࠦࡁࡏࡆࠣࡷࡴࡻࡲࡤࡧࡀࡃࠥࡇࡎࡅࠢࡶࡸࡦࡸࡴࡠࡦࡤࡸࡪࠦ࠾࠾ࠢࡂࠤࡔࡘࡄࡆࡔࠣࡆ࡞ࠦࡳࡵࡣࡵࡸࡤࡪࡡࡵࡧࠣࡅࡘࡉࠠࡍࡋࡐࡍ࡙ࠦ࠱ࠨ਄"),
            [program.channel.id, KEY, program.endDate])
        row = c.fetchone()
        if row:
            nextProgram = Program(program.channel, row[l11l1_opy_ (u"ࠪࡸ࡮ࡺ࡬ࡦࠩਅ")], row[l11l1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡢࡨࡦࡺࡥࠨਆ")], row[l11l1_opy_ (u"ࠬ࡫࡮ࡥࡡࡧࡥࡹ࡫ࠧਇ")], row[l11l1_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫਈ")],
                                  row[l11l1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪࡥ࡬ࡢࡴࡪࡩࠬਉ")], row[l11l1_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫࡟ࡴ࡯ࡤࡰࡱ࠭ਊ")], None, row[l11l1_opy_ (u"ࠩࡶࡩࡦࡹ࡯࡯ࠩ਋")], row[l11l1_opy_ (u"ࠪࡩࡵ࡯ࡳࡰࡦࡨࠫ਌")],
                                  row[l11l1_opy_ (u"ࠫ࡮ࡹ࡟࡮ࡱࡹ࡭ࡪ࠭਍")], row[l11l1_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧ਎")])
        c.close()
        return nextProgram
    def getPreviousProgram(self, program):
        previousProgram = None
        c = self.conn.cursor()
        c.execute(
            l11l1_opy_ (u"࠭ࡓࡆࡎࡈࡇ࡙ࠦࠪࠡࡈࡕࡓࡒࠦࡰࡳࡱࡪࡶࡦࡳࡳ࡙ࠡࡋࡉࡗࡋࠠࡤࡪࡤࡲࡳ࡫࡬࠾ࡁࠣࡅࡓࡊࠠࡴࡱࡸࡶࡨ࡫࠽ࡀࠢࡄࡒࡉࠦࡥ࡯ࡦࡢࡨࡦࡺࡥࠡ࠾ࡀࠤࡄࠦࡏࡓࡆࡈࡖࠥࡈ࡙ࠡࡵࡷࡥࡷࡺ࡟ࡥࡣࡷࡩࠥࡊࡅࡔࡅࠣࡐࡎࡓࡉࡕࠢ࠴ࠫਏ"),
            [program.channel.id, KEY, program.startDate])
        row = c.fetchone()
        if row:
            previousProgram = Program(program.channel, row[l11l1_opy_ (u"ࠧࡵ࡫ࡷࡰࡪ࠭ਐ")], row[l11l1_opy_ (u"ࠨࡵࡷࡥࡷࡺ࡟ࡥࡣࡷࡩࠬ਑")], row[l11l1_opy_ (u"ࠩࡨࡲࡩࡥࡤࡢࡶࡨࠫ਒")],
                                      row[l11l1_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨਓ")], row[l11l1_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࡢࡰࡦࡸࡧࡦࠩਔ")], row[l11l1_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࡣࡸࡳࡡ࡭࡮ࠪਕ")], None, row[l11l1_opy_ (u"࠭ࡳࡦࡣࡶࡳࡳ࠭ਖ")],
                                      row[l11l1_opy_ (u"ࠧࡦࡲ࡬ࡷࡴࡪࡥࠨਗ")], row[l11l1_opy_ (u"ࠨ࡫ࡶࡣࡲࡵࡶࡪࡧࠪਘ")], row[l11l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫਙ")])
        c.close()
        return previousProgram
    def getPreviousChannel(self, currentChannel):
        idx = self.channels.index(currentChannel)
        idx -= 1
        if idx < 0:
            idx = len(self.channels) - 1
        return self.channels[idx]
    def getNextChannel(self, currentChannel):
        idx = self.channels.index(currentChannel)
        idx += 1
        if idx > len(self.channels) - 1:
            idx = 0
        return self.channels[idx]
    def getCurrentChannel(self, currentChannel, category=l11l1_opy_ (u"ࠥࡅࡱࡲࠠࡄࡪࡤࡲࡳ࡫࡬ࡴࠤਚ")):
        try:
            if category == l11l1_opy_ (u"ࠫࡆࡲ࡬ࠡࡅ࡫ࡥࡳࡴࡥ࡭ࡵࠪਛ"):
                idx = self.channels.index(currentChannel)
            else:
                channels = self.getChannelList(category=category)
                idx = channels.index(currentChannel)
        except ValueError:
            gui.ADDON.setSetting(l11l1_opy_ (u"ࠬࡲࡡࡴࡶ࠱ࡧࡦࡺࡥࡨࡱࡵࡽࠬਜ"), l11l1_opy_ (u"ࠨࡁ࡭࡮ࠣࡇ࡭ࡧ࡮࡯ࡧ࡯ࡷࠧਝ"))
            category = l11l1_opy_ (u"ࠢࡂ࡮࡯ࠤࡈ࡮ࡡ࡯ࡰࡨࡰࡸࠨਞ")
            idx = self.channels.index(currentChannel)
            return idx
        return idx
    def l11ll1ll1_opy_(self, l11ll1l11_opy_):
        if l11ll1l11_opy_+1 < 0:
            l11ll1l11_opy_ = 0
        if l11ll1l11_opy_+1 > len(self.channels):
            l11ll1l11_opy_ = 0
        return self.channels[l11ll1l11_opy_]
    def getChannelList(self, onlyVisible=True, category=l11l1_opy_ (u"ࠣࡃ࡯ࡰࠥࡉࡨࡢࡰࡱࡩࡱࡹࠢਟ")):
        c = self.conn.cursor()
        channelList = list()
        if onlyVisible:
            c.execute(l11l1_opy_ (u"ࠩࡖࡉࡑࡋࡃࡕࠢ࠭ࠤࡋࡘࡏࡎࠢࡦ࡬ࡦࡴ࡮ࡦ࡮ࡶࠤ࡜ࡎࡅࡓࡇࠣࡷࡴࡻࡲࡤࡧࡀࡃࠥࡇࡎࡅࠢࡹ࡭ࡸ࡯ࡢ࡭ࡧࡀࡃࠥࡇࡎࡅࠢࡦ࡬ࡳࡩࡡࡵࡧࡪࡳࡷࡿࠠࡍࡋࡎࡉࠥࡅࠠࡐࡔࡇࡉࡗࠦࡂ࡚ࠢࡺࡩ࡮࡭ࡨࡵࠩਠ"), [KEY, True, l11l1_opy_ (u"ࠪࠩࠬਡ")+category+l11l1_opy_ (u"ࠫࠪ࠭ਢ")])
        else:
            c.execute(l11l1_opy_ (u"࡙ࠬࡅࡍࡇࡆࡘࠥ࠰ࠠࡇࡔࡒࡑࠥࡩࡨࡢࡰࡱࡩࡱࡹࠠࡘࡊࡈࡖࡊࠦࡳࡰࡷࡵࡧࡪࡃ࠿ࠡࡃࡑࡈࠥࡩࡨ࡯ࡥࡤࡸࡪ࡭࡯ࡳࡻࠣࡐࡎࡑࡅࠡࡁࠣࡓࡗࡊࡅࡓࠢࡅ࡝ࠥࡽࡥࡪࡩ࡫ࡸࠬਣ"), [KEY, l11l1_opy_ (u"࠭ࠥࠨਤ")+category+l11l1_opy_ (u"ࠧࠦࠩਥ")])
        for row in c:
            channel = Channel(row[l11l1_opy_ (u"ࠨ࡫ࡧࠫਦ")], row[l11l1_opy_ (u"ࠩࡷ࡭ࡹࡲࡥࠨਧ")], row[l11l1_opy_ (u"ࠪࡧ࡭ࡴࡣࡢࡶࡨ࡫ࡴࡸࡹࠨਨ")], row[l11l1_opy_ (u"ࠫࡨ࡮࡮ࡢࡦࡧࡳࡳ࠭਩")], row[l11l1_opy_ (u"ࠬࡲ࡯ࡨࡱࠪਪ")], row[l11l1_opy_ (u"࠭ࡳࡵࡴࡨࡥࡲࡥࡵࡳ࡮ࠪਫ")], row[l11l1_opy_ (u"ࠧࡷ࡫ࡶ࡭ࡧࡲࡥࠨਬ")], row[l11l1_opy_ (u"ࠨࡹࡨ࡭࡬࡮ࡴࠨਭ")])
            if (gui.ADDON.getSetting(l11l1_opy_ (u"ࠩࡧࡩࡽࡺࡥࡳ࠰ࡨࡲࡦࡨ࡬ࡦࡦࠪਮ")) == l11l1_opy_ (u"ࠪࡸࡷࡻࡥࠨਯ") and dex in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠫࡷ࡫࡬ࡰࡣࡧࡩࡩ࠴ࡥ࡯ࡣࡥࡰࡪࡪࠧਰ")) == l11l1_opy_ (u"ࠬࡺࡲࡶࡧࠪ਱") and reloaded in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"࠭ࡏࡕࡖࡗ࡚࠳࡫࡮ࡢࡤ࡯ࡩࡩ࠭ਲ")) == l11l1_opy_ (u"ࠧࡵࡴࡸࡩࠬਲ਼") and OTTTV in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠨࡵࡸ࡭ࡨ࡯ࡤࡦ࠴࠴࠲ࡪࡴࡡࡣ࡮ࡨࡨࠬ਴")) == l11l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧਵ") and suicide21 in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳ࡯ࡤࡸ࡭ࡺࡶ࠯ࡧࡱࡥࡧࡲࡥࡥࠩਸ਼")) == l11l1_opy_ (u"ࠫࡹࡸࡵࡦࠩ਷") and aftermathtv in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠬࡻ࡫ࡵࡷࡵ࡯࠳࡫࡮ࡢࡤ࡯ࡩࡩ࠭ਸ")) == l11l1_opy_ (u"࠭ࡴࡳࡷࡨࠫਹ") and ukturk in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠧࡴࡣࡱࡧࡹࡻࡡࡳࡻ࠱ࡩࡳࡧࡢ࡭ࡧࡧࠫ਺")) == l11l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭਻") and sanctuary in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠩࡉࡘ࡛࠴ࡥ࡯ࡣࡥࡰࡪࡪ਼ࠧ")) == l11l1_opy_ (u"ࠪࡸࡷࡻࡥࠨ਽") and FTV in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠫࡺࡱࡴࡷࡰࡲࡻ࠳࡫࡮ࡢࡤ࡯ࡩࡩ࠭ਾ")) == l11l1_opy_ (u"ࠬࡺࡲࡶࡧࠪਿ") and uktvnow in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"࠭ࡣ࡭ࡷ࡬ࡴࡹࡼ࠮ࡦࡰࡤࡦࡱ࡫ࡤࠨੀ")) == l11l1_opy_ (u"ࠧࡵࡴࡸࡩࠬੁ") and cluiptv in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠨࡵࡸ࡭ࡨ࡯ࡤࡦ࠰ࡨࡲࡦࡨ࡬ࡦࡦࠪੂ")) == l11l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ੃") and suicide in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡧࡾࡶࡨࡦࡴ࠱ࡩࡳࡧࡢ࡭ࡧࡧࠫ੄")) == l11l1_opy_ (u"ࠫࡹࡸࡵࡦࠩ੅") and projectcypher in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠬࡴ࡯ࡵࡨ࡬ࡰࡲࡵ࡮࠯ࡧࡱࡥࡧࡲࡥࡥࠩ੆")) == l11l1_opy_ (u"࠭ࡴࡳࡷࡨࠫੇ") and notfilmon in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠧࡪࡵࡵࡥࡪࡲࡩࡷࡧ࠱ࡩࡳࡧࡢ࡭ࡧࡧࠫੈ")) == l11l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭੉") and israelive in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠩࡤࡨࡷ࡯ࡡ࡯ࡵࡳࡳࡷࡺࡳ࠯ࡧࡱࡥࡧࡲࡥࡥࠩ੊")) == l11l1_opy_ (u"ࠪࡸࡷࡻࡥࠨੋ") and adriansports in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠫࡪࡼ࡯࡭ࡸࡨ࠲ࡪࡴࡡࡣ࡮ࡨࡨࠬੌ")) == l11l1_opy_ (u"ࠬࡺࡲࡶࡧ੍ࠪ") and evolve in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"࠭ࡦࡳࡧࡨࡺ࡮࡫ࡷ࠯ࡧࡱࡥࡧࡲࡥࡥࠩ੎")) == l11l1_opy_ (u"ࠧࡵࡴࡸࡩࠬ੏") and freeview in channel.chnaddon or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠨࡣ࡯ࡰ࡫ࡸࡥࡦࡣࡧࡨࡴࡴࡳ࠯ࡧࡱࡥࡧࡲࡥࡥࠩ੐")) == l11l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧੑ") and (ukturk in channel.chnaddon or sanctuary in channel.chnaddon or FTV in channel.chnaddon or uktvnow in channel.chnaddon or
                    cluiptv in channel.chnaddon or suicide in channel.chnaddon or projectcypher in channel.chnaddon or notfilmon in channel.chnaddon or israelive in channel.chnaddon or adriansports in channel.chnaddon or evolve in channel.chnaddon or freeview in channel.chnaddon) or
                gui.ADDON.getSetting(l11l1_opy_ (u"ࠪࡥࡱࡲࡣࡩࡣࡱࡲࡪࡲࡳ࠯ࡧࡱࡥࡧࡲࡥࡥࠩ੒")) == l11l1_opy_ (u"ࠫࡹࡸࡵࡦࠩ੓")):
                channelList.append(channel)
        c.close()
        return channelList
    def getWeight(self, channel):
        return channel.weight
    def close(self):
        try:
            if self.conn:
                self.conn.rollback()
        except sqlite3.OperationalError:
            pass
        if self.conn:
            self.conn.close()
    def setchns(self):
        c = self.conn.cursor()
        if gui.ADDON.getSetting(l11l1_opy_ (u"ࠬࡩࡨ࡯ࡱࡵࡨࡪࡸࠧ੔")) == l11l1_opy_ (u"࠭ࡁ࠮࡜ࠪ੕"):
            c.execute(l11l1_opy_ (u"ࠢࡄࡔࡈࡅ࡙ࡋࠠࡕࡇࡐࡔࡔࡘࡁࡓ࡛ࠣࡘࡆࡈࡌࡆࠢࡤࡰࡵ࡮ࡡࡕࡧࡰࡴࠥࡧࡳ࡙ࠡࡌࡘࡍࠦࡷࡵࡨࡌ࡬ࡦࡺࡥ࡚ࡱࡸࠤࡆ࡙ࠠࠩࡵࡨࡰࡪࡩࡴࠡ࡫ࡧ࠰ࠥࡺࡩࡵ࡮ࡨ࠰ࠥࡽࡥࡪࡩ࡫ࡸ࠱ࠦࠨࡔࡇࡏࡉࡈ࡚ࠠࡄࡑࡘࡒ࡙࠮ࠪࠪࠢ࠰ࠤ࠶ࠦࡆࡓࡑࡐࠤࡨ࡮ࡡ࡯ࡰࡨࡰࡸࠦࡡ࡙ࠡࡋࡉࡗࡋࠠࡢ࠰ࡷ࡭ࡹࡲࡥࠡ࠾ࡀࠤࡧ࠴ࡴࡪࡶ࡯ࡩࠥࡉࡏࡍࡎࡄࡘࡊࠦࡎࡐࡅࡄࡗࡊ࠯ࠠࡢࡵࠣࡶࡴࡽࡎࡶ࡯ࡥࡩࡷࠦࡦࡳࡱࡰࠤࡈ࡮ࡡ࡯ࡰࡨࡰࡸࠦࡢࠡࡑࡵࡨࡪࡸࠠࡃࡻࠣࡸ࡮ࡺ࡬ࡦࠢࡆࡓࡑࡒࡁࡕࡇࠣࡒࡔࡉࡁࡔࡇࠣࡅࡘࡉࠩࠡࡵࡨࡰࡪࡩࡴࠡࠬࠣࡪࡷࡵ࡭ࠡࡹࡷࡪࡎ࡮ࡡࡵࡧ࡜ࡳࡺࠨ੖"))
            self.conn.commit()
            c.execute(l11l1_opy_ (u"ࠣࡗࡓࡈࡆ࡚ࡅࠡࡅ࡫ࡥࡳࡴࡥ࡭ࡵࠣࡗࡊ࡚ࠠࡸࡧ࡬࡫࡭ࡺࠠ࠾ࠢࠫࡷࡪࡲࡥࡤࡶࠣࡶࡴࡽࡎࡶ࡯ࡥࡩࡷࠦࡦࡳࡱࡰࠤࡦࡲࡰࡩࡣࡗࡩࡲࡶࠠࡸࡪࡨࡶࡪࠦࡩࡥࠢࡀࠤࡈ࡮ࡡ࡯ࡰࡨࡰࡸ࠴ࡩࡥࠫࠥ੗"))
            self.conn.commit()
            c.execute(l11l1_opy_ (u"ࠤࡇࡖࡔࡖࠠࡕࡃࡅࡐࡊࠦࡡ࡭ࡲ࡫ࡥ࡙࡫࡭ࡱࠤ੘"))
            self.conn.commit()
        if gui.ADDON.getSetting(l11l1_opy_ (u"ࠪࡧ࡭ࡴ࡯ࡳࡦࡨࡶࠬਖ਼")) == l11l1_opy_ (u"ࠫࡉ࡫ࡦࡢࡷ࡯ࡸࠬਗ਼"):
            c.execute(l11l1_opy_ (u"࡛ࠧࡐࡅࡃࡗࡉࠥࡩࡨࡢࡰࡱࡩࡱࡹࠠࡔࡇࡗࠤࡼ࡫ࡩࡨࡪࡷࠤࡂࠦࡲࡰࡹ࡬ࡨࠥ࠳ࠠ࠲ࠤਜ਼"))
            self.conn.commit()
        c.close()
    def updatechnlist(self):
        self.channels = self.getChannelList()
    def l111ll_opy_(self,l11lll1ll_opy_):
        c = self.conn.cursor()
        c.execute(l11l1_opy_ (u"࠭ࡓࡆࡎࡈࡇ࡙ࠦࠪࠡࡈࡕࡓࡒࠦࡣࡩࡣࡱࡲࡪࡲࡳ࡙ࠡࡋࡉࡗࡋࠠࡴࡱࡸࡶࡨ࡫࠽ࡀࠢࡄࡒࡉࠦࡩࡥ࠿ࡂࠫੜ"), [KEY, l11lll1ll_opy_])
        for row in c:
            channel = Channel(row[l11l1_opy_ (u"ࠧࡪࡦࠪ੝")], row[l11l1_opy_ (u"ࠨࡶ࡬ࡸࡱ࡫ࠧਫ਼")], row[l11l1_opy_ (u"ࠩࡦ࡬ࡳࡩࡡࡵࡧࡪࡳࡷࡿࠧ੟")], row[l11l1_opy_ (u"ࠪࡧ࡭ࡴࡡࡥࡦࡲࡲࠬ੠")], row[l11l1_opy_ (u"ࠫࡱࡵࡧࡰࠩ੡")], row[l11l1_opy_ (u"ࠬࡹࡴࡳࡧࡤࡱࡤࡻࡲ࡭ࠩ੢")], row[l11l1_opy_ (u"࠭ࡶࡪࡵ࡬ࡦࡱ࡫ࠧ੣")], row[l11l1_opy_ (u"ࠧࡸࡧ࡬࡫࡭ࡺࠧ੤")])
        c.close()
        return channel
    def l11lll1l1_opy_(self,l11lll1ll_opy_,programTitle):
        c = self.conn.cursor()
        c.execute(l11l1_opy_ (u"ࠨࡆࡈࡐࡊ࡚ࡅࠡࡨࡵࡳࡲࠦ࡮ࡰࡶ࡬ࡪ࡮ࡩࡡࡵ࡫ࡲࡲࡸࠦࡗࡉࡇࡕࡉࠥࡩࡨࡢࡰࡱࡩࡱࡃ࠿ࠡࡃࡑࡈࠥࡶࡲࡰࡩࡵࡥࡲࡥࡴࡪࡶ࡯ࡩࡂࡅࠧ੥"), [l11lll1ll_opy_,programTitle])
        c.close()
    def setCustomStreamUrl(self, channel, stream_url):
        if stream_url is not None:
            c = self.conn.cursor()
            c.execute(l11l1_opy_ (u"ࠤࡇࡉࡑࡋࡔࡆࠢࡉࡖࡔࡓࠠࡤࡷࡶࡸࡴࡳ࡟ࡴࡶࡵࡩࡦࡳ࡟ࡶࡴ࡯ࠤ࡜ࡎࡅࡓࡇࠣࡧ࡭ࡧ࡮࡯ࡧ࡯ࡁࡄࠨ੦"), [channel.id])
            c.execute(l11l1_opy_ (u"ࠥࡍࡓ࡙ࡅࡓࡖࠣࡍࡓ࡚ࡏࠡࡥࡸࡷࡹࡵ࡭ࡠࡵࡷࡶࡪࡧ࡭ࡠࡷࡵࡰ࠭ࡩࡨࡢࡰࡱࡩࡱ࠲ࠠࡴࡶࡵࡩࡦࡳ࡟ࡶࡴ࡯࠭ࠥ࡜ࡁࡍࡗࡈࡗ࠭ࡅࠬࠡࡁࠬࠦ੧"),
                      [channel.id, stream_url.decode(l11l1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ੨"), l11l1_opy_ (u"ࠬ࡯ࡧ࡯ࡱࡵࡩࠬ੩"))])
            self.conn.commit()
            c.close()
    def deleteCustomStreamUrl(self, channel):
        c = self.conn.cursor()
        c.execute(l11l1_opy_ (u"ࠨࡄࡆࡎࡈࡘࡊࠦࡆࡓࡑࡐࠤࡨࡻࡳࡵࡱࡰࡣࡸࡺࡲࡦࡣࡰࡣࡺࡸ࡬࡙ࠡࡋࡉࡗࡋࠠࡤࡪࡤࡲࡳ࡫࡬࠾ࡁࠥ੪"), [channel.id])
        self.conn.commit()
        c.close()
    def getStreamUrl(self, channel):
        customStreamUrl = self.getCustomStreamUrl(channel)
        if customStreamUrl:
            customStreamUrl = customStreamUrl.encode(l11l1_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭੫"), l11l1_opy_ (u"ࠨ࡫ࡪࡲࡴࡸࡥࠨ੬"))
            return customStreamUrl
        elif channel.isPlayable():
            streamUrl = channel.streamUrl.encode(l11l1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨ੭"), l11l1_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࠪ੮"))
            return streamUrl
        return None
    def getCustomStreamUrl(self, channel):
        c = self.conn.cursor()
        c.execute(l11l1_opy_ (u"ࠦࡘࡋࡌࡆࡅࡗࠤࡸࡺࡲࡦࡣࡰࡣࡺࡸ࡬ࠡࡈࡕࡓࡒࠦࡣࡶࡵࡷࡳࡲࡥࡳࡵࡴࡨࡥࡲࡥࡵࡳ࡮࡛ࠣࡍࡋࡒࡆࠢࡦ࡬ࡦࡴ࡮ࡦ࡮ࡀࡃࠧ੯"), [channel.id])
        stream_url = c.fetchone()
        c.close()
        if stream_url:
            return stream_url[0]
        else:
            return None
    def removeNotification(self, program):
        c = self.conn.cursor()
        c.execute(l11l1_opy_ (u"ࠧࡊࡅࡍࡇࡗࡉࠥࡌࡒࡐࡏࠣࡲࡴࡺࡩࡧ࡫ࡦࡥࡹ࡯࡯࡯ࡵ࡛ࠣࡍࡋࡒࡆࠢࡦ࡬ࡦࡴ࡮ࡦ࡮ࡀࡃࠥࡇࡎࡅࠢࡳࡶࡴ࡭ࡲࡢ࡯ࡢࡸ࡮ࡺ࡬ࡦ࠿ࡂࠤࡆࡔࡄࠡࡵࡲࡹࡷࡩࡥ࠾ࡁࠥੰ"),
                  [program.channel.id, program.title, KEY])
        self.conn.commit()
        c.close()
    def getCustomLineUp(self):
        c = self.conn.cursor()
        d = xbmcgui.DialogProgressBG()
        d.create(l11l1_opy_ (u"࠭ࡒࡦ࡮ࡲࡥࡩ࡫ࡤࠡࡖ࡙ࠤࡌࡻࡩࡥࡧࠣ࡟ࡈࡕࡌࡐࡔࠣࡻ࡭࡯ࡴࡦ࡟࠰ࠤࡘࡺ࡯ࡳ࡫ࡱ࡫ࠥࡉࡵࡴࡶࡲࡱࠥࡉࡨࡢࡰࡱࡩࡱࠦࡌࡪࡰࡨࡹࡵࠦࡄࡢࡶࡤࠤࡹࡵࠠࡂࡥࡦࡳࡺࡴࡴ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩੱ"), l11l1_opy_ (u"ࠢࡔࡶࡤࡶࡹ࡯࡮ࡨ࠰࠱࠲ࠧੲ"))
        c.execute(l11l1_opy_ (u"ࠣࡕࡈࡐࡊࡉࡔࠡ࡫ࡧ࠰ࡼ࡫ࡩࡨࡪࡷ࠰ࡻ࡯ࡳࡪࡤ࡯ࡩࠥ࡬ࡲࡰ࡯ࠣࡧ࡭ࡧ࡮࡯ࡧ࡯ࡷࠧੳ"))
        data = c.fetchall()
        c.close()
        l1l11lll1_opy_ = str(time.time())
        l1ll111l1_opy_ = []
        l1ll111l1_opy_.append((l11l1_opy_ (u"ࠤࡗ࡭ࡲ࡫ࠠࡖࡲࡧࡥࡹ࡫ࡤࠣੴ").encode(l11l1_opy_ (u"ࠥ࡬ࡪࡾࠢੵ")), l1l11lll1_opy_, 0))
        total = len(data) - 1
        l1l111l1l_opy_ = 0
        for row in data:
            t = (row[l11l1_opy_ (u"ࠫ࡮ࡪࠧ੶")].encode(l11l1_opy_ (u"ࠧ࡮ࡥࡹࠤ੷")), row[l11l1_opy_ (u"࠭ࡷࡦ࡫ࡪ࡬ࡹ࠭੸")], row[l11l1_opy_ (u"ࠧࡷ࡫ࡶ࡭ࡧࡲࡥࠨ੹")])
            l1ll111l1_opy_.append(t)
            l1l111l1l_opy_ += 1
            percent = 100.0 * l1l111l1l_opy_ / total
            d.update(int(percent), message=l11l1_opy_ (u"ࠨࡗࡳࡰࡴࡧࡤࡪࡰࡪࠤࠬ੺")+row[l11l1_opy_ (u"ࠩ࡬ࡨࠬ੻")])
        gui.ADDON.setSetting(l11l1_opy_ (u"ࠪࡥࡨࡩ࡬ࡶ࡮ࡤࡷࡹࡻࡰࡥࡣࡷࡩࠬ੼"), l1l11lll1_opy_)
        d.update(100, message=l11l1_opy_ (u"ࠦࡘࡺ࡯ࡳ࡫ࡱ࡫ࠥࡉࡵࡴࡶࡲࡱࠥࡉࡨࡢࡰࡱࡩࡱࠦࡌࡪࡰࡨࡹࡵࠦࡄࡢࡶࡤࠤࡹࡵࠠࡂࡥࡦࡳࡺࡴࡴࠡࡅࡲࡱࡵࡲࡥࡵࡧࡧࠥࠧ੽"))
        d.close()
        dialog.notification(l11l1_opy_ (u"ࠬ࠭੾"), l11l1_opy_ (u"࠭ࡓࡵࡱࡵ࡭ࡳ࡭ࠠࡄࡷࡶࡸࡴࡳࠠࡄࡪࡤࡲࡳ࡫࡬ࠡࡎ࡬ࡲࡪࡻࡰ࡝ࡰࡇࡥࡹࡧࠠࡵࡱࠣࡅࡨࡩ࡯ࡶࡰࡷࠤࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠡࠨ੿"), ICON, 4500)
        return json.dumps(l1ll111l1_opy_)
    def setCustomLineUp(self,data):
        c = self.conn.cursor()
        d = xbmcgui.DialogProgressBG()
        d.create(l11l1_opy_ (u"ࠧࡓࡧ࡯ࡳࡦࡪࡥࡥࠢࡗ࡚ࠥࡍࡵࡪࡦࡨࠤࡠࡉࡏࡍࡑࡕࠤࡼ࡮ࡩࡵࡧࡠ࠱ࠥࡏ࡭ࡱࡱࡵࡸ࡮ࡴࡧࠡࡅ࡫ࡥࡳࡴࡥ࡭ࠢࡏ࡭ࡳ࡫ࡵࡱࠢࡇࡥࡹࡧࠠࡧࡴࡲࡱࠥࡇࡣࡤࡱࡸࡲࡹࡡ࠯ࡄࡑࡏࡓࡗࡣࠧ઀"), l11l1_opy_ (u"ࠣࡕࡷࡥࡷࡺࡩ࡯ࡩ࠱࠲࠳ࠨઁ"))
        total = len(data) - 1
        l1l111l1l_opy_ = 0
        try:
            for id,weight,visible in data:
                id = id.decode(l11l1_opy_ (u"ࠤ࡫ࡩࡽࠨં"))
                if id == l11l1_opy_ (u"ࠪࡘ࡮ࡳࡥࠡࡗࡳࡨࡦࡺࡥࡥࠩઃ"):
                    time = weight
                    continue
                c.execute(l11l1_opy_ (u"࡚ࠦࡖࡄࡂࡖࡈࠤࡨ࡮ࡡ࡯ࡰࡨࡰࡸࠦࡓࡆࡖࠣࡻࡪ࡯ࡧࡩࡶࡀࡃ࠱ࠦࡶࡪࡵ࡬ࡦࡱ࡫࠽ࡀ࡚ࠢࡌࡊࡘࡅࠡ࡫ࡧࡁࡄࠨ઄"), [weight, visible, id])
                self.conn.commit()
                l1l111l1l_opy_ += 1
                percent = 100.0 * l1l111l1l_opy_ / total
                d.update(int(percent), message=l11l1_opy_ (u"ࠬࡏ࡭ࡱࡱࡵࡸ࡮ࡴࡧࠡࠩઅ")+id)
            c.close()
            gui.ADDON.setSetting(l11l1_opy_ (u"࠭ࡣࡩࡰࡲࡶࡩ࡫ࡲࠨઆ"), l11l1_opy_ (u"ࠢࡄࡷࡶࡸࡴࡳࠢઇ"))
            gui.ADDON.setSetting(l11l1_opy_ (u"ࠨࡣࡦࡧࡱࡻ࡬ࡢࡵࡷࡹࡵࡪࡡࡵࡧࠪઈ"), time)
            d.update(100, message=l11l1_opy_ (u"ࠤࡌࡱࡵࡵࡲࡵ࡫ࡱ࡫ࠥࡉࡵࡴࡶࡲࡱࠥࡉࡨࡢࡰࡱࡩࡱࠦࡌࡪࡰࡨࡹࡵࠦࡄࡢࡶࡤࠤ࡫ࡸ࡯࡮ࠢࡄࡧࡨࡵࡵ࡯ࡶࠣࡇࡴࡳࡰ࡭ࡧࡷࡩࡩࠧࠢઉ"))
            d.close()
            dialog.notification(l11l1_opy_ (u"ࠪࠫઊ"), l11l1_opy_ (u"ࠫࡎࡳࡰࡰࡴࡷ࡭ࡳ࡭ࠠࡄࡷࡶࡸࡴࡳࠠࡄࡪࡤࡲࡳ࡫࡬ࠡࡎ࡬ࡲࡪࡻࡰ࡝ࡰࡇࡥࡹࡧࠠࡧࡴࡲࡱࠥࡇࡣࡤࡱࡸࡲࡹࠦࡃࡰ࡯ࡳࡰࡪࡺࡥࡥࠣࠪઋ"), ICON, 4500)
        except:
            c.close()
            d.close()
    def programsdata(self):
        if not os.path.exists(l1l111l11_opy_):
            os.remove(l11lll111_opy_)
            dialog.ok(l11l1_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟ࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠠࡈࡷ࡬ࡨࡪࡡ࠯ࡄࡑࡏࡓࡗࡣࠧઌ"), l11l1_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠ࡟ࡇࡣࡅࡳࡴࡲࡶࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠥࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪઍ"), l11l1_opy_ (u"ࠧࠨ઎"), l11l1_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡࡧࡻ࡭ࡹ࡛ࠦࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠡࡣࡱࡨࠥࡸࡥ࠮࡮ࡤࡹࡳࡩࡨ࠭ࠢࡷࡳࠥ࡬࡯ࡳࡥࡨࠤࡩࡧࡴࡢࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠥࠬએ"))
            raise ValueError(l11l1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠦࠦࡎࡦࡧࡧࠤࡹࡵࠠࡧࡱࡵࡧࡪࠦࡤࡢࡶࡤࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࠴ࠧઐ"))
        c = self.conn.cursor()
        c.execute(l11l1_opy_ (u"ࠥࡈࡊࡒࡅࡕࡇࠣࡊࡗࡕࡍࠡ࡯ࡤ࡭ࡳ࠴ࡰࡳࡱࡪࡶࡦࡳࡳ࠼ࠤઑ"))
        self.conn.commit()
        c.execute(l11l1_opy_ (u"ࠦࡆ࡚ࡔࡂࡅࡋࠤࡉࡇࡔࡂࡄࡄࡗࡊࠦࠧࠦࡵࠪࠤࡆ࡙ࠠࡵࡧࡰࡴࡩࡨ࠻ࠣ઒") % (l1l111l11_opy_))
        c.execute(l11l1_opy_ (u"ࠧࡏࡎࡔࡇࡕࡘࠥࡏࡎࡕࡑࠣࡱࡦ࡯࡮࠯ࡲࡵࡳ࡬ࡸࡡ࡮ࡵࠣࡗࡊࡒࡅࡄࡖࠣ࠮ࠥࡌࡒࡐࡏࠣࡸࡪࡳࡰࡥࡤ࠱ࡴࡷࡵࡧࡳࡣࡰࡷࡀࠨઓ"))
        c.execute(l11l1_opy_ (u"ࠨࡄࡆࡖࡄࡇࡍࠦࡄࡂࡖࡄࡆࡆ࡙ࡅࠡࠩࡷࡩࡲࡶࡤࡣࠩ࠾ࠦઔ"))
        self.conn.commit()
        c.close()
        try:
            os.remove(l1l111l11_opy_)
        except:
            pass
class hm(object):
    def __init__(self, i):
        self.l11llll11_opy_ = i
        self.hm = gui
    def _channelUp(self):
        channel = self.l11llll11_opy_.kek.getNextChannel(self.l11llll11_opy_.currentChannel)
        program = self.l11llll11_opy_.kek.getCurrentProgram(channel)
        if not self.playChannel(channel, program, True):
            result = self.l11llll11_opy_.streamingService.detectStream(channel)
            if not result:
                self.l11llll11_opy_._showContextMenu(program)
            elif type(result) == str:
                self.l11llll11_opy_.database.setCustomStreamUrl(channel, result)
                self.playChannel(channel, program)
            else:
                result = sorted(result, key=self.l11lll11l_opy_)
                result = sorted(result, key=self.l1l1lllll_opy_)
                if channel.title == l11l1_opy_ (u"ࠧࡆࡒࡏࠫક") or channel.title == l11l1_opy_ (u"ࠨࡐࡉࡐࠬખ") or channel.title == l11l1_opy_ (u"ࠩࡑࡆࡆ࠭ગ") or channel.title == l11l1_opy_ (u"ࠪࡒࡍࡒࠧઘ") or channel.title == l11l1_opy_ (u"ࠫࡕࡖࡖࠨઙ") or channel.title == l11l1_opy_ (u"ࠬࡔࡂࡂࠩચ") or channel.title == l11l1_opy_ (u"࠭࠲࠵࠹ࠪછ") or channel.title == l11l1_opy_ (u"ࠧࡎࡎࡅࠫજ") or channel.title == l11l1_opy_ (u"ࠨࡏࡘࡗࡎࡉࠠࡄࡊࡒࡍࡈࡋࠧઝ") or len(channel.title) > 13:
                    selection = kappa.iI1(l11l1_opy_ (u"ࠤ࡞ࡆࡢࡌ࡯ࡶࡰࡧࠤࡲࡻ࡬ࡵ࡫ࡳࡰࡪࠦࡳࡰࡷࡵࡧࡪࡹࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡦ࡬ࡦࡴ࡮ࡦ࡮࠱ࠤࡕࡲࡥࡢࡵࡨࠤࡸ࡫࡬ࡦࡥࡷࠤࡴࡴࡥ࠯࡝࠲ࡆࡢࠨઞ"), result)
                    if selection is not None:
                        if selection == -1:
                            pass
                        else:
                            self.l11llll11_opy_.database.setCustomStreamUrl(channel, selection)
                            self.playChannel(channel, program)
                else:
                    d = self.hm.ChooseStreamAddonDialog(result)
                    d.doModal()
                    if d.stream is not None:
                        self.l11llll11_opy_.database.setCustomStreamUrl(channel, d.stream)
                        self.playChannel(channel, program)
    def _channelDown(self):
        channel = self.l11llll11_opy_.kek.getPreviousChannel(self.l11llll11_opy_.currentChannel)
        program = self.l11llll11_opy_.kek.getCurrentProgram(channel)
        if not self.playChannel(channel, program, True):
            result = self.l11llll11_opy_.streamingService.detectStream(channel)
            if not result:
                self.l11llll11_opy_._showContextMenu(program)
            elif type(result) == str:
                self.l11llll11_opy_.database.setCustomStreamUrl(channel, result)
                self.playChannel(channel, program)
            else:
                result = sorted(result, key=self.l11lll11l_opy_)
                result = sorted(result, key=self.l1l1lllll_opy_)
                if channel.title == l11l1_opy_ (u"ࠪࡉࡕࡒࠧટ") or channel.title == l11l1_opy_ (u"ࠫࡓࡌࡌࠨઠ") or channel.title == l11l1_opy_ (u"ࠬࡔࡂࡂࠩડ") or channel.title == l11l1_opy_ (u"࠭ࡎࡉࡎࠪઢ") or channel.title == l11l1_opy_ (u"ࠧࡑࡒ࡙ࠫણ") or channel.title == l11l1_opy_ (u"ࠨࡐࡅࡅࠬત") or channel.title == l11l1_opy_ (u"ࠩ࠵࠸࠼࠭થ") or channel.title == l11l1_opy_ (u"ࠪࡑࡑࡈࠧદ") or channel.title == l11l1_opy_ (u"ࠫࡒ࡛ࡓࡊࡅࠣࡇࡍࡕࡉࡄࡇࠪધ") or len(channel.title) > 13:
                    selection = kappa.iI1(l11l1_opy_ (u"ࠧࡡࡂ࡞ࡈࡲࡹࡳࡪࠠ࡮ࡷ࡯ࡸ࡮ࡶ࡬ࡦࠢࡶࡳࡺࡸࡣࡦࡵࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡩࡨࡢࡰࡱࡩࡱ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡴࡧ࡯ࡩࡨࡺࠠࡰࡰࡨ࠲ࡠ࠵ࡂ࡞ࠤન"), result)
                    if selection is not None:
                        if selection == -1:
                            pass
                        else:
                            self.l11llll11_opy_.database.setCustomStreamUrl(channel, selection)
                            self.playChannel(channel, program)
                else:
                    d = self.hm.ChooseStreamAddonDialog(result)
                    d.doModal()
                    if d.stream is not None:
                        self.l11llll11_opy_.database.setCustomStreamUrl(channel, d.stream)
                        self.playChannel(channel, program)
    def _previouschannel(self):
        if self.l11llll11_opy_.previouschannel is not None:
            previouschannel     = self.l11llll11_opy_.previouschannel
            l1l1llll1_opy_ = self.l11llll11_opy_.kek.getCurrentProgram(previouschannel)
            if not self.playChannel(previouschannel, l1l1llll1_opy_, True):
                result = self.l11llll11_opy_.streamingService.detectStream(previouschannel)
                if not result:
                    self.l11llll11_opy_._showContextMenu(l1l1llll1_opy_)
                elif type(result) == str:
                    self.l11llll11_opy_.database.setCustomStreamUrl(previouschannel, result)
                    self.playChannel(previouschannel, l1l1llll1_opy_)
                else:
                    result = sorted(result, key=self.l11lll11l_opy_)
                    result = sorted(result, key=self.l1l1lllll_opy_)
                    if previouschannel.title == l11l1_opy_ (u"࠭ࡅࡑࡎࠪ઩") or previouschannel.title == l11l1_opy_ (u"ࠧࡏࡈࡏࠫપ") or previouschannel.title == l11l1_opy_ (u"ࠨࡐࡅࡅࠬફ") or previouschannel.title == l11l1_opy_ (u"ࠩࡑࡌࡑ࠭બ") or previouschannel.title == l11l1_opy_ (u"ࠪࡔࡕ࡜ࠧભ") or previouschannel.title == l11l1_opy_ (u"ࠫࡓࡈࡁࠨમ") or previouschannel.title == l11l1_opy_ (u"ࠬ࠸࠴࠸ࠩય") or previouschannel.title == l11l1_opy_ (u"࠭ࡍࡍࡄࠪર") or previouschannel.title == l11l1_opy_ (u"ࠧࡎࡗࡖࡍࡈࠦࡃࡉࡑࡌࡇࡊ࠭઱") or len(previouschannel.title) > 13:
                        selection = kappa.iI1(l11l1_opy_ (u"ࠣ࡝ࡅࡡࡋࡵࡵ࡯ࡦࠣࡱࡺࡲࡴࡪࡲ࡯ࡩࠥࡹ࡯ࡶࡴࡦࡩࡸࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡥ࡫ࡥࡳࡴࡥ࡭࠰ࠣࡔࡱ࡫ࡡࡴࡧࠣࡷࡪࡲࡥࡤࡶࠣࡳࡳ࡫࠮࡜࠱ࡅࡡࠧલ"), result)
                        if selection is not None:
                            if selection == -1:
                                pass
                            else:
                                self.l11llll11_opy_.database.setCustomStreamUrl(previouschannel, selection)
                                self.playChannel(previouschannel, l1l1llll1_opy_)
                    else:
                        d = self.hm.ChooseStreamAddonDialog(result)
                        d.doModal()
                        if d.stream is not None:
                            self.l11llll11_opy_.database.setCustomStreamUrl(previouschannel, d.stream)
                            self.playChannel(previouschannel, l1l1llll1_opy_)
    def inputnumber(self, number, method):
        self.l11llll11_opy_.channelinput = True
        l11llllll_opy_ = int(gui.ADDON.getSetting(l11l1_opy_ (u"ࠩࡦࡰࡴࡹࡥࡪࡰࡳࡹࡹࡳࡳࠨળ")).replace(l11l1_opy_ (u"ࠪࠤࡲࡹࠧ઴"),l11l1_opy_ (u"ࠫࠬવ")))
        dialog = xbmcgui.Dialog()
        selection = dialog.input(l11l1_opy_ (u"ࠧࡏ࡮ࡱࡷࡷࠤࡨ࡮ࡡ࡯ࡰࡨࡰࠥࡴࡵ࡮ࡤࡨࡶࠧશ"), number, xbmcgui.INPUT_NUMERIC, autoclose=l11llllll_opy_)
        if int(selection) < 1 or selection == l11l1_opy_ (u"࠭ࠧષ"):
            selection = l11l1_opy_ (u"ࠧ࠲ࠩસ")
        if method == l11l1_opy_ (u"ࠨࡇࡓࡋࠬહ"):
            if self.l11llll11_opy_.currentcategory != l11l1_opy_ (u"ࠤࡄࡰࡱࠦࡃࡩࡣࡱࡲࡪࡲࡳࠣ઺"):
                self.hm.ADDON.setSetting(l11l1_opy_ (u"ࠪࡰࡦࡹࡴ࠯ࡥࡤࡸࡪ࡭࡯ࡳࡻࠪ઻"), l11l1_opy_ (u"ࠦࡆࡲ࡬ࠡࡅ࡫ࡥࡳࡴࡥ࡭ࡵ઼ࠥ"))
                self.l11llll11_opy_.currentcategory = self.hm.ADDON.getSetting(l11l1_opy_ (u"ࠬࡲࡡࡴࡶ࠱ࡧࡦࡺࡥࡨࡱࡵࡽࠬઽ"))
            self.l11llll11_opy_.viewStartDate = datetime.datetime.today()
            self.l11llll11_opy_.viewStartDate -= datetime.timedelta(minutes=self.l11llll11_opy_.viewStartDate.minute % 30, seconds=self.l11llll11_opy_.viewStartDate.second)
            self.l11llll11_opy_.focusPoint.y = self.l11llll11_opy_.epgView.top
            self.l11llll11_opy_.onRedrawEPG(int(selection)-1, self.l11llll11_opy_.viewStartDate)
        elif method == l11l1_opy_ (u"࠭ࡔࡗࠩા"):
            self.l11llll11_opy_.osdChannel = self.l11llll11_opy_.kek.l11ll1ll1_opy_(int(selection)-1)
            self.l11llll11_opy_.osdProgram = self.l11llll11_opy_.kek.getCurrentProgram(self.l11llll11_opy_.osdChannel)
            if not self.playChannel(self.l11llll11_opy_.osdChannel, self.l11llll11_opy_.osdProgram, True):
                result = self.l11llll11_opy_.streamingService.detectStream(self.l11llll11_opy_.osdChannel)
                if not result:
                    self.l11llll11_opy_._showContextMenu(self.l11llll11_opy_.osdProgram)
                elif type(result) == str:
                    self.l11llll11_opy_.database.setCustomStreamUrl(self.l11llll11_opy_.osdChannel, result)
                    self.playChannel(self.l11llll11_opy_.osdChannel, self.l11llll11_opy_.osdProgram)
                else:
                    result = sorted(result, key=self.l11lll11l_opy_)
                    result = sorted(result, key=self.l1l1lllll_opy_)
                    if self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠧࡆࡒࡏࠫિ") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠨࡐࡉࡐࠬી") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠩࡑࡆࡆ࠭ુ") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠪࡒࡍࡒࠧૂ") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠫࡕࡖࡖࠨૃ") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠬࡔࡂࡂࠩૄ") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"࠭࠲࠵࠹ࠪૅ") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠧࡎࡎࡅࠫ૆") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠨࡏࡘࡗࡎࡉࠠࡄࡊࡒࡍࡈࡋࠧે") or len(self.l11llll11_opy_.osdChannel.title) > 13:
                        selection = kappa.iI1(l11l1_opy_ (u"ࠤ࡞ࡆࡢࡌ࡯ࡶࡰࡧࠤࡲࡻ࡬ࡵ࡫ࡳࡰࡪࠦࡳࡰࡷࡵࡧࡪࡹࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡦ࡬ࡦࡴ࡮ࡦ࡮࠱ࠤࡕࡲࡥࡢࡵࡨࠤࡸ࡫࡬ࡦࡥࡷࠤࡴࡴࡥ࠯࡝࠲ࡆࡢࠨૈ"), result)
                        if selection is not None:
                            if selection == -1:
                                pass
                            else:
                                self.l11llll11_opy_.database.setCustomStreamUrl(self.l11llll11_opy_.osdChannel, selection)
                                self.playChannel(self.l11llll11_opy_.osdChannel, self.l11llll11_opy_.osdProgram)
                    else:
                        d = self.hm.ChooseStreamAddonDialog(result)
                        d.doModal()
                        if d.stream is not None:
                            self.l11llll11_opy_.database.setCustomStreamUrl(self.l11llll11_opy_.osdChannel, d.stream)
                            self.playChannel(self.l11llll11_opy_.osdChannel, self.l11llll11_opy_.osdProgram)
        elif method == l11l1_opy_ (u"ࠪࡓࡘࡊࠧૉ"):
            self.l11llll11_opy_.osdChannel = self.l11llll11_opy_.kek.l11ll1ll1_opy_(int(selection)-1)
            self.l11llll11_opy_.osdProgram = self.l11llll11_opy_.kek.getCurrentProgram(self.l11llll11_opy_.osdChannel)
            self._showOsd()
        self.l11llll11_opy_.channelinput = False
    def _showOsd(self, onplayback=False):
        if not self.l11llll11_opy_.osdEnabled:
            return
        if self.l11llll11_opy_.mode != self.hm.MODE_OSD:
            self.l11llll11_opy_.database.getEPGView(self.l11llll11_opy_.currentChannel, self.l11llll11_opy_.viewStartDate, self.l11llll11_opy_.onSourceProgressUpdate, clearExistingProgramList=False)
            self.l11llll11_opy_.osdChannel = self.l11llll11_opy_.currentChannel
            self.l11llll11_opy_.osdProgram = self.l11llll11_opy_.kek.getCurrentProgram(self.l11llll11_opy_.currentChannel)
        if self.l11llll11_opy_.osdProgram is None:
            self.l11llll11_opy_.osdProgram = self.hm.src.Program(self.l11llll11_opy_.osdChannel, self.hm.strings(self.hm.NO_PROGRAM_AVAILABLE), None, None, None)
        if self.l11llll11_opy_.osdProgram is not None and self.l11llll11_opy_.osdChannel is not None:
            self.l11llll11_opy_.setControlLabel(self.l11llll11_opy_.C_MAIN_OSD_TITLE, l11l1_opy_ (u"ࠫࡠࡈ࡝ࠦࡵ࡞࠳ࡇࡣࠧ૊") % self.l11llll11_opy_.osdProgram.title)
            if self.l11llll11_opy_.osdProgram.startDate or self.l11llll11_opy_.osdProgram.endDate:
                self.l11llll11_opy_.setControlLabel(self.l11llll11_opy_.C_MAIN_OSD_TIME, l11l1_opy_ (u"ࠬࡡࡂ࡞ࠧࡶࠤ࠲ࠦࠥࡴ࡝࠲ࡆࡢ࠭ો") % (
                    self.l11llll11_opy_.formatTime(self.l11llll11_opy_.osdProgram.startDate), self.l11llll11_opy_.formatTime(self.l11llll11_opy_.osdProgram.endDate)))
            else:
                self.l11llll11_opy_.setControlLabel(self.l11llll11_opy_.C_MAIN_OSD_TIME, l11l1_opy_ (u"࠭ࠧૌ"))
            self.l11llll11_opy_.setControlText(self.l11llll11_opy_.C_MAIN_OSD_DESCRIPTION, self.l11llll11_opy_.osdProgram.description)
            self.l11llll11_opy_.setControlLabel(self.l11llll11_opy_.C_MAIN_OSD_CHANNEL_TITLE, self.l11llll11_opy_.osdChannel.title)
            if self.l11llll11_opy_.osdProgram.channel.logo is not None and self.l11llll11_opy_.osdShowlogos:
                self.l11llll11_opy_.setControlImage(self.l11llll11_opy_.C_MAIN_OSD_CHANNEL_LOGO, self.l11llll11_opy_.osdProgram.channel.logo)
            else:
                self.l11llll11_opy_.setControlImage(self.l11llll11_opy_.C_MAIN_OSD_CHANNEL_LOGO, l11l1_opy_ (u"ࠧࠨ્"))
            if self.l11llll11_opy_.osdShownumbers:
                self.l11llll11_opy_.setControlText(self.l11llll11_opy_.C_MAIN_OSD_CHANNEL_NUMBER, str(self.l11llll11_opy_.kek.getCurrentChannel(self.l11llll11_opy_.osdChannel)+1))
        if not onplayback:
            self.l11llll11_opy_.mode = self.hm.MODE_OSD
        self.l11llll11_opy_._showControl(self.l11llll11_opy_.C_MAIN_OSD)
    def p1(self):
        if not self.playChannel(self.l11llll11_opy_.osdChannel, self.l11llll11_opy_.osdProgram, True):
            result = self.l11llll11_opy_.streamingService.detectStream(self.l11llll11_opy_.osdChannel)
            if not result:
                self.l11llll11_opy_._showContextMenu(self.l11llll11_opy_.osdProgram)
            elif type(result) == str:
                self.l11llll11_opy_.database.setCustomStreamUrl(self.l11llll11_opy_.osdChannel, result)
                self.playChannel(self.l11llll11_opy_.osdChannel, self.l11llll11_opy_.osdProgram)
            else:
                result = sorted(result, key=self.l11lll11l_opy_)
                result = sorted(result, key=self.l1l1lllll_opy_)
                if self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠨࡇࡓࡐࠬ૎") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠩࡑࡊࡑ࠭૏") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠪࡒࡇࡇࠧૐ") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠫࡓࡎࡌࠨ૑") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠬࡖࡐࡗࠩ૒") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"࠭ࡎࡃࡃࠪ૓") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠧ࠳࠶࠺ࠫ૔") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠨࡏࡏࡆࠬ૕") or self.l11llll11_opy_.osdChannel.title == l11l1_opy_ (u"ࠩࡐ࡙ࡘࡏࡃࠡࡅࡋࡓࡎࡉࡅࠨ૖") or len(self.l11llll11_opy_.osdChannel.title) > 13:
                    selection = kappa.iI1(l11l1_opy_ (u"ࠥ࡟ࡇࡣࡆࡰࡷࡱࡨࠥࡳࡵ࡭ࡶ࡬ࡴࡱ࡫ࠠࡴࡱࡸࡶࡨ࡫ࡳࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡧ࡭ࡧ࡮࡯ࡧ࡯࠲ࠥࡖ࡬ࡦࡣࡶࡩࠥࡹࡥ࡭ࡧࡦࡸࠥࡵ࡮ࡦ࠰࡞࠳ࡇࡣࠢ૗"), result)
                    if selection is not None:
                        if selection == -1:
                            pass
                        else:
                            self.l11llll11_opy_.database.setCustomStreamUrl(self.l11llll11_opy_.osdChannel, selection)
                            self.playChannel(self.l11llll11_opy_.osdChannel, self.l11llll11_opy_.osdProgram)
                else:
                    d = self.hm.ChooseStreamAddonDialog(result)
                    d.doModal()
                    if d.stream is not None:
                        self.l11llll11_opy_.database.setCustomStreamUrl(self.l11llll11_opy_.osdChannel, d.stream)
                        self.playChannel(self.l11llll11_opy_.osdChannel, self.l11llll11_opy_.osdProgram)
    def p2(self, program):
        if not self.playChannel(program.channel, program, True):
            result = self.l11llll11_opy_.streamingService.detectStream(program.channel)
            if not result:
                self.l11llll11_opy_._showContextMenu(program)
            elif type(result) == str:
                self.l11llll11_opy_.database.setCustomStreamUrl(program.channel, result)
                self.playChannel(program.channel, program)
            else:
                result = sorted(result, key=self.l11lll11l_opy_)
                result = sorted(result, key=self.l1l1lllll_opy_)
                if program.channel.title == l11l1_opy_ (u"ࠫࡊࡖࡌࠨ૘") or program.channel.title == l11l1_opy_ (u"ࠬࡔࡆࡍࠩ૙") or program.channel.title == l11l1_opy_ (u"࠭ࡎࡃࡃࠪ૚") or program.channel.title == l11l1_opy_ (u"ࠧࡏࡊࡏࠫ૛") or program.channel.title == l11l1_opy_ (u"ࠨࡒࡓ࡚ࠬ૜") or program.channel.title == l11l1_opy_ (u"ࠩࡑࡆࡆ࠭૝") or program.channel.title == l11l1_opy_ (u"ࠪ࠶࠹࠽ࠧ૞") or program.channel.title == l11l1_opy_ (u"ࠫࡒࡒࡂࠨ૟") or program.channel.title == l11l1_opy_ (u"ࠬࡓࡕࡔࡋࡆࠤࡈࡎࡏࡊࡅࡈࠫૠ") or len(program.channel.title) > 13:
                    selection = kappa.iI1(l11l1_opy_ (u"ࠨ࡛ࡃ࡟ࡉࡳࡺࡴࡤࠡ࡯ࡸࡰࡹ࡯ࡰ࡭ࡧࠣࡷࡴࡻࡲࡤࡧࡶࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡣࡩࡣࡱࡲࡪࡲ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡵࡨࡰࡪࡩࡴࠡࡱࡱࡩ࠳ࡡ࠯ࡃ࡟ࠥૡ"), result)
                    if selection is not None:
                        if selection == -1:
                            pass
                        else:
                            self.l11llll11_opy_.database.setCustomStreamUrl(program.channel, selection)
                            self.playChannel(program.channel, program)
                else:
                    d = self.hm.ChooseStreamAddonDialog(result)
                    d.doModal()
                    if d.stream is not None:
                        self.l11llll11_opy_.database.setCustomStreamUrl(program.channel, d.stream)
                        self.playChannel(program.channel, program)
    def playChannel(self, channel, program = None, l11ll11l1_opy_ = False):
        try:
            l1l11ll11_opy_ = self.l11llll11_opy_.player.isPlaying()
            url = self.l11llll11_opy_.database.getStreamUrl(channel)
            SAVESTREAM = self.hm.ADDON.getSetting(l11l1_opy_ (u"ࠧࡴࡣࡹࡩ࠳ࡹࡴࡳࡧࡤࡱࠬૢ")) == l11l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ૣ")
            l1l1111l1_opy_ = [l11l1_opy_ (u"ࠩ࠵࠸࠼࠭૤"),l11l1_opy_ (u"ࠪࡒࡇࡇࠧ૥"),l11l1_opy_ (u"ࠫࡓࡌࡌࠨ૦"),l11l1_opy_ (u"ࠬࡔࡈࡍࠩ૧"),l11l1_opy_ (u"࠭ࡅࡑࡎࠪ૨"),l11l1_opy_ (u"ࠧࡑࡒ࡙ࠫ૩"),l11l1_opy_ (u"ࠨࡏࡏࡆࠬ૪"),l11l1_opy_ (u"ࠩࡐࡹࡸ࡯ࡣࠡࡅ࡫ࡳ࡮ࡩࡥࠨ૫"),l11l1_opy_ (u"ࠪࡑ࡚࡙ࡉࡄࠢࡆࡌࡔࡏࡃࡆࠩ૬")]
            if url:
                if l1l11ll11_opy_:
                    self.l11llll11_opy_.channelswitch = True
                    self.l11llll11_opy_.previouschannel = self.l11llll11_opy_.currentChannel
                self.l11llll11_opy_.currentChannel = channel
                if program == None:
                    program = self.l11llll11_opy_.kek.getCurrentProgram(self.l11llll11_opy_.currentChannel)
                if channel.title in l1l1111l1_opy_ or not SAVESTREAM and not l11ll11l1_opy_:
                    self.l11llll11_opy_.database.deleteCustomStreamUrl(channel)
                if url.isdigit():
                    command = (l11l1_opy_ (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠢࠥ࠶࠳࠶ࠢ࠭ࠢࠥ࡭ࡩࠨ࠺ࠣ࠳ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠡࠤࡓࡰࡦࡿࡥࡳ࠰ࡒࡴࡪࡴࠢ࠭ࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧ࡯ࡴࡦ࡯ࠥ࠾ࢀࠨࡣࡩࡣࡱࡲࡪࡲࡩࡥࠤ࠽ࠩࡸࢃࡽࡾࠩ૭") % url)
                    xbmc.executeJSONRPC(command)
                    return
                if url.startswith(l11l1_opy_ (u"ࠬࡒࡉࡗࡇࡗ࡚ࠬ૮")):
                    import add;stream = add.l1l1111ll_opy_(url)
                    delay=0
                    delay=100
                    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                    playlist.clear()
                    playlist.add(stream, xbmcgui.ListItem(l11l1_opy_ (u"࠭ࠧ૯")))
                    try:
                        xbmc.Player().play(playlist)
                    except: pass
                    return
                if url.lower().startswith(l11l1_opy_ (u"ࠧࡥࡵࡩࠫ૰")):
                    import add
                    if add.playPlaylist(url, windowed):
                        print l11l1_opy_ (u"ࠨࡒ࡯ࡥࡾࡲࡩࡴࡶࠪ૱")
                    return
                if str.startswith(url,l11l1_opy_ (u"ࠤࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡱࡪࡺࡡࠣ૲")) and program is not None:
                    title = urllib.quote(program.title)
                    url += l11l1_opy_ (u"ࠥ࠳ࠪࡹ࠯ࠦࡵࠥ૳") % (title, program.language)
                if url[0:9] == l11l1_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࠧ૴") and self.l11llll11_opy_.alternativePlayback:
                    if self.l11llll11_opy_.alternativePlayback:
                        xbmc.executebuiltin(l11l1_opy_ (u"ࠬ࡞ࡂࡎࡅ࠱ࡖࡺࡴࡐ࡭ࡷࡪ࡭ࡳ࠮ࠥࡴࠫࠪ૵") % url)
                else:
                    if url[0:26] == l11l1_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡥࡧࡻ࠳ࠬ૶"):
                        url = re.findall(l11l1_opy_ (u"ࡲࠨࡷࡵࡰࡂ࠮࠮ࠬࡁࠬࠪࡲࡵࡤࡦࠩ૷"), url)
                        url = l11l1_opy_ (u"ࠨࠩ૸").join(url)
                        url = urllib.unquote_plus(url)
                    try:
                        listitem = xbmcgui.ListItem(l11l1_opy_ (u"ࠩࡗ࡭ࡹࡲࡥࠨૹ"), thumbnailImage=self.l11llll11_opy_.currentChannel.logo)
                        listitem.setInfo(l11l1_opy_ (u"ࠪࡺ࡮ࡪࡥࡰࠩૺ"), {l11l1_opy_ (u"࡙ࠫ࡯ࡴ࡭ࡧࠪૻ"): l11l1_opy_ (u"ࠧࡡࡃࡐࡎࡒࡖࠥࡹ࡫ࡺࡤ࡯ࡹࡪࡣ࡛ࡃ࡟ࠥૼ")+self.l11llll11_opy_.currentChannel.title+l11l1_opy_ (u"ࠨࠠ࠮ࠢ࡞ࡇࡔࡒࡏࡓࠢࡳࡥࡱ࡫ࡧࡳࡧࡨࡲࡢࠨ૽")+program.title+l11l1_opy_ (u"ࠢ࡜࠱ࡆࡓࡑࡕࡒ࡞࡝࠲ࡆࡢࠨ૾")})
                    except:
                        pass
                    if self.l11llll11_opy_.lolololol in url:
                        self.l11llll11_opy_.player.play(item=url, listitem=listitem, windowed=0)
                    else:
                        return
                if not l1l11ll11_opy_:
                    self.l11llll11_opy_._hideEpg()
                else:
                    self.l11llll11_opy_._hideOsd()
                self.hm.threading.Timer(1, self.l11llll11_opy_.waitForPlayBackStopped).start()
                xbmc.sleep(350)
                self.l11llll11_opy_.osdProgram = self.l11llll11_opy_.kek.getCurrentProgram(self.l11llll11_opy_.currentChannel)
                self.l11llll11_opy_.channelIdx = self.l11llll11_opy_.kek.getCurrentChannel(self.l11llll11_opy_.currentChannel)
            return url is not None
        except:
            if channel.title in l1l1111l1_opy_ or not SAVESTREAM and not l11ll11l1_opy_:
                self.l11llll11_opy_.database.deleteCustomStreamUrl(channel)
    def cw(self, kek):
        try:
            opener = URLopener()
            parsed_url = urlparse.urlparse(kek)
            if not bool(parsed_url.scheme):
                parsed_url = parsed_url._replace(**{l11l1_opy_ (u"ࠣࡵࡦ࡬ࡪࡳࡥࠣ૿"): l11l1_opy_ (u"ࠤ࡫ࡸࡹࡶࠢ଀")})
                kek = parsed_url.geturl()
                if kek[0:8] == l11l1_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲࠳ࠬଁ"):
                    kek = kek.replace(l11l1_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳࠴࠭ଂ"),l11l1_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴࠭ଃ"))
            response = opener.open(kek)
            try:
                code = response.getcode()
            finally:
                response.close()
            if code == 200:
                path = urlparse.urlparse(kek).path
                l1l11111l_opy_ = os.path.splitext(path)[1]
                l1l11llll_opy_ = path.split(l11l1_opy_ (u"࠭࠯ࠨ଄"))[-1].split(l11l1_opy_ (u"ࠧ࠯ࠩଅ"))[0]
                if (l11l1_opy_ (u"ࠣ࠰ࡳࡲ࡬ࠨଆ") in l1l11111l_opy_ or l11l1_opy_ (u"ࠤ࠱࡮ࡵ࡭ࠢଇ") in l1l11111l_opy_ or l11l1_opy_ (u"ࠥ࠲࡯ࡶࡥࡨࠤଈ") in l1l11111l_opy_ or l11l1_opy_ (u"ࠦ࠳࡭ࡩࡧࠤଉ") in l1l11111l_opy_):
                    mayfaircustomwp = xbmc.translatePath(os.path.join(gui.SKINdir, l11l1_opy_ (u"ࠬࡸࡥࡴࡱࡸࡶࡨ࡫ࡳࠨଊ"), l11l1_opy_ (u"࠭ࡳ࡬࡫ࡱࡷࠬଋ"), l11l1_opy_ (u"ࠧࡅࡧࡩࡥࡺࡲࡴࠨଌ"), l1l11llll_opy_))
                    if not os.path.exists(mayfaircustomwp+l1l11111l_opy_):
                        dp = xbmcgui.DialogProgress()
                        dp.create(l11l1_opy_ (u"ࠣ࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢࡘࡥ࡭ࡱࡤࡨࡪࡪࠠࡕࡘࠣࡋࡺ࡯ࡤࡦ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠣ࠱࡙ࠥ࡫ࡪࡰࠥ଍"),l11l1_opy_ (u"ࠩࡇࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡄࡷࡶࡸࡴࡳࠠࡃࡣࡦ࡯࡬ࡸ࡯ࡶࡰࡧࠤࡎࡳࡡࡨࡧ࠱࠲ࠬ଎"), l11l1_opy_ (u"ࠪࠫଏ"), l11l1_opy_ (u"ࠫࠬଐ"))
                        dp.update(0)
                        start_time=time.time()
                        opener.retrieve(kek, mayfaircustomwp+l1l11111l_opy_, lambda nb, bs, fs: self._pbhook(nb, bs, fs, dp, start_time))
                    return True, l1l11llll_opy_+l1l11111l_opy_
                else:
                    dialog = xbmcgui.Dialog()
                    dialog.ok(l11l1_opy_ (u"ࠧࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟ࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠠࡈࡷ࡬ࡨࡪࡡ࠯ࡄࡑࡏࡓࡗࡣࠢ଑"),base64.b64decode(l11l1_opy_ (u"ࠨࡓ࡙ࡓࡪࡧ࠷࡜࡬ࡣ࡚ࡐ࡫ࡪ࡝࠹࠲ࡋࡊ࡬࡭ࡪ࡭ࡖࡩࡦࡌࡏࡼࡤ࡮࡮࡮࡞࡜ࡗࡧ࡚࡙࠷࡫ࡦ࡝࠵࡫ࡤ࠶ࡎࡾࡠࡗࡏ࠲ࡥࡌࡰ࡭࡚࡮࠻ࡼࡦ࡜ࡌ࠰ࡥࡉ࡙࡯ࡎࡎࡖࡺࡤࡆࡆࡲࡨ࠳ࡊࡩ࡜࠷࡛ࢀࡤࡈ࠻ࡷࡍࡍࡔࡲࡢ࡙࠷࡫࡞ࡳࡆ࡫ࡣ࠵ࡨࡾࡨ࠳ࡗࡷ࡝ࡇࡇࡶࡢࡘࡈࡱ࡞ࡘ࠺࠽ࠣ଒")),l11l1_opy_ (u"ࠢࠣଓ"),base64.b64decode(l11l1_opy_ (u"ࠣࡗࡊࡼࡱ࡟ࡘࡏ࡮ࡌࡋ࠶࡮ࡡ࠳ࡗࡪࡧ࠸࡜ࡹ࡛ࡕࡅ࠹ࡧ࠹ࡕࡨࡥࡋࡎࡻࡪ࡭࡭࡭࡝ࡗࡇ࠶ࡡࡈࡗࡪ࡞ࡌࡲࡹ࡛࡙ࡑ࠴ࡎࡎࡖࡺࡤࡆࡆ࠵ࡨࡹࡃ࠲ࡤࡋ࡚࡭ࡡࡘ࠳࡫࡞࠷࡛ࡧ࡛࡯࡯ࡷ࡟࡙࠴ࡨࡍࡆ࠹ࡶࡩࡇࡤࡸࡏࡲࡇࡻ࡚ࡺ࠺ࡸࡥࡳࡈ࡬࡛ࡻ࠻ࡹ࡟࠸࡬࡮ࡍࡔࡁࡂࠨଔ")))
                    return False, l11l1_opy_ (u"ࠩࠪକ")
            else:
                dialog = xbmcgui.Dialog()
                dialog.ok(l11l1_opy_ (u"ࠥ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝ࡓࡧ࡯ࡳࡦࡪࡥࡥࠢࡗ࡚ࠥࡍࡵࡪࡦࡨ࡟࠴ࡉࡏࡍࡑࡕࡡࠧଖ"),base64.b64decode(l11l1_opy_ (u"ࠦࡘ࡞ࡑࡨࡥ࠵࡚ࡱࡨࡘࡎࡩࡧࡋ࡭ࡲࡉࡉࡘࡼࡦࡈࡈࡷࡤ࡯࠼࠶ࡦ࡝ࡒ࡭࡜ࡆࡆࡲࡨ࠳ࡊࡩ࡜࠷࡛ࢀࡤࡈ࠻ࡷࡍࡍࡔࡲࡢ࡙࠷࡫࡞ࡳࡆ࡫ࡣ࠵ࡨࡾࡨ࠳ࡗࡷ࡝ࡇࡇࡶࡢࡘࡈࡱ࡞ࡘࡈࡰࡤࡻࡅ࠷ࡨࡳ࠹ࡶ࡜ࡼࡆࡻࡩࡩࡃ࠲ࡤࡋ࡛ࡿ࡚ࡔࡄ࠶࡝࡝ࡓࡧ࡚࡙࠷࡫ࡦ࡞ࡎࡻࡦ࡚࡙࡬࡟࠲࠺ࡷࡥࡱ࡛ࡰࡤࡈ࡮ࡸ࡞ࡾࡈ࠰ࡣࡻࡅ࠴ࡦࡍࡆ࠱ࡋࡋࡨࡱ࡟࡮ࡏࡲࡧࡋ࡚࡮ࠢଗ")),l11l1_opy_ (u"ࠧࠨଘ"),base64.b64decode(l11l1_opy_ (u"ࠨࡕࡈࡺ࡯࡝࡝ࡔ࡬ࡊࡉ࡙ࡹࡩࡍࡖࡺࡋࡋࡖࡴࡠࡓࡃࡘࡘ࡯ࡼ࡭࡚࡙ࡪ࡫࡝࠸ࡗࡳࡊࡉࡑ࡬ࡨ࠸ࡕࡵࡥ࠵࡚ࡺࡩ࠲࡭࠲ࡤ࡜࡟ࡲࡌࡨ࠿ࡀࠦଙ")))
                return False, l11l1_opy_ (u"ࠧࠨଚ")
        except:
            dialog = xbmcgui.Dialog()
            dialog.ok(l11l1_opy_ (u"ࠣ࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢࡘࡥ࡭ࡱࡤࡨࡪࡪࠠࡕࡘࠣࡋࡺ࡯ࡤࡦ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠥଛ"), base64.b64decode(l11l1_opy_ (u"ࠤࡘ࠶࠾ࡺ࡚࡙ࡔࡲࡥ࡜࠻࡮ࡊࡊࡧࡰࡧࡴࡑࡨࡦ࠶ࡎࡻࡨ࡭ࡤࡩࡧ࠶ࡱ࠶ࡡࡄࡄ࠳ࡥࡌ࡛ࡧࡤࡊࡍࡺࡩࡳ࡬࡬࡜࡚ࡕ࡬࡟࠳ࡗࡼࡧࡋ࠾ࡺࡉࡈࡌ࡫࡝࠷ࡺ࡮ࡤ࡯࠼࠵ࡧࡳࡑࡨࡥ࠵ࡸࡵࡨࡩࡃ࠳ࡦࡱࡼ࡮ࠢଜ")),base64.b64decode(l11l1_opy_ (u"࡙ࠥࡌࡾ࡬࡚࡚ࡑࡰࡎࡍ࠱ࡩࡣ࠵࡙࡬ࡩ࠳ࡗࡻ࡝ࡗࡇ࠻ࡢ࠴ࡗࡪ࡝࡝ࡐ࡬ࡊࡉ࡙ࡹࡩࡍࡖࡺࡣ࡚࠹ࡳࡏࡇ࡭࠲ࡌࡋ࡛࠺࡙ࡘࡐ࠳ࡏࡌࡔࡨࡤ࠴ࡘࡸࡨ࠸ࡖࡶࡥ࠵ࡰ࠵ࡧࡘ࡛࡮ࡎࡗࡇ࡮ࡢ࡮ࡓࡪࡥ࡝ࡗ࡮ࡤࡻࡅ࠴ࡦࡍࡕࡨ࡜ࡊࡰࡾࡠࡗࡏ࠲ࡌࡋࡱࡺ࡙ࡘࡦ࡯ࡍࡋ࡜ࡓࡕࡅࡅࡰࡧࡳࡒࡱࡤࡰࡧ࡬ࡧࡗ࠵ࡩࡎࡇ࠺ࡷࡣࡈࡥࡹࡐࡲࡶࡷ࡛࡙ࡦࡺࡑࡴࡂࡶ࡜ࡼ࠼ࡺࡠ࠲࡭࡯ࡎࡕࡂࡃࠢଝ")),l11l1_opy_ (u"ࠦࠧଞ"))
            return False, l11l1_opy_ (u"ࠬ࠭ଟ")
    def StreamDown(self):
        dialog = xbmcgui.Dialog()
        try:
            if self.l11llll11_opy_.database.getStreamUrl(self.l11llll11_opy_.currentChannel):
                ret = dialog.yesno(l11l1_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨଠ"),l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡠࡈ࡝ࡆࡴࡵࡳࡷࠦࡷࡪࡶ࡫ࠤࠬଡ")+self.l11llll11_opy_.currentChannel.title+l11l1_opy_ (u"ࠨࠢࡶࡸࡷ࡫ࡡ࡮ࠣ࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨଢ"),l11l1_opy_ (u"ࠩࡖࡸࡷ࡫ࡡ࡮ࠢࡤࡴࡵ࡫ࡡࡳࡵࠣࡸࡴࠦࡢࡦࠢࡧࡳࡼࡴࠡࠡࡱࡵࠤࡨ࡮ࡥࡤ࡭ࠣࡽࡴࡻࡲࠡࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲ࠳࠴ࠧଣ"),l11l1_opy_ (u"ࠪࡈࡴࠦࡹࡰࡷࠣࡻ࡮ࡹࡨࠡࡶࡲࠤࡷ࡫࡭ࡰࡸࡨࠤࡹ࡮ࡩࡴࠢࡶࡸࡷ࡫ࡡ࡮ࠢࡤࡷࠥࡿ࡯ࡶࡴࠣࡨࡪ࡬ࡡࡶ࡮ࡷࠤࡸࡺࡲࡦࡣࡰࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡦ࡬ࡦࡴ࡮ࡦ࡮ࡂࠫତ"),l11l1_opy_ (u"ࠫࡓࡵࠧଥ"),l11l1_opy_ (u"ࠬ࡟ࡥࡴࠩଦ"))
                if ret:
                    self.l11llll11_opy_.database.deleteCustomStreamUrl(self.l11llll11_opy_.currentChannel)
                    return
                if not ret:
                    return
            else:
                dialog.ok(l11l1_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨଧ"),l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡠࡈ࡝ࡆࡴࡵࡳࡷࠦࡷࡪࡶ࡫ࠤࡸࡺࡲࡦࡣࡰࠥࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪନ"),l11l1_opy_ (u"ࠨࡕࡷࡶࡪࡧ࡭ࠡࡣࡳࡴࡪࡧࡲࡴࠢࡷࡳࠥࡨࡥࠡࡦࡲࡻࡳࠧࠠࡰࡴࠣࡧ࡭࡫ࡣ࡬ࠢࡼࡳࡺࡸࠠࡤࡱࡱࡲࡪࡩࡴࡪࡱࡱ࠲࠳࠭଩"),l11l1_opy_ (u"ࠩࠪପ"))
                return
        except:
            return
    def _pbhook(self, numblocks, blocksize, filesize, dp, start_time):
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
            mbs = l11l1_opy_ (u"ࠥࡇࡺࡹࡴࡰ࡯ࠣࡆࡦࡩ࡫ࡨࡴࡲࡹࡳࡪࠠࡊ࡯ࡤ࡫ࡪࡀࠠࠣଫ")+l11l1_opy_ (u"ࠫࠪ࠴࠰࠳ࡨࠣࡑࡇࠦ࡯ࡧࠢࠨ࠲࠵࠸ࡦࠡࡏࡅࠫବ") % (currently_downloaded, total)
            e = l11l1_opy_ (u"࡙ࠬࡰࡦࡧࡧ࠾ࠥࠫ࠮࠱࠴ࡩࠤࡐࡨ࠯ࡴࠢࠪଭ") % kbps_speed
            e += l11l1_opy_ (u"࠭ࡅࡕࡃ࠽ࠤࠪ࠶࠲ࡥ࠼ࠨ࠴࠷ࡪࠧମ") % divmod(eta, 60)
            dp.update(percent, mbs, e)
        except:
            percent = 100
            dp.update(percent)
        if dp.iscanceled():
            dp.close()
    def DansGame(self,KappaPride):
        gachiGASM = base64.b64decode(KappaPride)
        return gachiGASM
    def l11lll11l_opy_(self,item):
        return item[1]
    def l1l1lllll_opy_(self,item):
        return item[0]
    def systemvideosettings(self):
        try:
            dialog = xbmcgui.Dialog()
            l11ll1l1l_opy_ = json.loads(xbmc.executeJSONRPC(l11l1_opy_ (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡔࡧࡷࡸ࡮ࡴࡧࡴ࠰ࡊࡩࡹ࡙ࡥࡵࡶ࡬ࡲ࡬࡜ࡡ࡭ࡷࡨࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡷࡪࡺࡴࡪࡰࡪࠦ࠿ࠨࡶࡪࡦࡨࡳࡵࡲࡡࡺࡧࡵ࠲ࡺࡹࡥ࡮ࡧࡧ࡭ࡦࡩ࡯ࡥࡧࡦࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿࠷ࡽࠨଯ")))[l11l1_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࠣର")][l11l1_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣ଱")]
            l1l1lll1l_opy_ = json.loads(xbmc.executeJSONRPC(l11l1_opy_ (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠠࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡗࡪࡺࡴࡪࡰࡪࡷ࠳ࡍࡥࡵࡕࡨࡸࡹ࡯࡮ࡨࡘࡤࡰࡺ࡫ࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡳࡦࡶࡷ࡭ࡳ࡭ࠢ࠻ࠤࡹ࡭ࡩ࡫࡯ࡱ࡮ࡤࡽࡪࡸ࠮ࡶࡵࡨࡱࡪࡪࡩࡢࡥࡲࡨࡪࡩࡳࡶࡴࡩࡥࡨ࡫ࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻࠳ࢀࠫଲ")))[l11l1_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࠦଳ")][l11l1_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦ଴")]
            if l1l1lll1l_opy_ == True:
                ret = dialog.yesno(l11l1_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨଵ"),l11l1_opy_ (u"ࠧࡘࡧࠣ࡬ࡦࡼࡥࠡ࡝ࡅࡡࡩ࡫ࡴࡦࡥࡷࡩࡩࡡ࠯ࡃ࡟ࠣࡷࡴࡳࡥࠡࡱࡩࠤࡾࡵࡵࡳࠢࡎࡳࡩ࡯ࠠࡷ࡫ࡧࡩࡴࠦࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠡࡣࡵࡩࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࡥࠢ࡬ࡲࠥࡧࠠࡸࡣࡼࠤࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞࡝ࡅࡡࡹ࡮ࡡࡵࠢࡦࡳࡺࡲࡤࠡࡥࡤࡹࡸ࡫ࠠࡴࡧࡹࡩࡷࡧ࡬ࠡ࡫ࡶࡷࡺ࡫ࡳࠢ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧଶ"),l11l1_opy_ (u"ࠨࡆࡲࠤࡾࡵࡵࠡࡹࡤࡲࡹࠦࡵࡴࠢࡷࡳࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࠡࡶ࡫ࡩࡸ࡫ࠠࡴࡧࡷࡸ࡮ࡴࡧࡴࠢࡩࡳࡷࠦࡹࡰࡷࠣࡪࡴࡸࠠࡢࠢ࡞ࡆࡢࡹ࡭ࡰࡱࡷ࡬ࠥ࡫ࡸࡱࡧࡵ࡭ࡪࡴࡣࡦࡁ࡞࠳ࡇࡣࠠ࡜ࡅࡒࡐࡔࡘࠠ࡭࡫ࡰࡩ࡬ࡸࡥࡦࡰࡠ࡟ࡇࡣࡔࡩ࡫ࡶࠤ࡮ࡹࠠࡩ࡫ࡪ࡬ࡱࡿࠠࡳࡧࡦࡳࡲࡳࡥ࡯ࡦࡨࡨࠦࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫଷ"),l11l1_opy_ (u"ࠩࠪସ"),l11l1_opy_ (u"ࠪ࡝ࡪࡹࠧହ"),l11l1_opy_ (u"ࠫࡓࡵࠧ଺"))
                if ret:
                    gui.ADDON.setSetting(l11l1_opy_ (u"ࠬࡹࡹࡴࡶࡨࡱࡸ࡫ࡴࡵ࡫ࡱ࡫ࡨ࡮ࡥࡤ࡭ࠪ଻"), l11l1_opy_ (u"ࠨࡴࡳࡷࡨ଼ࠦ"))
                    return False
                if not ret:
                    xbmc.executeJSONRPC(l11l1_opy_ (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡔࡧࡷࡸ࡮ࡴࡧࡴ࠰ࡖࡩࡹ࡙ࡥࡵࡶ࡬ࡲ࡬࡜ࡡ࡭ࡷࡨࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡷࡪࡺࡴࡪࡰࡪࠦ࠿ࠨࡶࡪࡦࡨࡳࡵࡲࡡࡺࡧࡵ࠲ࡺࡹࡥ࡮ࡧࡧ࡭ࡦࡩ࡯ࡥࡧࡦࡷࡺࡸࡦࡢࡥࡨࠦ࠱ࠦࠢࡷࡣ࡯ࡹࡪࠨ࠺ࡧࡣ࡯ࡷࡪࢃࠬࠣ࡫ࡧࠦ࠿࠷ࡽࠨଽ"))
                    xbmc.executeJSONRPC(l11l1_opy_ (u"ࠨࡽࠥ࡮ࡸࡵ࡮ࡳࡲࡦࠦ࠿ࠨ࠲࠯࠲ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠣࡕࡨࡸࡹ࡯࡮ࡨࡵ࠱ࡗࡪࡺࡓࡦࡶࡷ࡭ࡳ࡭ࡖࡢ࡮ࡸࡩࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡸ࡫ࡴࡵ࡫ࡱ࡫ࠧࡀࠢࡷ࡫ࡧࡩࡴࡶ࡬ࡢࡻࡨࡶ࠳ࡻࡳࡦ࡯ࡨࡨ࡮ࡧࡣࡰࡦࡨࡧࠧ࠲ࠠࠣࡸࡤࡰࡺ࡫ࠢ࠻ࡶࡵࡹࡪࢃࠬࠣ࡫ࡧࠦ࠿࠷ࡽࠨା"))
                    gui.ADDON.setSetting(l11l1_opy_ (u"ࠩࡶࡽࡸࡺࡥ࡮ࡵࡨࡸࡹ࡯࡮ࡨࡥ࡫ࡩࡨࡱࠧି"), l11l1_opy_ (u"ࠥࡸࡷࡻࡥࠣୀ"))
                    dialog.ok(l11l1_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞ࡔࡨࡰࡴࡧࡤࡦࡦࠣࡘ࡛ࠦࡇࡶ࡫ࡧࡩࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ୁ"),l11l1_opy_ (u"ࠬ࡝ࡥࠡࡪࡤࡺࡪ࡛ࠦࡄࡑࡏࡓࡗࠦ࡬ࡪ࡯ࡨ࡫ࡷ࡫ࡥ࡯࡟࡞ࡆࡢࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼ࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡩࡩࠦࡹࡰࡷࡵࠤࡐࡵࡤࡪࠢࡹ࡭ࡩ࡫࡯ࠡࡵࡨࡸࡹ࡯࡮ࡨࡵࠣࡳࡳࠦࡹࡰࡷࡵࠤࡧ࡫ࡨࡢ࡮ࡩࠤ࡫ࡵࡲࠡࡣࠣࡷࡲࡵ࡯ࡵࡪࠣࡩࡽࡶࡥࡳ࡫ࡨࡲࡨ࡫ࠡࠨୂ"),l11l1_opy_ (u"࠭ࠧୃ"),l11l1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡳࡧ࠰ࡰࡦࡻ࡮ࡤࡪࠣࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫ࠧୄ"))
                    return True
        except:
            dialog.ok(l11l1_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢࡘࡥ࡭ࡱࡤࡨࡪࡪࠠࡕࡘࠣࡋࡺ࡯ࡤࡦ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪ୅"),l11l1_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡵࡩࡩࡣࡅࡳࡴࡲࡶࠦࡡ࠯ࡄࡑࡏࡓࡗࡣࠠࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡ࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢࡡࡂ࡞ࡹࡵࡳࡳ࡭࡛࠰ࡄࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠥࡽࡩࡵࡪࠣࡧ࡭ࡧ࡮ࡨ࡫ࡱ࡫ࠥࡿ࡯ࡶࡴࠣࡏࡴࡪࡩࠡࡸ࡬ࡨࡪࡵࠠࡴࡧࡷࡸ࡮ࡴࡧࡴࠣࠪ୆"),l11l1_opy_ (u"ࠪࠫେ"),l11l1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤࡷ࡫ࡰࡰࡴࡷࠤࡹ࡮ࡩࡴࠢࡷࡳࠥࡵࡵࡳࠢࡩࡥࡨ࡫ࡢࡰࡱ࡮ࠤ࡬ࡸ࡯ࡶࡲࠣࡥࡳࡪࠠࡪࡰࡦࡰࡺࡪࡥࠡࡻࡲࡹࡷࠦࡤࡦࡸ࡬ࡧࡪࠦ࡭ࡰࡦࡨࡰࠦ࠭ୈ"))
            return False
class okok(object):
    def __init__(self, i):
        self.i = i
        self.l1l1l1ll1_opy_ = False
        self.l1l1lll11_opy_ = None
        self.l1l1l1l11_opy_ = False
        self.l1l1ll11l_opy_ = requests.session()
        self.username = lolol.lolu()
        self.password = lolol.lolp()
        self.isrs = self.checkrs()
        if not self.isrs:
            self.loggedin = self.l11ll11ll_opy_()
        self.NOTICE = xbmc.translatePath(os.path.join(l11l1_opy_ (u"ࠬࡹࡰࡦࡥ࡬ࡥࡱࡀ࠯࠰ࡪࡲࡱࡪ࠵ࡡࡥࡦࡲࡲࡸ࠵ࠧ୉") + addon_id,l11l1_opy_ (u"࠭ࡎࡐࡖࡌࡇࡊ࠴ࡴࡹࡶࠪ୊")))
        self.cookiefile = xbmc.translatePath(os.path.join(l11l1_opy_ (u"ࠧࡴࡲࡨࡧ࡮ࡧ࡬࠻࠱࠲ࡴࡷࡵࡦࡪ࡮ࡨࠫୋ"), l11l1_opy_ (u"ࠨࡣࡧࡨࡴࡴ࡟ࡥࡣࡷࡥࠬୌ"), l11l1_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡳࡶࡴ࡭ࡲࡢ࡯࠱ࡶࡪࡲ࡯ࡢࡦࡨࡨࡹࡼ୍ࠧ"), l11l1_opy_ (u"ࠪࡧࡴࡵ࡫ࡪࡧࠪ୎")))
        if self.loggedin:
            lolol.save_cookies(self.l1l1ll11l_opy_.cookies, self.cookiefile)
    def checkrs(self):
        rsdata = self.i.get_reloaded_account_info()
        rsinfo = rsdata[base64.b64decode(l11l1_opy_ (u"ࠦࡩ࡞ࡎ࡭ࡥ࡯࠽ࡵࡨ࡭࡛ࡸࠥ୏"))]
        l111_opy_ = rsinfo[base64.b64decode(l11l1_opy_ (u"ࠧ࡟ࡘࡗ࠲ࡤࡅࡂࡃࠢ୐"))]
        if l111_opy_ == 0:
            dialog = xbmcgui.Dialog()
            dialog.ok(l11l1_opy_ (u"ࠨ࡛ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠣ୑"), base64.b64decode(l11l1_opy_ (u"ࠢࡓ࡚ࡍࡽࡧ࠹ࡉࡩࡋࡄࡁࡂࠨ୒"))+l11l1_opy_ (u"ࠣࡔࡨࡰࡴࡧࡤࡦࡦࠣࡘ࡛ࠨ୓")+base64.b64decode(l11l1_opy_ (u"ࠤࡌࡉࡋࡰ࡙࠳࠻࠴ࡦࡳࡗࡧࡣ࡯࠼࠴ࡎࡍ࡚ࡷࡦ࡚࠹ࡰࡏࡑ࠾࠿ࠥ୔")), base64.b64decode(l11l1_opy_ (u"࡙ࠥࡌࡾ࡬࡚࡚ࡑࡰࡎࡍࡎࡰ࡜࡚ࡒࡷࡏࡈ࡭ࡸࡧ࡜ࡎ࡭ࡤ࡙ࡐ࡯ࡧࡲ࠻ࡨࡣ࡙ࡘ࡫ࡧ࠹ࡉࡨࡥࡊࡊࡿࡩ࠳ࡥࡸࡦࡱࡖ࡭ࡡࡘ࠶ࡪ࡞࠸࡜ࡰ࡛ࡉࡘ࡫ࡨ࠸ࡖ࠱ࡦࡊࡰࡺࡠ࠳ࡎ࠿ࠥ୕")), l11l1_opy_ (u"ࠦࠧୖ"))
            lklklklk = dialog.input(base64.b64decode(l11l1_opy_ (u"ࠬࡘࡗ࠶࠲࡝࡜ࡎ࡭ࠧୗ"))+l11l1_opy_ (u"ࠨࡒࡦ࡮ࡲࡥࡩ࡫ࡤࠡࡖ࡙ࠦ୘")+base64.b64decode(l11l1_opy_ (u"ࠢࡊࡈ࡙ࡾ࡟࡞ࡊࡶ࡛࡚࠵ࡱࠨ୙")), type=xbmcgui.INPUT_ALPHANUM)
            lklklkl = dialog.input(base64.b64decode(l11l1_opy_ (u"ࠨࡔ࡚࠹࠵ࡠࡘࡊࡩࠪ୚"))+l11l1_opy_ (u"ࠤࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠢ୛")+base64.b64decode(l11l1_opy_ (u"ࠥࡍࡋࡈࡨࡤ࠵ࡑ࠷ࡧ࠹ࡊ࡬ࠤଡ଼")), type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
            gui.ADDON.setSetting(base64.b64decode(l11l1_opy_ (u"ࠫࡨࡳࡖࡴࡤ࠵ࡊࡰࡠࡗࡒࡷࡧ࡜ࡓࡲࡣࡨ࠿ࡀࠫଢ଼")), lklklklk)
            gui.ADDON.setSetting(base64.b64decode(l11l1_opy_ (u"ࠬࡩ࡭ࡗࡵࡥ࠶ࡋࡱ࡚ࡘࡓࡸࡧࡌࡌࡺࡤࡹࡀࡁࠬ୞")), lklklkl)
            return False
        rsinfo = rsinfo[base64.b64decode(l11l1_opy_ (u"ࠨ࡚࡙ࡪࡺ࡜࠷ࡘࡨࡥࡉࡘࡁࠧୟ"))]
        if rsinfo:
            self.loggedin = True
            return True
        return False
    def l11ll11ll_opy_(self):
        username = lolol.lolu()
        password = lolol.lolp()
        if username != l11l1_opy_ (u"ࠧࠨୠ") and password != l11l1_opy_ (u"ࠨࠩୡ"):
            l1l111ll1_opy_      = l11l1_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࡰࡥࡾ࡬ࡡࡪࡴࡪࡹ࡮ࡪࡥࡴ࠰ࡦࡳࡲ࠵ࡰࡳࡱ࠲ࡻࡵ࠳࡬ࡰࡩ࡬ࡲ࠳ࡶࡨࡱࠩୢ")
            data  = {l11l1_opy_ (u"ࠪࡰࡴ࡭ࠧୣ") : username, l11l1_opy_ (u"ࠫࡵࡽࡤࠨ୤") : password, l11l1_opy_ (u"ࠬࡽࡰ࠮ࡵࡸࡦࡲ࡯ࡴࠨ୥"): l11l1_opy_ (u"࠭ࡌࡰࡩࠣࡍࡳ࠭୦")}
            try:
                lolol.show_busy_dialog()
                request  = self.l1l1ll11l_opy_.post(l1l111ll1_opy_, headers={l11l1_opy_ (u"ࠧࡖࡵࡨࡶ࠲ࡇࡧࡦࡰࡷࠫ୧"): (UA)}, data=data)
                content = request.content
                code = request.status_code
                self.l1l1lll11_opy_ = re.findall(l11l1_opy_ (u"ࡳࠩ࠳࠷࠽ࡁ࡟ࡸࡲࡱࡳࡳࡩࡥ࠾ࠪ࠱࠯ࡄ࠯ࠢ࠿ࡎࡲ࡫ࠥࡕࡵࡵ࠾࠲ࡥࡃࡂ࠯࡭࡫ࡁࠫ୨"), content)
                self.l1l1lll11_opy_ = l11l1_opy_ (u"ࠩࠪ୩").join(self.l1l1lll11_opy_)
                l1l1ll1ll_opy_ = re.findall(l11l1_opy_ (u"ࡵࠫࡳࡧ࡭ࡦ࠿ࠥࡻࡸࡥࡰ࡭ࡷࡪ࡭ࡳࡥ࡟ࡴ࠴ࡰࡩࡲࡨࡥࡳࡡࡳࡶࡴ࡬ࡩ࡭ࡧࡢࡰࡴ࡭ࡩ࡯ࠤࠣ࡭ࡩࡃࠢࡸࡵ࠰ࡴࡱࡻࡧࡪࡰ࠰࠱ࡸ࠸࡭ࡦ࡯ࡥࡩࡷ࠳ࡰࡳࡱࡩ࡭ࡱ࡫࠭࡭ࡱࡪ࡭ࡳࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡸࡵ࠰ࡴࡱࡻࡧࡪࡰ࠰࠱ࡸ࠸࡭ࡦ࡯ࡥࡩࡷ࠳ࡰࡳࡱࡩ࡭ࡱ࡫࠭ࡧ࡫ࡨࡰࡩࠦࡦࡰࡴࡰ࠱ࡨࡵ࡮ࡵࡴࡲࡰࠧࠦࡶࡢ࡮ࡸࡩࡂࠨࠨ࠯࠭ࡂ࠭ࠧࠦࡤࡪࡵࡤࡦࡱ࡫ࡤ࠾ࠩ୪"), content)
                l1l1ll1ll_opy_ = l11l1_opy_ (u"ࠫࠬ୫").join(l1l1ll1ll_opy_)
                lolol.hide_busy_dialog()
                if l11l1_opy_ (u"ࠬࡂ࡬ࡪࠢ࡬ࡨࡂࠨࡷࡱ࠯ࡤࡨࡲ࡯࡮࠮ࡤࡤࡶ࠲ࡲ࡯ࡨࡱࡸࡸࠧࡄࠧ୬") in content and l1l1ll1ll_opy_.lower() != self.username.lower():
                    dialog.ok(l11l1_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨ୭"),l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡠࡈ࡝࡚ࡱࡸࠤࡦࡸࡥࠡࡷࡶ࡭ࡳ࡭ࠠࡺࡱࡸࡶࠥ࡫࡭ࡢ࡫࡯ࠤࡦࡪࡤࡳࡧࡶࡷࠥࡧࡳࠡࡻࡲࡹࡷࠦࡕࡴࡧࡵࡲࡦࡳࡥࠢ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧ୮"),l11l1_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡥ࡮ࡣ࡬ࡰࠥࡧࡤࡥࡴࡨࡷࡸࠦࡩࡴࠢ࡞ࡇࡔࡒࡏࡓࠢࡵࡩࡩࡣ࡛ࡃ࡟ࡑࡓ࡙ࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠤࡾࡵࡵࡳࠢࡸࡷࡪࡸ࡮ࡢ࡯ࡨ࠰ࠥࡏࡦࠡࡻࡲࡹࠥ࡬࡯ࡳࡩࡲࡸࠥࡺࡨࡪࡵ࠯ࠤࡵࡲࡥࡢࡵࡨࠤࡨࡵ࡮ࡵࡣࡦࡸࠥࡻࡳࠢࠩ୯"),l11l1_opy_ (u"ࠩࠪ୰"))
                    return False
                if l11l1_opy_ (u"ࠪࡅࡨࡩࡥࡴࡵࠣࡉࡽࡶࡩࡳࡧࡧࠫୱ") in content or l11l1_opy_ (u"࡚ࠫࡴࡰࡢ࡫ࡧࠫ୲") in content:
                    dialog.ok(l11l1_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟ࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠠࡈࡷ࡬ࡨࡪࡡ࠯ࡄࡑࡏࡓࡗࡣࠧ୳"),l11l1_opy_ (u"࠭ࡉࡵࠢࡤࡴࡵ࡫ࡡࡳࡵࠣࡽࡴࡻࡲࠡࡩࡸ࡭ࡩ࡫ࠠࡴࡷࡥࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠦࡨࡢࡵࠣࡩࡽࡶࡩࡳࡧࡧࠥࠬ୴"),l11l1_opy_ (u"ࠧࠨ୵"),l11l1_opy_ (u"ࠨࠩ୶"))
                    return False
                elif l11l1_opy_ (u"ࠩࡱࡳ࠲ࡧࡣࡤࡧࡶࡷ࠲ࡸࡥࡥ࡫ࡵࡩࡨࡺࠧ୷") in content:
                    dialog.ok(l11l1_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝ࡓࡧ࡯ࡳࡦࡪࡥࡥࠢࡗ࡚ࠥࡍࡵࡪࡦࡨ࡟࠴ࡉࡏࡍࡑࡕࡡࠬ୸"),l11l1_opy_ (u"ࠫࡎࡺࠠࡢࡲࡳࡩࡦࡸࡳࠡࡻࡲࡹࡷࠦࡧࡶ࡫ࡧࡩࠥࡹࡵࡣࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠤࡲࡧࡹࠡࡪࡤࡺࡪࠦࡥࡹࡲ࡬ࡶࡪࡪࠠࡰࡴࠣࡽࡴࡻࠠࡩࡣࡹࡩࠥ࡫࡮ࡵࡧࡵࡩࡩࠦࡷࡳࡱࡱ࡫ࠥࡲ࡯ࡨ࡫ࡱࠤࡩ࡫ࡴࡢ࡫࡯ࡷ࠳࠭୹"),l11l1_opy_ (u"ࠬ࠭୺"),l11l1_opy_ (u"࠭ࡉࡧࠢࡼࡳࡺࠦࡦࡰࡴࡪࡳࡹࠦࡴࡩ࡫ࡶ࠰ࠥࡶ࡬ࡦࡣࡶࡩࠥࡩ࡯࡯ࡶࡤࡧࡹࠦࡵࡴࠣࠪ୻"))
                    lolol.l1ll11_opy_()
                    return False
                elif l11l1_opy_ (u"ࠧ࠽࡮࡬ࠤ࡮ࡪ࠽ࠣࡹࡳ࠱ࡦࡪ࡭ࡪࡰ࠰ࡦࡦࡸ࠭࡭ࡱࡪࡳࡺࡺࠢ࠿ࠩ୼") in content:
                    self.l1l1l1ll1_opy_ = True
                    self.loggedin = True
                    threading.Timer(1, self.l11ll1lll_opy_).start()
                    return True
                else:
                    l1l1ll1l1_opy_ = re.findall(l11l1_opy_ (u"ࡳࠩ࠿ࡸ࡮ࡺ࡬ࡦࡀࠫ࠲࠰ࡅࠩ࠽࠱ࡷ࡭ࡹࡲࡥ࠿ࠩ୽"), content)
                    l1l1ll1l1_opy_ = l11l1_opy_ (u"ࠩࠪ୾").join(l1l1ll1l1_opy_)
                    l1l1ll1l1_opy_ = l1l1ll1l1_opy_.replace(l11l1_opy_ (u"ࠪࡀࡸࡺࡲࡰࡰࡪࡂࠬ୿"),l11l1_opy_ (u"ࠫࠬ஀")).replace(l11l1_opy_ (u"ࠬࡂࡢࡳࠢ࠲ࡂࠬ஁"),l11l1_opy_ (u"࠭ࠧஂ")).replace(l11l1_opy_ (u"ࠧ࠽࠱ࡶࡸࡷࡵ࡮ࡨࡀࠪஃ"),l11l1_opy_ (u"ࠨࠩ஄"))
                    if l11l1_opy_ (u"ࠩࡳࡰࡪࡧࡳࡦࠢࡨࡱࡦ࡯࡬ࠨஅ") in content:
                        l1l1l111l_opy_ = re.findall(l11l1_opy_ (u"ࡵࠫࡁࡹࡴࡳࡱࡱ࡫ࡃ࠮࠮ࠬࡁࠬࡀࡦࠦࡣ࡭ࡣࡶࡷࡂࠨ࡟ࡠࡥࡩࡣࡪࡳࡡࡪ࡮ࡢࡣࠧ࠭ஆ"), content)
                        l1l1l111l_opy_ = l11l1_opy_ (u"ࠫࠬஇ").join(l1l1l111l_opy_)
                        l1l1l111l_opy_ = l1l1l111l_opy_.replace(l11l1_opy_ (u"ࠬࡶ࡬ࡦࡣࡶࡩࠥ࡫࡭ࡢ࡫࡯ࠤࠬஈ"),l11l1_opy_ (u"࠭ࡰ࡭ࡧࡤࡷࡪࠦࡣࡰࡰࡷࡥࡨࡺࠠࡶࡵࠪஉ"))
                    else:
                        l1l1l111l_opy_ = re.findall(l11l1_opy_ (u"ࡲࠨ࠾ࡶࡸࡷࡵ࡮ࡨࡀࠫ࠲࠰ࡅࠩ࠽࠱ࡥࡳࡩࡿ࠾ࠨஊ"), content)
                        l1l1l111l_opy_ = l11l1_opy_ (u"ࠨࠩ஋").join(l1l1l111l_opy_)
                    l1l1l111l_opy_ = l1l1l111l_opy_.replace(l11l1_opy_ (u"ࠩ࠿ࡷࡹࡸ࡯࡯ࡩࡁࠫ஌"),l11l1_opy_ (u"ࠪࠫ஍")).replace(l11l1_opy_ (u"ࠫࡁࡨࡲࠡ࠱ࡁࠫஎ"),l11l1_opy_ (u"ࠬ࠭ஏ")).replace(l11l1_opy_ (u"࠭࠼࠰ࡵࡷࡶࡴࡴࡧ࠿ࠩஐ"),l11l1_opy_ (u"ࠧࠨ஑"))
                    if l11l1_opy_ (u"ࠨ࠾ࡧ࡭ࡻࠦࡩࡥ࠿ࠥࡰࡴ࡭ࡩ࡯ࡡࡨࡶࡷࡵࡲࠣࡀࠪஒ") in content:
                        if l11l1_opy_ (u"ࠩ࠿ࡷࡹࡸ࡯࡯ࡩࡁࡉࡗࡘࡏࡓ࠾࠲ࡷࡹࡸ࡯࡯ࡩࡁ࠾ࠥࡓࡡࡹࠢࡶ࡭ࡲࡻ࡬ࡵࡣࡱࡩࡴࡻࡳࠡ࡮ࡲ࡫࡮ࡴࡳࠡࡨࡲࡶࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠧஓ") in content:
                            dialog.ok(l11l1_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝ࡓࡧ࡯ࡳࡦࡪࡥࡥࠢࡗ࡚ࠥࡍࡵࡪࡦࡨ࡟࠴ࡉࡏࡍࡑࡕࡡࠬஔ"),l11l1_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞࡝ࡅࡡࡑࡵࡧࡪࡰࠣࡉࡷࡸ࡯ࡳࠣࠣ࠱ࠥ࡟࡯ࡶࠢ࡫ࡥࡻ࡫ࠠࡦࡺࡦࡩࡪࡪࡥࡥࠢࡰࡥࡽࠦࠨ࠴ࠫࠣࡥࡱࡲ࡯ࡸࡣࡥࡰࡪࠦࡤࡦࡸ࡬ࡧࡪࡹ࠮࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭க"),l11l1_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡫ࡸࡪࡶࠣࡸ࡭࡫ࠠࡨࡷ࡬ࡨࡪࠦ࡯࡯ࠢࡲࡸ࡭࡫ࡲࠡࡦࡨࡺ࡮ࡩࡥࠩࡵࠬࠤࡴࡸࠠࡸࡣ࡬ࡸࠥ࠻ࠠ࡮࡫ࡱࡹࡹ࡫ࡳࠡࡣࡱࡨࠥࡺࡲࡺࠢࡤ࡫ࡦ࡯࡮ࠢࠢࡌࡪࠥࡿ࡯ࡶࠢࡷ࡬࡮ࡴ࡫ࠡࡶ࡫࡭ࡸࠦࡩࡴࠢࡺࡶࡴࡴࡧ࠭ࠢࡳࡰࡪࡧࡳࡦࠢࡦࡳࡳࡺࡡࡤࡶࠣࡹࡸࠧࠧ஖"),l11l1_opy_ (u"࠭ࠧ஗"))
                        else:
                            l1l1l111l_opy_ = re.findall(l11l1_opy_ (u"ࡲࠨ࠾ࡧ࡭ࡻࠦࡩࡥ࠿ࠥࡰࡴ࡭ࡩ࡯ࡡࡨࡶࡷࡵࡲࠣࡀࠫ࠲࠰ࡅࠩ࡝ࡰ࠿࠳ࡩ࡯ࡶ࠿ࠩ஘"), content)
                            l1l1l111l_opy_ = l11l1_opy_ (u"ࠨࠩங").join(l1l1l111l_opy_)
                            l1l1l111l_opy_ = l1l1l111l_opy_.replace(l11l1_opy_ (u"ࠩ࠿ࡷࡹࡸ࡯࡯ࡩࡁࠫச"),l11l1_opy_ (u"ࠪࠫ஛")).replace(l11l1_opy_ (u"ࠫࡁࡨࡲࠡ࠱ࡁࠫஜ"),l11l1_opy_ (u"ࠬ࠭஝")).replace(l11l1_opy_ (u"࠭࠼࠰ࡵࡷࡶࡴࡴࡧ࠿ࠩஞ"),l11l1_opy_ (u"ࠧࠨட")).replace(l11l1_opy_ (u"ࠨ࠾ࡤࠤ࡭ࡸࡥࡧ࠿ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࡱࡦࡿࡦࡢ࡫ࡵ࡫ࡺ࡯ࡤࡦࡵ࠱ࡧࡴࡳ࠯ࡱࡴࡲ࠳ࡼࡶ࠭࡭ࡱࡪ࡭ࡳ࠴ࡰࡩࡲࡂࡥࡨࡺࡩࡰࡰࡀࡰࡴࡹࡴࡱࡣࡶࡷࡼࡵࡲࡥࠤࡁࡐࡴࡹࡴࠡࡻࡲࡹࡷࠦࡰࡢࡵࡶࡻࡴࡸࡤࡀ࠾࠲ࡥࡃ࠭஠"),l11l1_opy_ (u"ࠩࠪ஡")).replace(l11l1_opy_ (u"ࠪࡉࡗࡘࡏࡓ࠼ࠪ஢"),l11l1_opy_ (u"ࠫࠬண"))
                            l1l1l111l_opy_ = l1l1l111l_opy_.strip()
                            if l11l1_opy_ (u"ࠬࡂࡳࡵࡴࡲࡲ࡬ࡄࡅࡓࡔࡒࡖࡁ࠵ࡳࡵࡴࡲࡲ࡬ࡄ࠺ࠡࡋࡱࡺࡦࡲࡩࡥࠢࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫத") in content:
                                dialog.ok(l11l1_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨ஥"), l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡠࡈ࡝ࡍࡱࡪ࡭ࡳࠦࡅࡳࡴࡲࡶࠦࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫ஦"),l1l1l111l_opy_.replace(l11l1_opy_ (u"ࠣࡡࡵࡩࡱࡵࡡࡥࡧࡧࡣࡦࡶࡩࠣ஧"),l11l1_opy_ (u"ࠩࠪந")),l11l1_opy_ (u"ࠪࠫன"))
                            elif l11l1_opy_ (u"࡙ࠫ࡮ࡥࠡࡲࡤࡷࡸࡽ࡯ࡳࡦࠣࡽࡴࡻࠠࡦࡰࡷࡩࡷ࡫ࡤࠡࡨࡲࡶࠥࡺࡨࡦࠢࡨࡱࡦ࡯࡬ࠡࡣࡧࡨࡷ࡫ࡳࡴࠩப") in content:
                                dialog.ok(l11l1_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟ࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠠࡈࡷ࡬ࡨࡪࡡ࠯ࡄࡑࡏࡓࡗࡣࠧ஫"), l11l1_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠ࡟ࡇࡣࡌࡰࡩ࡬ࡲࠥࡋࡲࡳࡱࡵࠥࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪ஬"),l11l1_opy_ (u"ࠧࡕࡪࡨࠤࡵࡧࡳࡴࡹࡲࡶࡩࠦࡹࡰࡷࠣࡩࡳࡺࡥࡳࡧࡧࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡫࡭ࡢ࡫࡯ࠤࡦࡪࡤࡳࡧࡶࡷࠥ࠭஭")+self.username.replace(l11l1_opy_ (u"ࠣࡡࡵࡩࡱࡵࡡࡥࡧࡧࡣࡦࡶࡩࠣம"),l11l1_opy_ (u"ࠩࠪய"))+l11l1_opy_ (u"ࠪࠤ࡮ࡹࠠࡪࡰࡦࡳࡷࡸࡥࡤࡶ࠱ࠫர"),l11l1_opy_ (u"ࠫࠬற"))
                            elif l11l1_opy_ (u"ࠬࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡥ࡮ࡣ࡬ࡰࠥࡧࡤࡥࡴࡨࡷࡸ࠭ல") in content:
                                dialog.ok(l11l1_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨள"), l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡠࡈ࡝ࡍࡱࡪ࡭ࡳࠦࡅࡳࡴࡲࡶࠦࠦ࠭ࠡࡋࡱࡺࡦࡲࡩࡥࠢࡨࡱࡦ࡯࡬ࠡࡣࡧࡨࡷ࡫ࡳࡴࠣ࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨழ"),l11l1_opy_ (u"ࠨࡋࡩࠤࡾࡵࡵࠡࡨࡲࡶ࡬ࡵࡴࠡࡶ࡫࡭ࡸ࠲ࠠࡱ࡮ࡨࡥࡸ࡫ࠠࡤࡱࡱࡸࡦࡩࡴࠡࡷࡶࠥࠬவ"),l11l1_opy_ (u"ࠩࠪஶ"))
                            else:
                                dialog.ok(l11l1_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝ࡓࡧ࡯ࡳࡦࡪࡥࡥࠢࡗ࡚ࠥࡍࡵࡪࡦࡨ࡟࠴ࡉࡏࡍࡑࡕࡡࠬஷ"), l11l1_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞࡝ࡅࡡࡑࡵࡧࡪࡰࠣࡉࡷࡸ࡯ࡳࠣ࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨஸ"),l1l1l111l_opy_.replace(l11l1_opy_ (u"ࠧࡥࡲࡦ࡮ࡲࡥࡩ࡫ࡤࡠࡣࡳ࡭ࠧஹ"),l11l1_opy_ (u"࠭ࠧ஺")),l11l1_opy_ (u"ࠧࠨ஻"))
                            if l11l1_opy_ (u"ࠨ࠾ࡶࡸࡷࡵ࡮ࡨࡀࡈࡖࡗࡕࡒ࠽࠱ࡶࡸࡷࡵ࡮ࡨࡀ࠽ࠤࡎࡴࡶࡢ࡮࡬ࡨࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠧ஼") in content or l11l1_opy_ (u"ࠩ࠿ࡷࡹࡸ࡯࡯ࡩࡁࡉࡗࡘࡏࡓ࠾࠲ࡷࡹࡸ࡯࡯ࡩࡁ࠾࡚ࠥࡨࡦࠢࡳࡥࡸࡹࡷࡰࡴࡧࠤࡾࡵࡵࠡࡧࡱࡸࡪࡸࡥࡥࠢࡩࡳࡷࠦࡴࡩࡧࠣࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ஽") in content:
                                lolol.l1ll11_opy_()
                        return False
                    else:
                        dialog.ok(l1l1ll1l1_opy_,l1l1l111l_opy_.replace(l11l1_opy_ (u"ࠥࡣࡷ࡫࡬ࡰࡣࡧࡩࡩࡥࡡࡱ࡫ࠥா"),l11l1_opy_ (u"ࠫࠬி")),l11l1_opy_ (u"ࠬ࠭ீ"),l11l1_opy_ (u"࠭ࠧு"))
                        return False
            except:
                lolol.hide_busy_dialog()
                import sys
                import traceback as tb
                (etype, value, traceback) = sys.exc_info()
                tb.print_exception(etype, value, traceback)
                dialog.ok(l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡗ࡫࡬ࡰࡣࡧࡩࡩࠦࡔࡗࠢࡊࡹ࡮ࡪࡥ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩூ"),l11l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠡࠡࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡨࡵ࡮࡯ࡧࡦࡸࠥࡺ࡯ࠡࡵࡨࡶࡻ࡫ࡲ࠯࠰࠱ࠫ௃"),l11l1_opy_ (u"ࠩࠪ௄"),l11l1_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣࡸࡷࡿࠠࡢࡩࡤ࡭ࡳࠦ࡬ࡢࡶࡨࡶ࠳࠭௅"))
                sys.exit(1)
        else:
            dialog.ok(l11l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠤࠤࡓࡵࠠࡶࡵࡨࡶࡳࡧ࡭ࡦࠢࡲࡶࠥࡶࡡࡴࡵࡺࡳࡷࡪ࠮ࠨெ"),l11l1_opy_ (u"ࠬࡘࡥ࡭ࡱࡤࡨࡪࡪࠠࡕࡘࠣࡋࡺ࡯ࡤࡦࠢࡵࡩࡶࡻࡩࡳࡧࡶࠤࡦࡴࠠࡢࡥࡷ࡭ࡻ࡫ࠠࡴࡷࡥࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠴ࠧே"),l11l1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡥ࡯ࡶࡨࡶࠥࡿ࡯ࡶࡴࠣࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠥࡧ࡮ࡥࠢࡳࡥࡸࡹࡷࡰࡴࡧ࠲ࠬை"),l11l1_opy_ (u"ࠧࠨ௉"))
            lolol.l1ll11_opy_()
            return False
    def logout(self, l1l1l11l1_opy_=False):
        if self.isrs:
            return
        while self.l1l1l1l11_opy_:
            xbmc.sleep(100)
        if self.l1l1l1ll1_opy_ == True:
            self.l1l1l1ll1_opy_ = False
        if self.l1l1lll11_opy_:
            try:
                request = self.l1l1ll11l_opy_.post(l11l1_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࡯ࡤࡽ࡫ࡧࡩࡳࡩࡸ࡭ࡩ࡫ࡳ࠯ࡥࡲࡱ࠴ࡶࡲࡰ࠱ࡺࡴ࠲ࡲ࡯ࡨ࡫ࡱ࠲ࡵ࡮ࡰࡀࡣࡦࡸ࡮ࡵ࡮࠾࡮ࡲ࡫ࡴࡻࡴࠧࡡࡺࡴࡳࡵ࡮ࡤࡧࡀࠫொ")+self.l1l1lll11_opy_)
                content = request.content
                self.l1l1ll11l_opy_.close()
                if not l11l1_opy_ (u"ࠩ࡜ࡳࡺࠦࡡࡳࡧࠣࡲࡴࡽࠠ࡭ࡱࡪ࡫ࡪࡪࠠࡰࡷࡷࠫோ") in content and not l1l1l11l1_opy_:
                    dialog.ok(l11l1_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝ࡓࡧ࡯ࡳࡦࡪࡥࡥࠢࡗ࡚ࠥࡍࡵࡪࡦࡨ࡟࠴ࡉࡏࡍࡑࡕࡡࠬௌ"),l11l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡰࡴ࡭ࡧࡪࡰࡪࠤࡴࡻࡴ்ࠢࠩ"),l11l1_opy_ (u"࡙ࠬ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫ࠥࡽࡩࡵࡪࠣࡰࡴ࡭࡯ࡶࡶࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࠬ௎"),l11l1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡲࡦࡲࡲࡶࡹࠦࡴࡩ࡫ࡶࠤࡹࡵࠠࡶࡵ࠱ࠫ௏"))
            except:
                if not l1l1l11l1_opy_:
                    import sys
                    import traceback as tb
                    (etype, value, traceback) = sys.exc_info()
                    tb.print_exception(etype, value, traceback)
                    dialog.ok(l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡗ࡫࡬ࡰࡣࡧࡩࡩࠦࡔࡗࠢࡊࡹ࡮ࡪࡥ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩௐ"),l11l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠ࡭ࡱࡪ࡫࡮ࡴࡧࠡࡱࡸࡸࠦ࠭௑"),l11l1_opy_ (u"ࠩࡆࡳࡳࡴࡥࡤࡶ࡬ࡳࡳࠦࡥࡳࡴࡲࡶ࠳࠭௒"),l11l1_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣࡶࡪࡶ࡯ࡳࡶࠣࡸ࡭࡯ࡳࠡࡶࡲࠤࡺࡹ࠮ࠨ௓"))
        else:
            if self.i is not None and not l1l1l11l1_opy_:
                dialog.ok(l11l1_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞ࡔࡨࡰࡴࡧࡤࡦࡦࠣࡘ࡛ࠦࡇࡶ࡫ࡧࡩࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭௔"),l11l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡱࡵࡧࡨ࡫ࡱ࡫ࠥࡵࡵࡵࠣࠪ௕"),l11l1_opy_ (u"࠭ࡎࡰࠢ࡯ࡳ࡬ࡵࡵࡵࠢࡩࡳࡺࡴࡤ࠯࠰ࠪ௖"),l11l1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡳࡧࡳࡳࡷࡺࠠࡵࡪ࡬ࡷࠥࡺ࡯ࠡࡷࡶ࠲ࠬௗ"))
    def l11ll1lll_opy_(self):
        while self.l1l1l1ll1_opy_ and self.loggedin and not self.l1l1l1l11_opy_ and not xbmc.abortRequested and not self.i.isClosing:
            xbmc.sleep(240000)
            if not self.l1l1l1ll1_opy_ or not self.loggedin or self.l1l1l1l11_opy_ or xbmc.abortRequested or self.i.isClosing:
                self.logout(True)
                break
            self.l1l1l1l11_opy_ = True
            l1l111ll1_opy_     = l11l1_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࡯ࡤࡽ࡫ࡧࡩࡳࡩࡸ࡭ࡩ࡫ࡳ࠯ࡥࡲࡱ࠴ࡶࡲࡰ࠱࡯ࡳ࡬࡭ࡥࡥ࡫ࡱ࠳ࠬ௘")
            try:
                request = self.l1l1ll11l_opy_.post(l1l111ll1_opy_)
            except:
                xbmc.log(l11l1_opy_ (u"ࠩࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠠࡈࡷ࡬ࡨࡪࡀࠠࡆࡴࡵࡳࡷࠦࡣࡰࡰࡱࡩࡨࡺࡩ࡯ࡩࠣࡸࡴࠦࡳࡦࡴࡹࡩࡷࠧࠠ࡬ࡧࡨࡴࠥࡧ࡬ࡪࡸࡨࠤ࠭࠷ࠩࠨ௙"), xbmc.LOGWARNING)
                self.l1l1l1ll1_opy_ = False
            content = request.content
            code    = request.status_code
            if l11l1_opy_ (u"ࠪࡗࡺࡩࡣࡦࡵࡶࠥࠥࡉࡵࡳࡴࡨࡲࡹࡲࡹࠡ࡮ࡲ࡫࡬࡫ࡤࠡ࡫ࡱࠥࠬ௚") in content:
                self.l1l1l1ll1_opy_ = True
            elif l11l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠤࠤࡈࡻࡲࡳࡧࡱࡸࡱࡿࠠ࡯ࡱࡷࠤࡱࡵࡧࡨࡧࡧࠤ࡮ࡴࠡࠨ௛") in content:
                xbmc.log(l11l1_opy_ (u"ࠬࡘࡥ࡭ࡱࡤࡨࡪࡪࠠࡕࡘࠣࡋࡺ࡯ࡤࡦ࠼ࠣࡉࡷࡸ࡯ࡳࠣࠣࡇࡺࡸࡲࡦࡰࡷࡰࡾࠦ࡮ࡰࡶࠣࡰࡴ࡭ࡧࡦࡦࠣ࡭ࡳࠧࠠ࡬ࡧࡨࡴࠥࡧ࡬ࡪࡸࡨࠤ࠭࠸ࠩࠨ௜"), xbmc.LOGWARNING)
                self.l1l1l1ll1_opy_ = False
            else:
                xbmc.log(l11l1_opy_ (u"࠭ࡒࡦ࡮ࡲࡥࡩ࡫ࡤࠡࡖ࡙ࠤࡌࡻࡩࡥࡧ࠽ࠤࡊࡸࡲࡰࡴࠤࠤࡘࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪ࠲࠳ࠦ࡫ࡦࡧࡳࠤࡦࡲࡩࡷࡧࠣࠬ࠸࠯ࠧ௝"), xbmc.LOGWARNING)
                self.l1l1l1ll1_opy_ = False
            self.l1l1l1l11_opy_ = False
    def l11llll1l_opy_(self, l1l11l1ll_opy_):
        class TextBox():
            WINDOW=10147
            CONTROL_LABEL=1
            CONTROL_TEXTBOX=5
            def __init__(self,*args,**kwargs):
                xbmc.executebuiltin(l11l1_opy_ (u"ࠢࡂࡥࡷ࡭ࡻࡧࡴࡦ࡙࡬ࡲࡩࡵࡷࠩࠧࡧ࠭ࠧ௞") % (self.WINDOW, ))
                self.win=xbmcgui.Window(self.WINDOW)
                xbmc.sleep(500)
                self.setControls()
            def setControls(self):
                self.win.getControl(self.CONTROL_LABEL).setLabel(l11l1_opy_ (u"ࠨࡎࡤࡸࡪࡹࡴࠡࡰࡨࡻࡸࠦࡦࡳࡱࡰࠤࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞ࡔࡨࡰࡴࡧࡤࡦࡦࠣࡘ࡛ࠦࡇࡶ࡫ࡧࡩࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭௟"))
                try: f=open(l1l11l1ll_opy_); text=f.read()
                except: text=l1l11l1ll_opy_
                self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
                return
        TextBox()
        while xbmc.getCondVisibility(l11l1_opy_ (u"࡚ࠩ࡭ࡳࡪ࡯ࡸ࠰ࡌࡷ࡛࡯ࡳࡪࡤ࡯ࡩ࠭࠷࠰࠲࠶࠺࠭ࠬ௠")):
            time.sleep(.5)
    def l1_opy_(self, url):
        try:
            lolol.show_busy_dialog()
            request = self.l1l1ll11l_opy_.post(url)
            data = request.content
            lolol.hide_busy_dialog()
            if l11l1_opy_ (u"ࠪࡀࡸࡺࡲࡰࡰࡪࡂ࠹࠶࠱࠻࠾࠲ࡷࡹࡸ࡯࡯ࡩࡁࠤࡘࡵࡲࡳࡻ࠯ࠤࡦࡩࡣࡦࡵࡶࠤࡩ࡫࡮ࡪࡧࡧࠫ௡") in data:
                dialog.ok(l11l1_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞ࡔࡨࡰࡴࡧࡤࡦࡦࠣࡘ࡛ࠦࡇࡶ࡫ࡧࡩࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭௢"),l11l1_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟࡞ࡆࡢࡒ࡯ࡨ࡫ࡱࠤࡊࡸࡲࡰࡴࠤࠤ࠲࡙ࠦࡰࡷࠣ࡬ࡦࡼࡥࠡࡧࡻࡧࡪ࡫ࡤࡦࡦࠣࡱࡦࡾࠠࠩ࠵ࠬࠤࡦࡲ࡬ࡰࡹࡤࡦࡱ࡫ࠠࡥࡧࡹ࡭ࡨ࡫ࡳࠡࡹ࡬ࡸ࡭ࠦࡴࡩࡧࠣ࡫ࡺ࡯ࡤࡦ࠰࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨ௣"),l11l1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡥࡹ࡫ࡷࠤࡹ࡮ࡥࠡࡩࡸ࡭ࡩ࡫ࠠࡰࡰࠣࡳࡹ࡮ࡥࡳࠢࡧࡩࡻ࡯ࡣࡦࠪࡶ࠭ࠥࡵࡲࠡࡹࡤ࡭ࡹࠦ࠵ࠡ࡯࡬ࡲࡺࡺࡥࡴࠢࡤࡲࡩࠦࡴࡳࡻࠣࡥ࡬ࡧࡩ࡯ࠣࠣࡍ࡫ࠦࡹࡰࡷࠣࡸ࡭࡯࡮࡬ࠢࡷ࡬࡮ࡹࠠࡪࡵࠣࡻࡷࡵ࡮ࡨ࠮ࠣࡴࡱ࡫ࡡࡴࡧࠣࡧࡴࡴࡴࡢࡥࡷࠤࡺࡹ࠮ࠨ௤"),l11l1_opy_ (u"ࠧࠨ௥"))
                self.i.close()
            if l11l1_opy_ (u"ࠨࡥ࡫ࡩࡨࡱ࡯ࡶࡶ࠰ࡪࡴࡸ࡭ࠨ௦") in data:
                dialog.ok(l11l1_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡵࡩࡩࡣࡒࡦ࡮ࡲࡥࡩ࡫ࡤࠡࡖ࡙ࠤࡌࡻࡩࡥࡧ࡞࠳ࡈࡕࡌࡐࡔࡠࠫ௧"),l11l1_opy_ (u"ࠪࡍࡹࠦࡡࡱࡲࡨࡥࡷࡹࠠࡺࡱࡸࡶࠥ࡭ࡵࡪࡦࡨࠤࡸࡻࡢࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠣࡱࡦࡿࠠࡩࡣࡹࡩࠥ࡫ࡸࡱ࡫ࡵࡩࡩࠦ࡯ࡳࠢࡼࡳࡺࠦࡨࡢࡸࡨࠤࡪࡴࡴࡦࡴࡨࡨࠥࡽࡲࡰࡰࡪࠤࡱࡵࡧࡪࡰࠣࡨࡪࡺࡡࡪ࡮ࡶ࠲ࠬ௨"),l11l1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤࡷ࡫࡭ࡦ࡯ࡥࡩࡷࠦࡹࡰࡷࡵࠤࡪࡳࡡࡪ࡮ࠣ࡭ࡸࠦࡎࡐࡖࠣࡽࡴࡻࡲࠡࡷࡶࡩࡷࡴࡡ࡮ࡧ࠱ࠫ௩"),l11l1_opy_ (u"ࠬ࠭௪"))
                yesno = dialog.yesno(l11l1_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨ௫"),l11l1_opy_ (u"ࠧࡅࡱࠣࡽࡴࡻࠠࡸ࡫ࡶ࡬ࠥࡺ࡯ࠡࡴࡨ࠱ࡪࡴࡴࡦࡴࠣࡽࡴࡻࡲࠡࡩࡸ࡭ࡩ࡫ࠠ࡭ࡱࡪ࡭ࡳࠦࡤࡦࡶࡤ࡭ࡱࡹࠠ࡯ࡱࡺࡃࠬ௬"),l11l1_opy_ (u"ࠨࠩ௭"),l11l1_opy_ (u"ࠩࠪ௮"))
                if yesno:
                    lolol.l1ll11_opy_()
                self.i.close()
            else:
                return data
        except requests.exceptions.SSLError:
            lolol.hide_busy_dialog()
            dialog.ok(l11l1_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝ࡓࡧ࡯ࡳࡦࡪࡥࡥࠢࡗ࡚ࠥࡍࡵࡪࡦࡨ࡟࠴ࡉࡏࡍࡑࡕࡡࠬ௯"),l11l1_opy_ (u"ࠫࡎࡺࠠࡢࡲࡳࡩࡦࡸࡳࠡࡻࡲࡹࡷࠦࡧࡶ࡫ࡧࡩࠥࡹࡵࡣࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠤࡲࡧࡹࠡࡪࡤࡺࡪࠦࡥࡹࡲ࡬ࡶࡪࡪࠠࡰࡴࠣࡽࡴࡻࠠࡩࡣࡹࡩࠥ࡫࡮ࡵࡧࡵࡩࡩࠦࡷࡳࡱࡱ࡫ࠥࡲ࡯ࡨ࡫ࡱࠤࡩ࡫ࡴࡢ࡫࡯ࡷ࠳࠭௰"),l11l1_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥࡸࡥ࡮ࡧࡰࡦࡪࡸࠠࡺࡱࡸࡶࠥ࡫࡭ࡢ࡫࡯ࠤ࡮ࡹࠠࡏࡑࡗࠤࡾࡵࡵࡳࠢࡸࡷࡪࡸ࡮ࡢ࡯ࡨ࠲ࠬ௱"),l11l1_opy_ (u"࠭ࠧ௲"))
            yesno = dialog.yesno(l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡗ࡫࡬ࡰࡣࡧࡩࡩࠦࡔࡗࠢࡊࡹ࡮ࡪࡥ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩ௳"),l11l1_opy_ (u"ࠨࡆࡲࠤࡾࡵࡵࠡࡹ࡬ࡷ࡭ࠦࡴࡰࠢࡵࡩ࠲࡫࡮ࡵࡧࡵࠤࡾࡵࡵࡳࠢࡪࡹ࡮ࡪࡥࠡ࡮ࡲ࡫࡮ࡴࠠࡥࡧࡷࡥ࡮ࡲࡳࠡࡰࡲࡻࡄ࠭௴"),l11l1_opy_ (u"ࠩࠪ௵"),l11l1_opy_ (u"ࠪࠫ௶"))
            if yesno:
                lolol.l1ll11_opy_()
            self.i.close()
    def l11lll_opy_(self, filePath):
        with open(filePath, l11l1_opy_ (u"ࠫࡷࡨࠧ௷")) as may:
            l11_opy_ = hashlib.md5()
            while True:
                data = may.read(8192).decode(l11l1_opy_ (u"ࠧ࡮ࡥࡹࠤ௸"))
                if not data:
                    break
                l11_opy_.update(data)
            return l11_opy_.hexdigest()
    def donotice(self):
        if not os.path.exists(self.NOTICE):
            if self.isrs:
                l1l1l1lll_opy_ = self.l1_opy_(lolol.lolrs(l11l1_opy_ (u"࠭ࡎࡐࡖࡌࡇࡊ࠴ࡩ࡯࡫ࠪ௹")))
            else:
                l1l1l1lll_opy_ = self.l1_opy_(lolol.lolf(l11l1_opy_ (u"ࠧࡏࡑࡗࡍࡈࡋ࠮ࡪࡰ࡬ࠫ௺")))
            if len(l1l1l1lll_opy_)>1:
                try:
                    l1l11l11l_opy_ = open(self.NOTICE, l11l1_opy_ (u"ࠣࡹࠥ௻"))
                    l1l11l11l_opy_.write(l1l1l1lll_opy_.encode(l11l1_opy_ (u"ࠤ࡫ࡩࡽࠨ௼")))
                    l1l11l11l_opy_.close()
                    f = open(self.NOTICE,mode=l11l1_opy_ (u"ࠪࡶࠬ௽")); msg = f.read(); f.close()
                    self.l11llll1l_opy_(l11l1_opy_ (u"ࠦࠪࡹࠢ௾") % msg.decode(l11l1_opy_ (u"ࠧ࡮ࡥࡹࠤ௿")))
                except: pass
        else:
            if self.isrs:
                l1l1l1111_opy_ = self.l1_opy_(lolol.lolrs(l11l1_opy_ (u"࠭ࡎࡐࡖࡌࡇࡊ࠴࡭ࡥ࠷ࠪఀ")))
            else:
                l1l1l1111_opy_ = self.l1_opy_(lolol.lolf(l11l1_opy_ (u"ࠧࡏࡑࡗࡍࡈࡋ࠮࡮ࡦ࠸ࠫఁ")))
            if len(l1l1l1111_opy_)>1:
                try:
                    if not l1l1l1111_opy_ == self.l11lll_opy_(self.NOTICE):
                        if self.isrs:
                            l1l1l1lll_opy_ = self.l1_opy_(lolol.lolrs(l11l1_opy_ (u"ࠨࡐࡒࡘࡎࡉࡅ࠯࡫ࡱ࡭ࠬం")))
                        else:
                            l1l1l1lll_opy_ = self.l1_opy_(lolol.lolf(l11l1_opy_ (u"ࠩࡑࡓ࡙ࡏࡃࡆ࠰࡬ࡲ࡮࠭ః")))
                        l1l11l11l_opy_ = open(self.NOTICE, l11l1_opy_ (u"ࠥࡻࠧఄ"))
                        l1l11l11l_opy_.write(l1l1l1lll_opy_.encode(l11l1_opy_ (u"ࠦ࡭࡫ࡸࠣఅ")))
                        l1l11l11l_opy_.close()
                        f = open(self.NOTICE,mode=l11l1_opy_ (u"ࠬࡸࠧఆ")); msg = f.read(); f.close()
                        self.l11llll1l_opy_(l11l1_opy_ (u"ࠨࠥࡴࠤఇ") % msg.decode(l11l1_opy_ (u"ࠢࡩࡧࡻࠦఈ")))
                except: pass
    def l1l11l1l1_opy_(self):
        if self.isrs:
            return
        l1l111ll1_opy_      = l11l1_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࡯ࡤࡽ࡫ࡧࡩࡳࡩࡸ࡭ࡩ࡫ࡳ࠯ࡥࡲࡱ࠴ࡶࡲࡰ࠱ࡤࡧࡨࡵࡵ࡯ࡶ࠲ࠫఉ")
        try:
            lolol.show_busy_dialog()
            request = self.l1l1ll11l_opy_.post(l1l111ll1_opy_)
            l1l11l111_opy_ = request.content
            l1ll11111_opy_ = re.findall(l11l1_opy_ (u"ࡴࠪࡺࡦࡲࡵࡦ࠿ࠥࠬ࠳࠱࠿ࠪࠤࠣࡲࡦࡳࡥ࠾ࠤࡺࡷࡤࡶ࡬ࡶࡩ࡬ࡲࡤࡥࡳ࠳࡯ࡨࡱࡧ࡫ࡲࡠࡲࡵࡳ࡫࡯࡬ࡦࡡࡸࡷࡪࡸ࡟ࡤࡷࡶࡸࡴࡳ࡟࡭࡫ࡱࡩࡺࡶࠢࠡ࡫ࡧࡁࠧࡽࡳ࠮ࡲ࡯ࡹ࡬࡯࡮࠮࠯ࡶ࠶ࡲ࡫࡭ࡣࡧࡵ࠱ࡵࡸ࡯ࡧ࡫࡯ࡩ࠲ࡻࡳࡦࡴ࠰ࡧࡺࡹࡴࡰ࡯࠰ࡰ࡮ࡴࡥࡶࡲࠥࠫఊ"), l1l11l111_opy_)
            l1ll11111_opy_ = l11l1_opy_ (u"ࠪࠫఋ").join(l1ll11111_opy_)
            l1ll11111_opy_ = l1ll11111_opy_.replace(l11l1_opy_ (u"ࠫࠫࡷࡵࡰࡶ࠾ࠫఌ"),l11l1_opy_ (u"ࠬࠨࠧ఍"))
            try:
                l1l1ll111_opy_ = json.loads(l1ll11111_opy_)
            except ValueError as e:
                if str(e) == l11l1_opy_ (u"࠭ࡎࡰࠢࡍࡗࡔࡔࠠࡰࡤ࡭ࡩࡨࡺࠠࡤࡱࡸࡰࡩࠦࡢࡦࠢࡧࡩࡨࡵࡤࡦࡦࠪఎ"):
                    lolol.hide_busy_dialog()
                    return None
            for id,weight,visible in l1l1ll111_opy_:
                id = id.decode(l11l1_opy_ (u"ࠢࡩࡧࡻࠦఏ"))
                if id == l11l1_opy_ (u"ࠨࡖ࡬ࡱࡪࠦࡕࡱࡦࡤࡸࡪࡪࠧఐ"):
                    lolol.hide_busy_dialog()
                    return weight
                else:
                    lolol.hide_busy_dialog()
                    return None
        except:
            lolol.hide_busy_dialog()
            import sys
            import traceback as tb
            (etype, value, traceback) = sys.exc_info()
            tb.print_exception(etype, value, traceback)
            dialog.ok(l11l1_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡵࡩࡩࡣࡒࡦ࡮ࡲࡥࡩ࡫ࡤࠡࡖ࡙ࠤࡌࡻࡩࡥࡧ࡞࠳ࡈࡕࡌࡐࡔࡠࠫ఑"),l11l1_opy_ (u"ࠪࡗࡴࡳࡥࡵࡪ࡬ࡲ࡬ࠦࡷࡦࡰࡷࠤࡼࡸ࡯࡯ࡩࠣࡻ࡮ࡺࡨࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡧࡺࡹࡴࡰ࡯ࠣࡰ࡮ࡴࡥࡶࡲࠣࡸ࡮ࡳࡥࠡࡦࡤࡸࡦࠦࡦࡳࡱࡰࠤࡦࡩࡣࡰࡷࡱࡸ࠳࠭ఒ"),l11l1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤࡹࡸࡹࠡࡣࡪࡥ࡮ࡴࠬࠡࡱࡵࠤࡷ࡫ࡰࡰࡴࡷࠤࡹ࡮ࡩࡴࠢࡥࡹ࡬ࠦࡴࡰࠢࡸࡷ࠳࠭ఓ"))
            return None
    def l1l111lll_opy_(self):
        if self.isrs:
            return
        l1l111ll1_opy_      = l11l1_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴ࡳࡡࡺࡨࡤ࡭ࡷ࡭ࡵࡪࡦࡨࡷ࠳ࡩ࡯࡮࠱ࡳࡶࡴ࠵ࡡࡤࡥࡲࡹࡳࡺ࠯ࠨఔ")
        try:
            request = self.l1l1ll11l_opy_.post(l1l111ll1_opy_)
            l1l11l111_opy_ = request.content
            l1ll11111_opy_ = re.findall(l11l1_opy_ (u"ࡸࠧࡷࡣ࡯ࡹࡪࡃࠢࠩ࠰࠮ࡃ࠮ࠨࠠ࡯ࡣࡰࡩࡂࠨࡷࡴࡡࡳࡰࡺ࡭ࡩ࡯ࡡࡢࡷ࠷ࡳࡥ࡮ࡤࡨࡶࡤࡶࡲࡰࡨ࡬ࡰࡪࡥࡵࡴࡧࡵࡣࡨࡻࡳࡵࡱࡰࡣࡱ࡯࡮ࡦࡷࡳࠦࠥ࡯ࡤ࠾ࠤࡺࡷ࠲ࡶ࡬ࡶࡩ࡬ࡲ࠲࠳ࡳ࠳࡯ࡨࡱࡧ࡫ࡲ࠮ࡲࡵࡳ࡫࡯࡬ࡦ࠯ࡸࡷࡪࡸ࠭ࡤࡷࡶࡸࡴࡳ࠭࡭࡫ࡱࡩࡺࡶࠢࠨక"), l1l11l111_opy_)
            l1ll11111_opy_ = l11l1_opy_ (u"ࠧࠨఖ").join(l1ll11111_opy_)
            l1ll11111_opy_ = l1ll11111_opy_.replace(l11l1_opy_ (u"ࠨࠨࡴࡹࡴࡺ࠻ࠨగ"),l11l1_opy_ (u"ࠩࠥࠫఘ"))
            l1l1ll111_opy_ = json.loads(l1ll11111_opy_)
            self.i.kek.setCustomLineUp(l1l1ll111_opy_)
        except:
            import sys
            import traceback as tb
            (etype, value, traceback) = sys.exc_info()
            tb.print_exception(etype, value, traceback)
            dialog.ok(l11l1_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝ࡓࡧ࡯ࡳࡦࡪࡥࡥࠢࡗ࡚ࠥࡍࡵࡪࡦࡨ࡟࠴ࡉࡏࡍࡑࡕࡡࠬఙ"),l11l1_opy_ (u"ࠫࡘࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪࠤࡼ࡯ࡴࡩࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡨࡻࡳࡵࡱࡰࠤࡱ࡯࡮ࡦࡷࡳࠤࡩࡧࡴࡢࠢࡩࡶࡴࡳࠠࡢࡥࡦࡳࡺࡴࡴ࠯ࠩచ"),l11l1_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥࡺࡲࡺࠢࡤ࡫ࡦ࡯࡮࠭ࠢࡲࡶࠥࡸࡥࡱࡱࡵࡸࠥࡺࡨࡪࡵࠣࡦࡺ࡭ࠠࡵࡱࠣࡹࡸ࠴ࠧఛ"))
    def submituserlineup(self):
        if self.isrs:
            return
        l1l111ll1_opy_      = l11l1_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵࡭ࡢࡻࡩࡥ࡮ࡸࡧࡶ࡫ࡧࡩࡸ࠴ࡣࡰ࡯࠲ࡴࡷࡵ࠯ࡢࡥࡦࡳࡺࡴࡴ࠰ࠩజ")
        l1l111111_opy_ = self.i.kek.getCustomLineUp()
        try:
            request = self.l1l1ll11l_opy_.post(l1l111ll1_opy_)
            l1l11l111_opy_ = request.content
            l1l1l11ll_opy_ = re.findall(l11l1_opy_ (u"ࡲࠨࡰࡤࡱࡪࡃࠢࡸࡵࡢࡴࡱࡻࡧࡪࡰࡢࡣࡸ࠸࡭ࡦ࡯ࡥࡩࡷࡥࡰࡳࡱࡩ࡭ࡱ࡫࡟ࡥ࡫ࡶࡴࡱࡧࡹࡠࡰࡤࡱࡪࠨࠠࡪࡦࡀࠦࡼࡹ࠭ࡱ࡮ࡸ࡫࡮ࡴ࠭࠮ࡵ࠵ࡱࡪࡳࡢࡦࡴ࠰ࡴࡷࡵࡦࡪ࡮ࡨ࠱ࡩ࡯ࡳࡱ࡮ࡤࡽ࠲ࡴࡡ࡮ࡧࠥࠤࡨࡲࡡࡴࡵࡀࠦࡼࡹ࠭ࡱ࡮ࡸ࡫࡮ࡴ࠭࠮ࡵ࠵ࡱࡪࡳࡢࡦࡴ࠰ࡴࡷࡵࡦࡪ࡮ࡨ࠱࡫࡯ࡥ࡭ࡦࠣࡪࡴࡸ࡭࠮ࡥࡲࡲࡹࡸ࡯࡭ࠤࠣࡺࡦࡲࡵࡦ࠿ࠥࠬ࠳࠱࠿ࠪࠤࠣࡸࡦࡨࡩ࡯ࡦࡨࡼࡂ࠭ఝ"), l1l11l111_opy_)
            l1l1l11ll_opy_ = l11l1_opy_ (u"ࠨࠩఞ").join(l1l1l11ll_opy_)
            email = re.findall(l11l1_opy_ (u"ࡴࠪࡲࡦࡳࡥ࠾ࠤࡺࡷࡤࡶ࡬ࡶࡩ࡬ࡲࡤࡥࡳ࠳࡯ࡨࡱࡧ࡫ࡲࡠࡲࡵࡳ࡫࡯࡬ࡦࡡࡨࡱࡦ࡯࡬ࠣࠢ࡬ࡨࡂࠨࡷࡴ࠯ࡳࡰࡺ࡭ࡩ࡯࠯࠰ࡷ࠷ࡳࡥ࡮ࡤࡨࡶ࠲ࡶࡲࡰࡨ࡬ࡰࡪ࠳ࡥ࡮ࡣ࡬ࡰࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡷࡴ࠯ࡳࡰࡺ࡭ࡩ࡯࠯࠰ࡷ࠷ࡳࡥ࡮ࡤࡨࡶ࠲ࡶࡲࡰࡨ࡬ࡰࡪ࠳ࡦࡪࡧ࡯ࡨࠥ࡬࡯ࡳ࡯࠰ࡧࡴࡴࡴࡳࡱ࡯ࠦࠥࡼࡡ࡭ࡷࡨࡁࠧ࠮࠮ࠬࡁࠬࠦࠥࡺࡡࡣ࡫ࡱࡨࡪࡾ࠽ࠨట"), l1l11l111_opy_)
            email = l11l1_opy_ (u"ࠪࠫఠ").join(email)
            l1l1l1l1l_opy_ = re.findall(l11l1_opy_ (u"ࡶࠬࡴࡡ࡮ࡧࡀࠦࡼࡹ࡟ࡱ࡮ࡸ࡫࡮ࡴ࡟ࡠࡵ࠵ࡱࡪࡳࡢࡦࡴࡢࡴࡷࡵࡦࡪ࡮ࡨࡣ࡫࡯ࡲࡴࡶࡢࡲࡦࡳࡥࠣࠢ࡬ࡨࡂࠨࡷࡴ࠯ࡳࡰࡺ࡭ࡩ࡯࠯࠰ࡷ࠷ࡳࡥ࡮ࡤࡨࡶ࠲ࡶࡲࡰࡨ࡬ࡰࡪ࠳ࡦࡪࡴࡶࡸ࠲ࡴࡡ࡮ࡧࠥࠤࡨࡲࡡࡴࡵࡀࠦࡼࡹ࠭ࡱ࡮ࡸ࡫࡮ࡴ࠭࠮ࡵ࠵ࡱࡪࡳࡢࡦࡴ࠰ࡴࡷࡵࡦࡪ࡮ࡨ࠱࡫࡯ࡥ࡭ࡦࠣࡪࡴࡸ࡭࠮ࡥࡲࡲࡹࡸ࡯࡭ࠤࠣࡺࡦࡲࡵࡦ࠿ࠥࠬ࠳࠱࠿ࠪࠤࠣࡸࡦࡨࡩ࡯ࡦࡨࡼࡂ࠭డ"), l1l11l111_opy_)
            l1l1l1l1l_opy_ = l11l1_opy_ (u"ࠬ࠭ఢ").join(l1l1l1l1l_opy_)
            l1ll1111l_opy_ = re.findall(l11l1_opy_ (u"ࡸࠧ࡯ࡣࡰࡩࡂࠨࡷࡴࡡࡳࡰࡺ࡭ࡩ࡯ࡡࡢࡷ࠷ࡳࡥ࡮ࡤࡨࡶࡤࡶࡲࡰࡨ࡬ࡰࡪࡥ࡬ࡢࡵࡷࡣࡳࡧ࡭ࡦࠤࠣ࡭ࡩࡃࠢࡸࡵ࠰ࡴࡱࡻࡧࡪࡰ࠰࠱ࡸ࠸࡭ࡦ࡯ࡥࡩࡷ࠳ࡰࡳࡱࡩ࡭ࡱ࡫࠭࡭ࡣࡶࡸ࠲ࡴࡡ࡮ࡧࠥࠤࡨࡲࡡࡴࡵࡀࠦࡼࡹ࠭ࡱ࡮ࡸ࡫࡮ࡴ࠭࠮ࡵ࠵ࡱࡪࡳࡢࡦࡴ࠰ࡴࡷࡵࡦࡪ࡮ࡨ࠱࡫࡯ࡥ࡭ࡦࠣࡪࡴࡸ࡭࠮ࡥࡲࡲࡹࡸ࡯࡭ࠤࠣࡺࡦࡲࡵࡦ࠿ࠥࠬ࠳࠱࠿ࠪࠤࠣࡸࡦࡨࡩ࡯ࡦࡨࡼࡂ࠭ణ"), l1l11l111_opy_)
            l1ll1111l_opy_ = l11l1_opy_ (u"ࠧࠨత").join(l1ll1111l_opy_)
            save = re.findall(l11l1_opy_ (u"ࡳࠩࡱࡥࡲ࡫࠽ࠣࡹࡶࡣࡵࡲࡵࡨ࡫ࡱࡣࡤࡹ࠲࡮ࡧࡰࡦࡪࡸ࡟ࡱࡴࡲࡪ࡮ࡲࡥࡠࡵࡤࡺࡪࠨࠠࡪࡦࡀࠦࡼࡹ࠭ࡱ࡮ࡸ࡫࡮ࡴ࠭࠮ࡵ࠵ࡱࡪࡳࡢࡦࡴ࠰ࡴࡷࡵࡦࡪ࡮ࡨ࠱ࡸࡧࡶࡦࠤࠣࡺࡦࡲࡵࡦ࠿ࠥࠬ࠳࠱࠿ࠪࠤࠣ࠳ࡃ࠭థ"), l1l11l111_opy_)
            save = l11l1_opy_ (u"ࠩࠪద").join(save)
            l11lllll1_opy_ = re.findall(l11l1_opy_ (u"ࡵࠫࡳࡧ࡭ࡦ࠿ࠥࡻࡸࡥࡰ࡭ࡷࡪ࡭ࡳࡥ࡟ࡴ࠴ࡰࡩࡲࡨࡥࡳࡡࡶࡧࡤࡶࡲࡰࡨ࡬ࡰࡪࡥࡳࡢࡸࡨࠦࠥ࡯ࡤ࠾ࠤࡺࡷ࠲ࡶ࡬ࡶࡩ࡬ࡲ࠲࠳ࡳ࠳࡯ࡨࡱࡧ࡫ࡲ࠮ࡵࡦ࠱ࡵࡸ࡯ࡧ࡫࡯ࡩ࠲ࡹࡡࡷࡧࠥࠤࡻࡧ࡬ࡶࡧࡀࠦ࠭࠴ࠫࡀࠫࠥࠤ࠴ࡄࠧధ"), l1l11l111_opy_)
            l11lllll1_opy_ = l11l1_opy_ (u"ࠫࠬన").join(l11lllll1_opy_)
            data  = {l11l1_opy_ (u"ࠬࡽࡳࡠࡲ࡯ࡹ࡬࡯࡮ࡠࡡࡶ࠶ࡲ࡫࡭ࡣࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࡤ࡫࡭ࡢ࡫࡯ࠫ఩") : email, l11l1_opy_ (u"࠭ࡷࡴࡡࡳࡰࡺ࡭ࡩ࡯ࡡࡢࡷ࠷ࡳࡥ࡮ࡤࡨࡶࡤࡶࡲࡰࡨ࡬ࡰࡪࡥࡦࡪࡴࡶࡸࡤࡴࡡ࡮ࡧࠪప") : l1l1l1l1l_opy_, l11l1_opy_ (u"ࠧࡸࡵࡢࡴࡱࡻࡧࡪࡰࡢࡣࡸ࠸࡭ࡦ࡯ࡥࡩࡷࡥࡰࡳࡱࡩ࡭ࡱ࡫࡟࡭ࡣࡶࡸࡤࡴࡡ࡮ࡧࠪఫ") : l1ll1111l_opy_, l11l1_opy_ (u"ࠨࡹࡶࡣࡵࡲࡵࡨ࡫ࡱࡣࡤࡹ࠲࡮ࡧࡰࡦࡪࡸ࡟ࡱࡴࡲࡪ࡮ࡲࡥࡠࡦ࡬ࡷࡵࡲࡡࡺࡡࡱࡥࡲ࡫ࠧబ") : l1l1l11ll_opy_, l11l1_opy_ (u"ࠩࡺࡷࡤࡶ࡬ࡶࡩ࡬ࡲࡤࡥࡳ࠳࡯ࡨࡱࡧ࡫ࡲࡠࡲࡵࡳ࡫࡯࡬ࡦࡡࡸࡷࡪࡸ࡟ࡤࡷࡶࡸࡴࡳ࡟࡭࡫ࡱࡩࡺࡶࠧభ") : l1l111111_opy_, l11l1_opy_ (u"ࠪࡻࡸࡥࡰ࡭ࡷࡪ࡭ࡳࡥ࡟ࡴ࠴ࡰࡩࡲࡨࡥࡳࡡࡳࡶࡴ࡬ࡩ࡭ࡧࡢࡴࡦࡹࡳࡸࡱࡵࡨ࠶࠭మ") : l11l1_opy_ (u"ࠫࠬయ"), l11l1_opy_ (u"ࠬࡽࡳࡠࡲ࡯ࡹ࡬࡯࡮ࡠࡡࡶ࠶ࡲ࡫࡭ࡣࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࡤࡶࡡࡴࡵࡺࡳࡷࡪ࠲ࠨర") : l11l1_opy_ (u"࠭ࠧఱ"), l11l1_opy_ (u"ࠧࡸࡵࡢࡴࡱࡻࡧࡪࡰࡢࡣࡸ࠸࡭ࡦ࡯ࡥࡩࡷࡥࡳࡤࡡࡳࡶࡴ࡬ࡩ࡭ࡧࡢࡷࡦࡼࡥࠨల") : l11lllll1_opy_, l11l1_opy_ (u"ࠨࡹࡶࡣࡵࡲࡵࡨ࡫ࡱࡣࡤࡹ࠲࡮ࡧࡰࡦࡪࡸ࡟ࡱࡴࡲࡪ࡮ࡲࡥࡠࡵࡤࡺࡪ࠭ళ") : save}
            request  = self.l1l1ll11l_opy_.post(l1l111ll1_opy_, data=data)
        except:
            import sys
            import traceback as tb
            (etype, value, traceback) = sys.exc_info()
            tb.print_exception(etype, value, traceback)
            dialog.ok(l11l1_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡵࡩࡩࡣࡒࡦ࡮ࡲࡥࡩ࡫ࡤࠡࡖ࡙ࠤࡌࡻࡩࡥࡧ࡞࠳ࡈࡕࡌࡐࡔࡠࠫఴ"),l11l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠣࠣࡗࡴࡳࡥࡵࡪ࡬ࡲ࡬ࠦࡷࡦࡰࡷࠤࡼࡸ࡯࡯ࡩࠣࡻ࡮ࡺࡨࠡࡵࡸࡦࡲ࡯ࡴࡵ࡫ࡱ࡫ࠥࡩࡵࡴࡶࡲࡱࠥࡲࡩ࡯ࡧࡸࡴࠥࡪࡡࡵࡣࠣࡸࡴࠦࡡࡤࡥࡲࡹࡳࡺ࠮ࠨవ"),l11l1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤࡹࡸࡹࠡࡣࡪࡥ࡮ࡴࠬࠡࡱࡵࠤࡷ࡫ࡰࡰࡴࡷࠤࡹ࡮ࡩࡴࠢࡥࡹ࡬ࠦࡴࡰࠢࡸࡷ࠳࠭శ"))
    def doacclu(self):
        if self.isrs:
            return
        l1l11ll1l_opy_ = self.l1l11l1l1_opy_()
        if gui.ADDON.getSetting(l11l1_opy_ (u"ࠬࡧࡣࡤ࡮ࡸࠫష")) == l11l1_opy_ (u"࠭ࡴࡳࡷࡨࠫస"):
            if gui.ADDON.getSetting(l11l1_opy_ (u"ࠧࡤࡪࡱࡳࡷࡪࡥࡳࠩహ")) == l11l1_opy_ (u"ࠨࡅࡸࡷࡹࡵ࡭ࠨ఺") and not l1l11ll1l_opy_:
                self.submituserlineup()
            if gui.ADDON.getSetting(l11l1_opy_ (u"ࠩࡤࡧࡨࡲࡵ࡭ࡣࡶࡸࡺࡶࡤࡢࡶࡨࠫ఻")) != l1l11ll1l_opy_ and l1l11ll1l_opy_ is not None or gui.ADDON.getSetting(l11l1_opy_ (u"ࠪࡧ࡭ࡴ࡯ࡳࡦࡨࡶ఼ࠬ")) != l11l1_opy_ (u"ࠫࡈࡻࡳࡵࡱࡰࠫఽ") and l1l11ll1l_opy_ is not None:
                self.l1l111lll_opy_()