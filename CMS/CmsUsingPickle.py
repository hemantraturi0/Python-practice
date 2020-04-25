#BLL
import pickle
import random

class Customer:
    cusList=[]
    searchList=[]
    idGen=random.randrange(1000,9999)

    def __init__(self):
        self.id=Customer.idGen
        self.name=""
        self.age=""
        self.mobile=""


    def addCustomer(self):
        Customer.cusList.append(self)
        Customer.idGen = random.randrange(1000,9999)


    def searchId(self):
        for e in Customer.cusList:
            if(e.id==self.id):
                cus = Customer()
                cus.id = e.id
                cus.name = e.name
                cus.age = e.age
                cus.mobile = e.mobile
                Customer.searchList.append(cus)

    def searchName(self):
        for e in Customer.cusList:
            if(e.name==self.name):
                cus=Customer()
                cus.id=e.id
                cus.name=e.name
                cus.age=e.age
                cus.mobile=e.mobile
                Customer.searchList.append(cus)

    def searchAge(self):
        for e in Customer.cusList:
            if(e.age==self.age):
                cus = Customer()
                cus.id = e.id
                cus.name = e.name
                cus.age = e.age
                cus.mobile = e.mobile
                Customer.searchList.append(cus)

    def searchMobile(self):
        for e in Customer.cusList:
            if(e.mobile==self.mobile):
                cus = Customer()
                cus.id = e.id
                cus.name = e.name
                cus.age = e.age
                cus.mobile = e.mobile
                Customer.searchList.append(cus)

    def modId(self, x):
        for e in Customer.cusList:
            if(e.id==self.id):
                e.id=x

    def modName(self):
        for e in Customer.cusList:
            if(e.id==self.id):
                e.name=self.name

    def modAge(self):
        for e in Customer.cusList:
            if(e.id==self.id):
                e.age=self.age

    def modMobile(self):
        for e in Customer.cusList:
            if(e.id==self.id):
                e.mobile=self.mobile

    def modAll(self):
        for e in Customer.cusList:
            if(e.id==self.id):
                e.name=self.name
                e.age = self.age
                e.mobile = self.mobile

    def delete(self):
        for e in Customer.cusList:
            if(e.id==self.id):
                Customer.cusList.remove(e)

    @staticmethod
    def loadCms():
        try:
            f = open("CMSPickle.txt", "rb+")
            Customer.cusList = pickle.load(f)
        except:
            raise Exception("Empty database")
    @staticmethod
    def saveCms():
        try:
            f = open("CMSPickle.txt", "wb")
            pickle.dump(Customer.cusList, f)
        except:
            raise Exception("Error updating database")

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
            for e in Customer.cusList:
                if(e.id==int(value)):
                    return 1
    else:
        return -1 

if(__name__=="__main__"):
    try:
        Customer.loadCms()
    except Exception as ex:
        print(ex)
    print("Welcome to CMS".center(50,"="))
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
        #Searching
        elif(ch=="2"):
            while(True):
                cus = Customer()
                search = input("\nSearch by:\n1.ID\n2.Name\n3.age\n4.Mobile number\n5.To main menu\n")
                if(search=="1"):
                    Customer.searchList.clear()
                    tempId=input("Enter the id of customer: ")
                    temp=verify(tempId, para="id")
                    if temp==1:
                        cus.id=int(tempId)
                    else:
                        print("\nId incorrect! Try again.")
                        continue
                    cus.searchId()
                    if(len(Customer.searchList)==0):
                        print("\nNo such customer!")
                    else:
                        print("ID".ljust(5), "Name".ljust(15), "Age".ljust(5), "Mobile number")
                        print("------------------------------------------")
                        for e in Customer.searchList:
                            print(str(e.id).ljust(5), e.name.ljust(15), e.age.ljust(5), e.mobile)
                elif(search=="2"):
                    Customer.searchList.clear()
                    tempName = input("\nEnter the name of customer: ").lower().title()
                    temp = verify(tempName, para="name")
                    if temp == 1:
                        cus.name = tempName
                    else:
                        print("\nName incorrect! Try again.")
                        continue
                    cus.searchName()
                    if (len(Customer.searchList) == 0):
                        print("\nNo such customer!")
                    else:
                        print("ID".ljust(5), "Name".ljust(15), "Age".ljust(5), "Mobile number")
                        print("------------------------------------------")
                        for e in Customer.searchList:
                            print(str(e.id).ljust(5), e.name.ljust(15), e.age.ljust(5), e.mobile)
                elif(search=="3"):
                    Customer.searchList.clear()
                    tempAge = input("Enter the age of customer: ")
                    temp = verify(tempAge, para="age")
                    if temp == 1:
                        cus.age = tempAge
                    else:
                        print("\nAge incorrect! Try again.")
                        continue
                    cus.searchAge()
                    if (len(Customer.searchList) == 0):
                        print("\nNo such customer!")
                    else:
                        print("ID".ljust(5), "Name".ljust(15), "Age".ljust(5), "Mobile number")
                        print("------------------------------------------")
                        for e in Customer.searchList:
                            print(str(e.id).ljust(5), e.name.ljust(15), e.age.ljust(5), e.mobile)
                elif(search=="4"):
                    Customer.searchList.clear()
                    tempMob = input("Enter the mobile number of customer: ")
                    temp = verify(tempMob, para="mobile")
                    if temp == 1:
                        cus.mobile = tempMob
                    else:
                        print("\nMobile number incorrect! Try again.")
                        continue
                    cus.searchMobile()
                    if (len(Customer.searchList) == 0):
                        print("\nNo such customer!")
                    else:
                        print("ID".ljust(5), "Name".ljust(15), "Age".ljust(5), "Mobile number")
                        print("------------------------------------------")
                        for e in Customer.searchList:
                            print(str(e.id).ljust(5), e.name.ljust(15), e.age.ljust(5), e.mobile)
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
                mod=input("Modify: \n1.ID\n2.Name\n3.Age\n4.Mobile number\n5.ALL\n6.To main menu\n")
                if(mod=="1"):
                    x=input("Enter the new ID: ")
                    if(x.isnumeric()):
                        x=int(x)
                        cus.modId(x)
                    else:
                        print("Invalid id")
                        break
                    print("\nUpdated successfully!!")
                    another = input("\nModify another customer? (Y/N): ")
                    if (another == "N" or another == "n"):
                        break
                    elif (another == "Y" or another == "y"):
                        continue
                    else:
                        print("\nIncorrect input")
                        break
                elif (mod == "2"):
                    tempName = input("\nEnter the name of customer: ").lower().title()
                    temp = verify(tempName, para="name")
                    if temp == 1:
                        cus.name = tempName
                    else:
                        print("\nName incorrect! Try again.")
                        continue
                    cus.modName()
                    print("\nUpdated successfully!!")
                    another = input("\nModify another customer? (Y/N): ")
                    if (another == "N" or another == "n"):
                        break
                    elif (another == "Y" or another == "y"):
                        continue
                    else:
                        print("\nPlease enter Y/y or N/n.")
                elif (mod == "3"):
                    tempAge = input("Enter the age of customer: ")
                    temp = verify(tempAge, para="age")
                    if temp == 1:
                        cus.age = tempAge
                    else:
                        print("\nAge incorrect! Try again.")
                        continue
                    cus.modAge()
                    print("\nUpdated successfully!!")
                    another = input("\nModify another customer? (Y/N): ")
                    if (another == "N" or another == "n"):
                        break
                    elif (another == "Y" or another == "y"):
                        continue
                    else:
                        print("\nPlease enter Y/y or N/n.")
                elif (mod == "4"):
                    tempMob = input("Enter the mobile number of customer: ")
                    temp = verify(tempMob, para="mobile")
                    if temp == 1:
                        cus.mobile = tempMob
                    else:
                        print("\nMobile number incorrect! Try again.")
                        continue
                    cus.modMobile()
                    print("\nUpdated successfully!!")
                    another = input("\nModify another customer? (Y/N): ")
                    if (another == "N" or another == "n"):
                        break
                    elif (another == "Y" or another == "y"):
                        continue
                    else:
                        print("\nPlease enter Y/y or N/n.")
                elif (mod == "5"):
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
                    cus.modAll()
                    print("\nUpdated successfully!!")
                    another = input("\nModify another customer? (Y/N): ")
                    if (another == "N" or another == "n"):
                        break
                    elif (another == "Y" or another == "y"):
                        continue
                    else:
                        print("\nPlease enter Y/y or N/n.")
                elif(mod=="6"):
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
            cus.delete()
            print("\nCustomer delete successfully!!")
        #Show all
        elif (ch == "5"):
            try:
                if (len(Customer.cusList) != 0):
                    print("ID".ljust(5), "Name".ljust(15), "Age".ljust(5), "Mobile number")
                    print("------------------------------------------")
                    for e in Customer.cusList:
                        print(str(e.id).ljust(5), e.name.ljust(15), e.age.ljust(5), e.mobile)
                    print(len(Customer.cusList), "Records found")
                else:
                    print("\nNo records!")
            except Exception as ex:
                print(ex)
        #Exit
        elif(ch=="6"):
            try:
                Customer.saveCms()
            except Exception as ex:
                print(ex)
            print("==================================================")
            print("\nThanks for using CMS !!!")
            break
        else:
            print("\nChoice not available!! Try again!")