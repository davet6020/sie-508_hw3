from RealEstateAgent import RealEstateAgent
from Property import Property
from House import House
from Apartment import Apartment

property_count = 1
pnum = 1
pnam = "p"
rnam = "r"

# print("Input Three Properties")
# while property_count < 4:
#     propx = {pnum: pnam+str(pnum)}
#     realx = {pnum: rnam+str(pnum)}
#
#     propx[pnum] = Property()
#
#     AorH = input("Is this an Apartment or a House (A or H): ")
#     if AorH.upper() == "A":
#         a = Apartment()
#     else:
#         h = House()
#
#     property_count += 1
#     pnum += 1


# Time to assign property to realtor
r = RealEstateAgent()
r.addproperty('Jewel', 'House 1')
r.addproperty('Jewel', 'Apartment 1')
r.addproperty('Tom', 'House 2')
r.listproperties()
# realx[pnum] = RealEstateAgent(r1_name, propx[pnum])
# realx[pnum].listproperties()


