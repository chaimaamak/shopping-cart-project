# shopping_cart.py

import os
import datetime
from pprint import pprint

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

now = datetime.datetime.now()

## DATA SETUP

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

valid_ids = [str(i['id']) for i in products]   #> Identifies list of valid ids in the products list provided using list comprehension

def input_products():
    selected_ids = []
    while True:
        product_id = input("Please enter product ID, or 'Done' if there are no more products:") #>string type
        
        if product_id.lower() == "done":
            break
        elif product_id in valid_ids:
            selected_ids.append(int(product_id))
        else:
            print ("Invalid Entry. Try Again!")
    return selected_ids

## INFORMATION DISPLAY #> Calculate total cost and apply tax

def format_products(selected_ids):  #> Formatting my selected products into text
    text = ''
    for product_id in selected_ids:
        matching_products = [item for item in products if item["id"] == product_id] #>convert string to integer for comparison reasons
        matching_product = matching_products[0]
        text = text + '\n...' + matching_product["name"] + " " + str(matching_product["price"])
    return text

def final_price(selected_ids):
    subtotal = 0
    tax = 0
    total_price = 0
    for product_id in selected_ids:
        matching_products = [item for item in products if item["id"] == product_id] #>convert string to integer for comparison reasons
        matching_product = matching_products[0]
        subtotal = subtotal + matching_product["price"]
        tax = tax + subtotal * 0.0875
    total_price = tax + subtotal
    return subtotal, tax, total_price
    
def format_text(selected_ids):  #> Returns a template 
    text = '\n---~~~~~~~ HAPPY FOODS ~~~~~~~---'
    text += '\nWWW.HAPPY-FOODS.COM'
    text += "\n---------------------------------"
    text += "\nCHECKOUT AT:" + now.strftime("%Y-%m-%d %H:%M:%S")   #> Used online sample of datetime applicability
    text += "\n---------------------------------"
    text += "\nSELECTED PRODUCTS:"
    text += format_products(selected_ids)  
    subtotal, tax, total_price = final_price(selected_ids)
    text += '\n---------------------------------'
    text += '\nSUBTOTAL: ' + to_usd(subtotal) # format to USD
    text += '\nTAX: ' + to_usd(tax) # format to USD
    text += '\nTOTAL: ' + to_usd(total_price) # format to USD
    text += '\n---------------------------------'
    text += '\nTHANKS, SEE YOU AGAIN SOON!'
    text += '\n---------------------------------'
    return text


while True:
    selected_ids = input_products()
    print (format_text(selected_ids))

    ## Accept or Reject Transaction #> Prompt user to accept or alter the current items list

    user_decision = input ("Do You Accept or Reject This Transaction? (Accept/Reject)")

    if user_decision.lower() == "accept":
        email_print_decision = input("Would You Like an Email Receipt? (Yes/No)")
        if email_print_decision.lower() == "no":
            print ("\n\nHere A Validation of Your Purchase" + format_text(selected_ids))
        if email_print_decision.lower() == "yes":
            import os
            from dotenv import load_dotenv
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail
            load_dotenv()
            
            user_email = input ("Enter Your Email Address:")
            
            SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
            SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
            MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

            #print("API KEY:", SENDGRID_API_KEY)
            #print("TEMPLATE ID:", SENDGRID_TEMPLATE_ID)
            #print("EMAIL ADDRESS:", MY_ADDRESS)

            template_data = {
                "total_price_usd": to_usd(total_price),
                "human_friendly_timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
                "products": print (format_products(selected_ids))
            }

            client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
            print("CLIENT:", type(client))

            message = Mail(from_email=MY_ADDRESS, to_emails = MY_ADDRESS)
            print("MESSAGE:", type(message))

            message.template_id = SENDGRID_TEMPLATE_ID

            message.dynamic_template_data = template_data

            try:
                response = client.send(message)
                print("RESPONSE:", type(response))
                print(response.status_code)
                print(response.body)
                print(response.headers)

            except Exception as e:
                print("OOPS", e)        

        break
    elif user_decision.lower() == "reject":
        print ("Let's Start Over!")
    else:
        print ("Invalid Input. Try Again!")
    




## EMAIL SETUP FUNCTION

#def format_email(selected_ids):
#
#    load_dotenv()
#
#    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
#    SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
#    MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
#
#    #print("API KEY:", SENDGRID_API_KEY)
#    #print("TEMPLATE ID:", SENDGRID_TEMPLATE_ID)
#    #print("EMAIL ADDRESS:", MY_ADDRESS)
#    
#    template_data = {
#        "total_price_usd": to_usd(total_price),
#        "human_friendly_timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
#        "products": print (format_products(selected_ids))
#    }
#
#    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
#    print("CLIENT:", type(client))
#
#    message = Mail(from_email=MY_ADDRESS, to_emails = MY_ADDRESS)
#    print("MESSAGE:", type(message))
#
#    message.template_id = SENDGRID_TEMPLATE_ID
#
#    message.dynamic_template_data = template_data
#
#    try:
#        response = client.send(message)
#        print("RESPONSE:", type(response))
#        print(response.status_code)
#        print(response.body)
#        print(response.headers)
#
#    except Exception as e:
#        print("OOPS", e)
#    return message