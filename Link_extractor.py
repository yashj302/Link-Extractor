import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("Don't forget to include https:// or http://")
link = input("Enter URL for extraction: ")
html = urllib.request.urlopen(link, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')
list_of_links = list()
tags = soup('a')
for tag in tags:
    if str(tag.get('href',None)) not in list_of_links:
        list_of_links.append(str(tag.get('href',None)))
print("\n".join([l for l in list_of_links]))
