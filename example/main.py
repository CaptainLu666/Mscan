#!/usr/bin/python2.7
#coding:utf-8
#author:luwen

import os
import sys
import time
#import datetime
import logging
#reload(sys)
#sys.setdefaultencoding('utf-8')
###global variables
Log_Dir='/data/logs/scan'
logging.basicConfig(level=logging.WARNING,
        format="[%(asctime)s]  %(message)s",filename=Log_Dir+'/jfscan.log',filemode='w')
IMAGE_TYPE = ['gif','png','jpg','jpeg']
PHP_TYPE = ['php']
ASP_TYPE = ['asp','aspx']

#plusdir = ['phpplus','imageplus','aspplus']
def loadplus(plus):
    filelist = []
#os.walk(起始路径，起始路径下的文件夹，起始路径下的文件)
    for root,dirs,files in os.walk(plus):
        for filespath in files:
            if filespath[-3:] == '.py':
                plusname = filespath[:-3]
                if plusname == '__init__':
                    continue
                __import__(root+'.'+plusname)
                filelist.append(plusname)
    return filelist


def Scan(path):
    #global backdoor_count
    for root,dirs,files in os.walk(path):
        for dn in open("./exclude.txt","r"):
            dn = dn.strip('\n')
            if dn in dirs:
                dirs.remove(dn)
        for filename in files:
            sufix = os.path.splitext(filename)[1][1:]
            filepath = os.path.join(root,filename)
            if sufix in IMAGE_TYPE:
                for imagemod in imagelist:
                    result = sys.modules['imageplus.'+imagemod].Check(filepath)
                    if result!=None:
                        message = '%s  %s  [%s]' %(time.strftime('%Y-%m-%d %H:%M:%S',
                            time.localtime(os.path.getmtime(filepath))),result[0],filepath)
                        logging.error(message)
                        break
            elif sufix in PHP_TYPE:
                for phpmod in phplist:
                    #以二进制读模式打开是可能有些文件是windows上面的
                    file= open(filepath,"rb")
                    filestr = file.read()
                    file.close()
                    result = sys.modules['phpplus.'+phpmod].Check(filestr,filepath)
                    if result!=None:
                        message = '%s  %s  [%s]' %(time.strftime('%Y-%m-%d %H:%M:%S',
                            time.localtime(os.path.getmtime(filepath))),result[0],filepath)
                        logging.error(message)
                        break
            else:
                for aspmod in asplist:
                    file= open(filepath,"rb")
                    filestr = file.read()
                    file.close()
                    result = sys.modules['aspplus.'+aspmod].Check(filestr,filepath)
                    if result!=None:
                        message = '%s  %s  [%s]' %(time.strftime('%Y-%m-%d %H:%M:%S',
                            time.localtime(os.path.getmtime(filepath))),result[0],filepath)
                        logging.error(message)
                        break
            #if filename[-4:] == '.asp':
            #if sufix in ASP_TYPE:
            #    for aspmod in asplist:
            #        file= open(filepath,"rb")
            #        filestr = file.read()
            #        file.close()
            #        result = sys.modules['aspplus.'+aspmod].Check(filestr,filepath)
            #        if result!=None:
            #            message = '%s  %s  [%s]' %(time.strftime('%Y-%m-%d %H:%M:%S',
            #                time.localtime(os.path.getmtime(filepath))),result[0],filepath)
            #            logging.error(message)
            #            break

def ScanFiletime(path,times):
    global backdoor_count
    times = time.mktime(time.strptime(times, '%Y-%m-%d %H:%M:%S'))
    print '########################################'
    print '文件路径           最后修改时间   \n'

    for root,dirs,files in os.walk(path):
        for dn in open("./exclude.txt","r"):
            dn = dn.strip('\n')
            if dn in dirs:
                dirs.remove(dn)
        for curfile in files:
            filepath = os.path.join(root,curfile)
            FileTime =os.path.getmtime(filepath)
            if FileTime>times:
                backdoor_count +=1
                print filepath+'        '+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(FileTime))

if __name__ == "__main__":
    os.chdir(sys.path[0])
    phplist = loadplus('phpplus')
    imagelist = loadplus('imageplus')
    asplist = loadplus('aspplus')
    backdoor_count = 0
    if len(sys.argv)!=3 and len(sys.argv)!=2:
        print '【参数错误】'
        print '\t按恶意代码查杀: '+sys.argv[0]+' 目录名'
        print '\t按修改时间查杀: '+sys.argv[0]+' 目录名 最后修改时间(格式:"2013-09-09 12:00:00")'
        exit()
    if not os.path.exists(Log_Dir):
        os.makedirs(Log_Dir)

    if os.path.lexists(sys.argv[1])==False:
        print '【错误提示】：指定的扫描目录不存在--- '
        exit()

    if len(sys.argv)==2:
        logging.info('开始查杀')
        sys.argv[1]+'\n'
        Scan(sys.argv[1])
        logging.info('查杀完成')
    else:
        print '\n\n【开始查找】'
        print sys.argv[1]+'\n'
        ScanFiletime(sys.argv[1],sys.argv[2])
        print '\n【查找完成】'
        print '\t文件总数: '+str(backdoor_count)
