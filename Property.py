class Property:

    def __init__(self, square_feet, num_bedrooms, num_bathrooms, rent, address):
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.rent = rent
        self.address = address

    def initializeproperty(self):
        print("Address: {}".format(self.address))
        print("Square Footage: {}".format(self.square_feet))
        print("Number of Bedrooms: {}".format(self.num_bedrooms))
        print("Number of Bathrooms: {}".format(self.num_bathrooms))
        print("Rent: {}".format(self.rent))

    def display(self):
        pass
