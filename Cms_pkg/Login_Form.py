import tkinter
class Login_form(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.create_widget()
    def create_widget(self):
        self.email_id=tkinter.Label(master=self,text="Email Id",width=16)
        self.email_id.grid(row=0,column=0)
        self.password = tkinter.Label(master=self, text="Password", width=16)
        self.password.grid(row=1, column=0)
        self.var_email_id=tkinter.StringVar()
        self.txt_email_id=tkinter.Entry(master=self,textvariable=self.var_email_id)
        self.txt_email_id.grid(row=0,column=1)
        self.var_password = tkinter.StringVar()
        self.txt_password = tkinter.Entry(master=self, textvariable=self.var_password)
        self.txt_password.grid(row=1, column=1)
        self.btn_login=tkinter.Button(master=self,text="Login",command=self.btn_login_click)
        self.btn_login.grid(row=2,column=2)
    def btn_login_click(self):
        pass