#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
import json
import urllib2
import xml.dom.minidom
from weibopy.auth import OAuthHandler , BasicAuthHandler
from weibopy.api import API
import os
import sys
from LoginWindow import LoginWindow
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4 import QtGui, QtCore
import ConfigParser

    

        
"""def get_auth(token,tokenSecret):
    
    auth = OAuthHandler("2839869753","e38cb74f0f38eb33a1e0e25b7adde7cb")
    auth.setToken(token,tokenSecret)
    return auth"""


def get_token(auth_url):
    
    result = urllib2.urlopen(auth_url)
    xmls = result.read()
    doc = xml.dom.minidom.parseString(xmls)
    root = doc.documentElement
    verifier = root.getElementsByTagName("oauth_verifier")[0]
    oauth_verifier = ""
    for node in verifier.childNodes:
        oauth_verifier = node.data
    auth.get_access_token(oauth_verifier)      
    token = auth.access_token.key
    tokenSecret = auth.access_token.secret
    return token,tokenSecret
    


