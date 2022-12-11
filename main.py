from bs4 import BeautifulSoup
import re

with open("new.html", 'r') as f:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    for child in soup():
        if re.fullmatch(regex, child.text):
            print(child.text)
