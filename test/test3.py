#!/usr/bin/env python
# encoding: utf-8
import re

rulelist=[
    '[\'"]e[\'"]\.[\'"]v[\'"]\.[\'"]a[\'"]\.[\'"]l[\'"]',
    '[\'"]a[\'"]\.[\'"]s[\'"]\.[\'"]s[\'"]\.[\'"]e[\'"]\.[\'"]r[\'"]\.[\'"]t[\'"]'
]
filestr="'e'v'a'l'"
    #按正则查找
for rule in rulelist:
    result = re.search(rule,filestr)
    print result
#    try:
#        if result.group():
#        return ((result.group(),),)'已知后门特征'
#    except:
#        pass
