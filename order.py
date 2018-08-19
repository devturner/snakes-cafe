from uuid import uuid4
from textwrap import dedent
WIDTH = 56


class Order(object):
    """A record of the customers order, their uuid, and the receipt
    """
    def __init__(self):
        """ Creates an order with a uuid
        """
        self.id = uuid4()
        self.dishes = {}
        self.subtotal = 0
        self.tax = 0
        self.total = 0

    def add_item(self, dish, quantity=1):
        """ Adds an item to the order, and a quantity greater than 1, if provided
        """
        if dish in self.dishes:
            self.dishes[dish] += quantity
            return self.dishes
        else:
            self.dishes[dish] = quantity
            return self.dishes


    def remove_item(self, dish, quantity=1):
        """ Deletes an item to the order, and a quantity greater than 1, if provided
        """
        if quantity < 1:
            print('You can\'t do that')

        if dish in self.dishes:
            if quantity < self.dishes[dish]:
                self.dishes[dish] -= quantity
            elif quantity == self.dishes[dish]:
                del self.dishes[dish]
            else:
                print('You have ordered:', self.dishes[dish])

        return self.dishes


    def update_totals(self, tax, subtotal, total):
        """Set the objects totals for tax, subtotal, and total price
        """
        self.tax = tax
        self.subtotal = subtotal
        self.total = total
        return self


    def display_order(self):
        """ Prints the order out to the screen so it can be reviewed
        """
        str1 = str(dedent(f'''
            {'*' * WIDTH}
            {'*' * WIDTH}
                    The Snakes Cafe
                        "Eatability Counts"
            {'*' * WIDTH}
            {'Order: ' + str(self.id)}
            {'*' * WIDTH}
        '''))
        str2 = ''
        print(str1)
        for dish, quantity in self.dishes.items():
            print(dish.ljust(WIDTH - 4), 'x' + str(quantity))
            str2 += (dish.ljust(WIDTH - 3) + 'x' + str(quantity) + '\n')

        str3 = str(dedent(f'''
            {'*' * WIDTH}
            {'Subtotal:'.ljust(WIDTH - 6) + '$' + str('{0:.2f}'.format(self.subtotal))}
            {'Tax:'.ljust(WIDTH - 6) + '$' + str('{0:.2f}'.format(self.tax))}
            {'Total:'.ljust(WIDTH - 6) + '$' + str('{0:.2f}'.format(self.total))}
            {'*' * WIDTH}
            {'*' * WIDTH}
        '''))
        print(str3)

        return (str1 + str2 + str3)

    def print_receipt(self):
    #     """ Creates a file containing the text of the user’s full order
    #     """
        # order = str(self.display_order())
        with open(f'{self.id}.txt', 'w') as f:
            f.write(str(self.display_order()))
        print('The receipt has been printed as well')

    def __repr__(self):
        return f'<Order: {self.id}, | Items: {len(self.dishes)} | Total: {self.total}>'

    def __len__(self):
        return len(self.dishes.keys)

    def __str__(self):
        return f'Name: {self.first_name}, ID: {self.emp_id}'
