class Property:
    def __init__(self, square_feet = '', beds = '', baths = '', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("Square footage: {}".format(self.square_feet))
        print("Bedrooms: {}".format(self.num_bedrooms))
        print("Bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    beds = input("Enter the number of bedrooms: "),
                    baths = input("Enter the number of bathrooms: ")
                    )

    prompt_init = staticmethod(prompt_init)