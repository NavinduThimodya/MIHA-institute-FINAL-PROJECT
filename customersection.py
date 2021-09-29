from productupdate import Product
from billprint import Bill
import datetime
import time

class customerSection:
    def __init__(self):
        pass

    def run(self):
        print("\n#### --------------Welcome to customer section-------------- ####")

    def getCustomerDetails(self):
        customerDetailsLis = []
        with open("coviddetails.txt","r") as file1:
            for line in file1:
                temp1 = line.strip()
                customerDetailsLis.append(temp1)
        return customerDetailsLis

    def updateCustomerDetails(self,customerDetails):
        with open("coviddetails.txt","w") as file2:
            for item in range(len(customerDetails)-1):
                file2.write(customerDetails[item]+"\n")
            file2.write(customerDetails[-1])

    def covidDetails(self):
        print("\nWe want to get your information in this COVID-19 situation for your protection. The information that you provide here is only for the record purposes of our Galle foodcity\n")
        time.sleep(2)
        print("\n+------------------ Customer Details Form ------------------+")
        print("-------------------------------------------------------------")
        name = input(" * Your Name                 :")
        idnumber = input(" * NIC Number                :")
        tel = input(" * Telephone Number          :")
        address = input(" * Address                   :")
        vaccine = input(" * Did you get vaccine(Y/N)? :")
        print("-------------------------------------------------------------\n")
        customerDetails = self.getCustomerDetails()
        customerDetails.append(name+" "+idnumber+" "+tel+" "+address+" "+vaccine)
        self.updateCustomerDetails(customerDetails)
        print("\n####---------- Customer Details added success ----------####")

    def getAllProducts(self):
        productPriceLis = []
        with open('price.txt', 'r') as file:
            for line in file:
                temp = line.strip().split(" ")
                productPriceLis.append(temp)
        return productPriceLis

    def getProductMenu(self):
        print("\nNow you can see the available products and their prices in our foodcity.")
        time.sleep(2)
        productPriceLis = self.getAllProducts()
        print("+---------------------------------------------------+")
        print("| Number |       Product       |   Unit Price(Rs)   |")
        print("+---------------------------------------------------+")
        for item in productPriceLis:
            print("|{:8s}|{:21s}|{:20s}|".format("   "+str(productPriceLis.index(item)+1)," "+str(item[0])," "+str(item[1])))
        print("+---------------------------------------------------+")

    def order(self):
        productLis = []
        quantityLis = []
        unitPrices = []
        print("\nYou can choose a method from below for order.\n\
    1) If you want to choose products from product's name, please enter number '1'.\n\
    2) If you want to choose products from number relevant to product's name in above list, please enter number '2'.")
        while True:
            number = int(input("Enter number of a method : "))
            allProducts = self.getAllProducts()
            if number == 1:
                print("\nIf your order is complete you can press '#' key for get your bill.")
                while True:
                    product = input("\nProduct Name: ")
                    if product == "#":break
                    Quantity = int(input("Quantity: "))
                    for item3 in range(len(allProducts)):
                        if product == allProducts[item3][0]:
                            unitPrice = allProducts[item3][1]
                            break
                    else: unitPrice = None
                    updateProducts = Product(product,unitPrice)
                    state = updateProducts.autoUpdateQuantity(Quantity)
                    if state == "Success":
                        productLis.append(product)
                        quantityLis.append(Quantity)
                        unitPrices.append(unitPrice)
                    else:pass
                return productLis,unitPrices,quantityLis
            elif number == 2:
                print("\nIf your order is complete you can press '#' key for get your bill.")
                while True:
                    product = input("\nProduct's number: ")
                    if product == "#":break
                    if (type(int(product)) != int) or (int(product) > len(allProducts)):
                        print("#--------- Invalid Input ---------#")
                        continue
                    Quantity = int(input("Quantity: "))
                    updateProducts = Product(allProducts[int(product)-1][0],allProducts[int(product)-1][1])
                    state = updateProducts.autoUpdateQuantity(Quantity)
                    if state == "Success":
                        productLis.append(allProducts[int(product)-1][0])
                        unitPrices.append(allProducts[int(product)-1][1])
                        quantityLis.append(Quantity)
                    else:pass
                return productLis,unitPrices,quantityLis
            else:
                print("#--------- Invalid Input ---------#\n")
                continue

    def orderAndCreateBill(self):
        Lis_1,Lis_2,Lis_3 = self.order()
        if len(Lis_1) == 0:
            print("\nNo item selected")
            print("\n+----------------------------------------------------------+")
            print("|                   Thank You.Come Again                   |")
            print("+----------------------------------------------------------+")
        else:
            now = datetime.datetime.now()
            bill = Bill(now,Lis_1,Lis_2,Lis_3)
            bill.getTotal()
            paid = int(input("Enter your payment: "))
            time.sleep(0)
            bill.printBill(paid)
        
