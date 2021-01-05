#!/usr/bin/env python3

import sys
import subprocess
import requests
try:
    from bs4 import BeautifulSoup
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'bs4'])
finally:
    from bs4 import BeautifulSoup
    search = input("Search the city you want to check weather in: ")
    url = f"https://www.google.com/search?q=Weather in {search}"
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    update = s.find("div", class_="BNeawe").text
    print(update)
