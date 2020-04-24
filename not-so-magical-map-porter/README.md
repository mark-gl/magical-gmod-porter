# not-so-magical-map-porter
This tool will convert all of the assets placed in the 'convertme' folder. Map assets need to be extracted manually via bspsrc.

## Requirements
You will need:
- Java Runtime Environment
- Python 3.7
- Python Image Library (`python3 -m pip install --upgrade Pillow`)
- A map that you want to decompile and convert

## Instructions
1. Open bspsrc.jar from the 'bspsrc' folder
2. Add the .bsp file for the map you would like to convert
3. Ensure 'Extract embedded files' is ticked under 'Other'
4. Hit 'Decompile'. A new folder will be created next to the map.
5. Copy 'models' and 'materials' from the map's folder to the 'convertme' folder
6. Run `convert-the-convertme-folder.bat`.

## Notes
- Some maps contain materials that refer to other game materials, for example a shinier version of a brick wall from Half Life 2. These assets will cause an error, since the original is not present. You will be able to see a list of affected materials after running `convert-all-assets.bat`. To fix these materials, run `magical-gmod-porter` and copy the required materials from the 'extracted' folder to their respective folder within 'convertme'.
- BSP decompilation is always a hit or miss
- Barely any of the entities in the map will work and unless you remove most of them, it'll just crash on launch
- Once the map is opened in Source 2's Hammer editor, all the texture scaling will be incorrect
- Refer to magical-gmod-porter notes information about getting converted content into the Source 2 SDK.
