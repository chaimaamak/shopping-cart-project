# shopping_cart.py

import datetime
import os
import statistics

from pprint import pprint

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

now = datetime.datetime.now()

# DATA SETUP

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# pprint(products)


## INFORMATION CAPTURE  #> Prompts user for input to select from list of inventory

subtotal = 0
tax = 0
total_price = 0
valid_ids = [str(i['id']) for i in products]
selected_ids = []

while True:
    product_id = input("Please enter product ID, or 'Done' if there are no more products:") #>string type
    
    if product_id.lower() == "done":
        break
    elif product_id in valid_ids:
        selected_ids.append(int(product_id))
    else:
        print ("Invalid Entry. Try Again!")

## INFORMATION DISPLAY #> Calculate total cost and apply tax

for product_id in selected_ids:
    matching_products = [item for item in products if item["id"] == product_id] #>convert string to integer for comparison reasons
    matching_product = matching_products[0]
    subtotal = subtotal + matching_product["price"]
    tax = tax + subtotal * 0.0875
    print("..." + matching_product["name"] + " " + str(matching_product["price"]))

## Accept or Reject Transaction #> Prompt user to accept or alter the current items list



## RECEIPT #> Prompt user to either print a hard copy of the receipt or send it to their email address

total_price = tax + subtotal

print("HAPPY FOODS")
print("WWW.HAPPY-FOODS.COM")
print("---------------------------------")
print("CHECKOUT AT:" + now.strftime("%Y-%m-%d %H:%M:%S"))
print("---------------------------------")
print("SELECTED PRODUCTS:")
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Dry Nose Oil ($21.99)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Mint Chocolate Flavored Syrup ($4.50)
#>  ... Chocolate Fudge Layer Cake ($18.50)
print ("---------------------------------")
print ("SUBTOTAL: " + str(subtotal)) # format to USD
print ("TAX: " + str(tax)) # format to USD
print ("TOTAL: " + str(total_price) # format to USD
print ("---------------------------------")
print ("THANKS, SEE YOU AGAIN SOON!")
print ("---------------------------------")

# PRODUCT VALIDATION


