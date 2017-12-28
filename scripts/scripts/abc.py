# -*- coding: utf-8 -*-
import time
import sys

for i in range(1,30):
    print ">>>>>> ", i
    s = u"我的"
    print ">>>>>> ", s
    time.sleep(0.2)
    if i%10 == 0:
        print isinstance(s, unicode)
        
    pass