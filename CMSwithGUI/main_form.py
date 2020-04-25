import tkinter
from loginPage import Login_form

if __name__=="__main__":
    try:
        root = tkinter.Tk()
        lf = Login_form()
        lf.grid(row=0, column=0)
        #root.minsize(540, 155)
        root.mainloop()
    except Exception as ex:
        print(ex)