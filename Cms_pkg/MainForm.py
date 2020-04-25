import tkinter
from Cms_pkg import *
root=tkinter.Tk()
frmLogin=Login_Form.Login_form(master=root)
frmLogin.grid(row=0,column=0)
frmCustomer=Customer_Form.Customer_Form(master=root)
frmCustomer.grid(row=1,column=0)

root.mainloop()