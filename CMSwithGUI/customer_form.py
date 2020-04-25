from CMSwithDATABASE import Customer
import tkinter
import tkinter.messagebox

class Customer_form(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.create_widget()

    def create_widget(self):
        self.btn_add = tkinter.Button(master=self, text="Add Customer", width=14, command=self.btn_add_click)
        self.btn_add.grid(row=0, column=0)
        self.btn_delete = tkinter.Button(master=self, text="Delete Customer", width=14, command=self.btn_delete_click)
        self.btn_delete.grid(row=0, column=1)
        self.btn_search = tkinter.Button(master=self, text="Search Customer", width=14, command=self.btn_search_click)
        self.btn_search.grid(row=0, column=2)
        self.btn_modify = tkinter.Button(master=self, text="Modify Customer", width=14, command=self.btn_modify_click)
        self.btn_modify.grid(row=0, column=3)
        self.btn_show_all = tkinter.Button(master=self, text="Show all", width=14, command=self.btn_show_all_click)
        self.btn_show_all.grid(row=0, column=4)

        self.frame1=tkinter.LabelFrame(master=self, text="Input section", width=42)
        self.frame1.grid(row=1,column=2, columnspan=3)
        self.lbl_id = tkinter.Label(master=self.frame1, text="Customer ID", width=14)
        self.lbl_id.grid(row=0, column=0, columnspan=2)
        self.lbl_name = tkinter.Label(master=self.frame1, text="Name", width=14)
        self.lbl_name.grid(row=1, column=0, columnspan=2)
        self.lbl_age = tkinter.Label(master=self.frame1, text="Age", width=14)
        self.lbl_age.grid(row=2, column=0, columnspan=2)
        self.lbl_mobile_no = tkinter.Label(master=self.frame1, text="Mobile No", width=14)
        self.lbl_mobile_no.grid(row=3, column=0, columnspan=2)

        self.var_id = tkinter.IntVar()
        self.txt_id = tkinter.Entry(self.frame1, textvariable=self.var_id, state='disabled', width=28)
        self.txt_id.grid(row=0, column=2, columnspan=2)

        self.var_name = tkinter.StringVar()
        self.txt_name = tkinter.Entry(self.frame1, textvariable=self.var_name, state='disabled', width=28)
        self.txt_name.grid(row=1, column=2, columnspan=2)

        self.var_age = tkinter.StringVar()
        self.txt_age = tkinter.Entry(self.frame1, textvariable=self.var_age, state='disabled', width=28)
        self.txt_age.grid(row=2, column=2, columnspan=2)

        self.var_mobile_no = tkinter.StringVar()
        self.txt_mobile_no = tkinter.Entry(self.frame1, textvariable=self.var_mobile_no, state='disabled', width=28)
        self.txt_mobile_no.grid(row=3, column=2, columnspan=2)

    #Adding a customer
    def btn_add_click(self):
            self.btn_add = tkinter.Button(master=self.frame1, text="Add", width=14, command=self.btn_add_click_final)
            self.btn_add.grid(row=4, column=3)
            self.txt_id["state"]="disabled"
            self.txt_name["state"]="normal"
            self.txt_age["state"]="normal"
            self.txt_mobile_no["state"]="normal"
    def btn_add_click_final(self):
        try:
            cus = Customer()  # create a new Customer Object and variable, cus is a variable of Datatpe Customer means it has four memory blocks for id name address mobile_no because it is defind in constructor of Customer Class(__init__ method)
            if (len(self.var_name.get()) != 0):
                cus.name = self.var_name.get()
            else:
                raise Exception("Invalid inputs!!")
            if (len(self.var_name.get()) != 0):
                cus.age = self.var_age.get()
            else:
                raise Exception("Invalid inputs!!")
            if (len(self.var_name.get()) != 0):
                cus.mobile = self.var_mobile_no.get()
            else:
                raise Exception("Invalid inputs!!")
            cus.addCustomer()
            tkinter.messagebox.showinfo("SUCCESS", "Customer added successfully")
            self.var_id.set(0)
            self.var_name.set("")
            self.var_age.set("")
            self.var_mobile_no.set("")
        except Exception as ex:
            tkinter.messagebox.showerror('ERROR', ex)

    #Delete using id
    def btn_delete_click(self):
        self.btn_add = tkinter.Button(master=self.frame1, text="Delete", width=14, command=self.btn_delete_click_final)
        self.btn_add.grid(row=4, column=3)
        self.txt_id['state']="normal"
        self.txt_name["state"] = "disabled"
        self.txt_age["state"] = "disabled"
        self.txt_mobile_no["state"] = "disabled"
    def btn_delete_click_final(self):
        try:
            cus = Customer()
            cus.id = self.var_id.get()
            cus.delete()
            tkinter.messagebox.showinfo('SUCCESS', "Customer deleted Successfully")
            self.var_id.set(0)
            self.var_name.set("")
            self.var_age.set("")
            self.var_mobile_no.set("")
        except Exception as ex:
            tkinter.messagebox.showerror('ERROR', ex)

    def btn_search_click(self):
        self.txt_id['state'] = "disabled"
        self.txt_name["state"] = "disabled"
        self.txt_age["state"] = "disabled"
        self.txt_mobile_no["state"] = "disabled"
        self.search_frame=tkinter.LabelFrame(master=self, text="Search by", width=28)
        self.search_frame.grid(row=1,column=0, columnspan=2)
        self.search_var=tkinter.StringVar()
        r=tkinter.Radiobutton(self.search_frame, text="Select one", variable=self.search_var, value="none", command=self.search, anchor='w')
        r.grid(row=0,column=0)
        r1=tkinter.Radiobutton(self.search_frame, text="ID", variable=self.search_var, value="id", command=self.search)
        r1.grid(row=1,column=0)
        r2=tkinter.Radiobutton(self.search_frame, text="Name", variable=self.search_var, value="name", command=self.search)
        r2.grid(row=1,column=1)
        r3=tkinter.Radiobutton(self.search_frame, text="Age", variable=self.search_var, value="age", command=self.search)
        r3.grid(row=2,column=0)
        r4=tkinter.Radiobutton(self.search_frame, text="Mobile", variable=self.search_var, value="mobile", command=self.search)
        r4.grid(row=2,column=1)
        self.search_var.set('none')
    def search(self):
        self.btn_search_final = tkinter.Button(master=self.frame1, text="Search", width=14, command=self.search_final)
        self.btn_search_final.grid(row=4, column=3)
        if(self.search_var.get()=="id"):
            self.txt_id["state"]="normal"
            self.txt_name["state"] = "disabled"
            self.txt_age["state"] = "disabled"
            self.txt_mobile_no["state"] = "disabled"
        elif(self.search_var.get()=="name"):
            self.txt_id["state"] = "disabled"
            self.txt_name["state"]="normal"
            self.txt_age["state"] = "disabled"
            self.txt_mobile_no["state"] = "disabled"
        elif (self.search_var.get() == "age"):
            self.txt_id["state"] = "disabled"
            self.txt_name["state"] = "disabled"
            self.txt_age["state"] = "normal"
            self.txt_mobile_no["state"] = "disabled"
        elif (self.search_var.get() == "mobile"):
            self.txt_id["state"] = "disabled"
            self.txt_name["state"] = "disabled"
            self.txt_age["state"] = "disabled"
            self.txt_mobile_no["state"] = "normal"
        else:
            self.txt_id["state"] = "disabled"
            self.txt_name["state"] = "disabled"
            self.txt_age["state"] = "disabled"
            self.txt_mobile_no["state"] = "disabled"
    def search_final(self):
        try:
            cus=Customer()
            if self.txt_id["state"]=="normal":
                cus.id=self.var_id.get()
                cus.searchId()
            elif self.txt_name["state"]=="normal":
                cus.name=self.var_name.get()
                cus.searchName()
            elif self.txt_age["state"]=="normal":
                cus.age=self.var_age.get()
                cus.searchAge()
            elif self.txt_mobile_no["state"]=="normal":
                cus.mobile=self.var_mobile_no.get()
                cus.searchMobile()
            if (len(Customer.searchList) != 0):
                root = tkinter.Tk()
                lbl_id=tkinter.Label(root, text="ID", anchor="w", width=5)
                lbl_id.grid(row=0,column=0)
                lbl_name = tkinter.Label(root, text="Name", anchor="w", width=16)
                lbl_name.grid(row=0, column=1)
                lbl_age = tkinter.Label(root, text="Age", anchor="w",width=5)
                lbl_age.grid(row=0, column=2)
                lbl_mobile = tkinter.Label(root, text="Mobile", anchor="w",width=10)
                lbl_mobile.grid(row=0, column=3)
                line=1
                for e in Customer.searchList:
                    lbl_id = tkinter.Label(root, text=str(e.id), anchor="w", width=5)
                    lbl_id.grid(row=line, column=0)
                    lbl_name = tkinter.Label(root, text=e.name, anchor="w", width=16)
                    lbl_name.grid(row=line, column=1)
                    lbl_age = tkinter.Label(root, text=e.age, anchor="w", width=5)
                    lbl_age.grid(row=line, column=2)
                    lbl_mobile = tkinter.Label(root, text=e.mobile, anchor="w", width=10)
                    lbl_mobile.grid(row=line, column=3)
                    line+=1
            else:
                tkinter.messagebox.showinfo("CMS", "No records!!")
            self.var_id.set(0)
            self.var_name.set("")
            self.var_age.set("")
            self.var_mobile_no.set("")
        except Exception as ex:
            tkinter.messagebox.showerror("Error", ex)

    # Modify Customers
    def btn_modify_click(self):
        self.txt_id['state'] = "disabled"
        self.txt_name["state"] = "disabled"
        self.txt_age["state"] = "disabled"
        self.txt_mobile_no["state"] = "disabled"
        self.search_frame = tkinter.LabelFrame(master=self, text="Modify", width=28)
        self.search_frame.grid(row=1, column=0, columnspan=2)
        self.search_var = tkinter.StringVar()
        r = tkinter.Radiobutton(self.search_frame, text="Select one", variable=self.search_var, value="none", command=self.modify, anchor='w')
        r.grid(row=0, column=0)
        r1 = tkinter.Radiobutton(self.search_frame, text="Name", variable=self.search_var, value="name", command=self.modify)
        r1.grid(row=1, column=0)
        r2 = tkinter.Radiobutton(self.search_frame, text="Age", variable=self.search_var, value="age", command=self.modify)
        r2.grid(row=1, column=1)
        r3 = tkinter.Radiobutton(self.search_frame, text="Mobile", variable=self.search_var, value="mobile", command=self.modify)
        r3.grid(row=2, column=0)
        r4 = tkinter.Radiobutton(self.search_frame, text="All", variable=self.search_var, value="all", command=self.modify)
        r4.grid(row=2, column=1)
        self.search_var.set('none')
    def modify(self):
        self.btn_search_final = tkinter.Button(master=self.frame1, text="Modify", width=14, command=self.modify_final)
        self.btn_search_final.grid(row=4, column=3)
        if (self.search_var.get() == "all"):
            self.txt_id["state"] = "normal"
            self.txt_name["state"] = "normal"
            self.txt_age["state"] = "normal"
            self.txt_mobile_no["state"] = "normal"
        elif (self.search_var.get() == "name"):
            self.txt_id["state"] = "normal"
            self.txt_name["state"] = "normal"
            self.txt_age["state"] = "disabled"
            self.txt_mobile_no["state"] = "disabled"
        elif (self.search_var.get() == "age"):
            self.txt_id["state"] = "normal"
            self.txt_name["state"] = "disabled"
            self.txt_age["state"] = "normal"
            self.txt_mobile_no["state"] = "disabled"
        elif (self.search_var.get() == "mobile"):
            self.txt_id["state"] = "normal"
            self.txt_name["state"] = "disabled"
            self.txt_age["state"] = "disabled"
            self.txt_mobile_no["state"] = "normal"
        else:
            self.txt_id["state"] = "normal"
            self.txt_name["state"] = "disabled"
            self.txt_age["state"] = "disabled"
            self.txt_mobile_no["state"] = "disabled"
    def modify_final(self):
        try:
            cus = Customer()
            if self.txt_age["state"] == "normal" and self.txt_name["state"] == "normal" and self.txt_mobile_no["state"] == "normal":
                cus.id=self.var_id.get()
                if(len(self.var_name.get())!=0 and len(self.var_age.get())!=0 and len(self.var_mobile_no.get())!=0):
                    cus.name = self.var_name.get()
                    cus.age = self.var_age.get()
                    cus.mobile = self.var_mobile_no.get()
                    cus.modAll()
                else:
                    raise Exception("Invalid inputs!!")
            elif self.txt_name["state"] == "normal":
                cus.id = self.var_id.get()
                if(len(self.var_name.get())!=0):
                    cus.name = self.var_name.get()
                    cus.modName()
                else:
                    raise Exception("Invalid inputs!!")
            elif self.txt_age["state"] == "normal":
                cus.id = self.var_id.get()
                if(len(self.var_age.get()!=0)):
                    cus.age = self.var_age.get()
                    cus.modAge()
                else:
                    raise Exception("Invalid inputs!!")
            elif self.txt_mobile_no["state"] == "normal":
                cus.id = self.var_id.get()
                if(len(self.var_mobile_no.get()!=0)):
                    cus.mobile = self.var_mobile_no.get()
                    cus.modMobile()
                else:
                    raise Exception("Invalid inputs!!")
            tkinter.messagebox.showinfo("CMS", "Modified successfully!")
            self.var_id.set(0)
            self.var_name.set("")
            self.var_age.set("")
            self.var_mobile_no.set("")
        except Exception as ex:
            tkinter.messagebox.showerror("CMS,", ex)
    #Show all customers
    def btn_show_all_click(self):
        try:
            root=tkinter.Tk()
            Customer.showAll()
            if (len(Customer.searchList) != 0):
                lbl_id=tkinter.Label(root, text="ID", anchor="w", width=5)
                lbl_id.grid(row=0,column=0)
                lbl_name = tkinter.Label(root, text="Name", anchor="w", width=16)
                lbl_name.grid(row=0, column=1)
                lbl_age = tkinter.Label(root, text="Age", anchor="w",width=5)
                lbl_age.grid(row=0, column=2)
                lbl_mobile = tkinter.Label(root, text="Mobile", anchor="w",width=10)
                lbl_mobile.grid(row=0, column=3)
                line=1
                for e in Customer.searchList:
                    lbl_id = tkinter.Label(root, text=str(e.id), anchor="w", width=5)
                    lbl_id.grid(row=line, column=0)
                    lbl_name = tkinter.Label(root, text=e.name, anchor="w", width=16)
                    lbl_name.grid(row=line, column=1)
                    lbl_age = tkinter.Label(root, text=e.age, anchor="w", width=5)
                    lbl_age.grid(row=line, column=2)
                    lbl_mobile = tkinter.Label(root, text=e.mobile, anchor="w", width=10)
                    lbl_mobile.grid(row=line, column=3)
                    line+=1
            else:
                lbl_empty=tkinter.Label(root, text="No records !!")
                lbl_empty.grid(row=0, column=0)
            self.var_id.set(0)
            self.var_name.set("")
            self.var_age.set("")
            self.var_mobile_no.set("")
        except Exception as ex:
            tkinter.messagebox.showerror("Error", ex)

if __name__=="__main__":
    root=tkinter.Tk()
    cf=Customer_form()
    cf.grid(row=0,column=0)
    root.mainloop()