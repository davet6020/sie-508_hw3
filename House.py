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
        print("Number of stories: {}".format(self.num_stories))
        print("Has Garage: {}".format(self.garage))
        print("Has Fenced in yard: {}".format(self.fenced_yard))

    def display(self):
        pass
