from textwrap import dedent
from math import pi

import sys

WIDTH = 48

MENU = {
    'Appetizers':
        {
            'Wings': [0, 3.44],
            'Spring Rolls': [0, 7.55],
            'Rolls': [0, 2.66],
            'Cookies': [0, 4.34],
            'French Fires': [0, 3.21],
            'Poutine': [0, 7.65],
        },

    'Entrees':
        {
            'Hamburger': [0, 12.79],
            'Lobster': [0, 17.49],
            'Meatball Sub': [0, 9.85],
            'Pizza': [0, 14.26],
            'Hot Pocket': [0, 7.99],
            'Pasta': [0, 5.99],
        },

    'Desserts':
        {
            'Cake': [0, 2.00],
            'Ice Cream': [0, 1.04],
            'Pie': [0, 4.08],
            'Malt': [0, 3.79],
            'Rootbeer Float': [0, 4.59],
            'Shake': [0, 3.99],
        },

    'Drinks':
        {
            'Tea': [0, .79],
            'Coffee': [0, 1.99],
            'Soda': [0, 1.99],
            'Beer': [0, 6.49],
            'Hot Tea': [0, .99],
            'Milk': [0, .99],
        },

    'Sides':
        {
            'Salad': [0, 2.39],
            'Beans': [0, 1.96],
            'Steamed Vegetables': [0, 3.49],
            'Coleslaw': [0, 2.79],
            'Baked Potato': [0, 5.99],
            'Eggs': [0, 2.19],
        },
}


def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    ln_one = 'Welcome to the Snakes Cafe!'
    ln_two = 'Please see our menu below.'
    ln_three = 'To quit at any time, type "quit" or "q"'

    print(dedent(f'''
        {'*' * WIDTH}

        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
        {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}

        {(' ' * ((WIDTH - len(ln_three)) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}

        {'*' * WIDTH}
    '''))


def display_menu():
    ln_one = 'Here are the menu items'
    print(ln_one)
    for food_type, dishes in MENU.items():
        print(dedent(food_type))
        for dish in dishes:
            print(dedent(dish) + ' $' + str(dishes[dish][1]))


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
    if 'Menu' in user_input.title():
        display_menu()

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

def order():
    print(dedent(f'''
        {'*' * WIDTH}
    '''))
    user_input = input('What would you like to order? \n')
    print(dedent(f'''
        {'*' * WIDTH}
    '''))
    process_input(user_input)


def exit():
    print(dedent('''
        'Thanks for visiting'
    '''))
    sys.exit()

def run():
    greeting()
    display_menu()
    order()


if __name__ == '__main__':
    run()
