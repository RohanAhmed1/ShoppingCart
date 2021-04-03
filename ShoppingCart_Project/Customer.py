class Customer:
    def __init__(self):
        self.customer=[None,None,None,None,None,None]
    def setFirstName(self,fn):
        self.customer[0]=fn
    def setLastName(self,ln):
        self.customer[1]=ln
    def setUserName(self,un):
        self.customer[2]=un
    def setPassword(self,p):
        self.customer[3]=p
    def setNumber(self,n):
        self.customer[4]=n
    def setAddress(self,a):
        self.customer[5]=a
    def getFirstName(self):
        return self.customer[0]
    def getLastName(self):
        return self.customer[1]
    def getUserName(self):
        return self.customer[2]
    def getPassword(self):
        return self.customer[3]
    def getNumber(self):
        return self.customer[4]
    def getAddress(self):
        return self.customer[5]
    def getlist(self):
        return self.customer
    def printcustomerinformation(self):
        print('\n_______________________________________________________________Customer Information____________________________\
________________________________\n')
        print(f'First Name: {self.customer[0]:17}Last Name: {self.customer[1]:17}User Name: {self.customer[2]:15}Password: {self.customer[3]:15}Number:\
{self.customer[4]:15}Address: {self.customer[5]}')
        print('__________________________________________________________________________________________________________________________________\
__________________')
    def __str__(self):
        return str(self.customer)
