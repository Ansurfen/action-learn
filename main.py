# from bs4 import BeautifulSoup
import requests

url = 'https://central.sonatype.com/v1/browse/component_versions'
payload = dict(sortField="normalizedVersion", sortDirection="desc",
               page=0, size=10, filter=["name:spring"])
headers = {"content-type": "application/json"}
req = requests.post(url, json=payload, headers=headers)
with open('test.json', 'w+') as fp:
    fp.write(req.text)
    fp.close()