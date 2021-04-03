from Product import Product
from ProductDB import ProductDB
from Customer import Customer
from CustomerDB import CustomerDB

from copy import deepcopy

class Cart:
    def __init__(self):
        self.PDB=ProductDB()
        self.selectedProductList=[]
    def addselectedProduct(self):
        prod_code=input('Enter the Code of the Product:')
        if int(prod_code)<11 and int(prod_code)>0:
            prod_quan=input('Enter the Quantity:')
            self.productlist=deepcopy(self.PDB.ProductList)
            slct_prod=self.PDB.searchData(prod_code,self.productlist)
            avai_quan=int(self.PDB.searchQuantity(prod_code,self.productlist))
            if int(prod_quan)<avai_quan:
                #add in cart
                slct_prod.setProductQuantity(prod_quan)
                self.selectedProductList.append(slct_prod)
                Product_List=[]
                #Load Customer List
                try:
                    f=open('ProductDB.txt','r')
                except:
                    return
                for line in f:
                    data=eval(line)
                    Product_List.append(data)
                #search and change quantity
                list_type_product=slct_prod.getlist()
                for product in Product_List:
                    if product[-1]==list_type_product[-1]:
                        product[-2]=str(avai_quan-int(prod_quan))
                #save in file
                with open('ProductDB.txt','w') as f:
                    for product in Product_List:
                        f.write(str(product)+'\n')
                        
            elif avai_quan==0:
                print('The Selected Product is Out of Stock.')
            else:
                print('Your Quantity is greater than the Available Stock.')
        else:
            print('Enter the Code of the given Products.')
    def removeselectedProduct(self):
        prod_code=input('Enter the Code of the Product:')
        if int(prod_code)<11 and int(prod_code)>0:
            slct_prod=self.PDB.searchData(prod_code,self.productlist)
            count=1
            for product in self.selectedProductList:
                if product.getProductCode()==prod_code:
                    #remove from the cart
                    self.selectedProductList.remove(product)
                    #Load Customer List
                    Product_List=[]
                    try:
                        f=open('ProductDB.txt','r')
                    except:
                        return
                    for line in f:
                        data=eval(line)
                        Product_List.append(data)
                    #search and change quantity
                    list_type_product=slct_prod.getlist()
                    for product in Product_List:
                        if product==list_type_product:
                            product=list_type_product
                    #save in file
                    with open('ProductDB.txt','w') as f:
                        for product in Product_List:
                            f.write(str(product)+'\n')
                elif count==1:
                    print('The product is not in the cart')
                    count+=1
        else:
            print('Enter the Code of the given Products.')
            

                

    
    def printCart(self):
        print('\n__________________________________________________ CART __________________________________________________\n')
        print('------------------------------------------------------------\
-----------------------------------------')
        for product in self.selectedProductList:
            pkr=product.getProductPrize()+' PKR'
            print(f"Name: {product.getProductName():37}Prize: {pkr:15}Quantity: \
{product.getProductQuantity():10}Code: {product.getProductCode()}")
            print('------------------------------------------------------------\
-----------------------------------------')
        print('\n_________________________________________ Total Bill:',Cart.totalPrize(self.selectedProductList),'PKR _________________________________________\n')

    @staticmethod    
    def totalPrize(ProductList):
        totalbill=[]
        for product in ProductList:
            totalbill.append(int(product.getProductPrize())*int(product.getProductQuantity()))
        return sum(totalbill)

    def checkout(self):
        #selfproductlist
        spl=[]
        for product in self.selectedProductList:
            spl.append(product.getlist())
        #First we Take Input
        CDB=CustomerDB()
        print('For Checkout,You have to first Enter you User Name')
        us_name=input('Enter Your User Name:')
        if CDB.checkid(us_name,CDB.CustomerList)==True:    
            #Customer List
            Customer_Product_List=[]
            #Load Customer List
            try:
                f=open('CustomerProductsDB.txt','r')
            except:
                return
            for line in f:
                data=eval(line)
                Customer_Product_List.append(data)
            #return the customer in 'Customer type' from user name
            slct_cust=CDB.searchData(us_name,CDB.CustomerList)
            #this list stores a customer information and we make this list for comapring the list type to list type
            list_type_customer=slct_cust.getlist()
            #comparing and add product into the customer data
            for customer in Customer_Product_List:
                if customer[0]==list_type_customer:
                    customer.extend(spl)
            
            #for saving
            with open('CustomerProductsDB.txt','w') as f:
                for customer_product in Customer_Product_List:
                    f.write(str(customer_product)+'\n')
            print('\nYour Order has been placed. Thanks for your Order Sir.\n')
        else:
            print('Enter your ID correctly')

            
        
    

    def CustomerShoppingHistory(self):
        #this list stores a customer in 'Customer type' and product in product in 'Product type'
        CustomerProductsList=[]
        try:
            f=open('CustomerProductsDB.txt','r')
        except:
            return
        CDB=CustomerDB()
        user_name=input('Enter your User Name:')
        if CDB.checkid(user_name,CDB.CustomerList)==True:
            #return the customer in 'Customer type' from user name
            slct_cust=CDB.searchData(user_name,CDB.CustomerList)
            #this list stores a customer information and we make this list for comapring the list type to list type
            list_type_customer=slct_cust.getlist()
            #comparing and adding
            for line in f:
                data=eval(line)
                if list_type_customer==data[0]:
                    CustomerProductsList.extend(data)
            #for making different list of product and customer
            customerlist=[]
            productlist=[]
            #store the customer in the customerlist
            customerlist.extend(CustomerProductsList[0])
            #store the products in the product list
            for i in range(1,len(CustomerProductsList)):
                productlist.append(CustomerProductsList[i])
            #for printing Customer Information
            c=Customer()
            c.setFirstName(customerlist[0])
            c.setLastName(customerlist[1])
            c.setUserName(customerlist[2])
            c.setPassword(customerlist[3])
            c.setNumber(customerlist[4])
            c.setAddress(customerlist[5])
            c.printcustomerinformation()

            #For printing Product Information:
            print('\n\n_______________________________________________________________Your Shopping History_______________________________\
________________________________\n')
            ProductList=[]
            for product in productlist:
                p=Product()
                p.setProductName(product[0])
                p.setProductPrize(product[1])
                p.setProductQuantity(product[2])
                p.setProductCode(product[3])
                ProductList.append(p)
            print('                    -----------------------------------------------------------------------------------------------------')
            for product in ProductList:
                    pkr=product.getProductPrize()+' PKR'
                    print(f"                    Name: {product.getProductName():37}Prize:{pkr:15}Quantity: \
    {product.getProductQuantity():10}Code: {product.getProductCode()}")
                    print('                    -----------------------------------------------------------------------------------------------------')
            #close the file
            f.close()
        else:
            print('Enter your ID correctly')
