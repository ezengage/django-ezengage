#!/bin/env python
#coding=utf8
'''
A Simple EzEngage Api Client
>>> import time
>>> base_api_url = 'http://ezengage.com/api/v1/'
>>> c = EzEngageApiClient(base_api_url, 'tapp-key')
>>> id = c.get_profile('b55e5965d5ec464397fad447041718c8')['identity']
>>> id
u'http://t.sina.com.cn/1322895797'
>>> c.update_status(id, u'中文 ' + str(time.time()))
True
'''

import urllib
import urllib2
try:
    import simplejson as json
except ImportError,e:
    import json


class EzEngageApiClient(object):


    def __init__(self, api_root, app_key):
        self.api_root = api_root
        self.app_key = app_key

    def get_profile(self, token):
        url = self.api_root + 'profile.json'
        params = {
            'app_key' : self.app_key,
            'token' : to_utf8(token),
        }
        url = url + '?' + urllib.urlencode(params)
        code,response = self.request(url)
        if code == 200:
            return json.loads(response)
        else:
            return None
        
    def update_status(self, identity, status, lat = None, long = None):
        url = self.api_root + 'status.json'
        params = {
            'app_key' : self.app_key,
            'identity' : to_utf8(identity),
            'status' : to_utf8(status),
        }
        if lat:
            params['lat'] = lat
        if long:
            params['long'] = long
        code,response = self.request(url, method = 'POST', payload = urllib.urlencode(params))
        if code == 201:
            return True
        else:
            raise Exception(response)

    def request(self, url, method = 'GET', payload = None):
        req = urllib2.Request(url, payload)
        try:
            response = urllib2.urlopen(req)
            return response.code, unicode(response.read(), 'utf-8')
        except urllib2.HTTPError,e:
            return e.code, e.read()
            

def to_utf8(str):
    if type(str) is unicode:
        return str.encode('utf-8')
    else:
        return str
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
