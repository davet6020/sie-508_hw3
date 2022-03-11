from RealEstateAgent import RealEstateAgent
from Property import Property
from House import House
from Apartment import Apartment

property_count = 1
pnum = 1
pnam = "p"
rnam = "r"

agent1 = RealEstateAgent()
agent2 = RealEstateAgent()

print("Input Three Properties")
while property_count < 4:
    propx = {pnum: pnam+str(pnum)}
    realx = {pnum: rnam+str(pnum)}

    propx[pnum] = Property()

    AorH = input("Is this an Apartment or a House (A or H): ")
    if AorH.upper() == "A":
        a = Apartment()
    else:
        h = House()

    property_count += 1
    pnum += 1

# Time to assign property to realtor

agent1.addproperty('Jewel', 'House 1', 0)
agent1.addproperty('Jewel', 'Apartment 1', 1)
agent2.addproperty('Tom', 'House 2', 2)
agent2.listproperties()
