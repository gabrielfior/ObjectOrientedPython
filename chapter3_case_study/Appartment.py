from chapter3_case_study.Property import Property
from chapter3_case_study.helper_functions import get_valid_input


class Appartment(Property):

    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony = '', laundry = '', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APPARTMENT DETAILS")
        print("================")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property have? ", Appartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony? ", Appartment.valid_balconies)

        parent_init.update({
            "laundry" : laundry,
            "balcony" : balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


