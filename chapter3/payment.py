from .properties import get_valid_input


class Purchase:

    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super.display()
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    @staticmethod
    def prompt_init():
        return dict(price=input('What is the Selling price?: '),
                    taxes=input('Estimated taxes?: '))


class Rental:

    def __init__(self, rent='', furnished='', utilities='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))
        print()

    @staticmethod
    def prompt_init():
        return dict(rent=input("What is the monthly rent?: "),
                    utilities=input("Expected monthly utilities?: "),
                    furnished=get_valid_input(
                        "Is the house furnished?: ", ("yes", "no")
                    ))
