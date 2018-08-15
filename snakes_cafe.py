from textwrap import dedent
import sys

WIDTH = 48

MENU = {
    'Appetizers':
        {
            'Wings': [0, 3.99],
            'Spring Rolls': [0, 7.99],
            'Rolls': [0, 2.99],
            'Cookies': [0, 4.99],
            'French Fires': [0, 3.99],
            'Poutine': [0, 7.99],
        },

    'Entrees':
        {
            'Hamburger': [0, 12.99],
            'Lobster': [0, 17.99],
            'Meatball Sub': [0, 9.99],
            'Pizza': [0, 14.99],
            'Hot Pocket': [0, 7.99],
            'PB&J': [0, 5.99],
        },

    'Desserts':
        {
            'Cake': [0, 2.99],
            'Ice Cream': [0, 1.99],
            'Pie': [0, 4.99],
            'Malt': [0, 3.99],
            'Rootbeer Float': [0, 4.99],
            'Shake': [0, 3.99],
        },

    'Drinks':
        {
            'Tea': [0, .99],
            'Coffee': [0, 1.99],
            'Soda': [0, 1.99],
            'Beer': [0, 6.99],
            'Hot Tea': [0, .99],
            'Milk': [0, .99],
        },

    'Sides':
        {
            'Salad': [0, 2.99],
            'Beans': [0, 1.99],
            'Steamed Vegetables': [0, 3.99],
            'Coleslaw': [0, 2.99],
            'Baked Potato': [0, 5.99],
            'Eggs': [0, 2.99],
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
            print(dedent(dish), dishes[dish][1])


def total_order():
    total_price = 0
    for food_type, dishes in MENU.items():
        for dish in dishes:
            if dishes[dish][0] > 0:
                total_price += (dishes[dish][0] * dishes[dish][1])
    print(total_price)



def process_input(user_input):
    ordered = False
    item = ''
    if user_input.lower() == 'quit' or user_input.lower() == 'q':
        exit()
        return

    for food_type, dishes in MENU.items():
        for dish in dishes:
            if user_input.title() == dish:
                # print(dishes[str(dish)][0])
                dishes[dish][0] += 1
                item = dishes[user_input.title()]
                ordered = True

    if ordered:
        print('You have ordered', str(item)[1], user_input.title())
        print(total_order())
    else:
        print('Please try to order something on the menu!')

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

