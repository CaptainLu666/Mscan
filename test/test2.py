#!/usr/bin/env python
# encoding: utf-8
import os
a = ['php']
path='/opt/app/upload/'
for root,dirs,files in os.walk(path):
    for f in files:
        #print os.path.splitext(f)
        sufix = os.path.splitext(f)[1][1:]
        if sufix in a:
            print f
    #    if dict.has_key(sufix):
    #        dict[sufix]+=1
    #    else:
    #        dict[sufix]=1
#for item in dict.items():
#    print "%s:%s" % item
        #print filename
