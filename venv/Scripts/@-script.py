#!C:\Users\Administrator\Desktop\hai\python\novel\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'at==0.0.3','console_scripts','@'
__requires__ = 'at==0.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('at==0.0.3', 'console_scripts', '@')()
    )
