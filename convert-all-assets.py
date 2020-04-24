"""
Script that takes a set of Source 1 game vpks and converts their models/materials to Source 2 formats.
In particular, it extracts the vpks, uses VTFlib to extract material .tgas, then simply runs the source2utils converters.
Script by Mark. Credit to Neil Jedrzejewski, Ryan Gregg, and of course the authors of source2utils (Rectus, DankParrot/Alpyne, Caseytube).
"""

import os
import shutil
import subprocess
from pathlib import Path

# I couldn't find a simple way to quietly merge two folders, so here's some verbose StackOverflow code
# https://stackoverflow.com/questions/7419665/python-move-and-overwrite-files-and-folders
def copyAndMerge(source, destination):
    for src_dir, dirs, files in os.walk(source):
        dst_dir = src_dir.replace(source, destination, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
            shutil.copy(src_file, dst_dir)

# This code isn't very fancy, but it works
# Obviously, changing the order of the config sections will break it completely
file = open("config.txt","r")
config =  [x.strip() for x in file.readlines()]
file.close()
line = 0
while config[line-1] != "[Game Directory]":
    line += 1
if config[line][-1] != "\\":
    config[line] = config[line] + "\\"
gameDir = config[line]
vpkList = []
while config[line-1] != "[VPK List]":
    line += 1
while config[line] != "[Content Folders]" and config[line] != "":
    vpkList.append(config[line])
    line += 1
contentList = []
while config[line-1] != "[Content Folders]":
    line += 1
while line < len(config) and config[line] != "":
    contentList.append(config[line])
    line += 1

# Extraction
# Specified VPKs must be in a game directory, ie. relative ..\bin directory has a vpk.exe
workingDir = os.getcwd()
for vpk in vpkList:
    os.chdir(os.path.join(str(Path(gameDir + vpk).parents[1]) + "\\bin"))
    subprocess.run('vpk.exe "' + gameDir + vpk + '"', shell=True)
    copyAndMerge(gameDir + vpk[:-4] + "\\models", workingDir + "\\converted\\" + vpk.split("\\")[1] + "\\models")
    copyAndMerge(gameDir + vpk[:-4] + "\\materials", workingDir + "\\converted\\" + vpk.split("\\")[1] + "\\materials")
    shutil.rmtree(gameDir + vpk[:-4])
for folder in contentList:
    copyAndMerge(gameDir + folder + "\\models", workingDir + "\\converted\\" + folder.split("\\")[1] + "\\models")
    copyAndMerge(gameDir + folder + "\\materials", workingDir + "\\converted\\" + folder.split("\\")[1] + "\\materials")

# Conversion
os.chdir(workingDir)
subfolders = [folder.path for folder in os.scandir(workingDir + "\\converted\\") if folder.is_dir()]
for game in subfolders:
    # Naughty method of running another python file, but give me a break
    subprocess.run('python source2utils\\mdl_to_vmdl.py "' + game + '\\models"', shell=True)
    subprocess.run('vtflib\VTFCmd.exe -folder "' + game + '\\materials\\*.vtf" -recurse -exportformat "tga"', shell=True)
    open(game + '\\convertedBumpmaps.txt', 'a').close()
    subprocess.run('python source2utils\\vmt_to_vmat.py "' + game + '"', shell=True)
print("Done! The subfolders of 'converted' can now be copied to your Source 2 SDK's 'content' folder.")