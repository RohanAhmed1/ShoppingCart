from Product import Product
from CheckAndSearch import CheckAndSearch

class ProductDB(CheckAndSearch):
    def __init__(self):
        self.loadProductList()
    def printProductList(self):
        print('\n__________________________________________PRODUCTS LIST_______________________________________________\n')
        for product in self.ProductList:
            pkr=product.getProductPrize()+' PKR'
            print(f"Name: {product.getProductName():37}Prize:{pkr:15}Quantity: \
{product.getProductQuantity():10}Code: {product.getProductCode()}")
            print('-----------------------------------------------------------------------------------------------------')
            
    def loadProductList(self):
        self.ProductList=[]
        try:
            f=open('ProductDB.txt','r')
        except:
            return
        for line in f:
            product=eval(line)
            p=Product()
            p.setProductName(product[0])
            p.setProductPrize(product[1])
            p.setProductQuantity(product[2])
            p.setProductCode(product[3])
            self.ProductList.append(p)
        f.close()
        
    #Method is over-rided because we search product in terms of code,not from user name.
    def searchData(self,data,lst):
        for i in lst:
            if data==i.getProductCode():
                return i
        else:
            return 'Not Found' 
