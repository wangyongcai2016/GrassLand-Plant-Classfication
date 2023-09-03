#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import glob

if __name__ == '__main__':
    inpath = ""
    for f in os.listdir(inpath):
        subpath = os.path.join(inpath,f)
        imgf = glob.glob(os.path.join(subpath,"*"))
        for i,fname in enumerate(imgf):
            outfname = os.path.join(subpath, f"{f}_{i}" + os.path.basename(fname).split(".")[-1])
            os.rename(fname,outfname)