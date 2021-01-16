import os
import os.path


### Fetch all files from current working directory defined at line 3 into a list
#states = [f for f in os.listdir() if os.path.isfile(os.path.join(f))]

readfile = open("dev_scripts/taginput.txt", "r")
#writefile = open("tagoutput.txt", "w")
appendfile = open("localisation/countries_l_english.yml", "a")
filecontent = "\n"
for line in readfile: #read file line by line
    #filecontent += line
    tag = ""
    tag_name = ""
    tag_adj = ""
    
    comma1 = False #local flags
    comma2 = False
    for char in line:
        if (char == ","):
            if (comma1):
                comma2 = True
            else:
                comma1 = True
        else:
            if (comma1 and comma2):
                tag_adj += char
            elif (comma1):
                tag_name += char
            else:
                tag += char
    
    if (tag[0] == " "):
        tag = tag[1:len(tag)]
    if (tag[len(tag)-1] == "\n"):
        tag = tag[0:len(tag)-1]
    if (tag_name[0] == " "):
        tag_name = tag_name[1:len(tag_name)]
    if (tag_name[len(tag_name)-1] == "\n"):
        tag_name = tag_name[0:len(tag_name)-1]
    if (tag_adj[0] == " "):
        tag_adj = tag_adj[1:len(tag_adj)]
    if (tag_adj[len(tag_adj)-1] == "\n"):
        tag_adj = tag_adj[0:len(tag_adj)-1]
    newlines = ""
    newlines = newlines + " " + tag + "_independent:0 " + "\"" + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_independent_DEF:0 " + "\"" + "The " + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_japan:0 " + "\"" + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_japan_DEF:0 " + "\"" + "The " + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_germany:0 " + "\"" + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_germany_DEF:0 " + "\"" + "The " + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_soviet:0 " + "\"" + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_soviet_DEF:0 " + "\"" + "The " + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_britain:0 " + "\"" + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_britain_DEF:0 " + "\"" + "The " + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_france:0 " + "\"" + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_france_DEF:0 " + "\"" + "The " + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_america:0 " + "\"" + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_america_DEF:0 " + "\"" + "The " + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_italy:0 " + "\"" + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_italy_def:0 " + "\"" + "The " + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + ":0 " + "\"" + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_DEF:0 " + "\"" + "The " + tag_name + "\"" + "\n"
    newlines = newlines + " " + tag + "_ADJ:0 " + "\"" + tag_adj + "\"" + "\n"
    filecontent += newlines
readfile.close()

if (filecontent[len(filecontent)-1] == "\n"):
    filecontent = filecontent[0:len(filecontent)-1]

#Append to countries_l_english.yml
appendfile.write(filecontent)
