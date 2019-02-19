# Each product has a name, base price, and tax rate. There should also be a method to calculate and return the product's
# total price based on the base price and tax rate.

class Product:

    def __init__(self,name,price,tax=0):
        self.name = name
        self.price = float(price)
        self.tax = float(tax)

    def __str__(self):
        return "The product is {}, it costs ${:.2f}, and has a tax rate of {}.".format(self.name,self.price,self.tax)
