file = open("day1input.txt","r")
readme = file.read().splitlines()

# VARIABLE
days = 0

# PROCESSING
for line in readme:
    # convert strings to ints and then add!
    days += int(line)

# HAPPY HOLIDAY RESULTS
print("The resulting frequency is {}".format(days))
