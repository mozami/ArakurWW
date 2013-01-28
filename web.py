#!/usr/bin/env python
#! -*- coding: utf8 -*-
#Activación del virtualenv
import sys

repo_path = '/Users/joac/ArakurWW/'
sys.path.insert(0, repo_path + 'arakur_ww')

activate_this = '/Users/joac/ArakurWW/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from arakur_ww import app as application

application.run(threaded=True)
