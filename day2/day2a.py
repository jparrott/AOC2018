file = open("day2input.txt","r")
readme = file.read().splitlines()
#readme = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
counter2 = counter3 = dup2 = dup3 = 0
#counter3 = 0
#dup2 = 0
#dup3 = 0
# counter = 0

for line in readme:
    unique_vals = "".join(set(line))
    #print(line, unique_vals, "dup2 {} : dup3 {} : counter2 {} : counter3 {}".format(dup2,dup3,counter2,counter3))
    for char in unique_vals:
        #print(char, line.count(char))
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
    #print("dup2 {} : dup3 {} : counter2 {} : counter3 {}".format(dup2,dup3,counter2,counter3))
    dup2 = dup3 = 0
    # counter += 1
    # if counter > 10:
    #     break

print(counter2, counter3, counter2*counter3)
