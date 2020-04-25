#BLL
import json
import random

class employees:
    employList=[]
    searchList=[]

    def __init__(self):
        self.id=0
        self.name=""
        self.age=""
        self.mobile=""

    @staticmethod
    def loadEms():
        try:
            employees.employList.clear()
            f = open("EMSJson.txt", "r")
            employees.employList = json.load(f, object_hook=employees.toObj)
            f.close()
        except:
            raise Exception("Empty database")

    @staticmethod
    def toObj(d):
        if "MR" in d["id"]:
            man = manager()
            man.id = d["id"]
            man.name = d["name"]
            man.age = d["age"]
            man.mobile = d["mobile"]
            man.area = d["area"]
            return man
        if "TR" in d["id"]:
            tr=trainer()
            tr.id = d["id"]
            tr.name = d["name"]
            tr.age = d["age"]
            tr.mobile = d["mobile"]
            tr.course=d["course"]
            return tr
        if "DR" in d["id"]:
            dr=director()
            dr.id = d["id"]
            dr.name = d["name"]
            dr.age = d["age"]
            dr.mobile = d["mobile"]
            dr.shares=d["shares"]
            return dr

    @staticmethod
    def saveEms():
        try:
            f = open("EMSJson.txt", "w")
            json.dump(employees.employList, f, default=employees.toDict)
            f.close()
        except:
            raise Exception("Error updating database")

    @staticmethod
    def toDict(obj):
        return obj.__dict__

class manager(employees):
    def __init__(self):
        self.area=""
        super().__init__()

    def addManager(self):
        try:
            self.id="MR"+str(random.randrange(1000,9999))
            employees.employList.append(self)
        except:
            raise Exception("Error while adding!")

class trainer(employees):
    def __init__(self):
        self.course=""
        super().__init__()

    def addTrainer(self):
        try:
            self.id="TR"+str(random.randrange(1000,9999))
            employees.employList.append(self)
        except:
            raise Exception("Error while adding!")

class director(employees):
    def __init__(self):
        self.shares=""
        super().__init__()

    def addDirector(self):
        try:
            self.id="DR"+str(random.randrange(1000,9999))
            employees.employList.append(self)
        except:
            raise Exception("Error while adding!")


if __name__=="__main__":
    try:
        employees.loadEms()
    except Exception as ex:
        print(ex)
    try:
        print("========== Welcome to EMS ==========")
        while(True):
            choice=input("1.Add an employee\n2.Search employee\n3.Delete an employee\n4.Modify an employee\n5.Display all employees\n6.Exit\n")
            if choice=="1":
                try:
                    choice1=input("Enter the type of employee\n1.Manager\n2.Trainer\n3.Director\n")
                    if choice1=="1":
                        man=manager()
                        man.name=input("Enter the name of employee :")
                        man.age=input("Enter the age of employee :")
                        man.mobile=input("Enter the mobile number of employee :")
                        man.area=input("Enter the area :")
                        man.addManager()
                        print("employee added successfully!")
                    elif choice1=="2":
                        tr=trainer()
                        tr.name=input("Enter the name of employee :")
                        tr.age=input("Enter the age of employee :")
                        tr.mobile=input("Enter the mobile number of employee :")
                        tr.course=input("Enter the course :")
                        tr.addTrainer()
                        print("employee added successfully!")
                    elif choice1=="3":
                        dr=director()
                        dr.name=input("Enter the name of employee :")
                        dr.age=input("Enter the age of employee :")
                        dr.mobile=input("Enter the mobile number of employee :")
                        dr.shares=input("Enter the shares :")
                        dr.addDirector()
                        print("employee added successfully!")
                    else:
                        print("No such designation available!")
                except Exception as ex:
                    print(ex)
            elif choice=="2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                try:
                    if (len(employees.employList) != 0):
                        print("id".ljust(8), "Name".ljust(10), "Age".ljust(5), "Mobile".ljust(10), "Area".ljust(10), "Course".ljust(10), "Shares".ljust(10))
                        print("------------------------------------------------------------------")
                        for e in employees.employList:
                            if(e.id[0:2]=="MR"):
                                print(e.id.ljust(8), e.name.ljust(10), e.age.ljust(5), e.mobile.ljust(10), e.area.ljust(10), "N/A".ljust(10), "N/A".ljust(10))
                            if(e.id[0:2]=="TR"):
                                print(e.id.ljust(8), e.name.ljust(10), e.age.ljust(5), e.mobile.ljust(10), "N/A".ljust(10), e.course.ljust(10), "N/A".ljust(10))
                            elif (e.id[0:2] == "DR"):
                                print(e.id.ljust(8), e.name.ljust(10), e.age.ljust(5), e.mobile.ljust(10), "N/A".ljust(10), "N/A".ljust(10), e.shares+"%".ljust(10))
                        print(len(employees.employList), "Records found\n")
                    else:
                        print("\nNo records!")
                except Exception as ex:
                    print(ex)
            elif choice == "6":
                try:
                    employees.saveEms()
                except Exception as ex:
                    print(ex)
                break
            else:
                print("Invalid Choice! Try again...")
    except Exception as ex:
        print(ex)