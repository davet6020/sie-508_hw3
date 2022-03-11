from RealEstateAgent import RealEstateAgent
from Property import Property
from House import House
from Apartment import Apartment
import random

mls = {}
property_count = 0

# Instantiate two realtor obj
agent1 = RealEstateAgent()
agent2 = RealEstateAgent()

# Have user input 3 properties
print("Input Three Properties")
while property_count < 3:
    # By instantiating a Property object, you call Property.initializeproperty which asks for input
    p = Property()

    # Loop through p items() and put them into a dictionary for use in assigning the property to a realtor
    for attr, value in p.__dict__.items():
        if attr == 'address':
            mls['address'] = value
        if attr == 'rent':
            mls['rent'] = value

    # Determine if Apartment or House and call that Class.initializeproperty method
    AorH = input("Is this an Apartment or a House (A or H): ")
    if AorH.upper() == "A":
        a = Apartment()
        # We need the property type for assigning it to the realtor
        mls['property_type'] = 'Apartment'
    else:
        h = House()
        # We need the property type for assigning it to the realtor
        mls['property_type'] = 'House'

    # Time to assign property to realtor
    agent1.addproperty(random.choice(RealEstateAgent.agents), property_count, mls['address'], mls['property_type'],
                       mls['rent'])

    # Increment for next property
    property_count += 1

# Print out a list of all agents properties
agent2.listproperties()
