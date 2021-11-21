import tkinter

class PswdBox(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.geometry("400x100")
        self.label1 = tkinter.Label(self,text="パスワードを入力してください")
        self.label1.pack() 
        self.resizable(False, False)
        self.title('DEC File password')
        self.ent = tkinter.Entry(self,font=("",15),show='*')
        self.ent.pack()
        self.lbl = tkinter.Label(self, foreground='#ff0000')
        self.lbl.pack()
        self.btn = tkinter.Button(self, text='確定', command=self.submit)
        self.btn.pack()
        self.mainloop()
    def submit(self):
        self.pswd = self.ent.get()
        if self.pswd!="" and self.pswd!=" ":
            self.destroy()