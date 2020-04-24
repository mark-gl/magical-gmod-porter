# magical-gmod-porter
Automatically extracts and converts all Garry's Mod, Half-Life 2 and Counter-Strike: Source models and materials to formats ready to be used in Source 2's Hammer editor.

## Requirements
You will need:
- Python 3.7
- Python Image Library (`python3 -m pip install --upgrade Pillow`)
- Garry's Mod
- Counter-Strike: Source
- 12.8GB of disk space

HL2 does not need to be installed, as its content is included in both Gmod and CS:S.

## Instructions
1. Edit the second line of `config.txt` to contain the folder your games are installed in eg. `C:\Program Files (x86)\Steam\steamapps\common`
2. Run `convert-all-assets.py`! Converted assets will appear in the 'Extracted' folder.

## Notes
- To make the converted assets appear in Source 2 SDK, simply copy the 'models' and 'materials' folders into the SDK folder for your mod, eg. `content\hlvr`
- Once you have copied the converted assets to the HL:A SDK, Hammer might crash when you try to open the 'Materials' tab. This is fixed by running the SDK as an administrator. To do so, create a shortcut to your SDK's hlvr.exe (found in `{AlyxSDKFolder}\game\bin\win64`), right click it, go to properties and add `-sw -tools -toolsvr -novr -vconsole -noasserts -nopassiveasserts -dev -devcomp -nop4` to the Target, then switch to the Compatibility tab and enable 'Run as administrator'.
