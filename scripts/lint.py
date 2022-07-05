#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 18:00:51 2022

@author: jeff
"""

import os
import re

def lint_notebook(full_folder_name, file):
    print(f"{full_folder_name}/{file}")


folders = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]

for fld in folders:
    full_folder_name = f"./notebooks/{fld}"
    print("\n", full_folder_name)
    for file in sorted(os.listdir(full_folder_name)):
        if re.match("(.*)\.ipynb$", file):
            lint_notebook(full_folder_name, file)
            