# -*- coding: utf-8 -*-
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
import zipfile
import time
import xbmc
import xbmcaddon
import xbmcplugin
import xbmcgui
import os
import re
import requests
import urllib
import urllib2
import lolol
import sys
import cfscrape
import pickle
import base64
import shutil
import pyxbmct.addonwindow as pyxbmct
TITLE = l11l1_opy_ (u"ࠫࡗ࡫࡬ࡰࡣࡧࡩࡩࠦࡔࡗࠢࡊࡹ࡮ࡪࡥࠨऴ")
addon_id = l11l1_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡶࡲࡰࡩࡵࡥࡲ࠴ࡲࡦ࡮ࡲࡥࡩ࡫ࡤࡵࡸࠪव")
ADDON = xbmcaddon.Addon(id=addon_id)
l1llll1l1_opy_ = ADDON.getSetting(l11l1_opy_ (u"࠭ࡳ࡬࡫ࡱࠫश"))
l1lll11ll_opy_=l11l1_opy_ (u"ࠧ࠰ࡴࡨࡷࡴࡻࡲࡤࡧࡶ࠳ࡵࡴࡧ࠰ࠩष")
UA     = base64.b64decode(l11l1_opy_ (u"ࠨࡘ࡛ࡒࡱࡩࡩ࠲ࡄ࡝࠶࡛ࡻࡤࡄ࠳ࡑ࡝࡝ࡲ࡭࡚࡙࡯ࡽ࡚ࡌࡊࡑࠩस")) + l11l1_opy_ (u"ࠤࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠢह")
addonbase = base64.b64decode(l11l1_opy_ (u"ࠪࡧࡌࡾ࠱࡛࠴࡯ࡹࡑࡴࡂࡺࡤ࠵ࡨࡾ࡟ࡗ࠱ࡷࡥ࡜ࡗ࠸࡚࠴ࡘࡳ࡞ࡌ࡜ࡷࡤ࡯࠻ࡁࠬऺ"))
cookiefile = xbmc.translatePath(os.path.join(l11l1_opy_ (u"ࠫࡸࡶࡥࡤ࡫ࡤࡰ࠿࠵࠯ࡱࡴࡲࡪ࡮ࡲࡥࠨऻ"), l11l1_opy_ (u"ࠬࡧࡤࡥࡱࡱࡣࡩࡧࡴࡢ़ࠩ"), l11l1_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡰࡳࡱࡪࡶࡦࡳ࠮ࡳࡧ࡯ࡳࡦࡪࡥࡥࡶࡹࠫऽ"), l11l1_opy_ (u"ࠧࡤࡱࡲ࡯࡮࡫ࠧा")))
basePath = xbmc.translatePath(os.path.join(l11l1_opy_ (u"ࠨࡵࡳࡩࡨ࡯ࡡ࡭࠼࠲࠳ࡵࡸ࡯ࡧ࡫࡯ࡩࠬि"), l11l1_opy_ (u"ࠩࡤࡨࡩࡵ࡮ࡠࡦࡤࡸࡦ࠭ी"), l11l1_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡴࡷࡵࡧࡳࡣࡰ࠲ࡷ࡫࡬ࡰࡣࡧࡩࡩࡺࡶࠨु")))
tmp_File = os.path.join(basePath, l11l1_opy_ (u"ࠫࡹࡳࡰ࠯࡫ࡱ࡭ࠬू"))
l1ll11l11_opy_ = xbmc.translatePath(os.path.join(l11l1_opy_ (u"ࠬࡹࡰࡦࡥ࡬ࡥࡱࡀ࠯࠰ࡪࡲࡱࡪ࠵ࡡࡥࡦࡲࡲࡸ࠵ࠧृ") + addon_id + l1lll11ll_opy_, l11l1_opy_ (u"࠭ࡦࡰࡥࡸࡷ࠳ࡶ࡮ࡨࠩॄ")))
l1lll111l_opy_ = xbmc.translatePath(os.path.join(l11l1_opy_ (u"ࠧࡴࡲࡨࡧ࡮ࡧ࡬࠻࠱࠲࡬ࡴࡳࡥ࠰ࡣࡧࡨࡴࡴࡳ࠰ࠩॅ") + addon_id + l1lll11ll_opy_, l11l1_opy_ (u"ࠨࡤࡤࡧࡰ࡭ࡲࡰࡷࡱࡨ࠳ࡶ࡮ࡨࠩॆ")))
l1lll1l11_opy_  = pyxbmct.AddonDialogWindow(TITLE)
dialog = xbmcgui.Dialog()
l1lll1l11_opy_.setGeometry(1000, 500, 100, 50)
l1ll1llll_opy_=pyxbmct.Image(l1lll111l_opy_)
l1lll1l11_opy_.placeControl(l1ll1llll_opy_, -2, 0, 114, 52)
def l1lll1111_opy_():
	text=l11l1_opy_ (u"ࠩ࠳ࡼࡋࡌࡆࡇ࠲࠳࠴࠵࠭े")
	global List
	global l1lll11l1_opy_
	global l1lll1ll1_opy_
	global l1lllll11_opy_
	global Version
	global l1lll1l1l_opy_
	lolol.show_busy_dialog()
	List = pyxbmct.List(buttonFocusTexture=l1ll11l11_opy_,_space=11,_itemTextYOffset=-7,textColor=text)
	l1lll11l1_opy_=pyxbmct.Image(l11l1_opy_ (u"ࠪࠫै"), aspectRatio=2)
	l1lllll1l_opy_ = pyxbmct.Button(l11l1_opy_ (u"ࠫࡈࡲ࡯ࡴࡧࠪॉ"))
	l1lll1ll1_opy_ = pyxbmct.Label(l11l1_opy_ (u"ࠬ࠭ॊ"))
	l1lllll11_opy_ = pyxbmct.Label(l11l1_opy_ (u"࠭ࠧो"))
	Version = pyxbmct.Label(l11l1_opy_ (u"ࠧࠨौ"))
	l1lll1l1l_opy_ = pyxbmct.Label(l11l1_opy_ (u"ࠨ्ࠩ"))
	l1ll1ll11_opy_ = pyxbmct.Label(l11l1_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡪࡳࡱࡪ࡝࡜ࡄࡠࡔࡱ࡫ࡡࡴࡧࠣࡧ࡭ࡵ࡯ࡴࡧࠣࡥࠥࡹ࡫ࡪࡰࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡣࡱࡨࠥ࡯࡮ࡴࡶࡤࡰࡱࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫॎ"))
	l1lll1l11_opy_.placeControl(l1ll1ll11_opy_, 0, 15, 110, 30)
	l1lll1l11_opy_.placeControl(List, 10, 1, 110, 30)
	l1lll1l11_opy_.placeControl(l1lll11l1_opy_, 34, 32, 60, 18)
	l1lll1l11_opy_.placeControl(l1lllll1l_opy_, 100, 46, 10, 5)
	l1lll1l11_opy_.placeControl(l1lll1ll1_opy_, 10, 32, 10, 20)
	l1lll1l11_opy_.placeControl(l1lllll11_opy_, 17, 32, 10, 20)
	l1lll1l11_opy_.placeControl(Version, 24, 32, 10, 20)
	l1lll1l11_opy_.placeControl(l1lll1l1l_opy_, 31, 32, 10, 20)
	l1lll1l11_opy_.connectEventList(
	[pyxbmct.ACTION_MOVE_DOWN,
	pyxbmct.ACTION_MOVE_UP,
		pyxbmct.ACTION_MOUSE_MOVE],
	l1ll1l1ll_opy_)
	List.controlRight(l1lllll1l_opy_)
	l1lllll1l_opy_.controlLeft(List)
	l1lll1l11_opy_.connect(List, getSkin)
	l1lll1l11_opy_.connect(l1lllll1l_opy_, l1lll1l11_opy_.close)
	l1lll1l11_opy_.connect(pyxbmct.ACTION_NAV_BACK, l1lll1l11_opy_.close)
	l1ll11l1l_opy_()
	lolol.hide_busy_dialog()
def l1ll11l1l_opy_():
	global l1ll11lll_opy_
	global l1ll1ll1l_opy_
	global l1ll1l1l1_opy_
	global l1llll111_opy_
	global l1ll1l111_opy_
	global l1llll11l_opy_
	global l1ll1l11l_opy_
	global headers
	global isrs
	l1ll11lll_opy_=[]
	l1ll1ll1l_opy_=[]
	l1ll1l1l1_opy_=[]
	l1llll111_opy_=[]
	l1ll1l111_opy_=[]
	l1llll11l_opy_=[]
	l1ll1l11l_opy_=[]
	isrs = lolol.checkrs()
	if isrs:
		skins = lolol.lolrs(l11l1_opy_ (u"ࠪࡷࡰ࡯࡮ࡴ࠱ࡶ࡯࡮ࡴࡳ࠯࡫ࡱ࡭ࠬॏ"))
	else:
		skins = lolol.lolf(l11l1_opy_ (u"ࠫࡸࡱࡩ࡯ࡵ࠲ࡷࡰ࡯࡮ࡴ࠰࡬ࡲ࡮࠭ॐ"))
	path  = os.path.join(basePath, l11l1_opy_ (u"ࠬࡸࡥࡴࡱࡸࡶࡨ࡫ࡳࠨ॑"), l11l1_opy_ (u"࠭ࡳ࡬࡫ࡱࡷ॒ࠬ"))
	try:
		currenttime = time.time()
		cookieexpire = currenttime - 870
		if os.path.exists(cookiefile):
			cookiemodifedtime = os.path.getmtime(cookiefile)
		if not os.path.exists(cookiefile) or cookiemodifedtime < cookieexpire:
			session = requests.session()
			scraper = cfscrape.create_scraper(sess=session)
			r = scraper.get(skins, headers={l11l1_opy_ (u"ࠧࡖࡵࡨࡶ࠲ࡇࡧࡦࡰࡷࠫ॓"): (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False)
			save_cookies(scraper.cookies, cookiefile)
			session.close
		else:
			r = requests.get(skins, headers={l11l1_opy_ (u"ࠨࡗࡶࡩࡷ࠳ࡁࡨࡧࡱࡸࠬ॔"): (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False, cookies=load_cookies(cookiefile))
		if r.status_code != 200:
			error = r.content.replace(l11l1_opy_ (u"ࠩ࠿ࡷࡹࡸ࡯࡯ࡩࡁࠫॕ"),l11l1_opy_ (u"ࠪࠫॖ")).replace(l11l1_opy_ (u"ࠫࡁࡨࡲࠡ࠱ࡁࠫॗ"),l11l1_opy_ (u"ࠬ࠭क़")).replace(l11l1_opy_ (u"࠭࠼࠰ࡵࡷࡶࡴࡴࡧ࠿ࠩख़"),l11l1_opy_ (u"ࠧࠨग़")).replace(l11l1_opy_ (u"ࠨ࠶࠳࠵࠿ࠦࡓࡰࡴࡵࡽ࠱ࠦࡡࡤࡥࡨࡷࡸࠦࡤࡦࡰ࡬ࡩࡩ࠴ࠧज़"),l11l1_opy_ (u"ࠩࡖࡳࡷࡸࡹ࠭ࠢࡄࡧࡨ࡫ࡳࡴࠢࡧࡩࡳ࡯ࡥࡥࠣࠣࡔࡱ࡫ࡡࡴࡧࠣࡱࡦࡱࡥࠡࡵࡸࡶࡪࠦࡹࡰࡷࠣ࡬ࡦࡼࡥࠡࡧࡱࡸࡪࡸࡥࡥࠢࡼࡳࡺࡸࠠࠨड़")+TITLE+l11l1_opy_ (u"ࠪࠤࡱࡵࡧࡪࡰࠣࡨࡪࡺࡡࡪ࡮ࡶࠤࡨࡵࡲࡳࡧࡦࡸࡱࡿࠡࠨढ़"))
			dialog.ok(TITLE,l11l1_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞ࡇࡵࡶࡴࡸࠡ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩफ़"),error,l11l1_opy_ (u"ࠬ࠭य़"))
		match = re.compile(l11l1_opy_ (u"࠭ࡳ࡬࡫ࡱࠤࡳࡧ࡭ࡦ࠿ࠥࠬ࠳࠱࠿ࠪࠤࠣࡹࡷࡲ࠽ࠣࠪ࠱࠯ࡄ࠯ࠢࠡࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࡃࠢࠩ࠰࠮ࡃ࠮ࠨࠠࡷࡧࡵࡷ࡮ࡵ࡮࠾ࠤࠫ࠲࠰ࡅࠩࠣࠢ࡬ࡱࡦ࡭ࡥ࠾ࠤࠫ࠲࠰ࡅࠩࠣࠩॠ")).findall(r.content)
		l1ll11lll_opy_.append(l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠ࡭࡫ࡰࡩ࡬ࡸࡥࡦࡰࡠ࡛ࡦࡴࡴࠡࡶࡲࠤࡸࡻࡢ࡮࡫ࡷࠤࡦࠦࡳ࡬࡫ࡱࡃࠥࡉ࡬ࡪࡥ࡮ࠤ࡭࡫ࡲࡦࠢࡩࡳࡷࠦ࡭ࡰࡴࡨࠤ࡮ࡴࡦࡰࠣ࡞࠳ࡈࡕࡌࡐࡔࡠࠫॡ"))
		l1ll1ll1l_opy_.append(os.path.join(l11l1_opy_ (u"ࠨࡵࡳࡩࡨ࡯ࡡ࡭࠼࠲࠳࡭ࡵ࡭ࡦ࠱ࡤࡨࡩࡵ࡮ࡴࠩॢ"), addon_id, l11l1_opy_ (u"ࠩ࡬ࡧࡴࡴ࠮ࡱࡰࡪࠫॣ")))
		l1ll1l1l1_opy_.append(l11l1_opy_ (u"ࠪࡒࡴࡴࡥࠨ।"))
		l1llll111_opy_.append(l11l1_opy_ (u"ࠫࠬ॥"))
		l1ll1l111_opy_.append(l11l1_opy_ (u"ࠬ࠭०"))
		l1ll1l11l_opy_.append(l11l1_opy_ (u"࠭ࠧ१"))
		l1llll11l_opy_.append(l11l1_opy_ (u"ࠧࠨ२"))
		List.addItem(l11l1_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡ࡮࡬ࡱࡪ࡭ࡲࡦࡧࡱࡡ࡜ࡧ࡮ࡵࠢࡷࡳࠥࡹࡵࡣ࡯࡬ࡸࠥࡧࠠࡴ࡭࡬ࡲࡄࠦࡃ࡭࡫ࡦ࡯ࠥ࡮ࡥࡳࡧࠣࡪࡴࡸࠠ࡮ࡱࡵࡩࠥ࡯࡮ࡧࡱࠤ࡟࠴ࡉࡏࡍࡑࡕࡡࠬ३"))
		for name,url,desc,ver,image in match:
			l1llll11l_opy_.append(url)
			if isrs:
				url = lolol.lolrs(l11l1_opy_ (u"ࠩࡶ࡯࡮ࡴࡳ࠰ࠩ४")+url)
			else:
				url = lolol.lolf(l11l1_opy_ (u"ࠪࡷࡰ࡯࡮ࡴ࠱ࠪ५")+url)
			if name == l1llll1l1_opy_ and os.path.exists(os.path.join(path, name)):
				name = name+l11l1_opy_ (u"ࠦࡠࡉࡏࡍࡑࡕࠤࡱ࡯࡭ࡦࡩࡵࡩࡪࡴ࡝ࠡ࡝ࡆࡹࡷࡸࡥ࡯ࡶ࡯ࡽࠥࡏ࡮ࡴࡶࡤࡰࡱ࡫ࡤ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠥ६")
			l1ll11lll_opy_.append(name)
			l1ll1ll1l_opy_.append(image)
			l1ll1l1l1_opy_.append(url)
			l1llll111_opy_.append(desc)
			l1ll1l111_opy_.append(ver)
			if os.path.exists(os.path.join(path, name.replace(l11l1_opy_ (u"ࠧࡡࡃࡐࡎࡒࡖࠥࡲࡩ࡮ࡧࡪࡶࡪ࡫࡮࡞ࠢ࡞ࡇࡺࡸࡲࡦࡰࡷࡰࡾࠦࡉ࡯ࡵࡷࡥࡱࡲࡥࡥ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠦ७"),l11l1_opy_ (u"࠭ࠧ८")))):
				l1ll1l11l_opy_.append(l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠ࡭࡫ࡰࡩ࡬ࡸࡥࡦࡰࡠ࡝ࡪࡹ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨ९"))
			else:
				l1ll1l11l_opy_.append(l11l1_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢࡔ࡯࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩ॰"))
			List.addItem(name)
			l1lll1l11_opy_.setFocus(List)
	except:
		lolol.hide_busy_dialog()
		import sys
		import traceback as tb
		(etype, value, traceback) = sys.exc_info()
		tb.print_exception(etype, value, traceback)
def l1ll1l1ll_opy_():
	global l1ll1lll1_opy_
	global l1lll1lll_opy_
	global name
	global l1ll111ll_opy_
	if l1lll1l11_opy_.getFocus() == List:
		pos=List.getSelectedPosition()
		l1lll1lll_opy_=l1ll1ll1l_opy_[pos]
		name=l1ll11lll_opy_[pos]
		author=l1llll111_opy_[pos]
		version=l1ll1l111_opy_[pos]
		downloaded=l1ll1l11l_opy_[pos]
		l1ll1lll1_opy_=l1ll1l1l1_opy_[pos]
		l1ll111ll_opy_=l1llll11l_opy_[pos]
		l1lll1ll1_opy_.setLabel(l11l1_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡪࡳࡱࡪ࡝ࡔ࡭࡬ࡲࠥࡔࡡ࡮ࡧ࠽ࠤࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ॱ")+name)
		l1lllll11_opy_.setLabel(l11l1_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣ࡫ࡴࡲࡤ࡞ࡃࡸࡸ࡭ࡵࡲ࠻ࠢ࡞࠳ࡈࡕࡌࡐࡔࡠࠫॲ")+author)
		Version.setLabel(l11l1_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤ࡬ࡵ࡬ࡥ࡟࡙ࡩࡷࡹࡩࡰࡰ࠽ࠤࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ॳ")+version)
		l1lll1l1l_opy_.setLabel(l11l1_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥ࡭࡯࡭ࡦࡠࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪ࠺ࠡ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪॴ")+downloaded)
		l1lll11l1_opy_.setImage(l1lll1lll_opy_)
def l1llll1ll_opy_():
	play=xbmc.Player()
	liz=xbmcgui.ListItem(name, iconImage=l1lll1lll_opy_,thumbnailImage=l1lll1lll_opy_)
	l1lll1l11_opy_.close()
	play.play(l1ll1lll1_opy_, liz, False)
def getSkin():
	label = name.replace(l11l1_opy_ (u"ࠨ࡛ࡄࡑࡏࡓࡗࠦ࡬ࡪ࡯ࡨ࡫ࡷ࡫ࡥ࡯࡟ࠣ࡟ࡈࡻࡲࡳࡧࡱࡸࡱࡿࠠࡊࡰࡶࡸࡦࡲ࡬ࡦࡦࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠧॵ"),l11l1_opy_ (u"ࠧࠨॶ"))
	url = l1ll1lll1_opy_
	path    = os.path.join(basePath, l11l1_opy_ (u"ࠨࡴࡨࡷࡴࡻࡲࡤࡧࡶࠫॷ"), l11l1_opy_ (u"ࠩࡶ࡯࡮ࡴࡳࠨॸ"))
	if l11l1_opy_ (u"࡛ࠪࡦࡴࡴࠡࡶࡲࠤࡸࡻࡢ࡮࡫ࡷࠤࡦࠦࡳ࡬࡫ࡱࠫॹ") in name:
		dialog.ok(TITLE,l11l1_opy_ (u"ࠫࡎ࡬ࠠࡺࡱࡸࠤࡼ࡯ࡳࡩࠢࡷࡳࠥࡹࡵࡣ࡯࡬ࡸࠥࡧࠠࡴ࡭࡬ࡲࠥࡹ࡯ࠡࡹࡨࠤࡨࡧ࡮ࠡࡪࡤࡺࡪࠦࡩࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥ࡬࡯ࡳࠢࡲࡸ࡭࡫ࡲࠡࡷࡶࡩࡷࡹࠠࡵࡱࠣࡹࡸ࡫ࠬࠡࡲ࡯ࡩࡦࡹࡥࠡࡧࡰࡥ࡮ࡲࠠࡴ࡭࡬ࡲࡅࡳࡡࡺࡨࡤ࡭ࡷ࡭ࡵࡪࡦࡨࡷ࠳ࡩ࡯࡮ࠩॺ"),l11l1_opy_ (u"ࠬࡧ࡮ࡥࠢ࡞ࡇࡔࡒࡏࡓࠢ࡯࡭ࡲ࡫ࡧࡳࡧࡨࡲࡢࡶࡲࡰࡸ࡬ࡨࡪࠦࡳ࡬࡫ࡱࠤࡳࡧ࡭ࡦ࠮ࡤࡹࡹ࡮࡯ࡳ࠮ࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠦ࡯ࡧࠢࡶ࡯࡮ࡴࠠࡢࡰࡧࠤࡹ࡮ࡥࠡࡵ࡮࡭ࡳࠦࡦࡰ࡮ࡧࡩࡷࠦࡺࡪࡲࡳࡩࡩࠦࡵࡱࠢࡤࡷࠥ࡫࡭ࡢ࡫࡯ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴ࠯࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪॻ"),l11l1_opy_ (u"࠭ࠧॼ"))
		dialog.ok(TITLE,l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡕࡲࡥࡢࡵࡨࠤࡳࡵࡴࡦ࠮ࠣࡻࡪࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡪࡨࡰࡵࠦࡵࡴࡧࡵࡷࠥࡩࡲࡦࡣࡷࡩࠥࡹ࡫ࡪࡰࡶ࠲ࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ॽ"),l11l1_opy_ (u"ࠨࠩॾ"),l11l1_opy_ (u"ࠩࠪॿ"))
		return
	if not os.path.exists(os.path.join(path, label)):
		if DialogYesNo(l11l1_opy_ (u"࡛ࠪࡴࡻ࡬ࡥࠢࡼࡳࡺࠦ࡬ࡪ࡭ࡨࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡤࡲࡩࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࠨঀ") + l11l1_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡴࡸࡡ࡯ࡩࡨࡡࠬঁ") + label + l11l1_opy_ (u"ࠬࡡ࠯ࡄࡑࡏࡓࡗࡣࠧং") + l11l1_opy_ (u"࠭ࠠࡴ࡭࡬ࡲࠥࡧ࡮ࡥࠢࡰࡥࡰ࡫ࠠࡪࡶࠣࡽࡴࡻࡲࠡࡣࡦࡸ࡮ࡼࡥࠡࡵ࡮࡭ࡳࡅࠧঃ"), l11l1_opy_ (u"ࠧࠨ঄"), l11l1_opy_ (u"ࠨࡋࡷࠤࡼ࡯࡬࡭ࠢࡥࡩࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࠢࡤࡲࡩࠦࡩ࡯ࡵࡷࡥࡱࡲࡥࡥࠢ࡬ࡲࡹࡵࠠࡺࡱࡸࡶࠥࡹࡹࡴࡶࡨࡱ࠳࠭অ")):
			download = l1ll11ll1_opy_(label, url, l1ll111ll_opy_)
			if download == l11l1_opy_ (u"ࠩࡗࡶࡺ࡫ࠧআ"):
				ADDON.setSetting(l11l1_opy_ (u"ࠪࡷࡰ࡯࡮ࠨই"), label)
				dialog.ok(TITLE,l11l1_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡴࡸࡡ࡯ࡩࡨࡡࠬঈ") + label + l11l1_opy_ (u"ࠬࡡ࠯ࡄࡑࡏࡓࡗࡣࠧউ") + l11l1_opy_ (u"࠭ࠠࡴ࡭࡬ࡲࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠪঊ"), l11l1_opy_ (u"ࠧࠨঋ"), l11l1_opy_ (u"ࠨࡋࡷࠤ࡮ࡹࠠ࡯ࡱࡺࠤࡸ࡫ࡴࠡࡣࡶࠤࡾࡵࡵࡳࠢࡤࡧࡹ࡯ࡶࡦࠢࡶ࡯࡮ࡴࠡࠨঌ"))
				l1lll1l11_opy_.close()
				ADDON.openSettings()
			elif download == l11l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠨ঍"):
				dialog.ok(TITLE,l11l1_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝ࡆࡴࡵࡳࡷࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡦࡴࡤࠡ࡫ࡱࡷࡹࡧ࡬࡭࡫ࡱ࡫ࠥ࠭঎") + l11l1_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡴࡸࡡ࡯ࡩࡨࡡࠬএ") + label + l11l1_opy_ (u"ࠬࡡ࠯ࡄࡑࡏࡓࡗࡣࠧঐ") + l11l1_opy_ (u"࠭ࠠࡴ࡭࡬ࡲࠦࡡ࠯ࡄࡑࡏࡓࡗࡣࠧ঑"),l11l1_opy_ (u"ࠧࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭࠮࠯ࠢࡓࡰࡪࡧࡳࡦࠢࡵࡩࡵࡵࡲࡵࠢࡷ࡬࡮ࡹࠠࡵࡱࠣࡷࡺࡶࡰࡰࡴࡷࠥࠬ঒"),l11l1_opy_ (u"ࠨࠩও"))
	else:
		if DialogYesNo(l11l1_opy_ (u"ࠩ࡜ࡳࡺࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡩࡣࡹࡩࠥࡡࡃࡐࡎࡒࡖࠥࡵࡲࡢࡰࡪࡩࡢ࠭ঔ") + label + l11l1_opy_ (u"ࠪ࡟࠴ࡉࡏࡍࡑࡕࡡࠬক") + l11l1_opy_ (u"ࠫࠥࡹ࡫ࡪࡰࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪ࠮࡙ࠡࡲࡹࡱࡪࠠࡺࡱࡸࠤࡱ࡯࡫ࡦࠢࡷࡳࠥࡪࡥ࡭ࡧࡷࡩࠥࡧ࡮ࡥࠢࡸࡲ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡡࡃࡐࡎࡒࡖࠥࡵࡲࡢࡰࡪࡩࡢ࠭খ") + label + l11l1_opy_ (u"ࠬࡡ࠯ࡄࡑࡏࡓࡗࡣࠧগ") + l11l1_opy_ (u"࠭ࠠࡰࡴࠣࡱࡦࡱࡥࠡ࡫ࡷࠤࡾࡵࡵࡳࠢࡤࡧࡹ࡯ࡶࡦࠢࡶ࡯࡮ࡴ࠿ࠨঘ"), l11l1_opy_ (u"ࠧࠨঙ"), l11l1_opy_ (u"ࠨࠩচ"), l11l1_opy_ (u"ࠩࡇࡩࡱ࡫ࡴࡦࠢࡤࡲࡩࠦࡵ࡯࡫ࡱࡷࡹࡧ࡬࡭ࠩছ"), l11l1_opy_ (u"ࠪࡗࡪࡺࠠࡢࡵࠣࡥࡨࡺࡩࡷࡧࠣࡷࡰ࡯࡮ࠨজ")):
			ADDON.setSetting(l11l1_opy_ (u"ࠫࡸࡱࡩ࡯ࠩঝ"), label)
			dialog.ok(TITLE,l11l1_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡵࡲࡢࡰࡪࡩࡢ࠭ঞ") + label + l11l1_opy_ (u"࡛࠭࠰ࡅࡒࡐࡔࡘ࡝ࠨট") + l11l1_opy_ (u"ࠧࠡࡵ࡮࡭ࡳࠦࡩࡴࠢࡱࡳࡼࠦࡳࡦࡶࠣࡥࡸࠦࡹࡰࡷࡵࠤࡦࡩࡴࡪࡸࡨࠤࡸࡱࡩ࡯ࠣࠪঠ"), l11l1_opy_ (u"ࠨࠩড"), l11l1_opy_ (u"ࠩࠪঢ"))
			l1lll1l11_opy_.close()
			ADDON.openSettings()
		else:
			if not label == l11l1_opy_ (u"ࠪࡈࡪ࡬ࡡࡶ࡮ࡷࠫণ"):
				if DialogYesNo(l11l1_opy_ (u"ࠫࡆࡸࡥࠡࡻࡲࡹࠥࡹࡵࡳࡧࠣࡽࡴࡻࠠࡸࡣࡱࡸࠥࡺ࡯ࠡࡦࡨࡰࡪࡺࡥࠡࡣࡱࡨࠥࡻ࡮ࡪࡰࡶࡸࡦࡲ࡬ࠡ࡝ࡆࡓࡑࡕࡒࠡࡱࡵࡥࡳ࡭ࡥ࡞ࠩত") + label + l11l1_opy_ (u"ࠬࡡ࠯ࡄࡑࡏࡓࡗࡣࠧথ") + l11l1_opy_ (u"࠭࠿ࠨদ"),l11l1_opy_ (u"ࠧࠨধ"),l11l1_opy_ (u"ࠨࡖ࡫࡭ࡸࠦࡷࡪ࡮࡯ࠤࡵ࡫ࡲ࡮ࡣࡱࡩࡳࡺ࡬ࡺࠢࡧࡩࡱ࡫ࡴࡦࠢࡷ࡬࡮ࡹࠠࡴ࡭࡬ࡲࠥ࡬ࡲࡰ࡯ࠣࡽࡴࡻࡲࠡࡵࡼࡷࡹ࡫࡭࠯ࠩন")):
					for root, dirs, files in os.walk(os.path.join(path, label)):
						file_count = 0
						file_count += len(files)
						if file_count > 0:
							for f in files:
								try:
									os.unlink(os.path.join(root, f))
								except: pass
							for d in dirs:
								try:
									shutil.rmtree(os.path.join(root, d))
								except: pass
					if os.path.exists(os.path.join(path, label)):
						try:
							shutil.rmtree(os.path.join(path, label))
						except: pass
					if label == l1llll1l1_opy_:
						ADDON.setSetting(l11l1_opy_ (u"ࠩࡶ࡯࡮ࡴࠧ঩"), l11l1_opy_ (u"ࠪࡈࡪ࡬ࡡࡶ࡮ࡷࠫপ"))
			else:
				dialog.ok(TITLE,l11l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠤࠤ࡞ࡵࡵࠡࡥࡤࡲࡳࡵࡴࠡࡦࡨࡰࡪࡺࡥࠡࡣࡱࡨࠥࡻ࡮ࡪࡰࡶࡸࡦࡲ࡬ࠡࡶ࡫ࡩࠥࡊࡥࡧࡣࡸࡰࡹࠦࡳ࡬࡫ࡱࠥࠬফ"),l11l1_opy_ (u"ࠬ࠭ব"),l11l1_opy_ (u"࠭ࠧভ"))
def DialogYesNo(line1, line2=l11l1_opy_ (u"ࠧࠨম"), line3=l11l1_opy_ (u"ࠨࠩয"), noLabel=None, yesLabel=None):
	d = xbmcgui.Dialog()
	if noLabel == None or yesLabel == None:
		return d.yesno(TITLE, line1, line2 , line3) == True
	else:
		return d.yesno(TITLE, line1, line2 , line3, noLabel, yesLabel) == True
def l1ll11ll1_opy_(label, url, filename):
	try:
		path    = os.path.join(basePath, l11l1_opy_ (u"ࠩࡵࡩࡸࡵࡵࡳࡥࡨࡷࠬর"), l11l1_opy_ (u"ࠪࡷࡰ࡯࡮ࡴࠩ঱"), filename)
		tmpFile = os.path.join(basePath, l11l1_opy_ (u"ࠫࡷ࡫ࡳࡰࡷࡵࡧࡪࡹࠧল"), l11l1_opy_ (u"ࠬࡹ࡫ࡪࡰࡶࠫ঳"), l11l1_opy_ (u"࠭ࡴ࡮ࡲࠪ঴"))
		if os.path.exists(tmpFile):
			try:
				os.remove(tmpFile)
			except:
				pass
		if os.path.exists(path):
			try:
				os.remove(path)
			except:
				pass
		if os.path.exists(path.replace(l11l1_opy_ (u"ࠧ࠯ࡼ࡬ࡴࠬ঵"),l11l1_opy_ (u"ࠨࠩশ"))):
			try:
				for root, dirs, files in os.walk(os.path.join(path, label)):
					file_count = 0
					file_count += len(files)
					if file_count > 0:
						for f in files:
							try:
								os.unlink(os.path.join(root, f))
							except: pass
						for d in dirs:
							try:
								shutil.rmtree(os.path.join(root, d))
							except: pass
				if os.path.exists(os.path.join(path, label)):
					try:
						shutil.rmtree(os.path.join(path, label))
					except: pass
			except:
				pass
		tmpData = mayfairdownloader(url,tmpFile,label)
		if tmpData:
			if os.path.getsize(tmpFile) > 0:
				os.rename(tmpFile, path)
				zin = zipfile.ZipFile(path, l11l1_opy_ (u"ࠩࡵࠫষ"))
				zin.extractall(os.path.join(basePath, l11l1_opy_ (u"ࠪࡶࡪࡹ࡯ࡶࡴࡦࡩࡸ࠭স"), l11l1_opy_ (u"ࠫࡸࡱࡩ࡯ࡵࠪহ")))
				zin.close()
				os.remove(path)
				return l11l1_opy_ (u"࡚ࠬࡲࡶࡧࠪ঺")
		else:
			return l11l1_opy_ (u"࠭ࡆࡢ࡮ࡶࡩࠬ঻")
	except:
		import sys
		import traceback as tb
		(etype, value, traceback) = sys.exc_info()
		tb.print_exception(etype, value, traceback)
		return l11l1_opy_ (u"ࠧࡆࡴࡵࡳࡷ়࠭")
def mayfairdownloader(url, dest, label):
	BUFFSIZE = 1024 * 4
	progress = xbmcgui.DialogProgress()
	progress.create(TITLE,l11l1_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࠦࠡࡋࡱࡷࡹࡧ࡬࡭࡫ࡱ࡫ࠥࠨঽ")+label+l11l1_opy_ (u"ࠤࠣࡗࡰ࡯࡮࠯࠰ࠥা"), l11l1_opy_ (u"ࠪࠤࠬি"), l11l1_opy_ (u"ࠫࠥ࠭ী"))
	currenttime = time.time()
	cookieexpire = currenttime - 870
	if os.path.exists(cookiefile):
		cookiemodifedtime = os.path.getmtime(cookiefile)
	if not os.path.exists(cookiefile) or cookiemodifedtime < cookieexpire:
		session = requests.session()
		scraper = cfscrape.create_scraper(sess=session)
		r = scraper.get(url, headers={l11l1_opy_ (u"࡛ࠬࡳࡦࡴ࠰ࡅ࡬࡫࡮ࡵࠩু"): (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False, stream=True)
		save_cookies(scraper.cookies, cookiefile)
		session.close
	else:
		r = requests.get(url, headers={l11l1_opy_ (u"࠭ࡕࡴࡧࡵ࠱ࡆ࡭ࡥ࡯ࡶࠪূ"): (UA)}, auth=(lolol.lolu(), lolol.lolp()), verify=False, cookies=load_cookies(cookiefile), stream=True)
	if r.status_code != 200:
		progress.close()
		error = r.content.replace(l11l1_opy_ (u"ࠧ࠽ࡵࡷࡶࡴࡴࡧ࠿ࠩৃ"),l11l1_opy_ (u"ࠨࠩৄ")).replace(l11l1_opy_ (u"ࠩ࠿ࡦࡷࠦ࠯࠿ࠩ৅"),l11l1_opy_ (u"ࠪࠫ৆")).replace(l11l1_opy_ (u"ࠫࡁ࠵ࡳࡵࡴࡲࡲ࡬ࡄࠧে"),l11l1_opy_ (u"ࠬ࠭ৈ"))
		dialog.ok(TITLE,l11l1_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡉࡷࡸ࡯ࡳࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡢࡰࡧࠤ࡮ࡴࡳࡵࡣ࡯ࡰ࡮ࡴࡧࠡࠩ৉") + l11l1_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡰࡴࡤࡲ࡬࡫࡝ࠨ৊") + label + l11l1_opy_ (u"ࠨ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪো") + l11l1_opy_ (u"ࠩࠣࡷࡰ࡯࡮ࠢ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪৌ"),error,l11l1_opy_ (u"্ࠪࠫ"))
		return False
	downloaded = 0
	total = r.headers[l11l1_opy_ (u"ࠫࡨࡵ࡮ࡵࡧࡱࡸ࠲ࡲࡥ࡯ࡩࡷ࡬ࠬৎ")]\
		if l11l1_opy_ (u"ࠬࡩ࡯࡯ࡶࡨࡲࡹ࠳࡬ࡦࡰࡪࡸ࡭࠭৏") in r.headers else None
	with open(dest, l11l1_opy_ (u"࠭ࡷࡣࠩ৐")) as outfile:
		start_time = time.time()
		for chunk in r.iter_content(chunk_size=BUFFSIZE):
			outfile.write(chunk)
			downloaded += len(chunk)
			text = [l11l1_opy_ (u"ࠧࡅࡱࡺࡲࡱࡵࡡࡥࡧࡧࠤࠪ࠴࠲ࡧࠢࡐࠫ৑") % (downloaded / 1024.0 / 1024.0)]
			completion = 0
			if total:
				elapsed = time.time() - start_time
				completion = downloaded / float(total)
				if completion > 0:
					remaining = elapsed / completion - elapsed
					text.append(l11l1_opy_ (u"ࠨࡖ࡬ࡱࡪࠦࡲࡦ࡯ࡤ࡭ࡳ࡯࡮ࡨ࠼ࠣࠩࡸ࠭৒") %
								format_delta(remaining))
			progress.update(int(completion) * 100, l11l1_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࠧࠢࡌࡲࡸࡺࡡ࡭࡮࡬ࡲ࡬ࠦࠢ৓")+label+l11l1_opy_ (u"ࠥࠤࡘࡱࡩ࡯࠰࠱ࠦ৔"), *text)
			if progress.iscanceled():
				break
	outfile.close()
	progress.close()
	return True
def ReplaceText(SourceFile, tmpFile, old1, new1, old2, new2, old3, new3, old4, new4):
    if os.path.exists(tmpFile):
        os.remove(tmpFile)
    os.rename(SourceFile, tmpFile)
    try:
        s=open(tmpFile).read()
        s=s.replace(old1, new1)
        s=s.replace(old2, new2)
        s=s.replace(old3, new3)
        s=s.replace(old4, new4)
        f=open(SourceFile,l11l1_opy_ (u"ࠫࡦ࠭৕"))
        f.write(s)
        f.close()
        os.remove(tmpFile)
    except: pass
def format_delta(s):
    s = int(s)
def load_cookies(filename):
    with open(filename, l11l1_opy_ (u"ࠬࡸࡢࠨ৖")) as f:
        return pickle.load(f)
def save_cookies(requests_cookiejar, filename):
    with open(filename, l11l1_opy_ (u"࠭ࡷࡣࠩৗ")) as f:
        pickle.dump(requests_cookiejar, f)
xbmc.executebuiltin(l11l1_opy_ (u"ࠧࡅ࡫ࡤࡰࡴ࡭࠮ࡄ࡮ࡲࡷࡪ࠮࠱࠱࠳࠷࠴࠮࠭৘"))
l1lll1111_opy_()
l1lll1l11_opy_.doModal()
del l1lll1l11_opy_