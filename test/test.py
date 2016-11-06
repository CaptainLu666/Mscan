#!/usr/bin/python2.7
#coding:utf-8

import re
import os
import subprocess
#import plus.php.php_array_map

#rule='((eval|assert)[\s|\n]{0,30}\([\s|\n]{0,30}(\\\\{0,1}\$((_(GET|POST|REQUEST|SESSION|SERVER)(\[[\'"]{0,1})[\w\(\)]{0,15}([\'"]{0,1}\]))|\w{1,10}))\s{0,5}\))'
#rule1='((eval|assert)[\s|\n]{0,30}\((gzuncompress|gzinflate\(){0,1}[\s|\n]{0,30}base64_decode.{0,100})'
#rule2='\s{0,10}=\s{0,10}([{@]{0,2}\\\\{0,1}\$_(GET|POST|REQUEST)|file_get_contents|["\']a["\']\.["\']s["\']\.|["\']e["\']\.["\']v["\']\.|["\']ass["\']\.).{0,20}'
#print rule

#for root,dirs,files in os.walk("/opt/app/upload/"):
#filepath='/opt/app/upload/portal.php'
#whitefilter=[
#                (['install/svinfo.php'],['fsockopen("tcp:']),
#            ]
#for white in whitefilter:
#    print white[0][0]
#    print white[1][0]
#    print filepath.replace('\\','/')
    #if white[0][0] in filepath.replace('\\','/') and white[1][0] in key:

#print whitefilter[1][0]
#print whitefilter[1][1]
#filepath.replace('\\','/')
#plusdir = ['phpplus','imageplus','aspplus']
#for plus in plusdir:
#    for root,dirs,files in os.walk(plus):
#        print root
        #for filespath in files:
            #if filespath[-3:] == '.py':
                #plusname = filespath[:-3]
                #print plusname
                #if plusname=='__init__':
                    #continue


#rule='(shell_exec|execute|request|base64_decode|eval|%>|\$\w*\(\);)'
rule = '((?:eval|eval_r|execute|ExecuteGlobal)\s*?\(?request)'
#rule2='\s{0,10}=\s{0,10}([{@]{0,2}\\\\{0,1}\$_(GET|POST|REQUEST)|file_get_contents|["\']a["\']\.["\']s["\']\.|["\']e["\']\.["\']v["\']\.|["\']ass["\']\.).{0,20}'
#vararr=['$_GET','$_POST','$_REQUEST','$_SESSION','$_SERVER']
#$\w*();
#shell_exec execute request %> base64_decode eval
def Check(filepath):
    os.environ['photo'] = str(filepath)
    imagestr = subprocess.Popen("xxd $photo", stdout=subprocess.PIPE, shell=True).communicate()[0]
    print imagestr
    result = re.compile(rule).findall(imagestr)
    if len(result)>0:
        for group in result:
            return result,'图片有后门'
    return None
#filepath = "/opt/app/SeayFindShell/photo/comments.gif"
#filepath = "/opt/app/SeayFindShell/photo/lu.gif"
filepath = "/opt/app/upload/lu.gif"
print Check(filepath)
