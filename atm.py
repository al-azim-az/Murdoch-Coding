#for excrcie
pin=int(input("PIn"))
account_type=(input("account type"))
balance=float(input("balance"))
if pin== 1234:
    if account_type=="savings":
        print("Acess Grannted")
        if balance>5000:
            print("Acess")
        else:
            print("granted")    
    else:
        print("Invalid account type")


else:
    print("wrong pin ")