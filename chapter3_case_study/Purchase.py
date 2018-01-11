from chapter3_case_study.helper_functions import get_valid_input


class Purchase:
    def __init__(self, price = '', taxes = '', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("================")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init(self):
        return dict(
            price = input("What is the selling price? "),
            taxes = input("What are the estimated taxes? ")
        )
    prompt_init = staticmethod(prompt_init)

class Rental:
    def __init__(self, furnished='', utilities='', rent = '', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print("RENT DETAILS")
        print("================")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(
            rent = input("What is the monthly rent? "),
            utilities = input("What are the estimated utilities? "),
            furnished = get_valid_input("Is the property furnished? ",("yes","no")))
    prompt_init = staticmethod(prompt_init)


