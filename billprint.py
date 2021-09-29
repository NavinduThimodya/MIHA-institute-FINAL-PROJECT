class Bill:
    def __init__(self,date,productList,unitPrice,quantity):
        self.date = date
        self.productLis = productList
        self.unitPrice = unitPrice
        self.quantity = quantity

    def printBillHead(self):
        print("\n+--------------------------------------------+")
        print("|               GALLE FOODCITY               |")
        print("+--------------------------------------------+")
        print("| Date :  {:35s}|".format(str(self.date)))

    def printBillFooter(self):
        print("|            Thank You.Come Again            |")
        print("+--------------------------------------------+")

    def getTotal(self):
        l = len(self.productLis)
        subToLis = []
        for value in range(l):
            subTot = int(self.quantity[value]) * int(self.unitPrice[value])
            subToLis.append(subTot)
        print("\nTotal price is Rs."+str(sum(subToLis)))

    def printBill(self,paid):
        l = len(self.productLis)
        subToLis = []
        self.printBillHead()
        print("+----------------+--------------+------------+")
        print("| Name           |Quantity      |Price       |")
        print("+----------------+--------------+------------+")
        for value in range(l):
            subTot = int(self.quantity[value]) * int(self.unitPrice[value])
            subToLis.append(subTot)
            print("|{:16s}|{:14s}|{:12s}|".format(" "+self.productLis[value],"  "+str(self.quantity[value]),"  "+str(subTot)))
            print("+--------------------------------------------+")
        print("|        Total   : Rs{:24s}|".format(" "+str(sum(subToLis))))
        print("+--------------------------------------------+")
        print("|        Paid    : Rs{:24s}|".format(" "+str(paid)))
        print("+--------------------------------------------+")
        print("|        Balance : Rs{:24s}|".format(" "+str(paid-sum(subToLis))))
        print("+--------------------------------------------+")
        self.printBillFooter()


