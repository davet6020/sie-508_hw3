class RealEstateAgent:
    agents = ['Jewel', 'Tom']
    pr = {}
    property_list = {}

    def __init__(self):
        self.agent = None
        self.propertiid = None
        self.address = None
        self.property_type = None
        self.rent = None
        self.none = None

    def listproperties(self):
        self.none = None
        print("Agent -\tRent -\tProperty Type -\tAddress")
        for pid, pinfo in RealEstateAgent.property_list.items():
            print("{: >10} {: >6} {: >15} {: >30}".format(pinfo['agent'], pinfo['rent'], pinfo['property_type'],
                                                          pinfo['address']))

    def addproperty(self, agent, propertiid,  address, property_type, rent):
        self.agent = agent
        self.propertiid = propertiid
        self.address = address
        self.property_type = property_type
        self.rent = rent

        RealEstateAgent.pr = {'agent': self.agent, 'address': self.address,
                              'property_type': self.property_type, 'rent': self.rent}
        RealEstateAgent.property_list[self.propertiid] = RealEstateAgent.pr
