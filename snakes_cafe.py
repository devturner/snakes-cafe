from textwrap import dedent
from math import pi
from uuid import uuid4

import sys
import csv

WIDTH = 48

MENU = {
    'Appetizers':
        {
            'Wings': [0, 3.44, 10],
            'Spring Rolls': [0, 7.55, 10],
            'Rolls': [0, 2.66, 10],
            'Cookies': [0, 4.34, 10],
            'French Fires': [0, 3.21, 10],
            'Poutine': [0, 7.65, 10],
            'Hotter Wings': [0, 8.99, 10],
            'Chicken Tenders': [0, 9.99, 10],
            'Bean Salad': [0, 2.99, 10],
        },

    'Entrees':
        {
            'Hamburger': [0, 12.79, 10],
            'Lobster': [0, 17.49, 10],
            'Meatball Sub': [0, 9.85, 10],
            'Pizza': [0, 14.26, 10],
            'Hot Pocket': [0, 7.99, 10],
            'Pasta': [0, 5.99, 10],
            'Tofu': [0, 9.99, 10],
            'Tacos': [0, 9.99, 10],
            'Veggie Burger': [0, 12.99, 10],
        },

    'Desserts':
        {
            'Cake': [0, 2.00, 10],
            'Ice Cream': [0, 1.04, 10],
            'Pie': [0, 4.08, 10],
            'Malt': [0, 3.79, 10],
            'Rootbeer Float': [0, 4.59, 10],
            'Shake': [0, 3.99, 10],
            'Chocolate': [0, 2.99, 10],
            'Caramelled Nuts': [0, 2.99, 10],
            'Candy': [0, .99, 10],
        },

    'Drinks':
        {
            'Tea': [0, .79, 10],
            'Coffee': [0, 1.99, 10],
            'Soda': [0, 1.99, 10],
            'Beer': [0, 6.49, 10],
            'Hot Tea': [0, .99, 10],
            'Milk': [0, .99, 10],
            'Import Beer': [0, 2.99, 10],
            'Water': [0, 2.99, 10],
            'Esspresso': [0, 2.99, 10],
        },

    'Sides':
        {
            'Salad': [0, 2.39, 10],
            'Beans': [0, 1.96, 10],
            'Steamed Vegetables': [0, 3.49, 10],
            'Coleslaw': [0, 2.79, 10],
            'Baked Potato': [0, 5.99, 10],
            'Eggs': [0, 2.19],
            'Chips': [0, 2.99, 10],
            'Apples': [0, 2.99, 10],
            'Big Salad': [0, 2.99, 10],
        },
}


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


def display_defualt_menu():
    ln_one = 'Here are the menu items'
    print(ln_one)
    for food_type, dishes in MENU.items():
        print(dedent(food_type))
        for dish in dishes:
            print(dedent(dish) + ' $' + str(dishes[dish][1]))
    order()


def display_special_menu():
    with open('special_menu2.csv', newline='') as csvfile:
        menu = csv.DictReader(csvfile)
        i = 0
        for row in menu:
            i += 1
            # this is shitty
            if i == 1 or i == 11 or i == 20 or i == 29 or i == 38 :
                print(row['type'])
            else:
                print(row['dish'], '$' + row['price'])
    special_order()


def choose_menu():
    user_input = input('Enter 1 for our normal menu or 2 for our special menu \n')
    if user_input == str(1):
        display_defualt_menu()
    elif user_input == str(2):
        display_special_menu()

def total_order():
    subtotal_price = 0
    for food_type, dishes in MENU.items():
        for dish in dishes:
            if dishes[dish][0] > 0:
                subtotal_price += (dishes[dish][0] * dishes[dish][1])

    tax = float(subtotal_price) * .10
    total_price = subtotal_price + tax
    total_price = '{0:.2f}'.format(total_price)
    tax = '{0:.2f}'.format(tax)
    subtotal_price = '{0:.2f}'.format(subtotal_price)
    print('Subtotal: $' + str(subtotal_price))
    print('Tax: $' + str(tax))
    print('Total: $' + str(total_price))


def bill():
    print(dedent(f'''
        {'~' * WIDTH}
        {'~' * WIDTH}
        The Snakes Cafe
            "Eatability Counts"
        {'~' * WIDTH}
        {'Order: ' + str(uuid4())}
        {'~' * WIDTH}
    '''))
    for food_type, dishes in MENU.items():
        for dish in dishes:
            if dishes[dish][0] > 0:
                print(dish, 'x' + str(dishes[dish][0]), '$' + str(dishes[dish][1]))

    print(dedent(f'''
        {'~' * WIDTH}
    '''))
    total_order()
    print(dedent(f'''
        {'~' * WIDTH}

    '''))

def process_input(user_input):
    ordered = False
    item = ''
    if user_input.lower() == 'quit' or user_input.lower() == 'q':
        exit()
        return
    if 'Order' in user_input.title():
        bill()
    if '2' in user_input.title():
        display_special_menu()
    if '1' in user_input.title() or 'Menu' in user_input.title():
        display_defualt_menu()


    for food_type, dishes in MENU.items():
        for dish in dishes:
            if user_input.title() == food_type:
                print(dedent(dish) + ' $' + str(dishes[dish][1]))
            if user_input.title() == dish:
                # print(dishes[str(dish)][0])
                dishes[dish][0] += 1
                item = dishes[user_input.title()]
                ordered = True
            if 'Remove' in user_input.title() and dish in user_input.title() and dishes[dish][0] > 0:
                dishes[dish][0] -= 1
                print('Removed', dish, 'from your order')
                total_order()

    if ordered:
        print('You have ordered', str(item)[1], user_input.title())
        total_order()
    else:
        print('Order something on the menu!')

    order()

def special_process_input(user_input):
    pass


def order():
    print(dedent(f'''
        {'*' * WIDTH}
    '''))
    user_input = input('What would you like to order? \n')
    print(dedent(f'''
        {'*' * WIDTH}
    '''))
    process_input(user_input)

def special_order():
    print(dedent(f'''
        {'*' * WIDTH}
    '''))
    user_input = input('What would you like to order? \n')
    print(dedent(f'''
        {'*' * WIDTH}
    '''))
    special_process_input(user_input)

def exit():
    print(dedent('''
        'Thanks for visiting'
    '''))
    sys.exit()

def run():
    greeting()
    choose_menu()


if __name__ == '__main__':
    run()
