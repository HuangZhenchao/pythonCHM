# pythonCHM
#2021.02.06
python调用hhc.exe来编译chm文档

from pythonChm.pythonChm import pythonCHM
#两个参数：
#fileDir    文件路径
#delflag    是否删除中间生成的.hhp、.hhc、.hhk、Readme.txt文件,非必须，默认为True
pyCHM=pythonCHM(fileDir=u'D:\\book'[,delfalg=True])
pyCHM.excute()