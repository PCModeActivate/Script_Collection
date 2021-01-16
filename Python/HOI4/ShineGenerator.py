import os
import os.path

#Shine overlay script
'''
    README FIRST!

    IO:
        Read from before-Overlay.txt
        Write into after-Overlay.txt
    
    Warning: This will after-Overlay WILL be overwritten every time the script is ran!

    This script runs under the assumption that something like is already written with the correct directories.
    This script also runs under the assumption that the input file is .tga, whereby shine_overlay.tga is used.

    To use this script for .dds, simply make sure shine_overlay.dds is present in your gfx file, and replace 'shine_overlay.tga' with 'shine_overlay.dds' in the script

    Example Input: (spaces around '=' are STRICTLY ENFORCED, otherwise it WILL NOT WORK (until I make something more user friendly))
    SpriteType = {
	    name = "GFX_goal_continuous_air_production"
	    texturefile = "gfx/interface/goals/goal_continuous_air_production.tga"			
	}

    See exampleinput.txt for input style guide.
'''

os.chdir("dev_scripts")

### Fetch all files from current working directory defined at line 3 into a list
#states = [f for f in os.listdir() if os.path.isfile(os.path.join(f))]

readfile = open("before-Overlay.txt", "r")
writefile = open("after-Overlay.txt", "w")

gfxName = ""
gfxDirectory = ""

filecontent = "" #parse through the file

for line in readfile: #read file line by line
    filecontent += line
    currentLine = format(line.strip()) 
    if (currentLine.find("name = ") != -1):
        gfxName = currentLine[6:len(currentLine)]
    elif (currentLine.find("texturefile = ") != -1):
        gfxDirectory = currentLine[13:len(currentLine)]
    elif (currentLine.find('}') != -1):
        newlines = ""
        newlines += "\tSpriteType = {"
        newlines += "\n\t\tname = " + gfxName[0:-1] + '_shine"'
        newlines += "\n\t\ttexturefile = " + gfxDirectory

        newlines += '\n\t\teffectFile = "gfx/FX/buttonstate.lua"'
        newlines += '\n\t\tanimation = {'
        newlines += '\n\t\t\tanimationmaskfile = ' + gfxDirectory
        newlines += '\n\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.tga"'
        newlines += '\n\t\t\tanimationrotation = -90.0'
        newlines += '\n\t\t\tanimationlooping = yes'
        newlines += '\n\t\t\tanimationtime = 0.75'
        newlines += '\n\t\t\tanimationdelay = 1.0'
        newlines += '\n\t\t\tanimationblendmode = "add"'
        newlines += '\n\t\t\tanimationtype = "scrolling"'
        newlines += '\n\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }'
        newlines += '\n\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }'
        newlines += '\n\t\t}'
        newlines += '\n\t\tanimation = {'
        newlines += '\n\t\t\tanimationmaskfile = ' + gfxDirectory
        newlines += '\n\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.tga"'
        newlines += '\n\t\t\tanimationrotation = 90.0'
        newlines += '\n\t\t\tanimationlooping = yes'
        newlines += '\n\t\t\tanimationtime = 0.75'
        newlines += '\n\t\t\tanimationdelay = 1.0'
        newlines += '\n\t\t\tanimationblendmode = "add"'
        newlines += '\n\t\t\tanimationtype = "scrolling"'
        newlines += '\n\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }'
        newlines += '\n\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }'
        newlines += '\n\t\t}'
        newlines += '\n\t\tlegacy_lazy_load = no'
        newlines += '\n\t}\n'
        filecontent += newlines
readfile.close()

#Write the new file with the filecontent
writefile.write(filecontent)