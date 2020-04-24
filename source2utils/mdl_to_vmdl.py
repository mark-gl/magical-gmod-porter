# Modified usage: mdl_to_vmdl.py C:/full/path/to/models
import re, sys, os

INPUT_FILE_EXT = '.mdl'
OUTPUT_FILE_EXT = '.vmdl'
PATH_TO_CONTENT_ROOT = ""
    
VMDL_BASE = '''<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:generic:version{7412167c-06e9-4698-aff2-e63eb59037e7} -->
{
    m_sMDLFilename = "<mdl>"
}
'''

def walk_dir(dirname):
    files = []

    for root, dirs, filenames in os.walk(dirname):
        for filename in filenames:
            if filename.lower().endswith(INPUT_FILE_EXT):
                files.append(os.path.join(root,filename))
            
    return files

abspath = ''
files = []
PATH_TO_CONTENT_ROOT = sys.argv[1] + "/"
print(PATH_TO_CONTENT_ROOT)

# recursively search all dirs and files
abspath = os.path.abspath(PATH_TO_CONTENT_ROOT)
if os.path.isdir(abspath):
    files.extend(walk_dir(abspath))

def putl(f, line, indent = 0):
    f.write(('\t' * indent) + line + '\r\n')

def strip_quotes(s):
    return s.strip('"').strip("'")

def fix_path(s):
    return strip_quotes(s).replace('\\', '/').replace('//', '/').strip('/')

def relative_path(s, base):
    base = base.replace(abspath, '')
    base = base.replace(os.path.basename(base), '')

    return fix_path(os.path.basename(abspath) + base + '/' + fix_path(s))

def get_mesh_name(file):
    return os.path.splitext(os.path.basename(fix_path(file)))[0]
    
print('Source 2 VMDL Generator! By Rectus via Github.')
print('Initially forked by Alpyne, this version by caseytube.')
print('--------------------------------------------------------------------------------------------------------')

for filename in files:
    out_name = filename.replace(INPUT_FILE_EXT, OUTPUT_FILE_EXT)
    if os.path.exists(out_name): continue

    print('Importing', os.path.basename(filename))

    out = sys.stdout
    
    mdl_path = fix_path(filename.replace(abspath, ""))
    
    with open(out_name, 'w') as out:
        putl(out, VMDL_BASE.replace('<mdl>', mdl_path).replace((' ' * 4), '\t'))