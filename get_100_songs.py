import random

class Song:
    def __init__(self, title, artist, weight):
        self.title = title
        self.artist = artist
        self.weight = weight
        self.used = False

NUMSONGS = 100
songs = []
songs100 = []

# this takes a weight and returns index of song selected
def returnIndex(w):  # w = weight of picked song   
    sum = 0
    i = 0
    found = False
    while not found:
        sum += songs[i].weight
        if sum >= w:
            found = True
        else:
            i += 1
    return i

totalWeight = 0
with open("songs.tsv") as f:
    for line in f:
        if(line.strip(' \n') != ""):
            sss = line.split("\t")
            t = sss[0].strip()     # title
            a = sss[1].strip()     # artist
            w = int(sss[2].strip())   # weight
            totalWeight += w
            s = Song(t, a, w)          # song
            songs.append(s)

iterationCounter = 0

counter = NUMSONGS
while counter > 0:
    weightNum = random.randint(1,totalWeight)
    iterationCounter += 1
    # call function that returns index of selected song
    i = returnIndex(weightNum)   # i is index of song
    totalWeight -= songs[i].weight
    songs[i].used = True
    songs[i].weight = 0
    songs100.append(songs[i])
    counter -= 1

print("\niterations:",iterationCounter)
print("total weight:",totalWeight,"\n")

j = open("newfile.csv","w")

for x in songs100:
    j.write(x.title)
    j.write(";")
    j.write(x.artist)
    j.write("\n")

j.close()


lonelySong = songs[0]
# write to external file
k = open("songs.tsv","w")
for y in songs:
    k.write(y.title)
    k.write("\t")
    k.write(y.artist)
    k.write("\t")
    if y.used == False:
        y.weight += 1
    k.write(str(y.weight))
    k.write("\n")

    if(y.weight > lonelySong.weight):
        lonelySong = y

print("\nThe song that has been unused the longest is",lonelySong.title,"by",lonelySong.artist)
print("It has gone",lonelySong.weight,"times without being picked.","\n")

k.close()

# 2235 songs
# 2280