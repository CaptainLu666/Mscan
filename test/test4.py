#!/usr/bin/env python
# encoding: utf-8

import os

FileList = []
rootdir = "/opt/app/jfscan"

for root, subFolders, files in os.walk(rootdir):
    #排除特定的子目录
    for fs in open('exclude.txt'):
        fs = fs.strip('\n')
        if fs in subFolders:
            subFolders.remove(fs)
    #if 'phpplus' in subFolders:
    #    subFolders.remove('phpplus')
    #        print subFolders
    #查找特定扩展名的文件，只要包含'.py'字符串的文件，都会被包含
    for f in files:
        if f.find('.py') != -1:
            FileList.append(os.path.join(root, f))

for item in FileList:
    print item

a = []
for line in open("exclude.txt","r"):
    line=line.strip('\n')
    print line
