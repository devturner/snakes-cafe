from textwrap import dedent
import sys

WIDTH = 48

MENU = {
    'Appetizers':
        {
            'Wings': 0,
            'Spring Rolls': 0,
            'Rolls': 0,
        },
        
    'Entrees':
        {
            'Hamburger': 0,
            'Lobster': 0,
            'Meatball Sub': 0,
        },

    'Desserts':
        {
            'Cake': 0,
            'Ice Cream': 0,
            'Pie': 0,
        },
        
    'Drinks':
        {
            'Tea': 0,
            'Coffee': 0,
            'Soda': 0,
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

    for food_type, items in MENU.items():
        print(dedent(food_type))
        
        for key in items:
            print(dedent(key))


def process_input(user_input):
    ordered = False
    item = ''
    if user_input.lower() == 'quit' or user_input.lower() == 'q':
        exit()
        return

    for food_type, dishes in MENU.items():
        for dish in dishes:
            if user_input.title() == dish:
                dishes[user_input.title()] += 1
                item = dishes[user_input.title()]
                ordered = True   

    if ordered:
        print('You have ordered', str(item), user_input.title())
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

