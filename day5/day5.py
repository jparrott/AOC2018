from collections import deque as deck

#poly = "dabAcCaCBAcCcaDA"
file = open("day5input.txt","r")
poly = file.read().rstrip()

def liketype(unit1, unit2):
    return unit1.upper() == unit2.upper()

def polarity(unit1, unit2):
    return unit1.isupper() and unit2.islower() or unit1.islower() and unit2.isupper()

new_poly = deck()

for unit in poly:
    if len(new_poly) > 0 and liketype(unit,new_poly[-1]) and polarity(unit, new_poly[-1]):
        new_poly.pop()
    else:
        new_poly.append(unit)

print(f"Fully reacted polymer length is : {len(new_poly)}")

# # START PART B # #

short_poly = deck()
poly_dict = {}
unique_units = set(poly)

for x in unique_units:
    replacement = poly.replace(x,"").replace(x.swapcase(),"")
    for unit in replacement:
        if len(short_poly) > 0 and liketype(unit,short_poly[-1]) and polarity(unit, short_poly[-1]):
            short_poly.pop()
        else:
            short_poly.append(unit)
    poly_dict[x] = len(short_poly)
    short_poly.clear() # this step is important...

for key, val in poly_dict.items():
    if val == min(poly_dict.values()):
        print(f"Remove {key}/{key.swapcase()} and the fully reacted polymer length is : {val}")
        break
