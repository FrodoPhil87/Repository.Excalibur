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
import xbmcgui
import xbmcaddon
import os
import sys
import gui
from strings import *
ADDONID = l11l1_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡳࡶࡴ࡭ࡲࡢ࡯࠱ࡶࡪࡲ࡯ࡢࡦࡨࡨࡹࡼࠧ࢑")
ICON  = xbmc.translatePath(os.path.join(l11l1_opy_ (u"ࠪࡷࡵ࡫ࡣࡪࡣ࡯࠾࠴࠵ࡨࡰ࡯ࡨ࠳ࡦࡪࡤࡰࡰࡶࠫ࢒"), ADDONID, l11l1_opy_ (u"ࠫ࡮ࡩ࡯࡯࠰ࡳࡲ࡬࠭࢓")))
ADDON =  xbmcaddon.Addon(ADDONID)
channelTitle = sys.argv[1]
programTitle = sys.argv[2]
startTime    = sys.argv[3]
def playChannel(channel, program = None):
	url = lel.getStreamUrl(channel)
	if url:
		if url[0:9] == l11l1_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࠨ࢔") and ADDON.getSetting(l11l1_opy_ (u"࠭ࡡ࡭ࡶࡨࡶࡳࡧࡴࡪࡸࡨ࠲ࡵࡲࡡࡺࡤࡤࡧࡰ࠭࢕")) == l11l1_opy_ (u"ࠧࡵࡴࡸࡩࠬ࢖"):
			xbmc.executebuiltin(l11l1_opy_ (u"ࠨ࡚ࡅࡑࡈ࠴ࡒࡶࡰࡓࡰࡺ࡭ࡩ࡯ࠪࠨࡷ࠮࠭ࢗ") % url)
		else:
			if url[0:26] == l11l1_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡨࡪࡾ࠯ࠨ࢘"):
				url = re.findall(l11l1_opy_ (u"ࡵࠫࡺࡸ࡬࠾ࠪ࠱࠯ࡄ࠯ࠦ࡮ࡱࡧࡩ࢙ࠬ"), url)
				url = l11l1_opy_ (u"࢚ࠫࠬ").join(url)
				url = urllib.unquote_plus(url)
			try:
				listitem = xbmcgui.ListItem(l11l1_opy_ (u"࡚ࠬࡩࡵ࡮ࡨ࢛ࠫ"), thumbnailImage=channel.logo)
				listitem.setInfo(l11l1_opy_ (u"࠭ࡶࡪࡦࡨࡳࠬ࢜"), {l11l1_opy_ (u"ࠧࡕ࡫ࡷࡰࡪ࠭࢝"): l11l1_opy_ (u"ࠣ࡝ࡆࡓࡑࡕࡒࠡࡵ࡮ࡽࡧࡲࡵࡦ࡟࡞ࡆࡢࠨ࢞")+channel.title+l11l1_opy_ (u"ࠤࠣ࠱ࠥࡡࡃࡐࡎࡒࡖࠥࡶࡡ࡭ࡧࡪࡶࡪ࡫࡮࡞ࠤ࢟")+program.title+l11l1_opy_ (u"ࠥ࡟࠴ࡉࡏࡍࡑࡕࡡࡠ࠵ࡂ࡞ࠤࢠ")})
			except:
				pass
			xbmc.Player().play(item=url, listitem=listitem, windowed=0)
	return url is not None
def createAlarmClockName(programTitle, startTime):
    return l11l1_opy_ (u"ࠫࡹࡼࡧࡶ࡫ࡧࡩ࠲ࠫࡳ࠮ࠧࡶࠫࢡ") % (programTitle, startTime)
def l11l11_opy_(programTitle, startTime):
    name = createAlarmClockName(programTitle, startTime)
    xbmc.executebuiltin(l11l1_opy_ (u"ࠬࡉࡡ࡯ࡥࡨࡰࡆࡲࡡࡳ࡯ࠫࠩࡸ࠳࠵࡮࡫ࡱࡷ࠱࡚ࡲࡶࡧࠬࠫࢢ") % name.encode(l11l1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬࢣ"), l11l1_opy_ (u"ࠧࡳࡧࡳࡰࡦࡩࡥࠨࢤ")))
    xbmc.executebuiltin(l11l1_opy_ (u"ࠨࡅࡤࡲࡨ࡫࡬ࡂ࡮ࡤࡶࡲ࠮ࠥࡴ࠯ࡱࡳࡼ࠲ࡔࡳࡷࡨ࠭ࠬࢥ") % name.encode(l11l1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨࢦ"), l11l1_opy_ (u"ࠪࡶࡪࡶ࡬ࡢࡥࡨࠫࢧ")))
def removeNotification(program):
    lel.removeNotification(program)
    l11l11_opy_(program.title, program.startDate)
try:
	dialog = xbmcgui.Dialog()
	lel = gui.lel(None)
	streamingService = gui.streaming.StreamsService(ADDON)
	l1111l_opy_ = lel.l111ll_opy_(channelTitle)
	l11ll1_opy_ = lel.getCurrentProgram(l1111l_opy_)
	l11l1l_opy_ = lel.getNextProgram(l11ll1_opy_)
	if sys.argv[3] == l11l1_opy_ (u"ࠫ࠺ࡳࡩ࡯ࠩࢨ"):
		ret = dialog.yesno(l11l1_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟ࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠠࡈࡷ࡬ࡨࡪࡡ࠯ࡄࡑࡏࡓࡗࡣࠧࢩ"),programTitle + l11l1_opy_ (u"࠭ࠠࠨࢪ") + strings(NOTIFICATION_5_MINS, channelTitle),l11l1_opy_ (u"ࠧࡅࡱࠣࡽࡴࡻࠠࡸ࡫ࡶ࡬ࠥࡺ࡯ࠡࡹࡤࡸࡨ࡮ࠠࡵࡪ࡬ࡷࠥࡶࡲࡰࡩࡵࡥࡲࡅࠧࢫ"),l11l1_opy_ (u"ࠨࠩࢬ"),l11l1_opy_ (u"࡚ࠩࡥࡹࡩࡨࠡࡰࡲࡻࠬࢭ"),l11l1_opy_ (u"ࠪࡖࡪࡳࡩ࡯ࡦࠣࡱࡪࠦࡩ࡯ࠢ࠸ࡱ࡮ࡴࡵࡵࡧࡶࠫࢮ"))
		if ret:
			pass
		elif not ret:
			removeNotification(l11l1l_opy_)
			xbmc.executebuiltin(l11l1_opy_ (u"ࠫࡓࡵࡴࡪࡨ࡬ࡧࡦࡺࡩࡰࡰࠫࠩࡸ࠲ࠥࡴ࠮࠸࠴࠵࠶ࠬࠦࡵࠬࠫࢯ") % (l11l1_opy_ (u"ࠬࡖࡲࡰࡩࡵࡥࡲࠦࡒࡦ࡯࡬ࡲࡩ࡫ࡲࠨࢰ"), l11l1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡰࡪࡥ࡮ࠤࡦࠦࡳࡰࡷࡵࡧࡪࠦࡴࡰࠢࡳࡰࡦࡿࠠࡑࡴࡲ࡫ࡷࡧ࡭ࠨࢱ"), ICON))
			if not playChannel(l1111l_opy_, l11l1l_opy_):
				result = streamingService.detectStream(l1111l_opy_)
				if not result:
					dialog.ok(l11l1_opy_ (u"ࠢ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡗ࡫࡬ࡰࡣࡧࡩࡩࠦࡔࡗࠢࡊࡹ࡮ࡪࡥ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠤࢲ"), l11l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠡࠣࢳ"), l11l1_opy_ (u"ࠤࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥࡪࡥࡵࡧࡦࡸࠥࡧ࡮ࡺࠢࡶࡸࡷ࡫ࡡ࡮ࡵࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡩࡨࡢࡰࡱࡩࡱ࠴࠮ࠣࢴ"), l11l1_opy_ (u"ࠥࠦࢵ"))
					sys.exit(1)
				elif type(result) == str:
					lel.setCustomStreamUrl(l1111l_opy_, result)
					playChannel(l1111l_opy_, l11l1l_opy_)
					if gui.l111l1_opy_:
						lel.deleteCustomStreamUrl(l1111l_opy_)
				else:
					if l1111l_opy_.title == l11l1_opy_ (u"ࠫࡊࡖࡌࠨࢶ") or l1111l_opy_.title == l11l1_opy_ (u"ࠬࡔࡆࡍࠩࢷ") or l1111l_opy_.title == l11l1_opy_ (u"࠭ࡎࡃࡃࠪࢸ") or l1111l_opy_.title == l11l1_opy_ (u"ࠧࡏࡊࡏࠫࢹ") or l1111l_opy_.title == l11l1_opy_ (u"ࠨࡒࡓ࡚ࠬࢺ") or l1111l_opy_.title == l11l1_opy_ (u"ࠩࡑࡆࡆ࠭ࢻ") or l1111l_opy_.title == l11l1_opy_ (u"ࠪ࠶࠹࠽ࠧࢼ") or len(l1111l_opy_.title) > 13:
						selection = kappa.iI1(result)
						if selection is not None:
							if selection == -1:
								pass
							else:
								lel.setCustomStreamUrl(l1111l_opy_, selection)
								playChannel(l1111l_opy_, l11l1l_opy_)
								if gui.l111l1_opy_:
									lel.deleteCustomStreamUrl(l1111l_opy_)
					else:
						d = gui.ChooseStreamAddonDialog(result)
						d.doModal()
						if d.stream is not None:
							lel.setCustomStreamUrl(l1111l_opy_, d.stream)
							playChannel(l1111l_opy_, l11l1l_opy_)
							if gui.l111l1_opy_:
								lel.deleteCustomStreamUrl(l1111l_opy_)
	elif sys.argv[3] == l11l1_opy_ (u"ࠫࡳࡵࡷࠨࢽ"):
		ret = dialog.yesno(l11l1_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟ࡕࡩࡱࡵࡡࡥࡧࡧࠤ࡙࡜ࠠࡈࡷ࡬ࡨࡪࡡ࠯ࡄࡑࡏࡓࡗࡣࠧࢾ"),programTitle + l11l1_opy_ (u"࠭ࠠࠨࢿ") + strings(NOTIFICATION_NOW, channelTitle),l11l1_opy_ (u"ࠧࡅࡱࠣࡽࡴࡻࠠࡸ࡫ࡶ࡬ࠥࡺ࡯ࠡࡹࡤࡸࡨ࡮ࠠࡵࡪ࡬ࡷࠥࡶࡲࡰࡩࡵࡥࡲࡅࠧࣀ"),l11l1_opy_ (u"ࠨࠩࣁ"),l11l1_opy_ (u"࡚ࠩࡥࡹࡩࡨࠡࡰࡲࡻࠬࣂ"),l11l1_opy_ (u"ࠪࡈࡪࡲࡥࡵࡧࠣࡶࡪࡳࡩ࡯ࡦࡨࡶࠬࣃ"))
		if ret:
			removeNotification(l11l1l_opy_)
		elif not ret:
			removeNotification(l11l1l_opy_)
			xbmc.executebuiltin(l11l1_opy_ (u"ࠫࡓࡵࡴࡪࡨ࡬ࡧࡦࡺࡩࡰࡰࠫࠩࡸ࠲ࠥࡴ࠮࠸࠴࠵࠶ࠬࠦࡵࠬࠫࣄ") % (l11l1_opy_ (u"ࠬࡖࡲࡰࡩࡵࡥࡲࠦࡒࡦ࡯࡬ࡲࡩ࡫ࡲࠨࣅ"), l11l1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡰࡪࡥ࡮ࠤࡦࠦࡳࡰࡷࡵࡧࡪࠦࡴࡰࠢࡳࡰࡦࡿࠠࡑࡴࡲ࡫ࡷࡧ࡭ࠨࣆ"), ICON))
			if not playChannel(l1111l_opy_, l11l1l_opy_):
				result = streamingService.detectStream(l1111l_opy_)
				if not result:
					dialog.ok(l11l1_opy_ (u"ࠢ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡗ࡫࡬ࡰࡣࡧࡩࡩࠦࡔࡗࠢࡊࡹ࡮ࡪࡥ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠤࣇ"), l11l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠡࠣࣈ"), l11l1_opy_ (u"ࠤࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥࡪࡥࡵࡧࡦࡸࠥࡧ࡮ࡺࠢࡶࡸࡷ࡫ࡡ࡮ࡵࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡩࡨࡢࡰࡱࡩࡱ࠴࠮ࠣࣉ"), l11l1_opy_ (u"ࠥࠦ࣊"))
					sys.exit(1)
				elif type(result) == str:
					lel.setCustomStreamUrl(l1111l_opy_, result)
					playChannel(l1111l_opy_, l11l1l_opy_)
					if gui.l111l1_opy_:
						lel.deleteCustomStreamUrl(l1111l_opy_)
				else:
					if l1111l_opy_.title == l11l1_opy_ (u"ࠫࡊࡖࡌࠨ࣋") or l1111l_opy_.title == l11l1_opy_ (u"ࠬࡔࡆࡍࠩ࣌") or l1111l_opy_.title == l11l1_opy_ (u"࠭ࡎࡃࡃࠪ࣍") or l1111l_opy_.title == l11l1_opy_ (u"ࠧࡏࡊࡏࠫ࣎") or l1111l_opy_.title == l11l1_opy_ (u"ࠨࡒࡓ࡚࣏ࠬ") or l1111l_opy_.title == l11l1_opy_ (u"ࠩࡑࡆࡆ࣐࠭") or l1111l_opy_.title == l11l1_opy_ (u"ࠪ࠶࠹࠽࣑ࠧ") or len(l1111l_opy_.title) > 13:
						selection = kappa.iI1(result)
						if selection is not None:
							if selection == -1:
								pass
							else:
								lel.setCustomStreamUrl(l1111l_opy_, selection)
								playChannel(l1111l_opy_, l11l1l_opy_)
								if gui.l111l1_opy_:
									lel.deleteCustomStreamUrl(l1111l_opy_)
					else:
						d = gui.ChooseStreamAddonDialog(result)
						d.doModal()
						if d.stream is not None:
							lel.setCustomStreamUrl(l1111l_opy_, d.stream)
							playChannel(l1111l_opy_, l11l1l_opy_)
							if gui.l111l1_opy_:
								lel.deleteCustomStreamUrl(l1111l_opy_)
except:
	xbmc.executebuiltin(l11l1_opy_ (u"ࠫࡓࡵࡴࡪࡨ࡬ࡧࡦࡺࡩࡰࡰࠫࠩࡸ࠲ࠥࡴ࠮࠴࠴࠵࠶࠰࠭ࠧࡶ࣒࠭ࠬ") % (l11l1_opy_ (u"ࠬࡋࡲࡳࡱࡵ࣓ࠥࠬ"), l11l1_opy_ (u"࠭ࡓࡰ࡯ࡨࡸ࡭࡯࡮ࡨࠢࡺࡩࡳࡺࠠࡸࡴࡲࡲ࡬ࠦࡷࡪࡶ࡫ࠤࡕࡸ࡯ࡨࡴࡤࡱࠥࡸࡥ࡮࡫ࡱࡨࡪࡸࠡࠨࣔ"), ICON))
	removeNotification(l11l1l_opy_)
	import sys
	import traceback as tb
	(etype, value, traceback) = sys.exc_info()
	tb.print_exception(etype, value, traceback)