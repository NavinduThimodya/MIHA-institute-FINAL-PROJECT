from billprint import Bill
from productupdate import Product
import datetime

class SellerSection:

    def __init__(self):
        self.seller = ["Kamal","Silva"]

    def run(self):
        print("\n#### --------Welcome Seller Section-------- ####")

        while True:
            print("\nEnter Number to access to system")
            print("\nSeller Tasks \n 1) Type 1: Create new bill \n 2) Type 2: Add new item \n 3) Type 3: Update Quantity \n 4) Type 0: Go Back")
            number = int(input("\nEnter number:"))
            print("\n####    ----loading----    ####\n")
            if (number == 1):
                self.task1()
            elif (number == 2):
                self.task2()
            elif (number == 3):
                self.task3()
            elif (number == 0):
                break
            else:
                print("\n#### ----invalid input---- ####")

######################################SECSION 1 ##################################################################################

    def getAllProducts(self):
        print("Available Products and Unit Price(Rs)")
        productPriceLis = []
        with open('price.txt', 'r') as file:
            for line in file:
                temp = line.strip()
                productPriceLis.append(temp)
        return productPriceLis
    
    def displayTotal(self,pNames,oQuantity,products):
        prouctList = pNames
        unitPrices =[]
        item = 0
        for p in prouctList:
            for oneP in products:
                if(p in oneP):
                    unitP = int(oneP.split(" ")[1])
                    unitPrices.append(unitP)
                    productRemove = Product(p,unitP)
                    productRemove.autoUpdateQuantity(oQuantity[item])
            item += 1
                    
        today = str(datetime.datetime.now())
        bill = Bill(today,prouctList,unitPrices,oQuantity)
        bill.getTotal()
        print("To print Bill")
        paid = int(input("Enter paid amount: "))
        bill.printBill(paid)
        print("\n")

    def createBill(self,orderList,products):
        pNames = []
        oQuantity = []
        total = 0
        for value in orderList:
            if(value == "#"):
                break
            n = value.split(" ")
            pNames.append(n[0])
            oQuantity.append(int(n[1]))
        if(len(pNames) == 0):
            return "No Item Selected"
        self.displayTotal(pNames,oQuantity,products)

    def task1(self):
        products = self.getAllProducts()
        print("####----Create New Bill----####")
        print("Enter:Product_Name Ordered_Quantity")
        itemList = []
        getTotal =''
        i = 1
        while (getTotal !="#"):
            print("ADD ITEM PRESS \" 1 \" AND GET TOTAL PRESS \" # \"")
            getTotal = input("PRESS : ")
            if getTotal == "1":
                item = input("Item "+str(i)+" : ")
                qy = input("Quantity : ")
                itemList.append(item+" "+qy)
                print("ADDED SUCCESS")
            else:
                itemList.append(getTotal)
            i += 1
        print(itemList)
        self.createBill(itemList,products)

#############################################SECSION 2 ##############################################################################
    def addNewItem(self,productName,unitPrice,stock):
        prod = Product(productName,unitPrice)
        prod.manuallyUpdateQuantity(stock)
        print("####--- New Item added success ---####")
        print("\n")
        
    def task2(self):
        print("####----Add New Item----####")
        name = input("Enter product name: ")
        uPrice = int(input("Enter unit price: "))
        stock = int(input("Enter Quantity: "))
        self.addNewItem(name,uPrice,stock)

#############################################SECSION 3 ##############################################################################
    def updateaddStock(self,productName,unitPrice,stock):
        prod = Product(productName,unitPrice)
        prod.manuallyUpdateQuantity(stock)
        print("####--- stock update success ---####")
        
    def updateremoveStock(self,productName,unitPrice,stock):
        prod = Product(productName,unitPrice)
        prod.autoUpdateQuantity(stock)
        print("####--- stock update success ---####")

    def task3(self):
        print("####----Update stock----####")
        name = input("Enter product name: ")
        uPrice = int(input("Enter unit price: "))
        stock = int(input("Enter Quantity: "))
        self.updateremoveStock(name,uPrice,stock)


