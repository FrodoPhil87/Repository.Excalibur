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
import xbmc
import xbmcaddon
import base64
import xbmcgui
import time
import os
import requests
import urllib
import urllib2
import json
import cfscrape
import pickle
import sys
import re
import hashlib
ADDONID     = l11l1_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡵࡸ࡯ࡨࡴࡤࡱ࠳ࡸࡥ࡭ࡱࡤࡨࡪࡪࡴࡷࠩࠀ")
ADDON       =  xbmcaddon.Addon(ADDONID)
cookiefile 	= xbmc.translatePath(os.path.join(l11l1_opy_ (u"ࠬࡹࡰࡦࡥ࡬ࡥࡱࡀ࠯࠰ࡲࡵࡳ࡫࡯࡬ࡦࠩࠁ"), l11l1_opy_ (u"࠭ࡡࡥࡦࡲࡲࡤࡪࡡࡵࡣࠪࠂ"), l11l1_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡱࡴࡲ࡫ࡷࡧ࡭࠯ࡴࡨࡰࡴࡧࡤࡦࡦࡷࡺࠬࠃ"), l11l1_opy_ (u"ࠨࡥࡲࡳࡰ࡯ࡥࠨࠄ")))
b           = base64.b64decode
dialog      = xbmcgui.Dialog()
PROFILE     =  xbmc.translatePath(ADDON.getAddonInfo(l11l1_opy_ (u"ࠩࡳࡶࡴ࡬ࡩ࡭ࡧࠪࠅ")))
usrsetting  = os.path.join(PROFILE)
addonini    = xbmc.translatePath(os.path.join(usrsetting, l11l1_opy_ (u"ࠪࡥࡩࡪ࡯࡯ࡵ࠱࡭ࡳ࡯ࠧࠆ")))
UA          = base64.b64decode(l11l1_opy_ (u"࡛ࠫ࡞ࡎ࡭ࡥ࡬࠵ࡇࡠ࠲ࡗࡷࡧࡇ࠶ࡔ࡙࡙࡮ࡰ࡝࡜ࡲࡹࡖࡈࡍࡔࠬࠇ")) + l11l1_opy_ (u"ࠧࡘࡥ࡭ࡱࡤࡨࡪࡪࠠࡕࡘࠥࠈ")
addonbase   = base64.b64decode(l11l1_opy_ (u"࠭ࡣࡈࡺ࠴࡞࠷ࡲࡵࡍࡰࡅࡽࡧ࠸ࡤࡺ࡛࡚࠴ࡺࡨࡘࡓ࠴࡝࠷࡛ࡶ࡚ࡈࡘࡺࡧࡲ࠾࠽ࠨࠉ"))
def lolu():
	return ADDON.getSetting(l11l1_opy_ (u"ࠧࡳࡧ࡯ࡳࡦࡪࡥࡥ࠰ࡸࡷࡪࡸࠧࠊ"))+l11l1_opy_ (u"ࠣࡡࡵࡩࡱࡵࡡࡥࡧࡧࡣࡦࡶࡩࠣࠋ")
def lolp():
	return ADDON.getSetting(l11l1_opy_ (u"ࠩࡵࡩࡱࡵࡡࡥࡧࡧ࠲ࡵࡧࡳࡴࠩࠌ"))
def lolf(f):
	MAIN_URL = b(l11l1_opy_ (u"ࠪࡥࡍࡘ࠰ࡤࡆࡲࡺࡑ࠸࠱ࡩࡧ࡚࡞࡭ࡧࡘࡋࡰࡧ࡛ࡱࡱ࡚࡙ࡏࡸ࡝࠷࠿ࡴࡍ࠵ࡅࡽࡧࢀ࠹ࡻࡏࡰ࠵ࡱࡨࡗࡋ࡮ࡦࡰ࠾ࡳࡡࡘࡺ࡯࡜࠷ࡘࡶࡥ࠴࠸ࡷࡧ࠸ࡆ࡬ࡒ࡚ࡊ࡯࡟࠲ࡗࡼࡦࡽ࠶ࢀࡍ࡮࠳࡯ࡦ࡜ࡐ࡬ࡤ࡫࠴࡮࡞࠸ࡆࡸࡎ࡛ࡎࡱࡨࡇ࠺ࡪ࡝ࡋ࡛ࡱࡘ࠳ࡈ࡭࡝࠷࡜ࡺࡤࡻ࠻ࡁࠬࠍ"))
	l11l_opy_ = b(l11l1_opy_ (u"ࠫࡏࡴࡍࡺࡤ࡚࡚ࡹ࡟࡭ࡗࡻ࡛࠶࡟ࡶࡢࡈࡘࡩࡧࡲ࡜ࡴࡣ࠵ࡕࡰࡕ࡞࡬࡭ࡥࡺࡁࡂ࠭ࠎ"))
	return MAIN_URL+f+l11l_opy_
def lolrs(f):
	MAIN_URL = b(l11l1_opy_ (u"ࠬࡧࡈࡓ࠲ࡦࡈࡴࡼࡌ࠳࠳࡫ࡩ࡜ࡠࡨࡢ࡚ࡍࡲࡩ࡝࡬࡬࡜࡛ࡑࡺ࡟࠲࠺ࡶࡏ࠷ࡇࡿࡢࡺ࠻ࡼ࡞࡜ࡾࡶ࡚࡙ࡕࡰ࡟ࡌ࠹ࡺࡥࡼ࠼ࡂ࠭ࠏ"))
	return MAIN_URL+f
def lolkek(a):
	a = a.decode(b(l11l1_opy_ (u"࠭ࡡࡈࡘ࠷ࠫࠐ")))
	a = b(a)
	return a
def load_cookies(filename):
	with open(filename, l11l1_opy_ (u"ࠧࡳࡤࠪࠑ")) as f:
		return pickle.load(f)
def save_cookies(requests_cookiejar, filename):
	with open(filename, l11l1_opy_ (u"ࠨࡹࡥࠫࠒ")) as f:
		pickle.dump(requests_cookiejar, f)
def show_busy_dialog():
	xbmc.executebuiltin(l11l1_opy_ (u"ࠩࡄࡧࡹ࡯ࡶࡢࡶࡨ࡛࡮ࡴࡤࡰࡹࠫ࠵࠵࠷࠳࠹ࠫࠪࠓ"))
def hide_busy_dialog():
	xbmc.executebuiltin(l11l1_opy_ (u"ࠪࡈ࡮ࡧ࡬ࡰࡩ࠱ࡇࡱࡵࡳࡦࠪ࠴࠴࠶࠹࠸ࠪࠩࠔ"))
	while xbmc.getCondVisibility(l11l1_opy_ (u"ࠫ࡜࡯࡮ࡥࡱࡺ࠲ࡎࡹࡁࡤࡶ࡬ࡺࡪ࠮࠱࠱࠳࠶࠼࠮࠭ࠕ")):
		xbmc.sleep(100)
def l1ll11_opy_():
	username = dialog.input(l11l1_opy_ (u"ࠬࡋ࡮ࡵࡧࡵࠤࡾࡵࡵࡳࠢࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠠࡖࡵࡨࡶࡳࡧ࡭ࡦࠣࠪࠖ"), type=xbmcgui.INPUT_ALPHANUM)
	password = dialog.input(l11l1_opy_ (u"࠭ࡅ࡯ࡶࡨࡶࠥࡿ࡯ࡶࡴࠣࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡒࡤࡷࡸࡽ࡯ࡳࡦࠤࠫࠗ"), type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
	ADDON.setSetting(l11l1_opy_ (u"ࠧࡳࡧ࡯ࡳࡦࡪࡥࡥ࠰ࡸࡷࡪࡸࠧ࠘"), username)
	ADDON.setSetting(l11l1_opy_ (u"ࠨࡴࡨࡰࡴࡧࡤࡦࡦ࠱ࡴࡦࡹࡳࠨ࠙"), password)
def checktime(l1ll1_opy_,l1l1l_opy_):
	l1ll1_opy_ = l1ll1_opy_.decode(l11l1_opy_ (u"ࠤ࡫ࡩࡽࠨࠚ"))
	l1l1l_opy_ = l1l1l_opy_.decode(l11l1_opy_ (u"ࠥ࡬ࡪࡾࠢࠛ"))
	l1l1l_opy_ = base64.b64decode(l1l1l_opy_)
	return l1ll1_opy_,l1l1l_opy_
def CheckForUpdates():
    l1l1ll_opy_ = int(ADDON.getAddonInfo(l11l1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬࠜ")).replace(l11l1_opy_ (u"ࠬ࠴ࠧࠝ"),l11l1_opy_ (u"࠭ࠧࠞ")))
    url = l11l1_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯࡮ࡣࡼࡪࡦ࡯ࡲࡨࡷ࡬ࡨࡪࡹ࠮ࡤࡱࡰ࠳ࡵࡸ࡯࠰ࡴࡨࡰࡴࡧࡤࡦࡦࡹࡩࡷ࠴ࡴࡹࡶࠪࠟ")
    request = requests.get(url, headers={l11l1_opy_ (u"ࠨࡗࡶࡩࡷ࠳ࡁࡨࡧࡱࡸࠬࠠ"): (UA)})
    if l11l1_opy_ (u"ࠩࡖࡩࡷࡼࡩࡤࡧࠣ࡬ࡦࡹࠠࡣࡧࡨࡲࠥࡹࡵࡴࡲࡨࡲࡩ࡫ࡤࠨࠡ") in request.content:
        dialog.ok(l11l1_opy_ (u"ࠥ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝ࡓࡧ࡯ࡳࡦࡪࡥࡥࠢࡗ࡚ࠥࡍࡵࡪࡦࡨ࡟࠴ࡉࡏࡍࡑࡕࡡࠧࠢ"), l11l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠤࠤࡘ࡫ࡲࡷ࡫ࡦࡩࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡴࡷࡶࡴࡪࡴࡤࡦࡦ࠱ࠦࠣ"),l11l1_opy_ (u"ࠧࠨࠤ"),l11l1_opy_ (u"ࠨࡐ࡭ࡧࡤࡷࡪࠦࡣࡰࡰࡷࡥࡨࡺࠠࡶࡵࠤࠦࠥ"))
        return True
    l1l1l1_opy_ = request.content
    l1l11l_opy_ = int(l1l1l1_opy_.replace(l11l1_opy_ (u"ࠧ࠯ࠩࠦ"),l11l1_opy_ (u"ࠨࠩࠧ")))
    if l1l1ll_opy_ < l1l11l_opy_:
        dialog = xbmcgui.Dialog()
        xbmc.executebuiltin(l11l1_opy_ (u"ࠩࡘࡴࡩࡧࡴࡦࡎࡲࡧࡦࡲࡁࡥࡦࡲࡲࡸ࠮ࠩࠨࠨ"))
        xbmc.executebuiltin(l11l1_opy_ (u"࡙ࠪࡵࡪࡡࡵࡧࡄࡨࡩࡵ࡮ࡓࡧࡳࡳࡸ࠮ࠩࠨࠩ"))
        dialog.ok(l11l1_opy_ (u"ࠦࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞ࡔࡨࡰࡴࡧࡤࡦࡦࠣࡘ࡛ࠦࡇࡶ࡫ࡧࡩࡠ࠵ࡃࡐࡎࡒࡖࡢࠨࠪ"), l11l1_opy_ (u"ࠧࡔࡥࡸࠢࡤࡨࡩࡵ࡮ࠡࡷࡳࡨࡦࡺࡥࠡࡨࡲࡹࡳࡪࠡࠣࠫ"),l11l1_opy_ (u"ࠨࡗࡦࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡺࠤࡧ࡫ࡧࡪࡰࠣࡹࡵࡪࡡࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࠥࠬ")+l1l1l1_opy_+l11l1_opy_ (u"ࠢ࠯ࠤ࠭"),l11l1_opy_ (u"ࠣࡖ࡫࡭ࡸࠦ࡭ࡢࡻࠣࡸࡦࡱࡥࠡࡣࠣࡪࡪࡽࠠ࡮࡫ࡱࡹࡹ࡫ࡳ࠭ࠢࡧࡩࡵ࡫࡮ࡥ࡫ࡱ࡫ࠥࡵ࡮ࠡࡻࡲࡹࡷࠦࡤࡦࡸ࡬ࡧࡪࠧ࡜࡯ࡒ࡯ࡩࡦࡹࡥࠡࡴࡨࡷࡹࡧࡲࡵࠢࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠠࡈࡷ࡬ࡨࡪࠦࡵࡱࡱࡱࠤࡺࡶࡤࡢࡶࡨࠤࡳࡵࡴࡪࡨ࡬ࡧࡦࡺࡩࡰࡰࠤࠦ࠮"))
        return True
def get_reloaded():
    try:
        u = base64.b64decode(l11l1_opy_ (u"ࠤࡤࡌࡗ࠶ࡣࡅࡱࡹࡐ࠷࠷ࡨࡦ࡙࡝࡬ࡦ࡞ࡊ࡯ࡦ࡚ࡰࡰࡠࡘࡎࡷ࡜࠶࠾ࡺࡌ࠳ࡦ࠴ࡥ࡜ࡘ࡬ࡍ࠵ࡍࡰࡧࡍ࠹ࡩ࡜ࡊ࡚ࡰࡒ࡮ࡓ࠶ࡧࡅࡂࡃࠢ࠯"))
        uu = requests.get(u, headers={l11l1_opy_ (u"࡙ࠪࡸ࡫ࡲ࠮ࡃࡪࡩࡳࡺࠧ࠰"): (UA)}).content
        return uu
    except:
        dialog = xbmcgui.Dialog()
        dialog.ok(l11l1_opy_ (u"ࠦࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞ࡔࡨࡰࡴࡧࡤࡦࡦࠣࡘ࡛ࠦࡇࡶ࡫ࡧࡩࡠ࠵ࡃࡐࡎࡒࡖࡢࠨ࠱"), base64.b64decode(l11l1_opy_ (u"ࠧࡘࡘࡋࡻࡥ࠷ࡎ࡮ࡉࡆࡐࡹࡨ࡜ࡾ࡫ࡊࡉ࠸ࡺࡩࡉࡂ࡫ࡤ࠵࠹ࡺࡠࡗࡏ࠲ࡌࡌࡗࡼࡉࡉࡐ࡯ࡧࡳࡠ࡬ࡤ࡫ࡅࡦࡒ࡜࠰࠾ࠤ࠲")),l11l1_opy_ (u"ࠨࠢ࠳"), base64.b64decode(l11l1_opy_ (u"ࠢࡖࡉࡻࡰ࡞࡞ࡎ࡭ࡋࡋࡖࡾ࡫ࡓࡃࡪ࡝࠶ࡋࡶࡢࡪࡄࡶ࡝࡝ࡘ࡬ࡤ࡫࠷ࡁࠧ࠴")))
def get_reloaded_account_info():
    try:
        show_busy_dialog()
        req = urllib2.Request(get_reloaded()+base64.b64decode(l11l1_opy_ (u"ࠣࡎ࠶ࡆ࡭ࡨ࡭ࡗࡵ࡛࠶ࡋࡽࡡࡔ࠷ࡺࡥࡍࡇ࠯ࡥ࡚ࡑࡰࡨࡳ࠵ࡩࡤ࡚࡙࠾ࡐࡘࡎ࡯ࡦࡋࡋࢀࡣ࠴ࡦࡹࡧࡲࡗ࠹ࡋ࡚ࡐࡁࠧ࠵"))%(urllib.quote_plus(ADDON.getSetting(base64.b64decode(l11l1_opy_ (u"ࠤࡦࡱ࡛ࡹࡢ࠳ࡈ࡮࡞࡜ࡗࡵࡥ࡚ࡑࡰࡨ࡭࠽࠾ࠤ࠶")))),urllib.quote_plus(ADDON.getSetting(base64.b64decode(l11l1_opy_ (u"ࠥࡧࡲ࡜ࡳࡣ࠴ࡉ࡯࡟࡝ࡑࡶࡥࡊࡊࡿࡩࡷ࠾࠿ࠥ࠷"))))))
        req.add_header(base64.b64decode(l11l1_opy_ (u"࡛ࠦ࡞ࡎ࡭ࡥ࡬࠵ࡇࡠ࠲ࡗࡷࡧࡅࡂࡃࠢ࠸")) , base64.b64decode(l11l1_opy_ (u"࡚ࠧࡗࡇ࠷࡝ࡱࡋࡶࡣ࡬ࡦ࠴ࡥ࡜ࡘ࡬ࡍࡘ࡙ࡾ࡟࡞ࡊࡃ࡜࠵࡚ࡺࡪࡁ࠾࠿ࠥ࠹")))
        response = urllib2.urlopen(req)
        link=response.read()
        jdata = json.loads(link.decode(l11l1_opy_ (u"࠭ࡵࡵࡨ࠻ࠫ࠺")))
        response.close()
        hide_busy_dialog()
        return jdata
    except:
        hide_busy_dialog()
        try:
            show_busy_dialog()
            req = urllib2.Request(base64.b64decode(l11l1_opy_ (u"ࠢࡢࡊࡕ࠴ࡨࡊ࡯ࡷࡎ࠶ࡎࡱࡨࡇ࠺ࡪ࡝ࡋ࡛ࡱࡢ࡮࠻࠶ࡐࡲࡔࡶࡣࡖࡲࡽࡒࡊࡧ࠳ࡎ࠶ࡆ࡭ࡨ࡭ࡗࡵ࡛࠶ࡋࡽࡡࡔ࠷ࡺࡥࡍࡇ࠯ࡥ࡚ࡑࡰࡨࡳ࠵ࡩࡤ࡚࡙࠾ࡐࡘࡎ࡯ࡦࡋࡋࢀࡣ࠴ࡦࡹࡧࡲࡗ࠹ࡋ࡚ࡐࡁࠧ࠻"))%(urllib.quote_plus(ADDON.getSetting(base64.b64decode(l11l1_opy_ (u"ࠣࡥࡰ࡚ࡸࡨ࠲ࡇ࡭࡝࡛ࡖࡻࡤ࡙ࡐ࡯ࡧ࡬ࡃ࠽ࠣ࠼")))),urllib.quote_plus(ADDON.getSetting(base64.b64decode(l11l1_opy_ (u"ࠤࡦࡱ࡛ࡹࡢ࠳ࡈ࡮࡞࡜ࡗࡵࡤࡉࡉࡾࡨࡽ࠽࠾ࠤ࠽"))))))
            req.add_header(base64.b64decode(l11l1_opy_ (u"࡚ࠥ࡝ࡔ࡬ࡤ࡫࠴ࡆ࡟࠸ࡖࡶࡦࡄࡁࡂࠨ࠾")) , base64.b64decode(l11l1_opy_ (u"࡙ࠦ࡝ࡆ࠶࡜ࡰࡊࡵࡩ࡫ࡥ࠳ࡤ࡛ࡗࡲࡌࡗࡘࡽ࡞࡝ࡐࡂ࡛࠴࡙ࡹࡩࡇ࠽࠾ࠤ࠿")))
            response = urllib2.urlopen(req)
            link=response.read()
            jdata = json.loads(link.decode(l11l1_opy_ (u"ࠬࡻࡴࡧ࠺ࠪࡀ")))
            response.close()
            hide_busy_dialog()
            return jdata
        except:
            hide_busy_dialog()
            dialog = xbmcgui.Dialog()
            dialog.ok(l11l1_opy_ (u"ࠨ࡛ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠣࡁ"),base64.b64decode(l11l1_opy_ (u"ࠢࡓ࡚ࡍࡽࡧ࠹ࡉࡩࠤࡂ")),base64.b64decode(l11l1_opy_ (u"ࠣࡕ࡛ࡑ࡬ࠨࡃ"))+l11l1_opy_ (u"ࠤࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠢࡄ")+base64.b64decode(l11l1_opy_ (u"ࠥࡍࡌࡘࡶࡥ࠴࠷࠳ࠧࡅ")),l11l1_opy_ (u"ࠦࠧࡆ"))
def checkrs():
    rsdata = get_reloaded_account_info()
    rsinfo = rsdata[base64.b64decode(l11l1_opy_ (u"ࠧࡪࡘࡏ࡮ࡦࡰ࠾ࡶࡢ࡮࡜ࡹࠦࡇ"))]
    l111_opy_ = rsinfo[base64.b64decode(l11l1_opy_ (u"ࠨ࡙࡙ࡘ࠳ࡥࡆࡃ࠽ࠣࡈ"))]
    if l111_opy_ == 0:
        dialog = xbmcgui.Dialog()
        dialog.ok(l11l1_opy_ (u"ࠢ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡗ࡫࡬ࡰࡣࡧࡩࡩࠦࡔࡗࠢࡊࡹ࡮ࡪࡥ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠤࡉ"), base64.b64decode(l11l1_opy_ (u"ࠣࡔ࡛ࡎࡾࡨ࠳ࡊࡪࡌࡅࡂࡃࠢࡊ"))+l11l1_opy_ (u"ࠤࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠢࡋ")+base64.b64decode(l11l1_opy_ (u"ࠥࡍࡊࡌࡪ࡚࠴࠼࠵ࡧࡴࡑࡨࡤࡰ࠽࠵ࡏࡇ࡛ࡸࡧ࡛࠺ࡱࡉࡒ࠿ࡀࠦࡌ")), base64.b64decode(l11l1_opy_ (u"࡚ࠦࡍࡸ࡭࡛࡛ࡒࡱࡏࡇࡏࡱ࡝࡛ࡓࡸࡉࡉ࡮ࡹࡨ࡝ࡏࡧࡥ࡚ࡑࡰࡨࡳ࠵ࡩࡤ࡚࡙࡬ࡨ࠳ࡊࡩࡦࡋࡋࢀࡣ࠴ࡦࡹࡧࡲࡗࡧࡢ࡙࠷࡫࡟࠹ࡖࡱ࡜ࡊ࡙࡬ࡩ࠲ࡗ࠲ࡧࡋࡱࡻ࡚࠴ࡏࡀࠦࡍ")), l11l1_opy_ (u"ࠧࠨࡎ"))
        lklklklk = dialog.input(base64.b64decode(l11l1_opy_ (u"࠭ࡒࡘ࠷࠳࡞࡝ࡏࡧࠨࡏ"))+l11l1_opy_ (u"ࠢࡓࡧ࡯ࡳࡦࡪࡥࡥࠢࡗ࡚ࠧࡐ")+base64.b64decode(l11l1_opy_ (u"ࠣࡋࡉ࡚ࡿࡠࡘࡋࡷ࡜࡛࠶ࡲࠢࡑ")), type=xbmcgui.INPUT_ALPHANUM)
        lklklkl = dialog.input(base64.b64decode(l11l1_opy_ (u"ࠩࡕ࡛࠺࠶࡚࡙ࡋࡪࠫࡒ"))+l11l1_opy_ (u"ࠥࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠣࡓ")+base64.b64decode(l11l1_opy_ (u"ࠦࡎࡌࡂࡩࡥ࠶ࡒ࠸ࡨ࠳ࡋ࡭ࠥࡔ")), type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
        gui.ADDON.setSetting(base64.b64decode(l11l1_opy_ (u"ࠬࡩ࡭ࡗࡵࡥ࠶ࡋࡱ࡚ࡘࡓࡸࡨ࡝ࡔ࡬ࡤࡩࡀࡁࠬࡕ")), lklklklk)
        gui.ADDON.setSetting(base64.b64decode(l11l1_opy_ (u"࠭ࡣ࡮ࡘࡶࡦ࠷ࡌ࡫࡛࡙ࡔࡹࡨࡍࡆࡻࡥࡺࡁࡂ࠭ࡖ")), lklklkl)
        return False
    rsinfo = rsinfo[base64.b64decode(l11l1_opy_ (u"࡛࡚ࠢ࡫ࡻ࡝࠸ࡒࡩࡦࡊ࡙ࡂࠨࡗ"))]
    if rsinfo:
        return True
    return False
def lold(l1llll_opy_):
	progress = xbmcgui.DialogProgress()
	progress.create(l11l1_opy_ (u"ࠣ࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢࡘࡥ࡭ࡱࡤࡨࡪࡪࠠࡕࡘࠣࡋࡺ࡯ࡤࡦ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠥࡘ"), l11l1_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࠧࠢࡌࡲࡸࡺࡡ࡭࡮࡬ࡲ࡬ࠦࡆࡪ࡮ࡨࡷ࡙ࠧ"), l11l1_opy_ (u"ࠪࠤ࡚ࠬ"), l11l1_opy_ (u"࡛ࠫࠥ࠭"))
	if os.path.exists(cookiefile):
		request = requests.get(l1llll_opy_, headers={l11l1_opy_ (u"࡛ࠬࡳࡦࡴ࠰ࡅ࡬࡫࡮ࡵࠩ࡜"): (UA)}, auth=(lolu(), lolp()), verify=False, cookies=load_cookies(cookiefile))
		content = request.content
		code = request.status_code
	else:
		request = requests.get(l1llll_opy_, headers={l11l1_opy_ (u"࠭ࡕࡴࡧࡵ࠱ࡆ࡭ࡥ࡯ࡶࠪ࡝"): (UA)}, auth=(lolu(), lolp()), verify=False)
		content = request.content
		code = request.status_code
	progress.close()
	return content
def loldd(url, dest):
    BUFFSIZE = 1024 * 4
    progress = xbmcgui.DialogProgress()
    progress.create(l11l1_opy_ (u"ࠢ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡗ࡫࡬ࡰࡣࡧࡩࡩࠦࡔࡗࠢࡊࡹ࡮ࡪࡥ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠤ࡞"), l11l1_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࠦࠡࡋࡱࡷࡹࡧ࡬࡭࡫ࡱ࡫ࠥࡌࡩ࡭ࡧࡶࠦ࡟"), l11l1_opy_ (u"ࠩࠪࡠ"), l11l1_opy_ (u"ࠪࠫࡡ"))
    if os.path.exists(cookiefile):
        r = requests.get(url, headers={l11l1_opy_ (u"࡚ࠫࡹࡥࡳ࠯ࡄ࡫ࡪࡴࡴࠨࡢ"): (UA)}, auth=(lolu(), lolp()), verify=False, cookies=load_cookies(cookiefile), stream=True)
    else:
        r = requests.get(url, headers={l11l1_opy_ (u"࡛ࠬࡳࡦࡴ࠰ࡅ࡬࡫࡮ࡵࠩࡣ"): (UA)}, auth=(lolu(), lolp()), verify=False, stream=True)
    downloaded = 0
    total = r.headers[l11l1_opy_ (u"࠭ࡣࡰࡰࡷࡩࡳࡺ࠭࡭ࡧࡱ࡫ࡹ࡮ࠧࡤ")]\
        if l11l1_opy_ (u"ࠧࡤࡱࡱࡸࡪࡴࡴ࠮࡮ࡨࡲ࡬ࡺࡨࠨࡥ") in r.headers else None
    with open(dest, l11l1_opy_ (u"ࠨࡹࡥࠫࡦ")) as outfile:
        start_time = time.time()
        for chunk in r.iter_content(chunk_size=BUFFSIZE):
            outfile.write(chunk)
            downloaded += len(chunk)
            text = [l11l1_opy_ (u"ࠩࡇࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࠦࠥ࠯࠴ࡩࠤࡒ࠭ࡧ") % (downloaded / 1024.0 / 1024.0)]
            completion = 0
            if total:
                elapsed = time.time() - start_time
                completion = downloaded / float(total)
                if completion > 0:
                    remaining = elapsed / completion - elapsed
                    text.append(l11l1_opy_ (u"ࠪࡘ࡮ࡳࡥࠡࡴࡨࡱࡦ࡯࡮ࡪࡰࡪ࠾ࠥࠫࡳࠨࡨ") %
                                format_delta(remaining))
            progress.update(int(completion) * 100, l11l1_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࠩࠤࡎࡴࡳࡵࡣ࡯ࡰ࡮ࡴࡧࠡࡈ࡬ࡰࡪࡹࠢࡩ"), *text)
            if progress.iscanceled():
                break
    outfile.close()
    progress.close()
def format_delta(s):
	s = int(s)
def ca():
	try:
		if os.path.exists(addonini):
			l1l_opy_ = l1_opy_(lolf(l11l1_opy_ (u"ࠬࡧࡤࡥࡱࡱࡷ࠳ࡳࡤ࠶ࠩࡪ")))
			if len(l1l_opy_)>1:
				if not l1l_opy_ == l11lll_opy_(addonini):
					progress = xbmcgui.DialogProgress()
					progress.create(l11l1_opy_ (u"ࠨ࡛ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠣ࡫"), l11l1_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࠬࠠࡊࡰࡶࡸࡦࡲ࡬ࡪࡰࡪࠤࡱ࡯࡮࡬ࡧࡧࠤࡦࡪࡤࡰࡰࡶࠤࡩࡧࡴࡢࠤ࡬"), l11l1_opy_ (u"ࠨࠢࠪ࡭"), l11l1_opy_ (u"ࠩࠣࠫ࡮"))
					os.remove(addonini)
					f = open(addonini, l11l1_opy_ (u"ࠪࡻࡧ࠭࡯"))
					if os.path.exists(cookiefile):
						tmpData = requests.get(lolf(l11l1_opy_ (u"ࠫࡦࡪࡤࡰࡰࡶ࠲࡮ࡴࡩࠨࡰ")), headers={l11l1_opy_ (u"࡛ࠬࡳࡦࡴ࠰ࡅ࡬࡫࡮ࡵࠩࡱ"): (UA)}, auth=(lolu(), lolp()), verify=False, cookies=load_cookies(cookiefile)).content
					else:
						tmpData = requests.get(lolf(l11l1_opy_ (u"࠭ࡡࡥࡦࡲࡲࡸ࠴ࡩ࡯࡫ࠪࡲ")), headers={l11l1_opy_ (u"ࠧࡖࡵࡨࡶ࠲ࡇࡧࡦࡰࡷࠫࡳ"): (UA)}, auth=(lolu(), lolp()), verify=False).content
					f.write(tmpData)
					f.close()
					progress.close()
					return True
	except:
		dialog.ok(l11l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠡࠣࡴ"),b(l11l1_opy_ (u"ࠤࡕ࡜ࡏࡿࡢ࠴ࡋ࡫ࠦࡵ")),b(l11l1_opy_ (u"࡙ࠥ࠷࠿ࡴ࡛࡚ࡕࡳࡦ࡝࠵࡯ࡋࡋࡨࡱࡨ࡮ࡒࡩࡧ࠷ࡏࡼࡢ࡮ࡥࡪࡨ࠷ࡲ࠰ࡢࡅࡅ࡮ࡦࡍࡖ࡫ࡣ࠵ࡰࡺࡠࡹࡃࡪ࡝ࡋࡗࡼࡢ࡯ࡏࡪ࡞ࡌࡌ࠰࡚ࡕࡈࡁࠧࡶ")),l11l1_opy_ (u"ࠦࠧࡷ"))
		return False
def cars():
	try:
		if os.path.exists(addonini):
			l1l_opy_ = l1_opy_(lolrs(l11l1_opy_ (u"ࠬࡧࡤࡥࡱࡱࡷ࠳ࡳࡤ࠶ࠩࡸ")))
			if len(l1l_opy_)>1:
				if not l1l_opy_ == l11lll_opy_(addonini):
					progress = xbmcgui.DialogProgress()
					progress.create(l11l1_opy_ (u"ࠨ࡛ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡖࡪࡲ࡯ࡢࡦࡨࡨ࡚ࠥࡖࠡࡉࡸ࡭ࡩ࡫࡛࠰ࡅࡒࡐࡔࡘ࡝ࠣࡹ"), l11l1_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࠬࠠࡊࡰࡶࡸࡦࡲ࡬ࡪࡰࡪࠤࡱ࡯࡮࡬ࡧࡧࠤࡦࡪࡤࡰࡰࡶࠤࡩࡧࡴࡢࠤࡺ"), l11l1_opy_ (u"ࠨࠢࠪࡻ"), l11l1_opy_ (u"ࠩࠣࠫࡼ"))
					os.remove(addonini)
					f = open(addonini, l11l1_opy_ (u"ࠪࡻࡧ࠭ࡽ"))
					if os.path.exists(cookiefile):
						tmpData = requests.get(lolrs(l11l1_opy_ (u"ࠫࡦࡪࡤࡰࡰࡶ࠲࡮ࡴࡩࠨࡾ")), headers={l11l1_opy_ (u"࡛ࠬࡳࡦࡴ࠰ࡅ࡬࡫࡮ࡵࠩࡿ"): (UA)}, auth=(lolu(), lolp()), verify=False, cookies=load_cookies(cookiefile)).content
					else:
						tmpData = requests.get(lolrs(l11l1_opy_ (u"࠭ࡡࡥࡦࡲࡲࡸ࠴ࡩ࡯࡫ࠪࢀ")), headers={l11l1_opy_ (u"ࠧࡖࡵࡨࡶ࠲ࡇࡧࡦࡰࡷࠫࢁ"): (UA)}, auth=(lolu(), lolp()), verify=False).content
					f.write(tmpData)
					f.close()
					progress.close()
					return True
	except:
		dialog.ok(l11l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠡࠣࢂ"),b(l11l1_opy_ (u"ࠤࡕ࡜ࡏࡿࡢ࠴ࡋ࡫ࠦࢃ")),b(l11l1_opy_ (u"࡙ࠥ࠷࠿ࡴ࡛࡚ࡕࡳࡦ࡝࠵࡯ࡋࡋࡨࡱࡨ࡮ࡒࡩࡧ࠷ࡏࡼࡢ࡮ࡥࡪࡨ࠷ࡲ࠰ࡢࡅࡅ࡮ࡦࡍࡖ࡫ࡣ࠵ࡰࡺࡠࡹࡃࡪ࡝ࡋࡗࡼࡢ࡯ࡏࡪ࡞ࡌࡌ࠰࡚ࡕࡈࡁࠧࢄ")),l11l1_opy_ (u"ࠦࠧࢅ"))
		return False
def l11lll_opy_(filePath):
	try:
		with open(filePath, l11l1_opy_ (u"ࠬࡸࡢࠨࢆ")) as may:
			l11_opy_ = hashlib.md5()
			while True:
				data = may.read()
				if not data:
					break
				l11_opy_.update(data)
			return l11_opy_.hexdigest()
	except:
		dialog.ok(l11l1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠦࠨࢇ"),b(l11l1_opy_ (u"ࠢࡓ࡚ࡍࡽࡧ࠹ࡉࡩࠤ࢈")),b(l11l1_opy_ (u"ࠣࡗ࠵࠽ࡹࡠࡘࡓࡱࡤ࡛࠺ࡴࡉࡉࡦ࡯ࡦࡳࡗࡧࡥ࠵ࡍࡺࡧࡳࡣࡨࡦ࠵ࡰ࠵ࡧࡃࡃࡻ࡝࡛ࡋࡱࡡࡘ࠷ࡱࡍࡌࡠࡰࡣࡉࡘ࡫࡞࠸ࡨ࡭࡛࠵ࡸࡿࡪࡗ࠱ࡪࠥࢉ")),l11l1_opy_ (u"ࠤࠥࢊ"))
def l1_opy_(url):
	try:
		show_busy_dialog()
		if os.path.exists(cookiefile):
			data = requests.get(url, headers={l11l1_opy_ (u"࡙ࠪࡸ࡫ࡲ࠮ࡃࡪࡩࡳࡺࠧࢋ"): (UA)}, auth=(lolu(), lolp()), verify=False, cookies=load_cookies(cookiefile)).content
		else:
			data = requests.get(url, headers={l11l1_opy_ (u"࡚ࠫࡹࡥࡳ࠯ࡄ࡫ࡪࡴࡴࠨࢌ"): (UA)}, auth=(lolu(), lolp()), verify=False).content
		hide_busy_dialog()
		return data
	except:
		dialog.ok(l11l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠥࠧࢍ"),b(l11l1_opy_ (u"ࠨࡒ࡙ࡌࡼࡦ࠸ࡏࡨࠣࢎ")),b(l11l1_opy_ (u"ࠢࡖ࠴࠼ࡸ࡟࡞ࡒࡰࡣ࡚࠹ࡳࡏࡈࡥ࡮ࡥࡲࡖ࡭ࡤ࠴ࡌࡹࡦࡲࡩࡧࡥ࠴࡯࠴ࡦࡉࡂ࡯࡜࡛ࡖ࠵ࡧࡗ࠶ࡰࡌࡋࡓࡵ࡚ࡘࡐࡵࡧ࠸࡜ࡴࡊࡓࡀࡁࠧ࢏")),l11l1_opy_ (u"ࠣࠤ࢐"))
		hide_busy_dialog()