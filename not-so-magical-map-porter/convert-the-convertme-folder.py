import os
import subprocess
subprocess.run('python ..\\source2utils\\mdl_to_vmdl.py "' +  os.getcwd() + '\\convertme\\models"', shell=True)
subprocess.run('..\\vtflib\VTFCmd.exe -folder "' + os.getcwd() + '\\convertme\\materials\\*.vtf" -recurse -exportformat "tga"', shell=True)
open('convertme\\convertedBumpmaps.txt', 'a').close()
subprocess.run('python ..\\source2utils\\vmt_to_vmat.py ' + os.getcwd() + '\\convertme', shell=True)
print("Done! The contents of 'convertme' can now be copied to your mod's folder.")