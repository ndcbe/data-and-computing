#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 18:00:51 2022

@author: jeff
"""

import os
import re
import requests
import nbformat

URL = r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?'

def lint_notebook(full_folder_name, file):
    path = f"{full_folder_name}/{file}"
    print("\n", path)
    with open(path, "r") as fp:
        nb = nbformat.read(fp, as_version=4)
        
    # check that urls are reachable
    print("finding and testing urls ...")
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            urls = re.findall(URL, cell.source)
            for protocol, domain, target in urls:
                url = "://".join([protocol, "".join([domain, target])])
                try:
                    get = requests.get(url, timeout=10)
                    if get.status_code == 200:
                        print(f"    OK: {url} is reachable")
                    else:
                        print(f"    WARNING: {url} is not reachable, status_code: {get.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"    ERROR: {url} {e}")

    # check that urls are reachable
    print("finding all headers")
    MARKDOWN_HEADER = re.compile(r'(^|\n)(?P<level>#{1,6})(?P<header>.*?)#*(\n|$)')
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            headers = re.findall(MARKDOWN_HEADER, cell.source)
            if headers:
                print(headers)


folders = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]

for fld in folders:
    full_folder_name = f"./notebooks/{fld}-publish"
    print("\n", full_folder_name)
    for file in sorted(os.listdir(full_folder_name)):
        if re.match("(.*)\.ipynb$", file):
            lint_notebook(full_folder_name, file)
            