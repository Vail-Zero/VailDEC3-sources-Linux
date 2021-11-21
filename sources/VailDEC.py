
# Copyright (c) 2020 Vail-Zero. All Rights Resarved.

# 必要なライブラリーインポート                
from tkinter import messagebox
from pack import decker
import tkinter
import threading
import os
import sys
from pack import passgen
# from pack import config
# from pack import GUIl
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import webbrowser
# from pack import regkey
global txt
from pack import PassBox
# 画像の後ろの背景色設定
backclr=""

args=sys.argv
if len(args)==2:
    pb = PassBox.PswdBox()
    pass1=str(pb.pswd)
    if os.path.isfile(args[1])==True:
        r, e = os.path.splitext(args[1])
        file=args[1]
        if e==".dec":
            ns=0
            n=decker.openzip(file,ns,pass1)
        else:
            n=decker.comzip(file,pass1)
        if e==".dec":
            root = tkinter.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            if n==0:
                messagebox.showerror('エラー', '指定されたファイルまたはディレクトリが見つかりません。')
            if n==1:
                messagebox.showinfo('確認', '復号化が終了しました!')
            if n==-2: 
                messagebox.showerror('エラー', 'パスワードが間違っています')
            if n==-3:
                messagebox.showerror('エラー', 'ファイルはアクセスが制限されています')
            root.destroy()
            root.mainloop()
        else:
            root = tkinter.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            if n==0:
                messagebox.showerror('エラー', '指定されたファイルまたはディレクトリが見つかりません。')
            if n==1:
                messagebox.showinfo('確認', '暗号化が終了しました!')
            if n==-3:
                messagebox.showerror('エラー', 'ファイルはアクセスが制限されています')
            if n==-2:
                messagebox.showerror('エラー', '対応していないファイルの可能性があります')            
            root.destroy()
            root.mainloop()
    else:
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)  
        messagebox.showerror('エラー', '指定されたファイルまたはディレクトリが見つかりません。')            
        root.destroy()
        root.mainloop()
var = {'Theme': "None", 'online':True,'cash':"None"}
# リソース読み込み関数
def resourcePath(filename):
  if hasattr(sys, "_MEIPASS"):
      return os.path.join(sys._MEIPASS, filename)
  return os.path.join(filename)

# ボタンクリック後の処理

# 暗号化
def btn_click(pass1):
    iDir = ""
    
    # var=config.loadconf()
    var = {'Theme': "None", 'online':True,'cash':"None"}
    fTyp = [("", "*")]
    # iDir=os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop"
    file = tkinter.filedialog.askopenfilename(filetypes=fTyp,initialdir=iDir)
    import shutil
    import tempfile
    if file=="":
        return
    if file=="":
        return
    n=decker.comzip(file,pass1)
    if n==0:
        messagebox.showerror('エラー', '指定されたファイルまたはディレクトリが見つかりません。')
    if n==1:
        messagebox.showinfo('確認', '暗号化が終了しました!')
    if n==-3:
        messagebox.showerror('エラー', 'ファイルはアクセスが制限されています')
    if n==-2:
        messagebox.showerror('エラー', '対応していないファイルの可能性があります')        
    return 

# 復号化関数
def btn2_click(pass1):
    iDir = ""
    n=-1
    var = {'Theme': "None", 'online':True,'cash':"None"}
    fTyp = [("DEC Files", "*.dec")]
    # iDir=os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop"
    file = tkinter.filedialog.askopenfilename(filetypes=fTyp,initialdir=iDir)
    import shutil
    import tempfile
    if file=="":
        return
    ns=0
    n=decker.openzip(file,ns,pass1)
    if n==0:
        messagebox.showerror('エラー', '指定されたファイルまたはディレクトリが見つかりません。')
    if n==1:
        messagebox.showinfo('確認', '復号化が終了しました!')
    if n==-2: 
        messagebox.showerror('エラー', 'パスワードが間違っています')
    if n==-3:
        messagebox.showerror('エラー', 'ファイルはアクセスが制限されています')
    if n==4:
        messagebox.showerror('エラー', 'ファイルが破損している可能性があります。\n元データでもう一度暗号化しなおしてください。\nこのファイルを他人から受け取った場合は、正式なファイルのコピーをもう一度取得してください')
    return
        
# 以下スレッド化
def btn():
    pass1=txt.get()
    if pass1=="":
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showerror('エラー', 'パスワードを入力してください')
        root.destroy()
        root.mainloop()
        return
    thread1 = threading.Thread(target=btn_click,args=([pass1]))
    thread1.start()
    txt.delete(0, tkinter.END)
    return

def btn2():
    pass1=txt.get()
    if pass1=="":
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showerror('エラー', 'パスワードを入力してください')
        root.destroy()
        root.mainloop()
        return
    thread1 = threading.Thread(target=btn2_click,args=([pass1]))
    thread1.start()
    txt.delete(0, tkinter.END)
    return

# ここまで

def btn04():
    import pyperclip
    txt.delete(0, tkinter.END)   
    import random
    cc=random.randint(5,20)
    bpass=passgen.gen(cc)
    b=messagebox.askyesno('確認', bpass+'\n 生成したパスワードをパスワードボックスに入れますか?\n 「OK」をクリックした場合、パスワードはクリップボードにコピーされます。')                
    if b==False:
        return
    pyperclip.copy(bpass)
    txt.insert(tkinter.END,bpass)
    return
 
# ここまで

# 画面初期化
def put(event):
    import pyperclip
    txt.insert(tkinter.END,pyperclip.paste())
    return

# GUIl.delcheck()

# メインウインドウを作成

window = tkinter.Tk()
window.geometry("451x300")
window.title("VailDEC ファイル暗号化ソフト")
#window.configure(bg=backclr)
window.resizable(False, False)

# 背景画像とアイコンの設定
iconfile = resourcePath('resources/IMG_8776.ICO')
# window.iconbitmap(iconfile)
window.attributes("-topmost", False)
txt = tkinter.Entry(font=("",15),show='*')
txt.place(x=130, y=200)
#label2 = ttk.Label(window, text='パスワード')
#label2.place(x=65, y=200)

# ボタンの追加と配置
btn4 = tkinter.Button(window, text="パスワード生成",command = btn04)
btn4.place(x=300, y=18)

label3 = ttk.Label(window, text='パスワードを下に入力してからボタンを押してください')
label3.place(x=101, y=180)

btn = tkinter.Button(window, text="暗号化",command = btn,font=("", 25))
btn.place(x=90, y=100)

btn2 = tkinter.Button(window, text="復号化",command = btn2,font=("", 25))
btn2.place(x=250, y=100)
window.mainloop()
