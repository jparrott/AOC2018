file = open("day2input.txt","r")
readme = file.read().splitlines()

counter2 = counter3 = dup2 = dup3 = 0

for line in readme:
    unique_vals = "".join(set(line))
    for char in unique_vals:
        if line.count(char) == 2:
            counter2 += 1
            dup2 += 1
        if line.count(char) == 3:
            counter3 += 1
            dup3 += 1
    if dup2 > 1:
        counter2 -= (dup2 - 1)
    if dup3 > 1:
        counter3 -= (dup3-1)
    dup2 = dup3 = 0

print(counter2, counter3, counter2*counter3)
