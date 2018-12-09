file = open("day1input.txt","r")
readme = file.read().splitlines()

# VARIABLES
findme = days = 0
freq = set()

# PROCESSING
while True:
    for line in readme:
        days += int(line)
        # freq is a set and as such will only have unique values
        # if we find days in freq we need to break out of our loops
        if days in freq:
            findme = days
            break
        else:
            # we didn't find a duplicate so we add the current day and continue
            freq.add(days)
    if findme == 0:
        continue
    else:
        break

# HAPPY HOLIDAY RESULTS
print("The first frequency the device reaches twice is {}.".format(findme))
