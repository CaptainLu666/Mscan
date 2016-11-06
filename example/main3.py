#!/usr/bin/python2.7
#coding:utf-8
#author:Mike
#blog:www.cnseay.com

import os
import sys
import time
import datetime
#reload(sys)
#sys.setdefaultencoding('utf-8')
###global variables
today = time.strftime('%Y%m%d',time.localtime(time.time()))
Log_Dir='/data/logs/scan'
Log_File_php='php-scan-' + today + '.log'
Log_File_image='image-scan-' + today + '.log'
Log_File_asp='asp-scan-' + today + '.log'
Logphp = os.path.join(Log_Dir,Log_File_php)
Logimage = os.path.join(Log_Dir,Log_File_image)
Logasp = os.path.join(Log_Dir,Log_File_asp)
fphp = open(Logphp,"a+")
fimage= open(Logimage,"a+")
fasp= open(Logasp,"a+")

IMAGE_TYPE = ['gif','png','jpg','jpeg']
PHP_TYPE = ['php']
ASP_TYPE = ['asp','aspx']

phparr=[] #插件列表
imagearr=[] #插件列表
asparr=[] #插件列表
backdoor_count=0

def loadplus():
    #if len(plusarr)>0:
    #    for plus in plusarr:
    #        del sys.modules['plus.'+plus]
    #    del plusarr[:]
#导入plus目录下的所有模块
#os.walk(起始路径，起始路径下的文件夹，起始路径下的文件)
    plusdir = ['phpplus','imageplus','aspplus']
    for plus in plusdir:
        for root,dirs,files in os.walk(plus):
            if root == 'phpplus':
                for filespath in files:
                    if filespath[-3:] == '.py':
                        plusname = filespath[:-3]
                        if plusname == '__init__':
                            continue
                        __import__(root+'.'+plusname)
                        phparr.append(plusname)
            if root == 'imageplus':
                for filespath in files:
    #                print filespath
                    if filespath[-3:] == '.py':
                        plusname = filespath[:-3]
                        if plusname == '__init__':
                            continue
                        __import__(root+'.'+plusname)
                        imagearr.append(plusname)
            if root == 'aspplus':
                for filespath in files:
                    if filespath[-3:] == '.py':
                        plusname = filespath[:-3]
                        if plusname == '__init__':
                            continue
    #                    print root
                        __import__(root+'.'+plusname)
                        asparr.append(plusname)
#            for filespath in files:
#                if filespath[-3:] == '.py':
#                    plusname = filespath[:-3]
#                    if plusname=='__init__':
#                        continue
#                    __import__(plus+'.'+plusname)

        #plusarr.append(plusname)

def Scan(path):
    loadplus() #动态加载插件
    #print sys.modules.keys()
    #print sys.modules.values()
    global backdoor_count
    for root,dirs,files in os.walk(path):
        for dn in open("./exclude.txt","r"):
            dn = dn.strip('\n')
            if dn in dirs:
                dirs.remove(dn)
        for filename in files:
            sufix = os.path.splitext(filename)[1][1:]
            filepath = os.path.join(root,filename)
            #if filename[-4:] == '.gif' or filename[-4:] == '.png' or filename[-4:] == '.jpg' or filename[-4:] == 'jpeg':
            if sufix in IMAGE_TYPE:
                for imagemod in imagearr:
                    result = sys.modules['imageplus.'+imagemod].Check(filepath)
                    if result!=None:
                        print >>fimage,'图片: ',
                        print >>fimage,filepath
                        print >>fimage,'后门代码: ',
                        for code in result[0]:
                            allstr = code + '|'
                            #print >>fimage,code[0][0:100]
                            print >>fimage,allstr
                        print >>fimage,'最后修改时间: '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filepath)))+'\n\n'
                        #backdoor_count= backdoor_count+1
                        break
            #if os.path.getsize(filepath)<500000:
            #if filename[-4:] == '.php':
            if sufix == 'php':
                for phpmod in phparr:
                    #以二进制读模式打开
                    file= open(filepath,"rb")
                    filestr = file.read()
                    file.close()
                    #运行模块里面的程序
                    result = sys.modules['phpplus.'+phpmod].Check(filestr,filepath)

                    if result!=None:
                        print >>fphp,'文件: ',
                        print >>fphp,filepath
                        print >>fphp,'后门描述: ',
                        print >>fphp,result[1]
                        print >>fphp,'后门代码: ',
                        for code in result[0]:
                            print >>fphp,code[0][0:100]
                        print >>fphp,'最后修改时间: '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filepath)))+'\n\n'
                        backdoor_count= backdoor_count+1
                        break
            #if filename[-4:] == '.asp':
            if sufix in ASP_TYPE:
                for aspmod in asparr:
                    #以二进制读模式打开
                    file= open(filepath,"rb")
                    filestr = file.read()
                    file.close()
                    #运行模块里面的程序
                    result = sys.modules['aspplus.'+aspmod].Check(filestr,filepath)
                    #print result

                    if result!=None:
                        print >>fasp,'文件: ',
                        print >>fasp,filepath
                        print >>fasp,'后门描述: ',
                        print result[1]
                        print >>fasp,result[1]
                        print >>fasp,'后门代码: ',
                        print result[0]
                        for code in result[0]:
                            print >>fasp,code + '|'
                        print >>fasp,'最后修改时间: '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filepath)))+'\n\n'
                        #backdoor_count= backdoor_count+1
                        break


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
#            if '.' in curfile:
#                suffix = curfile[-4:].lower()
            filepath = os.path.join(root,curfile)
                #可以配置需要扫描哪些文件的时间
#                if suffix=='.php' or suffix=='.jsp' or suffix=='.asp':
            FileTime =os.path.getmtime(filepath)
            if FileTime>times:
                backdoor_count +=1
                print filepath+'        '+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(FileTime))



if __name__ == "__main__":
    os.chdir(sys.path[0])
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
        print >>fphp,'\n\n【开始查杀】'
        print >>fphp,sys.argv[1]+'\n'
        Scan(sys.argv[1])
        print >>fphp,'【查杀完成】'
        print >>fphp,'\t后门总数: '+str(backdoor_count)
    else:
        print '\n\n【开始查找】'
        print sys.argv[1]+'\n'
        ScanFiletime(sys.argv[1],sys.argv[2])
        print '\n【查找完成】'
        print '\t文件总数: '+str(backdoor_count)
    fphp.close()
    fimage.close()
    fasp.close()
