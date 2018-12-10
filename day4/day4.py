from datetime import datetime as d

class Guard:

    def __init__(self, name):
        self.name = name

    def __str__():
        return self.name

    def sleep(self, entry):
        self.asleep = entry

    def awake(self, entry):
        self.woke = entry

    def zzz(self):
        return self.woke-self.asleep

file = open("day4example.txt","r")
readme = file.read().splitlines() #list
text = "[1518-11-01 00:00] Guard #10 begins shift"
# value[:-13] for guard name
guard_log = {}

for line in readme:
    parse = line.replace("[","").split("] ")
    guard_log[d.strptime(parse[0], "%Y-%m-%d %H:%M")] = parse[1]

guard_roster = {}
n = "1"
for k in sorted(guard_log):
    #print("{} ---> {}".format(k,guard_log[k]))



    if "Guard" in guard_log[k]:
        grdname = guard_log[k][:-13]
        if grdname not in guard_roster.keys():
            guard_roster[grdname] = Guard(grdname)
            print("Guard object's name is {}".format(guard_roster[grdname].name))
            n = grdname
            continue
    elif "asleep" in guard_log[k]:
        guard_roster[n].sleep(k)
        print("{} fell asleep at {}".format(guard_roster[n].name, guard_roster[n].asleep))
    elif "wakes" in guard_log[k]:
        guard_roster[n].awake(k)
        total = guard_roster[n].zzz()
        print("{} woke up at {} for a total of {} asleep".format(guard_roster[n].name, guard_roster[n].woke, total))

    #     if guard_log[k][:-13] not in guard_roster.keys():
    #         guard = Guard(guard_log[k][:-13])
    #         guard_roster[guard] = ""
    #     else:
    #         guard = next
    #         if "asleep" in guard_log[k]:
    #             guard.sleep(k)
    #         if "wakes" in guard_log[k]:
    #             guard.awake(k)


#for line in readme:
    # Convert the time in brackets to a datetime object
    # Assign datetime obj as the key in a dictionary with the rest of the str as the value
