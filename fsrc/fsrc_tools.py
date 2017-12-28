# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
import os


def save_remote_cookies(string_data, file_path, file_name="cookies_default.txt"):
    issuccess = False
    f = file(os.path.join(file_path, file_name), "w+")
    f.writelines(string_data)
    f.close()

    issuccess = True
    return issuccess


def read_remote_cookies(file_path, file_name="cookies_default.txt"):
    string_data = ""
    try:
        f = open(os.path.join(file_path, file_name))
        print 1
        tmp_line = f.readline()
        while tmp_line: 
            string_data = string_data + tmp_line
            print tmp_line
            tmp_line = f.readline() 

    except Exception as r:
        r.message
        string_data =""
    finally:
        f.close() 
    return string_data

def parser_cookies(cookies_string):
    """
    pid=TguMjQwLjI2LjIwMzIwMTcxMjAxMTQxNzM4NjI3MTc3Nzk3NzYN; sf_img=AM; ordr=1; 
    split 
    """
    cookie_dict = {}
    if cookies_string:
        cookie_list = cookies_string.split(";")
        for cookie in cookie_list:
            cookie_dict[str(cookie.partition("=")[0]).encode("UTF-8")] = str(cookie.partition("=")[2]).encode("UTF-8")
    print cookie_dict
    return cookie_dict

if __name__ == "__main__":
    file_dict = eval(read_remote_cookies("e:\myspace\space_fsrc\Django-Web\yola\scripts\scripts\\browser\cookies", "cookies_json3.txt"))
    # print read_remote_cookies("e:\myspace\space_fsrc\Django-Web\yola\scripts\scripts\\browser\cookies", "cookies_json3.txt")
    cookies_string = file_dict["u_cookie"]
    parser_cookies(cookies_string)