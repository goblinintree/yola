# -*- coding: UTF-8 -*-
import requests
import sys
from browser.browser import Browser
from browser.tools import cookietool
from browser.tools import htmltoolmiccn
from browser.tools import randomstring
print "aaa"
user_data={
    "username": "XXXXXXXXX",
    "password": "XXXXXXXX",
}


browser = Browser()
bbHeader={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
browser.initBrowser(bbHeader=bbHeader).do_get("http://membercenter.cn.made-in-china.com/login/?_=1")
browser.do_get("http://cd.abiz.com/logout?pn=miccn")
browser.bcookies =None  
req03_data = {
    "username": user_data["username"],
    "password": user_data["password"],
    "pn": "miccn",
    "tab": "miccn",
    "ticket": "undefined",
    "callback": "parent.focusSSOController.callFeedback",
    "sucurl": "http://membercenter.cn.made-in-china.com/?_=1",
    "rememberLogUserNameFlag": "0",
    "encoding": "GBK"}
browser.do_post("http://cd.abiz.com/logon/gbk", data=req03_data)
tmp =()
print "3>>>> "
tmp = htmltoolmiccn.tuple_search_from_string( r'createHiddenIframe(\(.*\)).*createHiddenIframe(\(.*\));',browser.response.text)
if 0 < len(tmp):
    tmp_url = eval(tmp[0])[0] + "&callback=focusSSOController.doCrossDomainCallBack&scriptId=ssoscript0&_=%s" % (randomstring.get_time_13())
browser.do_get(tmp_url)
tmp =[]
tmp = htmltoolmiccn.list_findall_from_string(r"'scriptId':'ssoscript0'",browser.response.text)
# if 0 < len(tmp):
#     print tmp
browser.do_get("http://membercenter.cn.made-in-china.com/member/main/")
browser.save_cookies()

print "3>>>> ", browser.response.text 
