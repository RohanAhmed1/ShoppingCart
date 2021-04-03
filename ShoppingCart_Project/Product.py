class Product:
    def __init__(self):
        self.product=['None','None','None','None']
    def setProductName(self,pn):
        self.product[0]=pn
    def setProductPrize(self,pp):
        self.product[1]=pp
    def setProductQuantity(self,q):
        self.product[2]=q
    def setProductCode(self,c):
        self.product[3]=c
    def getProductName(self):
        return self.product[0]
    def getProductPrize(self):
        return self.product[1]
    def getProductQuantity(self):
        return self.product[2]
    def getProductCode(self):
        return self.product[3]
    def getlist(self):
        return self.product
    def __str__(self):
        return str(self.product)
