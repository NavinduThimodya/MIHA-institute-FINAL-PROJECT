from customersection import customerSection
from sellersection import SellerSection
customer = customerSection()
seller = SellerSection()

print("### --------------- WELCOME TO GALLE FOODCITY--------------- ###")
print("+ --------------Enter Number to access to system-------------- +"+ "\n")
print("SYSTEM \n 1) Type 1 : Enter to shop management \n 2) Type 2 : Enter to Customer side")

number = int(input("Enter Number : "))
userNames = ["Food@1","Food@2","Food@3","Food@4","Food@5"] # add usernames of sellers to userNames list
passwords = ["200203103965","1946766@N","Ca123%32","yt@2020","hm@199902"] # add passwords to a list

while True:    
    if number == 1:
        while True:
            userName = input("\nEnter user name : ")
            password = input("Enter Password : ")
            for names in range(len(userNames)):
                    if userName == userNames[names]:x=names;break
                    else:x=0
            if (userName in userNames) and (password == passwords[x]): # This part is add for identify users
                seller.run()
            else:
                print("Back : 0 /n ReEnter username and password : 1")
                press = int(input("Press : "))
                if press == 1:
                    continue
                else:
                    break
    elif number == 2:
        customer.run()
        customer.covidDetails()
        customer.getProductMenu()
        customer.orderAndCreateBill()
        break
    else:
        print("invaid responce")
        number = int(input("Enter Number : "))
