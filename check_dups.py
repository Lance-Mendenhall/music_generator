
# check for title dup, but preserve artist


print()

# title_set = set()

# with open("songs.tsv") as f:
# 	for line in f:
# 		line = line.strip()
# 		if line != "":
#             # print(line)
# 			sss = line.split("\t")
# 			t = sss[0].strip().lower()     # title
# 			a = sss[1].strip()     # artist
# 			w = int(sss[2].strip())   # weight
# 			tp = int(sss[3].strip())   # times played
            
# 			if t in title_set:
# 				print("dup:",t,"\t",a)
# 			else:
# 				title_set.add(t)

mydict = {}

with open("songs.tsv") as f:
	for line in f:
		line = line.strip()
		if line != "":
            # print(line)
			sss = line.split("\t")
			t = sss[0].strip().lower()     # title
			a = sss[1].strip()    # artist

			if t in mydict.keys():
				print(t,'  ',a,'  ',mydict[t])
			else:
				mydict[t] = a
            


