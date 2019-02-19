# Each shopping cart has a collection of products. It should also have the following functionality:
#
# add an product to the cart
# remove an product from the cart
# add up the total cost of all products in the cart before tax
# add up the total cost of all products in the cart after tax

import product
macbook = product.Product("macbook",2000,5)
water_bottle = product.Product("water bottle",3,10)

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

cart1 = Cart([macbook,water_bottle])
print(cart1)
