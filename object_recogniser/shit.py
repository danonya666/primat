import requests
from html.parser import HTMLParser

print(1)
response = requests.get("http://free-proxy.cz/")
print(2)
parser = HTMLParser()
print(1)

parser.feed(response.text)