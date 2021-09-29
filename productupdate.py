class Product:
    def __init__(self,productName,unitPrice):
        self.productName = productName
        self._unitPrice = unitPrice

    def autoUpdateQuantity(self,boughtQuantity):
        productList = []
        productQuantity = []
        with open("product.txt",'r') as file:
            for line in file:
                product,quantity = line.strip().split(" ")
                productList.append(product)
                productQuantity.append(int(quantity))
            
        if self.productName in productList:
            if (productQuantity[productList.index(self.productName)] - boughtQuantity) >= 0:
                productQuantity[productList.index(self.productName)] = productQuantity[productList.index(self.productName)] - boughtQuantity
                with open("product.txt",'w') as file:
                    for i in range(len(productList)-1):
                        file.write(productList[i] + " " +str(productQuantity[i]) + "\n")
                    else:
                        file.write(productList[-1] + " " +str(productQuantity[-1]) + "\n")
                state = "Success"
                return state
            else:
                print("\nThis Quantity can not supply")
        else:
            print("\nOut of Stock")
                
    def manuallyUpdateQuantity(self,boughtQuantity):
        productList = []
        productQuantity = []
        productPrice = []
        with open("product.txt",'r') as file1:
            for line in file1:
                product,quantity = line.strip().split(" ")
                productList.append(product)
                productQuantity.append(int(quantity))
            
        if self.productName in productList:
            productQuantity[productList.index(self.productName)] = productQuantity[productList.index(self.productName)] + boughtQuantity
        else:
            with open("price.txt",'r') as file2:
                for line in file2:
                    product,price = line.strip().split(" ")
                    productPrice.append(int(price))
                    
        
        if self.productName in productList:
            with open("product.txt",'w') as file3:
                for i in range(len(productList)-1):
                    file3.write(productList[i] + " " +str(productQuantity[i]) + "\n")
                else:
                    file3.write(productList[-1] + " " +str(productQuantity[-1]))
        else:
            with open("price.txt",'w') as file4:
                for i in range(len(productList)):
                    file4.write(productList[i] + " " +str(productPrice[i]) + "\n")
                else:
                    file4.write(self.productName + " " +str(self._unitPrice))
            with open("product.txt",'w') as file5:
                for i in range(len(productList)):
                    file5.write(productList[i] + " " +str(productQuantity[i]) + "\n")
                else:
                    file5.write(self.productName + " " +str(boughtQuantity))
