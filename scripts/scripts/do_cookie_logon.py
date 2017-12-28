# -*- coding: UTF-8 -*-
from browser.browser import Browser
from browser.tools import htmltoolmiccn, cookietool

# 使用用户登陆留下的cookies，登陆应用
browser = Browser()
bbHeader={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
# browser.read_cookies()
browser.read_cookies_json()
# fsrc_tools.read_remote_cookies()


browser.initBrowser(bbHeader=bbHeader)

browser.do_get("http://membercenter.cn.made-in-china.com/member/main/")
# htmltoolmiccn.contain_subString("树中小鬼",browser.response.text)
if htmltoolmiccn.contain_subString(u"树中小鬼",browser.response.text):
    print u"成功登陆", "yulikui2011"
else:
    print u"登陆失败"




