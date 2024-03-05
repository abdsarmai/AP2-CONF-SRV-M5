#!/usr/bin/python

import logging
import sys

logging.basicCOnfig(stream=sys.stderr)
sys.path.append('/var/www/html/servAppBD')

from servAppBD import app as application