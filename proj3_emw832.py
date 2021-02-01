#Project 3 
#Author: Sai Ananthula
#ID: emw832

customer_name_age = [('Aaron','Priscilla','Marty','John','Bob','Alicia'
                    ,'Eve','Joesph','Michael','Donald'),
                    (18,15,42,25,29,75,15,38,62,68)]

#global lists above and below for customers and products

product_name_prices = [('Beans','Rice','Banana','Ice','Tea','Bread','Orange','Sugar'),
                    (3.25,4.31,6.88,3.3,5.25,4.89,6.32,2.25)]

discount = .1
boundary = 60
tax_rate = .07


# this function is for the program to ask for and test user input while dealing with tuples inside of lists
def get_user_selection(menu,min,max):
    control = False
    
    while control == False:
        try:
            choice = int(input(menu))
        except:
            control = False
            print(f'Please enter an integer between {min} and {max} inclusive.')
        else: 
            if choice <= max and choice >= min:
                control = True
            else:
                print('Input is either too high or too low')
                control = False
    
    return choice

#this function displays list in a standardized format
def display_list(listvar):
    control = 0
    control2 = 0
    while control < len(listvar):
        while control2 < len(listvar[0]):
            print(f'{control2}: ("{listvar[0][control2]}", {listvar[1][control2]})')
            control2 += 1
        control += 1

# this function is designed to ask the user to select an element in a list and make sure it exists 
def get_index(listvar):
    display_list(listvar)
    temp_length = len(listvar[0]) - 1
    
    control = False
    
    while control == False:
        try:
            choice = int(input(f'Enter your choice (0 to {temp_length}): '))
        except:
            control = False
            print(f'Please enter an integer between 0 and {temp_length} inclusive.')
        else: 
            if choice <= temp_length and choice >= 0:
                control = True
            else:
                print('Input is either too high or too low')
                control = False
    return choice

#this function handles the transaction and calls other methods. add to cart, print cart, complete transaction
#does not return anything and takes no parameters
def run_transaction():
    control = False
    shopping_cart= []
    print('Select a Customer: ')
    customer = get_index(customer_name_age)
    print(f'{customer} {customer_name_age[0][customer]} {customer_name_age[1][customer]}')
    if customer_name_age[1][customer] >= 60:
        age_discount = True
    else:
        age_discount = False

    while control == False:
    
        shop_menu = '1. Add Items to Cart\n2. Print Cart Content\n3. Complete the Transaction' \
            '\n4. Abort the Transaction\nEnter your choice: '

        choice = get_user_selection(shop_menu,1,4)
    
        if choice == 1:
            shopping_cart.append(add_to_cart(shopping_cart,age_discount))
        elif choice == 2:
            print_cart(shopping_cart)
        elif choice == 3:
            complete_transaction(shopping_cart)
            control = True
        elif choice == 4:
            control = True

#adds items to card and handles any possible input error
def add_to_cart(cart,age):
    control = False
    print('Add to Cart: ')
    choice = get_index(product_name_prices)

    while control == False:
        try:
            quantity = int(input(f'Enter quantity of {product_name_prices[0][choice]}: '))
        except:
            control = False
            print(f'Please enter an integer greater than 0')
        else: 
            if quantity > 0:
                control = True
            else:
                print('Input is either too low')
                control = False
    
    temp_dict = {'Name': product_name_prices[0][choice] , 'Quantity': quantity , 
                'Price': product_name_prices[1][choice], 'Discount' : age }
    return temp_dict
    

#prints the cart
def print_cart(cart):
    x = 0
    print('--------------------')
    while x < len(cart):
        item = cart[x]['Name']
        quantity = cart[x]['Quantity'] 
        price = cart[x]['Price']
        if cart[x]['Discount'] == True:
            total = quantity * price * discount
            print(f'Item:      {item}:   {quantity} @ ${price}\n  discount: ${total:0.2f}')
        else:
            print(f'Item:      {item}:   {quantity} @ ${price}')
        x += 1
    print('--------------------')

#prints the final cart and handles purchasing
# handles error handling
def complete_transaction(cart):
    control = False
    subtotal = get_subtotal(cart)
    tax = subtotal * tax_rate
    print(tax)
    total = subtotal + (tax / 2)
    print('Checkout')
    print_cart(cart)
    print(f'\tSub_total: ${subtotal:0.2f}')
    print(f'\tTax: ${tax:0.2f}')
    print(f'\tTotal: ${total:0.2f}')
    while control == False:
        try:
            payment = int(input('Enter cash amount: '))
        except:
            print('Enter a positive number')
        else:
            if payment > total:
                control = True
                change = payment - total

                print(f'Cash: ${payment:0.2f}')
                print(f'Change: ${change:0.2f}')
                print('Thank you for shapping at MyStore!')
            else:
                print('Insufficient payment. Try again.')    

#calculates subtotal
def get_subtotal(cart):
    x = 0
    subtotal = 0
    while x < len(cart):
        quantity = cart[x]['Quantity'] 
        price = cart[x]['Price']
        if cart[x]['Discount'] == True:
            subtotal += quantity * price * (1 - discount)
            
        else:
            subtotal += quantity * price
        x += 1

    return subtotal

#main method which asks the user what they want to do
def main():
    print('Project 3: Developed by Sai Ananthula')
    print('Welcome to MyStore!')
    

    choice = False
    while choice == False:
        start_menu = ('0. Exit\n1. Start a new transaction\nEnter your choice: ')
        user_choice = get_user_selection(start_menu,0,1)
        if user_choice == 1:
            run_transaction()
        else:
            choice = True
            print('Thank you for using this program. Bye.')

#calls main method
if __name__ == "__main__":
    main()