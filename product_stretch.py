# Each product has a name, base price, and tax rate. There should also be a method to calculate and return the product's
# total price based on the base price and tax rate.

class Product:
    """
    This class represents a retail product. It has a name, a base price, and a tax rate
    """

    def __init__(self,name,price,tax=0):
        self.name = name
        self.price = float(price)
        self.tax = float(tax)

    #str function to describe the product itself
    def __str__(self):
        # return "The product is {}, it costs ${:.2f}, and has a tax rate of {}.".format(self.name,self.price,self.tax)
        return "{}".format(self.name)

    #Function to figure out the total cost with taxes
    def total_price(self):
        return self.price * (1 + self.tax/100)
