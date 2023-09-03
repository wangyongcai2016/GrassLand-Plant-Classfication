import urllib
import os
import pickle
from multiprocessing import Pool
import time
import socket

def GetImage(parms):
    """
    parms[0]:图像的url的地址
    parms[1]:图像保存的根目录
    parms[2]:图像工程的名称
    parms[3]:图像所属类的名称
    parms[4]:输出图像的名称
    """
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent','Mozilla/5.0')]
    urllib.request.install_opener(opener)
    basepath = os.path.join(parms[1],parms[2],parms[3])
    if not os.path.exists(basepath):
        os.makedirs(basepath)
    outfname = os.path.join(basepath,parms[4])
    if not os.path.exists(outfname):
        urllib.request.urlretrieve(parms[0],outfname)
if __name__ == '__main__':
    #将参数序列化导入
    fd = open(r"F:\AI_iplant\Paramaters.txt","rb")
    parameters = pickle.load(fd)
    fd.close()
    #mypool = Pool(12)
    #mypool.map(GetImage,parameters)
    for i,parm in enumerate(parameters):
        fpath = os.path.join(parm[1],parm[2],parm[3])
        fname = os.path.join(fpath,parm[4])
        if os.path.exists(fname):
            continue
        if i % 100 == 0:
            time.sleep(5)
        GetImage(parm)
        print(parm[0])

