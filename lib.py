#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Matteo'

import httplib
import json
import urllib
import requests
import urllib2, re
import config
import sys

def find_str(s, char):
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index
            index += 1
    return -1

def create_config():
    info = {}
    info['user'] = config.USER
    info['pass'] = config.PASSWORD
    return info

def create_cookie(info):
    try:
        req = urllib2.Request("https://www.alldebrid.com/api.php?action=info_user&login="+info['user']+"&pw="+info['pass'], None,
                            {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        response = urllib2.urlopen(req).read()
        cookie = response.split('<cookie>')[-1].split('</cookie>')[0]
    except Exception, e:
        print "Error in cookie creation (check user and password setting)"
        sys.exit(-1)
    return cookie

def get_magnet():
    magnet = raw_input("Insert magnet:\n")
    return magnet

def create_upload_request(cookie, magnet):
    UPLOAD_MAGNET_HEADER = {
          'method': 'POST',
          'url': 'http://upload.alldebrid.com/uploadtorrent.php',
          'headers': { 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8' },
    }
    UPLOAD_PAYLOAD = {
        'domain': config.URL_PAYLOAD_UPLOAD_MAGNET,
        'uid': cookie,
        'magnet': magnet
    }
    UPLOAD_PAYLOAD = urllib.urlencode(UPLOAD_PAYLOAD)
    req = urllib2.Request(config.URL_UPLOAD_TORRENT, UPLOAD_PAYLOAD, UPLOAD_MAGNET_HEADER)
    return req

def execute_upload_request(req):
    response = urllib2.urlopen(req).read()
    return response

def get_torrent_page(cookie):
    try:
        url = 'http://www.alldebrid.com/api/torrent.php?json=true'

        header = {'Accept' : '*/*',
            'Accept-Encoding' : 'gzip, deflate, sdch',
            'Accept-Language' : 'it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4',
            'Cache-Control' : 'no-cache',
            'Connection' : 'keep-alive',
            'Cookie' : 'lang=en; domain=com; uid='+cookie+'; ssl=0;',
            'Host' : 'www.alldebrid.com',
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36'}
        req = requests.get(url, headers=header)
        return req.json()
    except Exception, e:
        print "Error in upload request (check header and req error in lib)"
        sys.exit(-1)

def get_unlocked_link(url):
    try:
        URL_DOWNLOAD = "http://www.alldebrid.com/service.php?pseudo="+config.USER+"&password="+config.PASSWORD+"&link="+url
        return urllib2.urlopen(URL_DOWNLOAD).read()
    except Exception, e:
        print "Error in retrieving upload download link (check url error in lib)"
        sys.exit(-1)

def get_unlocked_torrent(json):
    torrents_unlocked = {}
    counter = 0
    for i in json:
        # get info
        index = 3
        for k in i[4:]:
            k = str(k)
            if "a" in k or "img" in k:
                break
            else:
                index += 1
        infos = i[4:index+1]
        if len(infos) > 0:
            status = str(infos[0])
            downloaded = str(infos[1])
            filesize = str(infos[2])
            seeders = str(infos[3])
            speed = str(infos[4])
            adding_date = str(infos[5])

            # get data
            url = i[-2][10:41]
            name = i[3][find_str(i[3], "'>")+2 : find_str(i[3], "</")]
    #        unlocked = get_unlocked_link(url)
    #        first_ = find_str(unlocked, "href='")+6
    #        second_ = find_str(unlocked, "' style='")
    #        download_link = unlocked[first_ : second_]
    #        third_ = str(download_link).rindex("/")+1
    #        name = download_link[third_:]
            torrents_unlocked[counter] = {'name' : name,
                                          'download' : url,
                                          'status' : status,
                                          'downloaded' : downloaded,
                                          'filesize' : filesize,
                                          'seeders' : seeders,
                                          'speed' : speed,
                                          'adding_date' : adding_date
                                          }
            counter += 1
    return torrents_unlocked