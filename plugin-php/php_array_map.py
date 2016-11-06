#!/usr/bin/python2.7
#coding:utf-8

import re

#\x65 acsii码对应的字母是e,ass\\x65rt=assert
rule=r'(array_map[\s\n]{0,20}\(.{1,5}(eval|assert|ass\\x65rt).{1,20}\$_(GET|POST|REQUEST).{0,15})'

def Check(filestr,filepath):
    if 'array_map' in filestr:
        result = re.compile(rule).findall(filestr)
        if len(result)>0:
            return result,'array_map后门'
    else:
        return None
