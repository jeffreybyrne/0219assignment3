# Each shopping cart has a collection of products. It should also have the following functionality:
#
# add an product to the cart
# remove an product from the cart
# add up the total cost of all products in the cart before tax
# add up the total cost of all products in the cart after tax

import product

class Cart:
    """
    This class represents a shopping cart. It only consists of a list of products, but it has other useful methods as well
    """

    #General init function. You can either create a cart with an existing list, or you can create an empty cart
    def __init__(self,items=[]):
        self.items = items

    #String method to describe the list of items in the cart
    def __str__(self):
        list_of_items = "The following items are in your cart:\n"
        for num in range(0,len(self.items)):
            list_of_items += "{}\n".format(self.items[num])
        return list_of_items

    #Method to add a product to the cart
    def add_item(self,product):
        self.items.append(product)

    #Method to remove a product from the cart
    def remove_item(self,product):
        self.items.remove(product)

    #Method to return the sum of the base costs of each item in the cart
    def total_before_tax(self):
        total = 0
        for num in range(0,len(self.items)):
            total += self.items[num].price
        return str(total)

    #Method to return the sum of the total costs of each item in the cart with taxes applied
    def total_after_tax(self):
        total = 0
        for num in range(0,len(self.items)):
            total += self.items[num].total_price()
        return str(total)

    #Stretch goal 1: Add the ability to find the most expensive product in a cart.
    def most_expensive_item(self):
        #First, check to see if there's anything in the cart. If it's an empty list, tell the user
        if self.items == []:
            return "The cart is empty"
        #Otherwise, the first item is our starting highest price
        curr_item = self.items[0]
        #If that's the only item, clearly it's the most expensive so return it
        if len(self.items) == 1:
            return curr_item
        else:
            #Otherwise, loop through the remaining items and for each one compare it's price to the currently most expensive
            for num in range(1,len(self.items)):
                if self.items[num].price > curr_item.price:
                    curr_item = self.items[num]
            return curr_item

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
print(cart1.total_after_tax())
print(cart1.most_expensive_item())
cart1.remove_item(pants)
print(cart1.most_expensive_item())
cart1.remove_item(water_bottle)
print(cart1.most_expensive_item())
