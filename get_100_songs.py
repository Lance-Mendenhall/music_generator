import random
from datetime import date

class Song:
    def __init__(self, title, artist, weight, times_played):
        self.title = title
        self.artist = artist
        self.weight = weight
        self.times_played = times_played

MAX_WEIGHT = 50
BURIED_WEIGHT = -10
NUMSONGS = 100
songs = []
songs100 = []
totalWeight = 0

num = 0
with open("number.txt") as f:
    num = f.read()

num = int(num)
num += 1
num = str(num)

q = open("number.txt","w")
q.write(num)
q.close()

# this takes a weight and returns index of song selected
def returnIndex(w):  # w = weight of picked song   
    sum = 0
    i = 0
    found = False
    while not found:
        if songs[i].weight > 0:    
            sum += songs[i].weight
        if sum >= w:
            found = True
        else:
            i += 1
    return i


def getAverageWeight(mylist):
    w = 0
    num = 0
    for x in mylist:
        if x.weight > 0:
            num += 1
            w += x.weight
    return w/num

with open("songs.tsv") as f:
    for line in f:
        line = line.strip()
        if line != "":
            # print(line)
            sss = line.split("\t")
            t = sss[0].strip()     # title
            a = sss[1].strip()     # artist
            w = int(sss[2].strip())   # weight
            tp = int(sss[3].strip())   # times played
            if w > 0:
                totalWeight += w
            s = Song(t, a, w, tp)          # song
            songs.append(s)

print()
totalSongs = len(songs)
iterationCounter = 0
counter = NUMSONGS

# BURIED_WEIGHT = (int(totalSongs / NUMSONGS / 3) + 1) * -1

def pick_song(s):
    global totalWeight, counter, iterationCounter
    totalWeight -= s.weight
    s.weight = BURIED_WEIGHT                        
    s.times_played += 1
    songs100.append(s)
    counter -= 1
    iterationCounter += 1

for x in songs:
    if x.weight >= MAX_WEIGHT:
        print("max weight song:\t",x.title,"\t",x.artist)
        pick_song(x)

print("\nUsed",iterationCounter,"songs with max weight.")

while counter > 0:
    weightNum = random.randint(1,totalWeight)
    # call function that returns index of selected song
    i = returnIndex(weightNum)   # i is index of song

    pick_song(songs[i])

print("iterations:",iterationCounter)
print()
random.shuffle(songs100)

path = "../archive/classic_rock/CR_0" + num + ".csv"

j = open(path,"w")


print("songs playing for first time")
print()
for x in songs100:
    j.write(x.title + ";" + x.artist + "\n")
    if x.times_played == 1:
        print(x.title,"\t",x.artist)
j.close()

# shift the list 
# for _ in range(1):
z = songs.pop()
songs.insert(0,z)

average_weight = getAverageWeight(songs)

counter = 0
# write to external file
k = open("songs.tsv","w")
for y in songs:
    y.weight += 1
    k.write(y.title + "\t" + y.artist + "\t" + str(y.weight) + "\t" + str(y.times_played) + "\n")
k.close()

# keeping records

q = open("stats.txt","a")

today = date.today()
dd = today.strftime("%B %d, %Y")

q.write(dd)
q.write("\n\n")

q.write("playlist number:" + "\t" + str(num) + "\n")
q.write("total songs:" + "\t" + str(totalSongs) + "\n")
q.write("total weight:" + "\t" + str(totalWeight) + "\n")
q.write("average weight (includes only songs with positive weight):" + "\t" + str(average_weight) + "\n")

q.write("\n\n")
q.close()
