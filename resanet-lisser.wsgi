# /var/www/html/resanet/resanet-lisser.wsgi

import sys
sys.path.insert(0, '/var/www/html/resanet')

from app import app as application
