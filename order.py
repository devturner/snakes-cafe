from uuid import uuid4
from textwrap import dedent
WIDTH = 48


class Order:
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


    def _update_totals(self, tax, subtotal, total):
        """Set the objects totals for tax, subtotal, and total price
        """
        self.tax = tax
        self.subtotal = subtotal
        self.total = total
        return self


    def display_order(self):
        """ Prints the order out to the screen so it can be reviewed
        """
        print(dedent(f'''
            {'~' * WIDTH}
            {'~' * WIDTH}
            The Snakes Cafe
                "Eatability Counts"
            {'~' * WIDTH}
            {'Order: ' + str(uuid4())}
            {'~' * WIDTH}
        '''))
        for dish, quantity in self.dishes.items():
            print(dish, 'x' + str(quantity))

        print(dedent(f'''
            {'~' * WIDTH}
            {'Subtotal: $' + str(self.subtotal)}
            {'Tax: $' + str(self.tax)}
            {'Total: $' + str(self.total)}
            {'~' * WIDTH}
        '''))


    # def print_receipt():
    #     """ Creates a file containing the text of the user’s full order
    #     """
    #     pass




# <Order #ba99d8... | Items: 4 | Total: $754.23>
    def __repr__(self):
        return f'<Order: {self.id}, | Items: {len(self.dishes)} | Total: {self.total}>'

    def __str__(self):
        pass


    # def __str__(self):
    #     return f'Name: {self.first_name}, ID: {self.emp_id}'
