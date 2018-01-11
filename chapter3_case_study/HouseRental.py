from chapter3_case_study.Appartment import Appartment
from chapter3_case_study.House import House
from chapter3_case_study.Purchase import Rental, Purchase


class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class AppartmentRental(Rental, Appartment):
    def prompt_init():
        init = Appartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class AppartmentPurchase(Purchase, Appartment):
    def prompt_init():
        init = Purchase.prompt_init()
        init.update(Appartment.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)
