class RealEstateAgent:
    agents = ['Jewel', 'Tom']
    property_list = []

    def __init__(self):
        self.properti = None
        self.properti_number = None
        self.agent = None

    def listproperties(self):
        for p in RealEstateAgent.property_list:
            print("Realtor: {}".format(p))
            print("Property: {}".format(self.properti))

    def addproperty(self, agent, properti):
        i = 0
        self.agent = agent
        self.properti = properti
        RealEstateAgent.property_list.append(agent)
        pr = {i: self.properti}
        RealEstateAgent.property_list.appe
        # RealEstateAgent.property_list[agent][i][properti] = self.properti
        # print(RealEstateAgent.property_list['Jewel'])

        RealEstateAgent.property_list['agent'].append(self.properti)
        # print(RealEstateAgent.property_list[0])
