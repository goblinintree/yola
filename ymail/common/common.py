# -*- coding: utf-8 -*-

import requests
import random
import json
from django.conf import settings

class YolaMail:
    """
    处理邮件接口返回的数据
    """
    def __init__(self, mail_to, subject, content, html_content=""):
        """
        初始化相关数据,包括接口的url,headers和parm
        :return: None
        """
        parm_mail_to = mail_to or ["yulikui@amde-in-china.com",]
        parm_subject = subject or "[默认主题]来自YolaMail的问候" 
        parm_content = content or "[默认内容]你好，YolaMail的朋友."
        parm_html_content = html_content
        self.url = 'http://'+ settings.APP_DEMAIN +'/mail/mail/'
        # self.headers = {"yola": "Yola Mail","Content-Type":"application/json; charset=utf-8"}
        self.headers = {"yola": "Yola Mail"}
        self.parm = {
            "mail_to": parm_mail_to,
            "subject": parm_subject,
            "content": parm_content,
            "html_content": parm_html_content
        }

    def post_mail(self):
        """
        从接口获取 返回,返回json数据.
        :return:json
        """
        wb_data = requests.post(self.url, data=self.parm, headers=self.headers)
        data = wb_data.json()
        if data['error_code'] == 0:
            result = data['message'][0]
            random_num = random.randint(0, 19)
            data['error_code'] = random_num
            data = json.dumps(data,ensure_ascii=False).encode('UTF-8')
            return data
        else:
            return data

