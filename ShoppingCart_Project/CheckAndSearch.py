#This class has method to the check and search information in file.
class CheckAndSearch:
    def checkid(self,us_na,cust_list):
        for customer in cust_list:
            if us_na==customer.getUserName():
                return True
        return False
    def checkpassword(self,passw,cust_list):
        for customer in cust_list:
            if passw==customer.getPassword():
                return True
        return False
    def searchData(self,data,lst):
        for i in lst:
            if data==i.getUserName():
                return i
        else:
            return 'Not Found'
        
    def searchQuantity(self,data,lst):
        for i in lst:
            if data==i.getProductCode():
                return i.getProductQuantity()
        else:
            return 'Not Found'
