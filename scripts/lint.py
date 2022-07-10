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
HEADER = re.compile(r'(^|\n)(?P<level>#{1,6})(?P<header>.*?)#*(\n|$)')

def find_and_test_urls(cell):
    urls = re.findall(URL, cell.source)
    for protocol, domain, target in urls:
        url = "://".join([protocol, "".join([domain, target])])
        try:
            get = requests.get(url, timeout=10)
            if not get.status_code == 200:
                print(f"    WARNING: {url} is not reachable, status_code: {get.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"    ERROR: {url} {e}")

            
def find_headers(cell):
    headers = re.findall(HEADER, cell.source)
    if headers:
        print(f"   {' '.join(headers[0][1:3])}")

        
def lint_notebook(full_folder_name, file):
    path = f"{full_folder_name}/{file}"
    print(f"\n\nFILE: {path}")
    with open(path, "r") as fp:
        nb = nbformat.read(fp, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            find_headers(cell)
            find_and_test_urls(cell)


folders = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]

for fld in folders:
    full_folder_name = f"./notebooks/{fld}-publish"
    for file in sorted(os.listdir(full_folder_name)):
        if re.match("(.*)\.ipynb$", file):
            lint_notebook(full_folder_name, file)
            