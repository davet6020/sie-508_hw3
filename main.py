from RealEstateAgent import RealEstateAgent
from Property import Property
from House import House
from Apartment import Apartment

property_count = 1
pnum = 1
pnam = "p"
rnam = "r"

print("Enter two realtors")
r1_name = input("Enter the name for realtor one: ")
r2_name = input("Enter the name for realtor two: ")

print("Input Three Properties")
while property_count < 4:
    propx = {pnum: pnam+str(pnum)}
    realx = {pnum: rnam+str(pnum)}
    print(propx[pnum])
    print(realx[pnum])
    pnum += 1

    address = input("Enter address (street and number, city, state, zip): ")
    input_square_feet = input("Enter square feet: ")
    square_feet = int(input_square_feet)
    input_num_bedrooms = input("Enter number of bedrooms: ")
    num_bedrooms = int(input_num_bedrooms)
    input_num_bathrooms = input("Enter number of bathrooms: ")
    num_bathrooms = int(input_num_bathrooms)
    input_rent = input("Enter rent amount per month: ")
    rent = int(input_rent)

    propx[pnum] = Property(square_feet, num_bedrooms, num_bathrooms, rent, address)
    propx[pnum].initializeproperty()

    AorH = input("Is this an Apartment or a House (A or H): ")
    if AorH.upper() == "A":
        balcony = input("Does this apartment have a balcony: ")
        laundry = input("Does this apartment have a laundry facility: ")
        if balcony.upper() == "N" or int(balcony == 0):
            balcony = "No"
        else:
            balcony = "Yes"

        if laundry.upper() == "N" or int(laundry == 0):
            laundry = "No"
        else:
            laundry = "Yes"

        a = Apartment(propx[pnum], balcony, laundry)
        a.initializeproperty()
    else:
        input_num_stories = input("How many stories is this house: ")
        num_stories = int(input_num_stories)

        garage = input("Does this house have a garage: ")
        fenced_yard = input("Does this house have a fenced yard: ")

        if garage.upper() == "N" or int(garage == 0):
            garage = "No"
        else:
            garage = "Yes"

        if fenced_yard.upper() == "N" or int(fenced_yard == 0):
            fenced_yard = "No"
        else:
            fenced_yard = "Yes"

        h = House(propx[pnum], num_stories, garage, fenced_yard)
        h.initializeproperty()

    property_count += 1

    realx[pnum] = RealEstateAgent(r1_name, propx[pnum])
    realx[pnum].listproperties()
