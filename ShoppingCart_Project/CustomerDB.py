from Customer import Customer
from CheckAndSearch import CheckAndSearch

class CustomerDB(CheckAndSearch):
    def __init__(self):
        self.loadCustomersList()
    def addCustomer(self):
        #add customer in CustomerList to save in CustomerDB
        c=Customer()
        c.setFirstName(input('Enter your First Name:'))
        c.setLastName(input('Enter your Last Name:'))
        c.setUserName(input('Enter your User Name:'))
        c.setPassword(input('Enter your Password:'))
        c.setNumber(input('Enter your Number:'))
        c.setAddress(input('Enter your Address:'))
        self.CustomerList.append(c)
        #also save customer in CustomerProductsDB
        with open('CustomerProductsDB.txt','a+') as f:
            f.write('[')
            f.write(str(c))
            f.write(']\n')
        #we store the Customer Information in two places,one for only Customer data and one for Customer Data with products.
    def saveCustomerList(self):
        with open('CustomerDB.txt','w') as f:
            for customer in self.CustomerList:
                f.write(str(customer)+'\n')
    def loadCustomersList(self):
        #all customers are store in this list ,before save in File
        self.CustomerList=[]
        try:
            f=open('CustomerDB.txt','r')
        except:
            return
        for line in f:
            customer=eval(line)
            c=Customer()
            c.setFirstName(customer[0])
            c.setLastName(customer[1])
            c.setUserName(customer[2])
            c.setPassword(customer[3])
            c.setNumber(customer[4])
            c.setAddress(customer[5])
            self.CustomerList.append(c)
        f.close()
