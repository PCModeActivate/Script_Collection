import os
import os.path


### Fetch all files from current working directory defined at line 3 into a list
#states = [f for f in os.listdir() if os.path.isfile(os.path.join(f))]

from os import listdir
from os.path import isfile, join

path = "history/states/" 
files = [f for f in listdir(path) if isfile(join(path, f))]

for f in files:
    readfile = open(path+f, "r")
    readfileDuplicate = open(path+f, "r")
    filecontent = ""
    for line in readfile:
        currentLine = format(line.strip())

        if (currentLine == "add_core_of = FNG" or currentLine == "add_core_of = KRN" or currentLine == "add_core_of = JEH" or currentLine == "add_core_of = HLK"):
            for everyline in readfileDuplicate:
                current = format(everyline.strip())
                if (current[:9] == "manpower="):
                    manpower = int(current[9:])*25/33 # This is the constant
                    filecontent += "\tmanpower="+str(int(manpower))+"\n"
                else:
                    filecontent += everyline
            writefile = open(path+f, "w")
            writefile.write(filecontent)
            writefile.close()
    readfile.close()
    readfileDuplicate.close()