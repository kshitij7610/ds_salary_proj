# -*- coding: utf-8 -*-
"""
Created on Thu May 27 01:43:47 2021

@author: kshit
"""


import ds_salary as gs
import pandas as pd
path = "C:/ds_salary_proj/chromedriver"


df = gs.get_jobs('data scientist', 15, False, path, 15)

