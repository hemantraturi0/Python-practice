#Business Logic Layer
idlist=[]
agelist=[]
namelist=[]
idGen=0

def addCustomer(age,name):
    global idGen
    idGen+=1
    idlist.append(idGen)
    agelist.append(age)
    namelist.append(name)
def searchId(id):
    if(id not in idlist):
        return -1
    index=idlist.index(id)
    return index
def searchName(na):
    if(na not in namelist):
        return -1
    l=[]
    for i in range(len(namelist)):
        if(namelist[i]==na):
            l.append(i)
    return l
def searchAge(a):
    if(a not in agelist):
        return -1
    l = []
    for i in range(len(agelist)):
        if (agelist[i] == a):
            l.append(i)
    return l
def deleteCustomer(id):
    index=idlist.index(id)
    idlist.pop(index)
    agelist.pop(index)
    name=namelist.pop(index)
    return name
def modifyCustomer(id,age,name):
    index=idlist.index(id)
    agelist[index]=age
    namelist[index]=name
def modifyByAge(id, age):
    index=idlist.index(id)
    agelist[index]=age
def modifyByName(id, name):
    index=idlist.index(id)
    namelist[index]=name

#Presentation Layer
print("Welcome to Customer Management System")
while(1):
    print("===================================xxx============================")
    ch=input('''1. to Add Customer\n2. to Search Customer\n3. to Delete Customer\n4. to Modify Customer\n5. to show database\n6. to Exit\n''')

    # Adding a customer
    if(ch=="1"):
        name=input("Enter Customer Name:").lower().title()
        try:
            age=int(input("Enter Customer Age:"))
        except:
            print("Incorrect age")
        else:
            if(all(x.isalpha() or x.isspace() for x in name) and age>0 and age<=120):
                addCustomer(age, name)
                print("Customer Added Successfully")
            else:
                print("Please enter a valid name/age")

    # Searching Customer
    elif(ch=="2"):
        search=input("Search based on\n1. Name\n2. Id\n3. Age\n").lower().title()
        if(search=='1'):
            na=input("Enter the name of customer:").lower().title()
            i=searchName(na)
            if(i==-1):
                print("No such name available")
            else:
                print("ID".ljust(5), "Name".ljust(15), "Age".ljust(3))
                for j in i:
                    print(str(idlist[j]).ljust(5), str(namelist[j]).ljust(15), str(agelist[j]).ljust(3))
        elif(search=='2'):
            try:
                id=int(input("Enter Customer Id to Search:"))
            except:
                print("Incorrect Id")
            else:
                i=searchId(id)
                if(i==-1):
                    print("Id not available")
                else:
                    print("ID".ljust(5), "Name".ljust(15), "Age".ljust(3))
                    print(str(idlist[i]).ljust(5), str(namelist[i]).ljust(15), str(agelist[i]).ljust(3))
        elif(search=='3'):
            try:
                a=int(input("Enter the age of customer:"))
            except:
                print("Incorrect age")
            else:
                i=searchAge(a)
                if(i==-1):
                    print("No customer with this age available")
                else:
                    print("ID".ljust(5), "Name".ljust(15), "Age".ljust(3))
                    for j in i:
                        print(str(idlist[j]).ljust(5), str(namelist[j]).ljust(15), str(agelist[j]).ljust(3))
        else:
            print("Invalid parameter")

    # Delete Customer
    elif(ch=="3"):
        try:
            id=int(input("Enter Customer Id to Delete:"))
        except:
            print("Incorrect Id")
        else:
            name=deleteCustomer(id)
            print(f"Customer with Id: {id} and Name: {name} delete successfully")

    # Update Customer
    elif(ch=="4"):
        try:
            id = int(input("Enter Customer Id to modify details:"))
        except:
            print("Incorrect Id")
        else:
            if(id in idlist):
                choice=input("1. Update Age\n2. Update Name\n3. Update both\n")
                if(choice=='1'):
                    try:
                        age=int(input("Enter Updated Age:"))
                    except:
                        print("Incorrect age")
                    else:
                        if(age>0 and age<=120):
                            modifyByAge(id, age)
                            print("Customer updated successfully")
                        else:
                            print("Not a correct age")
                elif(choice=='2'):
                    name=input("Enter Updated Name:").lower().title()
                    if all(x.isalpha() or x.isspace() for x in name):
                        modifyByName(id, name)
                        print("Customer updated successfully")
                    else:
                        print("Not a valid name")
                elif(choice=='3'):
                    name = input("Enter Updated Name:")
                    try:
                        age=int(input("Enter Updated Age:"))
                    except:
                        print("Incorrect age")
                    else:
                        if (all(x.isalpha() or x.isspace() for x in name) and age > 0 and age <= 120):
                            modifyCustomer(id,age,name)
                            print("Customer updated successfully")
                        else:
                            print("Invalid name/age")
                else:
                    print("Invalid choice")
            else:
                print("Id not available")

    # Show database
    elif(ch=="5"):
        x = len(idlist)
        if(x==0):
            print("No customers yet")
        else:
            print("ID".ljust(5), "Name".ljust(15), "Age".ljust(3))
            for i in range(x):
                print(str(idlist[i]).ljust(5),str(namelist[i]).ljust(15),str(agelist[i]).ljust(3))

    # Exit
    elif(ch=="6"):
        print("Thanks for using CMS")
        break
    else:
        print("Incorrect Choice")