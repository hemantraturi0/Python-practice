from Cms_pkg.CustomerBLL import Customer
import tkinter
import tkinter.messagebox
class Customer_Form(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.create_widget()
    def create_widget(self):
        self.lbl_id = tkinter.Label(master=self, text="Customer ID", width=16)
        self.lbl_id.grid(row=0, column=0, columnspan=2)
        self.lbl_name = tkinter.Label(master=self, text="Name", width=16)
        self.lbl_name.grid(row=1, column=0, columnspan=2)
        self.lbl_address = tkinter.Label(master=self, text="Address", width=16)
        self.lbl_address.grid(row=2, column=0, columnspan=2)
        self.lbl_mobile_no = tkinter.Label(master=self, text="Mobile No", width=16)
        self.lbl_mobile_no.grid(row=3, column=0, columnspan=2)

        self.var_id = tkinter.IntVar()
        self.txt_id = tkinter.Entry(self, textvariable=self.var_id, width=16)
        self.txt_id.grid(row=0, column=2, columnspan=2)

        self.var_name = tkinter.StringVar()
        self.txt_name = tkinter.Entry(self, textvariable=self.var_name, width=16)
        self.txt_name.grid(row=1, column=2, columnspan=2)

        self.var_address = tkinter.StringVar()
        self.txt_address = tkinter.Entry(self, textvariable=self.var_address, width=16)
        self.txt_address.grid(row=2, column=2, columnspan=2)

        self.var_mobile_no = tkinter.StringVar()
        self.txt_mobile_no = tkinter.Entry(self, textvariable=self.var_mobile_no, width=16)
        self.txt_mobile_no.grid(row=3, column=2, columnspan=2)

        self.btn_add = tkinter.Button(master=self, text="Add Customer", width=16, command=self.btn_add_click)
        self.btn_add.grid(row=4, column=0)

        self.btn_delete = tkinter.Button(master=self, text="Delete Customer", width=16, command=self.btn_delete_click)
        self.btn_delete.grid(row=4, column=1)

        self.btn_search = tkinter.Button(master=self, text="Search Customer", width=16, command=self.btn_search_click)
        self.btn_search.grid(row=4, column=2)

        self.btn_modify = tkinter.Button(master=self, text="Modify Customer", width=16, command=self.btn_modify_click)
        self.btn_modify.grid(row=4, column=3)

    def btn_add_click(self):
        try:
            cus = Customer()  # creat a new Customer Object and variable, cus is a variable of Datatpe Customer means it has four memory blocks for id name address mobile_no because it is defind in constructor of Customer Class(__init__ method)

            cus.id = self.var_id.get()
            cus.name = self.var_name.get()
            cus.address = self.var_address.get()
            cus.mobile_no = self.var_mobile_no.get()
            cus.add_customer()
            tkinter.messagebox.showinfo("SUCESS","Customer added sucessfully")
        except Exception as ex:
            tkinter.messagebox.showerror('ERROR',ex)

    def btn_delete_click(self):
        try:
            id = self.var_id.get()
            cus = Customer()
            cus.delete_customer(id)
            tkinter.messagebox.showinfo('SUCESS',"Customer deleted Sucessfully")
        except Exception as ex:
            tkinter.messagebox.showerror('ERROR', ex)

    def btn_search_click(self):
        try:
            id = self.var_id.get()
            cus = Customer()
            cus.search_customer(id)
            self.var_name.set(cus.name)
            self.var_address.set(cus.address)
            self.var_mobile_no.set(cus.mobile_no)
        except Exception as ex:
            tkinter.messagebox.showerror('ERROR', ex)

    def btn_modify_click(self):
        try:
            cus = Customer()  # creat a new Customer Object and variable, cus is a variable of Datatpe Customer means it has four memory blocks for id name address mobile_no because it is defind in constructor of Customer Class(__init__ method)

            cus.id = self.var_id.get()
            cus.name = self.var_name.get()
            cus.address = self.var_address.get()
            cus.mobile_no = self.var_mobile_no.get()
            cus.modify_customer(cus.id)
            tkinter.messagebox.showinfo('SUCESS'"Customer Modified sucessfully")
        except Exception as ex:
            tkinter.messagebox.showerror('ERROR', ex)

