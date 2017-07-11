#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Matteo'

from lib import *

info = create_config()
cookie = create_cookie(info)
print cookie
json_torrent = get_torrent_page(cookie)
print json_torrent
download_link = get_unlocked_torrent(json_torrent)
for i, v in download_link.iteritems():
    print "\t"+v['name']
    print "\t\""+v['download']+"\""
    print "\tStatus: "+v['status']+" - Dimension: "+v['downloaded']
    print "\t\""+v['downloaded']+"\""
    print "\t\""+v['filesize']+"\""
    print "\t\""+v['seeders']+"\""
    print "\t\""+v['speed']+"\""
    print "\t\""+v['adding_date']+"\""

magnet = get_magnet()
info = create_config()
cookie = create_cookie(info)
print "Cookie created"
request = create_upload_request(cookie, magnet)
print "Request created"
response = execute_upload_request(request)
print "Torrent uploaded"#+response