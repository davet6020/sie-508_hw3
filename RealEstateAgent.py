class RealEstateAgent:
    agents = ['Jewel', 'Tom']
    property_list = []

    def __init__(self):
        self.properti = None
        self.properti_number = None
        self.agent = None

    def listproperties(self):
        for a in RealEstateAgent.agents:
            print("Realtor: {}".format(a))
            print("Property: {}".format(self.properti))

    def addproperty(self, agent, properti):
        i = 0
        self.agent = agent
        self.properti = properti
        RealEstateAgent.property_list['Jewel'][i][properti] = self.properti
        print(RealEstateAgent.property_list['Jewel'])

