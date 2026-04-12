attempt=1
while attempt<4 :
    password=input("password:")
    if password =="azim":
        print("congo")
        break
    else:
        if attempt==3:
            print("its over")
        else:
            print("try agian")  
        attempt=attempt+1