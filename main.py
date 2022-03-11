from RealEstateAgent import RealEstateAgent
from Property import Property
from House import House
from Apartment import Apartment
import random

mls = {}
property_count = 0

agent1 = RealEstateAgent()
agent2 = RealEstateAgent()

print("Input Three Properties")
while property_count < 3:
    p = Property()

    for attr, value in p.__dict__.items():
        if attr == 'address':
            mls['address'] = value
        if attr == 'rent':
            mls['rent'] = value

    AorH = input("Is this an Apartment or a House (A or H): ")
    if AorH.upper() == "A":
        a = Apartment()
        mls['property_type'] = 'Apartment'
    else:
        h = House()
        mls['property_type'] = 'House'

    # Time to assign property to realtor
    agent1.addproperty(random.choice(RealEstateAgent.agents), property_count, mls['address'], mls['property_type'], mls['rent'])

    property_count += 1


# agent1.addproperty('Jewel', 'Apartment 1', 1)
# agent2.addproperty('Tom', 'House 2', 2)
print("===============================")
agent1.listproperties()
print("===============================")
agent2.listproperties()
