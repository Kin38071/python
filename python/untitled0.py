# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:20:49 2022

@author: narut
"""

from datetime import datetime

now = datetime.now()
nowstring = now.strftime("%d/%m/%Y %H:%M:%S")

print(nowstring)