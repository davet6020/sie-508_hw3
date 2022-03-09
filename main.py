from RealEstateAgent import RealEstateAgent
from Property import Property
from House import House
from Apartment import Apartment


tom = RealEstateAgent('Tom', 1)
p = Property(2000, 3, 2, 1900, "1000 Bienville St, New Orleans, LA 70112")
p.initializeproperty()
h = House(p, 2, 5, "No")
h.initializeproperty()
print(h.num_stories)
print(h.square_feet)
a = Apartment(p, 3, "Yes")
a.initializeproperty()
print(a.square_feet)
print(a.balcony)

"""
Need to prompt for input
"""

