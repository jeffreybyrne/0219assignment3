# Each shopping cart has a collection of products. It should also have the following functionality:
#
# add an product to the cart
# remove an product from the cart
# add up the total cost of all products in the cart before tax
# add up the total cost of all products in the cart after tax

import product

class Cart:

    def __init__(self,items=[]):
        self.items = items

    def add_item(self,product):
        self.items.append(product)

    def remove_item(self,product):
        self.items.remove(product)

    def __str__(self):
        list_of_items = "The following items are in your cart:\n"
        for num in range(0,len(self.items)):
            list_of_items += "{}\n".format(self.items[num])
        return list_of_items

    def total_before_tax(self):
        total = 0
        for num in range(0,len(self.items)):
            total += self.items[num].price
        return str(total)

macbook = product.Product("macbook",2000,5)
water_bottle = product.Product("water bottle",3,10)
pants = product.Product("pants",50,5)


cart1 = Cart([macbook,water_bottle])
print(cart1)
cart1.add_item(pants)
print(cart1)
cart1.remove_item(macbook)
print(cart1)
print(cart1.total_before_tax())
