file = open("day2input.txt","r")
readme = file.read().splitlines()

# function mydif() by Marco Sulla on Stack Overflow
# https://stackoverflow.com/questions/25216328/compare-strings-allowing-one-character-difference

def mydif(a, b):
    pos = -1
    for i, (c1,c2) in enumerate(zip(a,b)):
        if c1 != c2:
            if pos != -1:
                return -1
            else:
                pos = i
    return pos

x = 0
y = 1
exit = False
while x < len(readme):
    # outer loop is the first value we compare to the rest of the list
    while y < len(readme):
        # inner loop compares readme[x] to readme[y:]
        check_dif = mydif(readme[x],readme[y])
        if check_dif != -1:
            # we have a match!
            exit = True
            mystr = readme[x]
            break
        else:
            y += 1
            continue # increment through the list still comparing to x
    if exit : break
    x += 1
    y = x + 1
print("Final answer is: {}".format((mystr[:check_dif] + mystr[check_dif+1:])))
