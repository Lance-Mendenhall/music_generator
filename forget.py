
linenumber = 1
noerrors = True

with open("songs.tsv") as f:
	for line in f:	
		line = line.strip()
		if(line != ""):
			sss = line.split("\t")

			if len(sss[2]) > 0 and sss[2][0] == "-":
				sss[2] = sss[2][1:]

			if len(sss) != 4 or (not sss[2].strip().isnumeric()) or (not sss[3].strip().isnumeric()):
				print("\nError on line",linenumber)
				print(line)
				noerrors = False

		linenumber += 1

if noerrors:
	print("\nNo errors")


