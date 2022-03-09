from Property import Property


class House(Property):

    def __init__(self, superproperty, num_stories, garage, fenced_yard):
        self.num_stories = num_stories
        self.garage = garage
        self.fenced_yard = fenced_yard
        self.square_feet = superproperty.square_feet
        self.num_bedrooms = superproperty.num_bedrooms
        self.num_bathrooms = superproperty.num_bathrooms
        self.rent = superproperty.rent
        self.address = superproperty.address

    def initializeproperty(self):
        print("House.initializeproperty")

    def display(self):
        pass
