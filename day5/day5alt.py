import re
file = open("day5input.txt","r")
poly = file.read()


def match(text):
    pattern1 = "[a-z][A-Z]"
    pattern2 = "[A-Z][a-z]"
    if re.search(pattern1,text):
        return True
    elif re.search(pattern2,text):
        return True
    else:
        return False


#print(f"Before: {poly}")

while True:
    start_len = len(poly)
    for i in range(0, start_len):
        pair = poly[i:i+2]
        if pair == '':
            break
        #print(f"Checking --> {pair} in {poly}")
        if match(pair):
            same = pair.upper()
            if same[0] == same[1]:
                poly = poly.replace(pair, "", 1)
                break
                #print(f"New string: {poly}")
    if len(poly) < start_len:
        print(len(poly)/1000)
        continue
    else:
        break

#     for pair in check:
#         if not case(pair):
#             quit = True
#         else:
#             break
# if quit:
#     break

print(f"Length: {len(poly)}")
