from textwrap import dedent
from order import Order
from uuid import uuid4

import sys
import csv

WIDTH = 56
menu = {}
guest_ticket = Order()


def built_in_menu():
    global menu
    menu = {
        'Appetizers':
            {
                'Wings': [3.44, 10],
                'Spring Rolls': [7.55, 10],
                'Rolls': [2.66, 10],
                'Cookies': [4.34, 10],
                'French Fires': [3.21, 10],
                'Poutine': [7.65, 10],
                'Hotter Wings': [8.99, 10],
                'Chicken Tenders': [9.99, 10],
                'Bean Salad': [2.99, 10],
            },

        'Entrees':
            {
                'Hamburger': [12.79, 10],
                'Lobster': [17.49, 10],
                'Meatball Sub': [9.85, 10],
                'Pizza': [14.26, 10],
                'Hot Pocket': [7.99, 10],
                'Pasta': [5.99, 10],
                'Tofu': [9.99, 10],
                'Tacos': [9.99, 10],
                'Veggie Burger': [12.99, 10],
            },

        'Desserts':
            {
                'Cake': [2.01, 10],
                'Ice Cream': [1.04, 10],
                'Pie': [4.08, 10],
                'Malt': [3.79, 10],
                'Root-beer Float': [4.59, 10],
                'Shake': [3.99, 10],
                'Chocolate': [2.99, 10],
                'Caramelized Nuts': [2.99, 10],
                'Candy': [0.99, 10],
            },

        'Drinks':
            {
                'Tea': [.79, 10],
                'Coffee': [1.99, 10],
                'Soda': [1.99, 10],
                'Beer': [6.49, 10],
                'Hot Tea': [.99, 10],
                'Milk': [.99, 10],
                'Import Beer': [2.99, 10],
                'Water': [2.99, 10],
                'Espresso': [2.99, 10],
            },

        'Sides':
            {
                'Salad': [2.39, 10],
                'Beans': [1.96, 10],
                'Steamed Vegetables': [3.49, 10],
                'Coleslaw': [2.79, 10],
                'Baked Potato': [5.99, 10],
                'Eggs': [2.19, 10],
                'Chips': [2.99, 10],
                'Apples': [2.99, 10],
                'Big Salad': [2.99, 10],
            },
    }
    return(menu)


def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    ln_one = 'Welcome to the Snakes Cafe!'
    ln_two = 'Please select a menu.'
    ln_three = 'To quit at any time, type "quit" or "q"'

    print(dedent(f'''
        {'*' * WIDTH}

        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
        {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}

        {(' ' * ((WIDTH - len(ln_three)) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}

        {'*' * WIDTH}
    '''))


def display_menu(menu):
    """ Display the menu that is built into the application and call the order function
    """
    print('Here are the menu items')
    try:
        for key, value in menu.items():
            print(key.title())
            print('-' * 8)
            for key, value in menu[key].items():
                if value[0] == '[':
                    print(key.ljust(50) + '$' + str(value[1:5]))
                else:
                    print(key.ljust(50) + '$' + str(value[0]))
            print('\n')
    except KeyError:
        print('Oops! Something was wrong with your request.')
    order()


def get_users_filepath():
    """ Get the user file path, error check it, and if the file is there, use it
    """

    user_input = input('Provide your file path, like: ./assets/special_menu.csv \n')
    file_path = user_input.split('/')
    file = file_path[len(file_path)-1].split('.')
    extension = file[len(file)-1]
    # import pdb; pdb.set_trace()
    if extension != 'csv':
        print('Please provide a csv file')
        return choose_menu()
    else:
        try:
            with open(user_input, 'r') as f:
                menu_import = csv.reader(f)
                for row in menu_import:
                    item = iter(row[1:])
                    if row[0] in menu.keys():
                        menu[row[0]].update(dict(zip(item, item)))
                    else:
                        menu[row[0]] = dict(zip(item, item))
                display_menu(menu)
        except (IndexError, FileNotFoundError) as error:
            raise Exception('File not found or incorrect filetype; please use a CSV.')


def choose_menu():
    """Function which will let the user choose their menu.
    """
    user_input = input('Enter 1 for our normal menu or 2 for an external menu \n')
    if user_input == str(1):
        display_menu(built_in_menu())
    elif user_input == str(2):
        get_users_filepath()


def total_order(ticket):
    """ Doing the math on the order to get the subtotal, tax, and total
    """
    tax = guest_ticket.tax
    total_price = guest_ticket.total
    subtotal_price = guest_ticket.subtotal
    for ordered_food, quantity in ticket.dishes.items():
        for food_type, dishes in menu.items():
            for dish, value in dishes.items():
                if ordered_food == dish:
                    if value[0] == '[':
                        cost = float(value[1:5])
                        subtotal_price = cost * quantity
                    else:
                        cost = value[0]
                        subtotal_price = cost * quantity

    tax = float(subtotal_price) * .10
    total_price = subtotal_price + tax
    guest_ticket._update_totals(tax, subtotal_price, total_price)
    guest_ticket.display_order()


def process_input(user_input):
    """Process all the user input from the program
    """

    avalible = 0
    if user_input.lower() == 'quit' or user_input.lower() == 'q':
        exit()
        return
    if 'Order' in user_input.title():
        total_order(guest_ticket)
        guest_ticket.print_receipt()
    if '2' in user_input.title():
        get_users_filepath()
    if '1' in user_input.title() or 'Menu' in user_input.title():
        display_menu(menu)

    for food_type, dishes in menu.items():
        for dish, value in dishes.items():
            if user_input.title() == food_type:
                if value[0] == '[':
                    print(dish.ljust(50) + '$' + str(value[1:5]))
                else:
                    print(dish.ljust(50) + '$' + str(value[0]))
            if user_input.title() == dish:
                if value[0] == '[':
                    avalible = int(value[-2])
                else:
                    avalible = value[1]
                try:
                    quantity = int(input('We have x' + str(avalible) + ' in stock. How many would you like? :'))
                    if quantity > 0 and quantity <= avalible:
                        print(dish + ': ' + str(quantity))
                        guest_ticket.add_item(dish, quantity)
                        order()
                    else:
                        print('please order > 1, or <', avalible)
                        order()
                except ValueError:
                    print("That wasn't a number!", user_input)
                    order()
            if 'Remove' in user_input.title() and dish in user_input.title() and dish in guest_ticket.dishes:
                guest_ticket.remove_item(dish)
    order()






def order():
    """ Prompt the guest to order something
    """
    print(dedent(f'''
        {'*' * WIDTH}
    '''))
    user_input_order = input('What would you like to order, or remove from your order? \n')
    print(dedent(f'''
        {'*' * WIDTH}
    '''))
    process_input(user_input_order)


def exit():
    """ Exits the app
    """
    print(dedent('''
        'Thanks for visiting'
    '''))
    sys.exit()


def run():
    """ Initilize the application
    """
    greeting()
    choose_menu()



if __name__ == '__main__':
    try:
        run()
    except(KeyboardInterrupt):
        exit()
