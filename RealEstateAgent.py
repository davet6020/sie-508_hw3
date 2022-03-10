class RealEstateAgent:
    agents = []

    def __init__(self, name, properties):
        self.__name = name
        self.properties = properties

    def listproperties(self):
        print("Realtor: {}".format(self.properties.name))
        print("Property: {}".format(self.properties.address))
