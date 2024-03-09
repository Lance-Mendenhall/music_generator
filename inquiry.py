# sort by times played
# be able to tell how many songs are with each "times played," and display the songs

class Song:
    def __init__(self, title, artist, weight, times_played):
        self.title = title
        self.artist = artist
        self.weight = weight
        self.times_played = times_played

songs = []

with open("songs.tsv") as f:
    for line in f:
        if(line.strip(' \n') != ""):
            sss = line.split("\t")
            t = sss[0].strip()     # title
            a = sss[1].strip()     # artist
            w = int(sss[2].strip())  # weight
            tp = int(sss[3].strip())   # times played
            s = Song(t, a, w, tp)          # song
            songs.append(s)

def list_tp_to_songs():
    choice = int(input("\nEnter the times played:\n"))
    print()
    counter = 0
    for s in songs:
        if s.times_played == choice:
            counter += 1
            print(s.title,"\t",s.artist)
    print(f"\n{counter} songs that have been played {choice} times.\n")

def weight_to_songs():
    choice = int(input("\nEnter the desired weight:\n"))
    print()
    for s in songs:
        if s.weight == choice:
            print(s.title,"\t",s.artist)
    print()

def weight_to_num_songs():
    choice = int(input("\nEnter the desired weight:\n"))
    counter = 0
    for s in songs:
        if s.weight == choice:
            counter += 1
    print("There are",counter,"songs with that weight.")
    print()

tp_num_dict = {}
tp_songs_dict = {}
weight_numsongs = {}

# num plays - num songs distribution   
# key: tp   value: how many songs have been played that many times. 
for s in songs:
    key = s.times_played
    if key in tp_num_dict.keys():
        tp_num_dict[key] += 1
    else:
       tp_num_dict[key] = 1 

# now create 2 D list to sort 

tp_num_list = []
for k in tp_num_dict:
    tp_num_list.append([k,tp_num_dict[k]])

tp_num_list.sort()

# tp_num_list has times played as keys, and num of songs played that many times as value

for s in songs:
    key = s.weight
    if key in weight_numsongs.keys():
        weight_numsongs[key] += 1
    else:
       weight_numsongs[key] = 1 

weight_num_list = []
for k in weight_numsongs:
    weight_num_list.append([k,weight_numsongs[k]])

weight_num_list.sort()

def weight_num_dist():
    print("weight  num of songs")
    for e in weight_num_list:
        print("  ",e[0],"\t",e[1])

def tp_num_dist():
    print("times played  num of songs")
    for e in tp_num_list:
        print("  ",e[0],"\t\t",e[1])

not_done = True

while not_done:
    print("\nEnter a selection. You can:\n")
    print("1) Display weight/num songs distribution")
    print("2) Display num plays/num songs distribution")
    print("3) List songs that have been played a certain number of times")
    print("4) List all songs with a certain weight")
    print("5) Tell how many songs have a certain weight")
    print("9) Quit\n")

    choice = input("What do you want to do?\n")

    if choice[0] == "1":
        weight_num_dist()
    elif choice[0] == "2":
        tp_num_dist()
    elif choice[0] == "3":
        list_tp_to_songs()
    elif choice[0] == "4":
        weight_to_songs()
    elif choice[0] == "5":
        weight_to_num_songs()

    elif choice[0] == "9" or choice[0] == "q" or choice[0] == "Q":
        not_done = False
    else:
        print("Daylight come and me wanna go home...")