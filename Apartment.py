from Property import Property


class Apartment(Property):

    def __init__(self, superproperty, balcony, laundry):
        self.balcony = balcony
        self.laundry = laundry
        self.square_feet = superproperty.square_feet
        self.num_bedrooms = superproperty.num_bedrooms
        self.num_bathrooms = superproperty.num_bathrooms
        self.rent = superproperty.rent
        self.address = superproperty.address

    def initializeproperty(self):
        print("Has Balcony: {}".format(self.balcony))
        print("Has Laundry: {}".format(self.laundry))

    def display(self):
        pass
