# 同名のファイルがあるか判定
from pack import zipfilejpn

def Filecheck(file):
    import os
    basedir=os.path.dirname(file)
    ext = os.path.splitext(os.path.basename(file))[0]
    checkfile=basedir+"/"
    with zipfilejpn.ZipFile(file) as zip_f:

        # ZIPの中身を取得
        lst = zip_f.namelist() 

        # リストから取り出す
        for fil in lst:
            pass
    checkfile=checkfile+fil
    return checkfile

def FileWarnings(file):
    file2=Filecheck(file)
    import glob
    import os
    basedir=os.path.dirname(file)
    ext = os.path.splitext(os.path.basename(file))[0]
    checkfile=file2
    c=glob.glob(checkfile)
    if os.path.isfile(checkfile)==True:
        c=True
    else:
        c=False
    return c

def FileWarnings2(file):
    import glob
    import os
    basedir=os.path.dirname(file)
    ext = os.path.splitext(os.path.basename(file))[0]
    checkfile=basedir+"/"+ext+".dec"
    c=glob.glob(checkfile)
    i=-1
    if os.path.isfile(checkfile)==True:
        c=True
    else:
        c=False
    return c