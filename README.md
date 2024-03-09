# music_generator_classic_rock

This program picks 100 classic rock songs and generates an output file. It uses a churning algorithm so the longer a song goes without being selected, the greater the chance it will be selected. 

The source file contains classic rock, songs I like, and artists I am experimenting with, so it is not strictly classic rock. 

I use a website called Soundiiz. I drag the output file there and it imports it into my YouTube library.

WARNING!

The program writes to an out output file. To work properly, the must me a folder one directory above called "archive". There must be a folder within archve called "classic_rock". Here is the line showing the path:

path = "../archive/classic_rock/CR_0" + num + ".csv"
