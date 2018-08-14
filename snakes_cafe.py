from textwrap import dedent
import sys

WIDTH = 48

# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
        #   2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

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



DISP_MENU = """
Appetizers
----------
Wings
Rolls
Spring Rolls

Entrees
-------
Hamburger
Lobster
Meatball Sub

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Soda
"""



def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    ln_one = 'Welcome to the Snakes Cafe!'
    ln_two = 'Please see our menu below.'
    ln_three = 'To quit at any time, type "quit"'

    print(dedent(f'''
        {'*' * WIDTH}

        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
        {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}

        {(' ' * ((WIDTH - len(ln_three)) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}

        {'*' * WIDTH}
    '''))


def display_menu():
    print('Here are the menu items')
        # print(dedent(f''' 
        # {(' ' * ((WIDTH - len(DISP_MENU)) // 2)) + DISP_MENU + (' ' * ((WIDTH - len(DISP_MENU)) // 2))}
        # '''))
    for food_type, items in MENU.items():
        print(food_type)
        for key in items:
            print(key)


# for p_id, p_info in people.items():
    # print("\nPerson ID:", p_id)
    
    # for key in p_info:
    #     print(key + ':', p_info[key])


def process_input(user_input):
    if user_input.lower() == 'quit':
        exit()
        return
    
    if user_input.title() in MENU:
        print("blah")

        # if user_input.lower() == i.lower():
        #     i.value() += 1


def exit():
    print(dedent('''
        'Thanks for visiting'
    '''))
    sys.exit()

def run():
    greeting()
    display_menu()
    user_input = input('What would you like to order? \n')
    process_input(user_input)

if __name__ == '__main__':
    run()

