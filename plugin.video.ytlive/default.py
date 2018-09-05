# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Jesse Ventura Addon by coldkeys
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: coldkeys
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.ytlive'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLU12uITxBEPHr7lxO464fmPXzwZ3dFi_A"
YOUTUBE_CHANNEL_ID_2 = "PLIFqWCuxNyoiFyreU-eTadb_Tdwv9546_"
YOUTUBE_CHANNEL_ID_3 = "PL8fVUTBmJhHLwtmRuJ9DON0Qez_9DLIq7"
YOUTUBE_CHANNEL_ID_4 = "PL57quI9usf_v5cXGLBH7RIxw8N_GgXj4B"
YOUTUBE_CHANNEL_ID_5 = "PLiCvVJzBupKlTpU9AmpakIlk3voRUp-2T"
YOUTUBE_CHANNEL_ID_6 = "PLnzhIyrsnB5Y2B4DE9rYHGZSYZiU94iZE"
YOUTUBE_CHANNEL_ID_7 = "PLnzhIyrsnB5bsacVHVVH8PM9Lb69Cu3um"





# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="שידורים חיים אחרונים",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://i141.photobucket.com/albums/r48/kobiko3030/live_zpsc2yq1vhl.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="שידורים חיים חדשות",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://i141.photobucket.com/albums/r48/kobiko3030/news_zpsqu2ddciq.jpg",
        folder=True )			
		
    plugintools.add_item( 
        #action="", 
        title="שידורים חיים ספורט",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://i141.photobucket.com/albums/r48/kobiko3030/sport_zpslvyjzbdd.jpg",
        folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="שידורים חיים חיות",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://i141.photobucket.com/albums/r48/kobiko3030/animales_zpsjhluwwnr.png",
        folder=True )		


    plugintools.add_item( 
        #action="", 
        title="שידורים חיים טכנולוגיה",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://i141.photobucket.com/albums/r48/kobiko3030/techn_zpspp6avamw.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="שידורים חיים משחקי מחשב",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://i141.photobucket.com/albums/r48/kobiko3030/games_zpsx0blc4s8.jpg",
        folder=True )
	
run()
