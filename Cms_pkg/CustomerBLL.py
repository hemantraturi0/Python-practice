#BLL Code Start from Here
#Class Code Starts fromHere
import pymysql
class Customer:
    con = pymysql.connect(host="localhost", user="root", password="root123", database="18thnovbatch")
    def __init__(self):
        self.id=0
        self.name=''
        self.address=''
        self.mobile_no=''
    def __str__(self):
        return "ID: "+str(self.id)+" Name: "+self.name+" Address: "+self.address+" Mobile No: "+self.mobile_no

    def checkId(self,id):
        for e in Customer.list_cus:
            if(e.id==id):
                return True
        return False

    def add_customer(self):
        # write code to add customer
        try:
            myCursor=Customer.con.cursor()
            strQuery = "insert into customer values(%s,%s,%s,%s)"
            myCursor.execute(strQuery, (self.id, self.name, self.address, self.mobile_no))
            Customer.con.commit()
        except Exception as ex:
            raise Exception("Id already Exists")

    def search_customer(self,id):
        myCursor = Customer.con.cursor()
        strQuery = "select * from customer where id=%s"
        rowafftected=myCursor.execute(strQuery, (id,))
        if rowafftected!=0:
            row=myCursor.fetchone()
            self.id = row[0]
            self.name = row[1]
            self.address = row[2]
            self.mobile_no = row[3]
        else:
            raise Exception("Id not Found")

    def delete_customer(self,id):
        myCursor = Customer.con.cursor()
        strQuery = "delete from customer where id=%s"
        rowafftected = myCursor.execute(strQuery, (id,))
        if rowafftected != 0:
            Customer.con.commit()
        else:
            raise Exception("Id not Found")

    def modify_customer(self, id):
        myCursor = Customer.con.cursor()
        strQuery = "update customer set name=%s,address=%s,mobile_no=%s where id=%s"
        rowafftected = myCursor.execute(strQuery, (self.name,self.address,self.mobile_no,id))
        if rowafftected != 0:
            Customer.con.commit()
        else:
            raise Exception("Id not Found")

    @staticmethod
    def getAllCustomer():
        myCursor = Customer.con.cursor()
        strQuery = "select * from customer"
        rowafftected = myCursor.execute(strQuery)
        if rowafftected!=0:
            l1=[]
            for row in myCursor.fetchall():
                cus=Customer()
                cus.id=row[0]
                cus.name=row[1]
                cus.address=row[2]
                cus.mobile_no=row[3]
                l1.append(cus)
            return l1
    @staticmethod
    def sortCustomer():
        Customer.list_cus.sort(key=lambda e:e.id)


#BLL Code Ends Here

