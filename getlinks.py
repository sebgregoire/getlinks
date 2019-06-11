from getlinks import Getlinks
import re
import sys

url = sys.argv[1]

if not re.search('^https?://', url.lower()):
    url = 'http://' + url

webpage = Getlinks(url)

for link in webpage.listLinks(unique=True):
    print(link)
