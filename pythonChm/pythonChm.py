#! /usr/bin/env python  
# -*- coding:utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class pythonCHM():
    #参数
    #项目名projectName，项目位置path
    def __init__(self, filedir,delfalg=True):
        self.filedir=filedir
        dirname, basename = os.path.split(filedir)
        self.filelist = os.listdir(filedir)
        self.chmTitle = basename + '.chm'

        self.chmFilePath = dirname + '\\'+self.chmTitle
        self.hhpFilePath = filedir + '\chm.hhp'
        self.hhcFilePath = filedir + '\chm.hhc'
        self.hhkFilePath = filedir + '\index.hhk'
        self.defaultTopicPath = filedir + '\Readme.txt'

        self.delflag=delfalg
    # 生成hhp文件(项目文件)
    def mk_hhpfile(self):
        hhpfilestr=''
        hhpfilestr += '[OPTIONS]\n'
        hhpfilestr += 'Title='+self.chmTitle+'\n'
        hhpfilestr += 'Compatibility=1.1 or later\n'
        hhpfilestr += 'Compiled file='+self.chmFilePath+'\n'
        hhpfilestr += 'Contents file='+self.hhcFilePath+'\n'
        hhpfilestr += 'Index file='+self.hhkFilePath+'\n'
        hhpfilestr += 'Default topic='+self.defaultTopicPath+'\n'
        hhpfilestr += 'Display compile progress=NO\n'
        hhpfilestr += 'Language=0x804 中文（中国）\n'
        hhpfilestr += 'Default Window=Main\n'
        hhpfilestr += '[WINDOWS]\n'
        hhpfilestr += 'Main=,"'+self.hhcFilePath+'","'+self.hhkFilePath+'",,,,,,,0x20,180,0x104E, [80,60,720,540],0x0,0x0,,,,,0\n'
        fp = open(self.hhpFilePath, 'wb')
        fp.write(hhpfilestr)
        fp.close()


    # 生成hhc文件(内容文件)
    def mk_hhcfile(self):
        hhcfilestr = ''
        hhcfilestr += '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">\n'
        hhcfilestr += '<HTML>\n'
        hhcfilestr += '<HEAD>\n'
        hhcfilestr += '<meta name="GENERATOR" content="Microsoft&reg; HTML Help Workshop 4.1">\n'
        hhcfilestr += '<!-- Sitemap 1.0 -->\n'
        hhcfilestr += '</HEAD>\n'
        hhcfilestr += '<BODY>\n'
        hhcfilestr += '<OBJECT type="text/site properties">\n'
        hhcfilestr += '<param name="Window Styles" value="0x237">\n'
        hhcfilestr += '</OBJECT>\n'
        hhcfilestr += self.c_tree(self.filedir, self.filelist)
        hhcfilestr += '</BODY>\n'
        hhcfilestr += '</HTML>\n'
        fp = open(self.hhcFilePath, 'wb')
        fp.write(hhcfilestr.encode('GB18030'))
        fp.close()


    def c_tree(self, filedir, filelist):
        treestr = ''
        for file in filelist:
            if os.path.isdir(filedir+'\\'+file):
                treestr += '<UL>\n'
                treestr += '<LI>\n'
                treestr += '<OBJECT type="text/sitemap">\n'
                treestr += '<param name="Name" value="'+file+'">\n'
                treestr += '</OBJECT>\n'
                treestr += self.c_tree(filedir+'\\'+file, os.listdir(filedir+'\\'+file))
                treestr += '</UL>\n'
            else:
                treestr += '<UL>\n'
                treestr += '<LI><OBJECT type="text/sitemap">\n'
                treestr += '<param name="Name" value="'+file+'">\n'
                treestr += '<param name="Local" value="'+filedir+'\\'+file+'">\n'
                treestr += '</OBJECT>\n'
                treestr += '</UL>\n'
        return treestr


    # 生成hhk文件(索引文件)
    def mk_hhkfile(self):
        hhkfilestr = ''
        hhkfilestr += '<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">\n'
        hhkfilestr += '<HTML>\n'
        hhkfilestr += '<HEAD>\n'
        hhkfilestr += '<meta name="GENERATOR" content="Microsoft&reg; HTML Help Workshop 4.1">\n'
        hhkfilestr += '<!-- Sitemap 1.0 -->\n'
        hhkfilestr += '</HEAD>\n'
        hhkfilestr += '<BODY>\n'
        hhkfilestr += '<UL>\n'
        hhkfilestr += '<LI> <OBJECT type="text/sitemap">\n'
        hhkfilestr += '<param name="Name" value="1">\n'
        hhkfilestr += '<param name="Local" value="'+self.defaultTopicPath+'">\n'
        hhkfilestr += '</OBJECT>\n'
        hhkfilestr += '</UL>\n'
        hhkfilestr += '</BODY>\n'
        hhkfilestr += '</HTML>\n'
        fp = open(self.hhkFilePath, 'wb')
        fp.write(hhkfilestr.encode('gbk'))
        fp.close()

    def mk_Readme(self):
        menustr=self.menu_tree(self.filedir,self.filelist)
        fp = open(self.filedir+'\Readme.txt', 'wb')
        fp.write(menustr.encode('GB18030'))
        fp.close()

    def menu_tree(self,filedir, filelist):
        menustr = ''
        for file in filelist:
            if os.path.isdir(filedir + '\\' + file):
                menustr += self.menu_tree(filedir + '\\' + file, os.listdir(filedir + '\\' + file))
            else:
                menustr += filedir + '\\' + file + '\n'

        return menustr

    # 执行方法
    def excute(self):
        #print chmTitle, chmFilePath, hhcFilePath, hhkFilePath, defaultTopicPath
        self.mk_hhpfile()
        self.mk_hhcfile()
        self.mk_hhkfile()
        self.mk_Readme()
        cmd = "HHC.EXE "+self.hhpFilePath
        r_v = os.system(cmd)
        print r_v

        if self.delflag==True:
            os.remove(self.hhpFilePath)
            os.remove(self.hhcFilePath)
            os.remove(self.hhkFilePath)
            os.remove(self.defaultTopicPath)

