from chapter3_case_study.HouseRental import HousePurchase, AppartmentRental, AppartmentPurchase, HouseRental
from chapter3_case_study.helper_functions import get_valid_input


class Agent:
    def __init__(self):
        self.property_list = []
        self.type_map = {
            ("house","rental"): HouseRental,
            ("house","purchase"): HousePurchase,
            ("appartment","rental"): AppartmentRental,
            ("appartment","purchase"): AppartmentPurchase
        }

    def add_property(self):
        property_type = get_valid_input("What type of property? ",
                                        ("house","appartment")).lower()
        payment_type = get_valid_input("What payment type? ",
                                       ("purchase","rental")).lower()

        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def display_properties(self):
        for property in self.property_list:
            property.display()