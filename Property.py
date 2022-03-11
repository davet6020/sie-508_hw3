class Property:

    # def __init__(self, square_feet, num_bedrooms, num_bathrooms, rent, address):
    def __init__(self):
        self.square_feet = None
        self.num_bedrooms = None
        self.num_bathrooms = None
        self.rent = None
        self.address = None
        self.initializeproperty()

    def initializeproperty(self):
        self.address = input("Enter address (street and number, city, state, zip): ")
        self.square_feet = int(input("Enter square feet: "))
        self.num_bedrooms = int(input("Enter number of bedrooms: "))
        self.num_bathrooms = int(input("Enter number of bathrooms: "))
        self.rent = int(input("Enter rent amount per month: "))

    def display(self):
        print("Address: {}".format(self.address))
        print("Square Footage: {}".format(self.square_feet))
        print("Number of Bedrooms: {}".format(self.num_bedrooms))
        print("Number of Bathrooms: {}".format(self.num_bathrooms))
        print("Rent: {}".format(self.rent))
