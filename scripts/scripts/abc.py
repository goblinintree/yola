# -*- coding: utf-8 -*-
import time
import sys

for i in range(1,30):
    print ">>>>>> ", i
    s = u"我的"
    print ">>>>>> ", s.encode("UTF-8")
    time.sleep(0.1)
    if i%10 == 0:
        print isinstance(s, unicode)
        print "## ", s.encode("UTF-8")
    pass
