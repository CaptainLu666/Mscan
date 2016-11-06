#!/usr/bin/python2.7
#coding:utf-8

import re
import os
import subprocess

rule='(shell_exec|execute|request|base64_decode|eval|%>|\$\w*\(\);)'
#rule='(shell_exec|execute|request|base64_decode|eval|\$\w*\(\);)'
rule = '((?:eval|eval_r|execute|ExecuteGlobal)\s*?\(?request)'
#rule2='\s{0,10}=\s{0,10}([{@]{0,2}\\\\{0,1}\$_(GET|POST|REQUEST)|file_get_contents|["\']a["\']\.["\']s["\']\.|["\']e["\']\.["\']v["\']\.|["\']ass["\']\.).{0,20}'
#vararr=['$_GET','$_POST','$_REQUEST','$_SESSION','$_SERVER']
#$\w*();
#shell_exec execute request %> base64_decode eval

def Check(filepath):
    os.environ['photo'] = str(filepath)
    imagestr = subprocess.Popen("xxd $photo", stdout=subprocess.PIPE, shell=True).communicate()[0]
    result = re.compile(rule).findall(imagestr)
    if len(result)>0:
        for group in result:
            return result,'图片有shell_exec|execute|request|base64_decode|eval后门'
    return None
