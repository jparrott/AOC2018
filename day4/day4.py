from datetime import datetime as d
from collections import deque as dq
from collections import Counter as c

class Guard:
    '''It's so boring to guard the lab by yourself...'''
    
    def __init__(self, name):
        self.name = name
        self.mins_asleep = []

    def __str__(self):
        return self.name, self.mins_asleep

    def total_sleep(self):
        '''Returns num of mins slept by calling len(mins_asleep)'''
        total_zzz = len(self.mins_asleep)
        return total_zzz

    def common_min(self):
        '''Returns a dictionary with the guard name, minute most often mins_asleep
        and how many times they were caught asleep at that minute'''
        sleepiest_min = c(self.mins_asleep).most_common(1)
        return {"Guard": self.name, "Minute": sleepiest_min[0][0], "Times": sleepiest_min[0][1]}

file = open("day4input.txt","r")
readme = file.read().splitlines() #list

nap_king = dq()
    # A deque keeping track of... something
guard_roster = {}
    # Encountered guards. Key: Guard's name, Value: Guard obj
guard_log = {}
    # Log of sleep/wake times. Key: datetime obj, Value: text
common_naptime = dq()

for line in readme:
    parse = line.replace("[","").split("] ")
    guard_log[d.strptime(parse[0], "%Y-%m-%d %H:%M")] = parse[1]

for k in sorted(guard_log):
    # Using sorted() puts each entry in chronological order

    if "Guard" in guard_log[k]:
        name = guard_log[k][:-13]
        if name not in guard_roster.keys():
            guard_roster[name] = Guard(name)
        active = name
            # active tells us which Guard to update
    elif "asleep" in guard_log[k]:
        snooze = k
    elif "wakes" in guard_log[k]:
        wakeup = k
        guard_roster[active].mins_asleep.extend(list(range(snooze.minute,wakeup.minute)))
            # guard_roster[active] selects the Guard obj
            # mins_asleep accesses that Guard's list of mins they've slept
            # extend(list(rangge())) adds the mins slept from this last cycle

for g in guard_roster:
    heir = guard_roster[g].total_sleep()
        # How long has each guard slept?
    if heir < 1:
        # If a guard never slept, we don't care about them
        continue
    sleepy_min = c(guard_roster[g].mins_asleep).most_common()[0]
        # find the minute the guard was asleep the most
    nap_king.append((heir, sleepy_min, guard_roster[g].name))
        # tuple contains num of mins asleep, the minute asleep most often, and name
    common_naptime.append((guard_roster[g].common_min()))
        # appends a dictionary with guard name, minute asleep most often, and num occurrences

winner = sorted(nap_king)[-1]

# Answer: 102688
print(f"{winner[2]} is the sleepiest guard and often falls asleep at minute {winner[1][0]}. Your answer is {int(winner[2][7:])*winner[1][0]}.")

winner2 = [elem for elem in common_naptime if elem["Times"] == max([x["Times"] for x in common_naptime])]
    # list comprehension... dun dun dun
    # for each dict in common_naptime, check to see if the number of
    # times asleep at the most common point is the highest, and if so
    # that's our second winner

# Answer: 56901
print("{} is the most consistent guard, falling asleep {} times at minute {}. Your answer is {}".format(winner2[0]["Guard"],winner2[0]["Times"],winner2[0]["Minute"],int(winner2[0]["Guard"][7:])*int(winner2[0]["Minute"])))
