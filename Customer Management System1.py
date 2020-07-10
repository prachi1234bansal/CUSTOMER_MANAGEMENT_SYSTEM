#BLL:Business Logic Layer
cus_name=[]
cus_id=[]
cus_age=[]
cus_mobile_no=[]
def addCustomer(name,id,age,mobile_no):
    cus_name.append(name)
    cus_id.append(id)
    cus_age.append(age)
    cus_mobile_no.append(mobile_no)
def searchCustomer(id):
        i=cus_id.index(id)
        return i
def deleteCustomer(id):
    i=cus_id.index(id)
    cus_id.pop(i)
    cus_name.pop(i)
    cus_age.pop(i)
    cus_mobile_no.pop(i)
def modifyCustomer(id,name,age,mobile_no):
    k=cus_id.index(id)
    cus_name[k]=name;
    cus_age[k]=age
    cus_id[k]=id
    cus_mobile_no[k]=mobile_no
#PL:Presentation Layer
while True:
    def showCustomer(i):
        print(f"Customer Id:{cus_id[i]},Customer name:{cus_name[i]},Customer age:{cus_age[i]},Customer mobile_no:{cus_mobile_no[i]}")
    print("Welcome to Prachi Customer Management System!!")
    print("1 for Add Customer")
    print("2 for Search Customer")
    print("3 for Delete Customer")
    print("4 for Modifying Customer")
    print("5 for Displaying Customer")
    print("6 for Exit")
    choice=int(input("Enter your choice which you want to enter:"))
    if choice==1:
        name=input("Enter the Customer Name:")
        id=int(input("Enter the Customer Id:"))
        age=int(input("Enter the Customer age:"))
        mobile_no=input("Enter the Customer Mobile No:")
        if mobile_no.isdecimal():
            if len(mobile_no)==10:
                addCustomer(name,id,age,mobile_no)
            else:
                print("Enter Mobile No in 10 NUMBER Digits!!")
    elif choice==2:
        id=int(input("Enter the Customer Id which You want to search it:"))
        if id in cus_id:
            w=searchCustomer(id)
            showCustomer(w)
        else:
            print("Id is not present in Customer Id List")
    elif choice==3:
        id=int(input("Enter the Customer Id which u want to delete:"))
        if id in cus_id:
            deleteCustomer(id)
        else:
            print("Id is not present in Customer Id List")
    elif choice==4:
        id = int(input("Enter the Customer Id which you want to modify::"))
        if id in cus_id:
            name = input("Enter the Customer Updated Name:")
            age = int(input("Enter the Customer Updated age:"))
            mobile_no = input("Enter the Customer Updated Mobile No:")
            if mobile_no.isdecimal():
                if len(mobile_no) == 10:
                    modifyCustomer(id, name, age, mobile_no)
                else:
                    print("Enter Mobile No in 10 NUMBER Digits!!")
        else:
            print("Enter the valid id for modifying the customer!!")
    elif choice==5:
        for i in range(len(cus_name)):
            showCustomer(i)
    elif choice==6:
        print("Thanku for using Prachi Customer Management System!!")
        break;
    else:
        print("Incorrect Choice")