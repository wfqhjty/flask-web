#!E:\python\practice\flask-web\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'repo==0.1.0','console_scripts','repo'
__requires__ = 'repo==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('repo==0.1.0', 'console_scripts', 'repo')()
    )
