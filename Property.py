class Property:

    def __init__(self, square_feet, num_bedrooms, num_bathrooms, rent, address):
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.rent = rent
        self.address = address

    def initializeproperty(self):
        print("Property.initializeproperty")

    def display(self):
        pass
