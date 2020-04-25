import pymysql

class Customer:
    con = pymysql.connect(host="localhost", user="root", password="", database="cms")
    searchList=[]
    def __init__(self):
        self.id=0
        self.name=""
        self.age=""
        self.mobile=""

    def addCustomer(self):
        try:
            global con
            myCursor=con.cursor()
            strQuery=f"INSERT INTO cms(name, age, mobile) values ('{self.name}','{self.age}','{self.mobile}')"
            rowsAffected=myCursor.execute(strQuery)
            if rowsAffected!=0:
                con.commit()
        except Exception:
            raise Exception("Error while adding to database")

    def searchId(self):
        try:
            Customer.searchList.clear()
            global con
            myCursor = con.cursor()
            strQuery = f"SELECT * FROM cms WHERE id={self.id}"
            rowsAffected=myCursor.execute(strQuery)
            if rowsAffected!=0:
                for rows in myCursor.fetchall():
                    if(rows[0]==self.id):
                        self.name = rows[1]
                        self.age = rows[2]
                        self.mobile = rows[3]
                        Customer.searchList.append(self)
        except Exception:
            raise Exception("Error while searching")

    def searchName(self):
        try:
            Customer.searchList.clear()
            global con
            myCursor = con.cursor()
            strQuery = f"SELECT * FROM cms WHERE name='{self.name}'"
            rowsAffected = myCursor.execute(strQuery)
            if rowsAffected != 0:
                for rows in myCursor.fetchall():
                    if (rows[1] == self.name):
                        cus=Customer()
                        cus.id = rows[0]
                        cus.name=rows[1]
                        cus.age = rows[2]
                        cus.mobile = rows[3]
                        Customer.searchList.append(cus)
        except Exception as ex:
            print(ex)
            raise Exception("Error while searching")

    def searchAge(self):
        try:
            Customer.searchList.clear()
            global con
            myCursor = con.cursor()
            strQuery = f"SELECT * FROM cms WHERE age='{self.age}'"
            rowsAffected = myCursor.execute(strQuery)
            if rowsAffected != 0:
                for rows in myCursor.fetchall():
                    if (rows[2] == self.age):
                        cus = Customer()
                        cus.id = rows[0]
                        cus.name = rows[1]
                        cus.age = rows[2]
                        cus.mobile = rows[3]
                        Customer.searchList.append(cus)
        except Exception:
            raise Exception("Error while searching")

    def searchMobile(self):
        try:
            Customer.searchList.clear()
            global con
            myCursor = con.cursor()
            strQuery = f"SELECT * FROM cms WHERE mobile='{self.mobile}'"
            rowsAffected = myCursor.execute(strQuery)
            if rowsAffected != 0:
                for rows in myCursor.fetchall():
                    if (rows[3] == self.mobile):
                        cus = Customer()
                        cus.id = rows[0]
                        cus.name = rows[1]
                        cus.age = rows[2]
                        cus.mobile = rows[3]
                        Customer.searchList.append(cus)
        except Exception:
            raise Exception("Error while searching")

    def modName(self):
        try:
            global con
            myCursor = con.cursor()
            strQuery = f"UPDATE cms SET name='{self.name}' WHERE id={self.id}"
            rowsAffected=myCursor.execute(strQuery)
            if rowsAffected!=0:
                con.commit()
        except Exception as ex:
            raise Exception("Error while updating")

    def modAge(self):
        try:
            global con
            myCursor = con.cursor()
            strQuery = f"UPDATE cms SET age='{self.age}' WHERE id={self.id}"
            rowsAffected = myCursor.execute(strQuery)
            if rowsAffected!=0:
                con.commit()
        except Exception as ex:
            raise Exception("Error while updating")

    def modMobile(self):
        try:
            global con
            myCursor = con.cursor()
            strQuery = f"UPDATE cms SET mobile='{self.mobile}' WHERE id={self.id}"
            rowsAffected = myCursor.execute(strQuery)
            if rowsAffected != 0:
                con.commit()
        except Exception as ex:
            raise Exception("Error while updating")

    def modAll(self):
        try:
            global con
            myCursor = con.cursor()
            strQuery = f"UPDATE cms SET name='{self.name}',age='{self.age}',mobile='{self.mobile}' WHERE id={self.id}"
            rowsAffected = myCursor.execute(strQuery)
            if rowsAffected != 0:
                con.commit()
        except Exception as ex:
            raise Exception("Error while updating")
    def delete(self):
        try:
            global con
            myCursor = con.cursor()
            strQuery = f"DELETE FROM cms WHERE id={self.id}"
            rowsAffected = myCursor.execute(strQuery)
            if rowsAffected != 0:
                con.commit()
        except Exception as ex:
            raise Exception("Error while deleting")

    @staticmethod
    def showAll():
        try:
            Customer.searchList.clear()
            global con
            myCursor=con.cursor()
            strQuery="SELECT * FROM cms"
            rowsAffected=myCursor.execute(strQuery)
            if rowsAffected!=0:
                for rows in myCursor.fetchall():
                    cus=Customer()
                    cus.id=rows[0]
                    cus.name=rows[1]
                    cus.age=rows[2]
                    cus.mobile=rows[3]
                    Customer.searchList.append(cus)
        except Exception:
            raise Exception("Error while retrieving")

    @staticmethod
    def connection(host="localhost", user="root", password="", database="cms"):
        try:
            global con
            con = pymysql.connect(host, user, password, database)
        except:
            raise Exception("Error while logging in")

#Verifying correctness of name,age and mobile number
def verify(value, para):
    if(para=="name"):
        if(all(x.isalpha() or x.isspace() for x in value)):
            return 1
    elif(para=="age"):
        if(value.isnumeric() and int(value)>0 and int(value)<=120):
            return 1
    elif(para=="mobile"):
        if(value.isnumeric() and len(value)==10):
            return 1
    elif(para=="id"):
        if(value.isnumeric()):
                    return 1
    else:
        return -1

if(__name__=="__main__"):
    print("Welcome to CMS".center(50,"="))
    while(True):
        try:
            host=input("Enter server name :")
            user=input("Enter user name :")
            password=input("Enter password :")
            database=input("Enter database name :")
            Customer.connection(host, user, password, database)
            print("Connection established !!")
            break
        except Exception as ex:
            print(ex)
    while(True):
        print("==================================================")
        ch=input("Enter your choice\n1.Add a customer.\n2.Search a customer.\n3.Modify a customer.\n4.Delete a customer.\n5.Show all customers.\n6.Exit\n")
        #Adding customers
        if(ch=="1"):
            while(True):
                cus=Customer()
                tempName=input("\nEnter the name of customer: ").lower().title()
                temp=verify(tempName, para="name")
                if temp==1:
                    cus.name=tempName
                else:
                    print("\nName incorrect! Try again.")
                    continue
                tempAge=input("Enter the age of customer: ")
                temp=verify(tempAge, para="age")
                if temp==1:
                    cus.age=tempAge
                else:
                    print("\nAge incorrect! Try again.")
                    continue
                tempMob=input("Enter the mobile number of customer: ")
                temp=verify(tempMob, para="mobile")
                if temp==1:
                    cus.mobile=tempMob
                else:
                    print("\nMobile number incorrect! Try again.")
                    continue
                try:
                    cus.addCustomer()
                    print("\nCustomer added successfully!!!")
                    another=input("\nAdd another customer? (Y/N): ")
                    if(another=="N" or another=="n"):
                        break
                    elif(another=="Y" or another=="y"):
                        continue
                    else:
                        print("\nIncorrect input")
                        break
                except Exception as ex:
                    print(ex)
        #Searching
        elif(ch=="2"):
            while(True):
                cus = Customer()
                search = input("\nSearch by:\n1.ID\n2.Name\n3.age\n4.Mobile number\n5.To main menu\n")
                if(search=="1"):
                    tempId=input("Enter the id of customer: ")
                    temp=verify(tempId, para="id")
                    if temp==1:
                        cus.id=int(tempId)
                    else:
                        print("\nId incorrect! Try again.")
                        continue
                    try:
                        cus.searchId()
                        if(len(Customer.searchList)==0):
                            print("\nNo such customer!")
                        else:
                            print("ID".ljust(5), "Name".ljust(15), "Age".ljust(5), "Mobile number")
                            print("------------------------------------------")
                            for e in Customer.searchList:
                                print(str(e.id).ljust(5), e.name.ljust(15), e.age.ljust(5), e.mobile)
                            print(len(Customer.searchList),"Records found")
                    except Exception as ex:
                        print(ex)
                elif(search=="2"):
                    tempName = input("\nEnter the name of customer: ").lower().title()
                    temp = verify(tempName, para="name")
                    if temp == 1:
                        cus.name = tempName
                    else:
                        print("\nName incorrect! Try again.")
                        continue
                    try:
                        cus.searchName()
                        if (len(Customer.searchList) == 0):
                            print("\nNo such customer!")
                        else:
                            print("ID".ljust(5), "Name".ljust(15), "Age".ljust(5), "Mobile number")
                            print("------------------------------------------")
                            for e in Customer.searchList:
                                print(str(e.id).ljust(5), e.name.ljust(15), e.age.ljust(5), e.mobile)
                            print(len(Customer.searchList),"Records found")
                    except Exception as ex:
                        print(ex)
                elif(search=="3"):
                    tempAge = input("Enter the age of customer: ")
                    temp = verify(tempAge, para="age")
                    if temp == 1:
                        cus.age = tempAge
                    else:
                        print("\nAge incorrect! Try again.")
                        continue
                    try:
                        cus.searchAge()
                        if (len(Customer.searchList) == 0):
                            print("\nNo such customer!")
                        else:
                            print("ID".ljust(5), "Name".ljust(15), "Age".ljust(5), "Mobile number")
                            print("------------------------------------------")
                            for e in Customer.searchList:
                                print(str(e.id).ljust(5), e.name.ljust(15), e.age.ljust(5), e.mobile)
                            print(len(Customer.searchList),"Records found")
                    except Exception as ex:
                        print(ex)
                elif(search=="4"):
                    tempMob = input("Enter the mobile number of customer: ")
                    temp = verify(tempMob, para="mobile")
                    if temp == 1:
                        cus.mobile = tempMob
                    else:
                        print("\nMobile number incorrect! Try again.")
                        continue
                    try:
                        cus.searchMobile()
                        if (len(Customer.searchList) == 0):
                            print("\nNo such customer!")
                        else:
                            print("ID".ljust(5), "Name".ljust(15), "Age".ljust(5), "Mobile number")
                            print("------------------------------------------")
                            for e in Customer.searchList:
                                print(str(e.id).ljust(5), e.name.ljust(15), e.age.ljust(5), e.mobile)
                            print(len(Customer.searchList),"Records found")
                    except Exception as ex:
                        print(ex)
                elif(search=="5"):
                    break
                else:
                    print("\nNot a valid parameter!! Try again.")
        #Modify
        elif(ch=="3"):
            while(True):
                cus = Customer()
                tempId = input("Enter the id of customer for modification: ")
                temp = verify(tempId, para="id")
                if temp == 1:
                    cus.id = int(tempId)
                else:
                    print("\nId incorrect! Try again.")
                    continue
                mod=input("Modify: \n1.Name\n2.Age\n3.Mobile number\n4.ALL\n5.To main menu\n")
                if (mod == "1"):
                    tempName = input("\nEnter the name of customer: ").lower().title()
                    temp = verify(tempName, para="name")
                    if temp == 1:
                        cus.name = tempName
                    else:
                        print("\nName incorrect! Try again.")
                        continue
                    try:
                        cus.modName()
                        print("\nUpdated successfully!!")
                        another = input("\nModify another customer? (Y/N): ")
                        if (another == "N" or another == "n"):
                            break
                        elif (another == "Y" or another == "y"):
                            continue
                        else:
                            print("\nPlease enter Y/y or N/n.")
                    except Exception as ex:
                        print(ex)
                elif (mod == "2"):
                    tempAge = input("Enter the age of customer: ")
                    temp = verify(tempAge, para="age")
                    if temp == 1:
                        cus.age = tempAge
                    else:
                        print("\nAge incorrect! Try again.")
                        continue
                    try:
                        cus.modAge()
                        print("\nUpdated successfully!!")
                        another = input("\nModify another customer? (Y/N): ")
                        if (another == "N" or another == "n"):
                            break
                        elif (another == "Y" or another == "y"):
                            continue
                        else:
                            print("\nPlease enter Y/y or N/n.")
                    except Exception as ex:
                        print(ex)
                elif (mod == "3"):
                    tempMob = input("Enter the mobile number of customer: ")
                    temp = verify(tempMob, para="mobile")
                    if temp == 1:
                        cus.mobile = tempMob
                    else:
                        print("\nMobile number incorrect! Try again.")
                        continue
                    try:
                        cus.modMobile()
                        print("\nUpdated successfully!!")
                        another = input("\nModify another customer? (Y/N): ")
                        if (another == "N" or another == "n"):
                            break
                        elif (another == "Y" or another == "y"):
                            continue
                        else:
                            print("\nPlease enter Y/y or N/n.")
                    except Exception as ex:
                        print(ex)
                elif (mod == "4"):
                    tempName = input("\nEnter the name of customer: ").lower().title()
                    temp = verify(tempName, para="name")
                    if temp == 1:
                        cus.name = tempName
                    else:
                        print("\nName incorrect! Try again.")
                        continue
                    tempAge = input("Enter the age of customer: ")
                    temp = verify(tempAge, para="age")
                    if temp == 1:
                        cus.age = tempAge
                    else:
                        print("\nAge incorrect! Try again.")
                        continue
                    tempMob = input("Enter the mobile number of customer: ")
                    temp = verify(tempMob, para="mobile")
                    if temp == 1:
                        cus.mobile = tempMob
                    else:
                        print("Please enter mobile number correctly!")
                        continue
                    try:
                        cus.modAll()
                        print("\nUpdated successfully!!")
                        another = input("\nModify another customer? (Y/N): ")
                        if (another == "N" or another == "n"):
                            break
                        elif (another == "Y" or another == "y"):
                            continue
                        else:
                            print("\nPlease enter Y/y or N/n.")
                    except Exception as ex:
                        print(ex)
                elif(mod=="5"):
                    break
                else:
                    print("\nNo such parameter!! Try again!")
        #Delete
        elif(ch=="4"):
            cus=Customer()
            tempId = input("Enter the id of customer: ")
            temp = verify(tempId, para="id")
            if temp == 1:
                cus.id = int(tempId)
            else:
                print("\nId incorrect! Try again.")
                continue
            try:
                cus.delete()
                print("\nCustomer delete successfully!!")
            except Exception as ex:
                print(ex)
        #Show all
        elif(ch=="5"):
            try:
                Customer.showAll()
                if(len(Customer.searchList)!=0):
                    print("ID".ljust(5), "Name".ljust(15), "Age".ljust(5), "Mobile number")
                    print("------------------------------------------")
                    for e in Customer.searchList:
                        print(str(e.id).ljust(5), e.name.ljust(15), e.age.ljust(5), e.mobile)
                    print(len(Customer.searchList), "Records found")
                else:
                    print("\nNo records!")
            except Exception as ex:
                print(ex)
        #Exit
        elif(ch=="6"):
            global con
            con.close()
            print("==================================================")
            print("\nThanks for using CMS !!!")
            break
        else:
            print("\nChoice not available!! Try again!")