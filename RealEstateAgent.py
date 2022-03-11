class RealEstateAgent:
    agents = ['Jewel', 'Tom']
    pr = {}
    property_list = {}

    def __init__(self):
        self.properti = None
        self.propertiid = None
        self.agent = None
        self.none = None

    def listproperties(self):
        self.none = None
        for p_id, p_info in RealEstateAgent.property_list.items():
            print('Agent: {} --- Property: {}'.format(p_info['agent'], p_info['properti']))

    def addproperty(self, agent, properti, propertiid):
        self.agent = agent
        self.properti = properti
        self.propertiid = propertiid

        RealEstateAgent.pr = {'agent': self.agent, 'properti': self.properti}
        RealEstateAgent.property_list[self.propertiid] = RealEstateAgent.pr
