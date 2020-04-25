import tkinter
from CMSwithDATABASE import Customer
from customer_form import Customer_form
import tkinter.messagebox

class Login_form(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.create_widget()

    def create_widget(self):
        self.lbl_user=tkinter.Label(master=self,text="Username", width=16)
        self.lbl_user.grid(row=0, column=0)
        self.lbl_password = tkinter.Label(master=self, text="Password", width=16)
        self.lbl_password.grid(row=1, column=0)
        self.var_user=tkinter.StringVar()
        self.txt_user=tkinter.Entry(master=self,textvariable=self.var_user)
        self.txt_user.grid(row=0,column=1)
        self.var_password = tkinter.StringVar()
        self.txt_password = tkinter.Entry(master=self,show="*", textvariable=self.var_password)
        self.txt_password.grid(row=1, column=1)
        self.btn_login=tkinter.Button(master=self,text="Login",command=self.btn_login_click)
        self.btn_login.grid(row=2,column=2)
    def btn_login_click(self):
        try:
            Customer.connection(self.var_user.get(), self.var_password.get())
            cf=Customer_form()
            cf.grid(row=0, column=0)
        except Exception as ex:
            tkinter.messagebox.showerror(title="SQL connection", message="Please check your username/password !")

if __name__=="__main__":
    try:
        root = tkinter.Tk()
        lf = Login_form()
        lf.grid(row=0, column=0)
        #root.minsize(324, 155)
        root.mainloop()
    except Exception as ex:
        print(ex)
