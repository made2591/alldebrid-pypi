#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Matteo'

#######################################################################################
######################## FIXED PARAMETER USED FOR CONNECTION ##########################
#######################################################################################
URL = "https://www.alldebrid.com/api.php?action=info_user&login="                     #
URL_UPLOAD_TORRENT = "http://upload.alldebrid.com/uploadtorrent.php"                  #
URL_PAYLOAD_UPLOAD_MAGNET = "http://www.alldebrid.com/torrent/"                       #
UPLOAD_MAGNET_HEADER = {                                                              #
  'method': 'POST',                                                                   #
  'url': 'http://upload.alldebrid.com/uploadtorrent.php',                             #
  'headers': { 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8' },  #
}                                                                                     #
#######################################################################################
#######################################################################################
#######################################################################################

#######################################################################################
################################# USER LOGIN PARAMATER ################################
#######################################################################################
USER = "YOUR_ALLDEBRID_USERNAME"
PASSWORD = "YOUR_ALLDEBRID_PASSWORD"
