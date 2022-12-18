from bs4 import BeautifulSoup
import re

with open("new.html", 'r') as f:
    regex = re.compile(r'\w+[\\.\w-]*@[-a-z0-9]+\.[a-z]+')
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    for child in soup():
        if re.fullmatch(regex, child.text):
            print(child.text)
