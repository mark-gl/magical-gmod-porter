mkdir convertme
python ..\source2utils\mdl_to_vmdl.py "%~dp0convertme\models"
..\vtflib\VTFCmd.exe -folder "%~dp0convertme\materials\*.vtf" -recurse -exportformat "tga"
echo. 2>convertme\convertedBumpmaps.txt
python ..\source2utils\vmt_to_vmat.py "%~dp0convertme"
pause