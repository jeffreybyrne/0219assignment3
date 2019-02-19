#Stretch Goal 2:
# Allow a quantity to be associated with each product in the cart. What is the best way to store this information?
# How does it affect each of your other methods?


# Each shopping cart has a collection of products. It should also have the following functionality:
#
# add an product to the cart
# remove an product from the cart
# add up the total cost of all products in the cart before tax
# add up the total cost of all products in the cart after tax

import product_stretch as product

class Cart:
    """
    This class represents a shopping cart. It only consists of a list of products, but it has other useful methods as well
    """

    #General init function. You can either create a cart with an existing list, or you can create an empty cart
    def __init__(self,items=[]):
        self.items = items

    #String method to describe the list of items in the cart
    def __str__(self):
        list = "Here's what's in your list:\n"
        for num in range(0,len(self.items)):
            list += "{} {}\n".format(self.items[num]['quantity'],self.items[num]['product'])
        return list

    #Method to add a product to the cart
    def add_item(self,item,quant):
        for num in range(0,len(self.items)):
            if self.items[num]['product'] == item:
                self.items[num]['quantity'] += int(quant)
                return None
        self.items.append({'product': item, 'quantity': int(quant)})
        return None

    #Method to remove a product from the cart
    def remove_item(self,item,quant):
        list = self.items
        for num in range(0,len(list)):
            if list[num]['product'] == item and list[num]['quantity'] == quant:
                list.pop(num)
                return None
            elif list[num]['product'] == item and list[num]['quantity'] > quant:
                list[num]['quantity'] -= int(quant)
                return None
        return None

    #Method to return the sum of the base costs of each item in the cart
    def total_before_tax(self):
        total = 0
        for num in range(0,len(self.items)):
            total += (self.items[num]['product'].price * self.items[num]['quantity'])
        return float(total)

    #Method to return the sum of the total costs of each item in the cart with taxes applied
    def total_after_tax(self):
        total = 0
        for num in range(0,len(self.items)):
            total += (self.items[num]['product'].total_price() * self.items[num]['quantity'])
        return float(total)

    #Stretch goal 1: Add the ability to find the most expensive product in a cart.
    def most_expensive_item(self):
        #First, check to see if there's anything in the cart. If it's an empty list, tell the user
        if self.items == []:
            return "The cart is empty"
        #Otherwise, the first item is our starting highest price
        curr_item = self.items[0]['product']
        #If that's the only item, clearly it's the most expensive so return it
        if len(self.items) == 1:
            return curr_item
        else:
            #Otherwise, loop through the remaining items and for each one compare it's price to the currently most expensive
            for num in range(1,len(self.items)):
                if self.items[num]['product'].price > curr_item.price:
                    curr_item = self.items[num]['product']
            return curr_item

macbook = product.Product("MacBook",2000,5)
water_bottle = product.Product("water bottle",3,10)
pants = product.Product("pants",50,5)


cart1 = Cart([
  {'product': macbook, 'quantity': 3},
  {'product': pants, 'quantity': 1},
  {'product': water_bottle, 'quantity': 1},
])
print(cart1)
print("Add two pairs of pants")
cart1.add_item(pants,2)
print(cart1)
print("Remove one macbook")
cart1.remove_item(macbook,1)
print(cart1)
print("Remove two more macbooks")
cart1.remove_item(macbook,2)
print(cart1)
print("Add one macbook back")
cart1.add_item(macbook,1)
print(cart1)
print("The total before tax is ${:.2f}.".format(cart1.total_before_tax()))
print("The total with taxes is ${:.2f}.".format(cart1.total_after_tax()))
print("The most expensive item in the cart is {}.".format(cart1.most_expensive_item()))
# cart1.remove_item(pants)
# print(cart1.most_expensive_item())
# cart1.remove_item(water_bottle)
# print(cart1.most_expensive_item())
