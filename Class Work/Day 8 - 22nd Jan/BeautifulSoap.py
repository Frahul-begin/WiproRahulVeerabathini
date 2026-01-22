import requests
import soap
from bs4 import BeautifulSoup
import json

url ="https://www.w3schools.com/html/html_tables.asp"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

pagetitle = soup.title.string if soup.title else "no title"
print(pagetitle)

for link in soup.find_all('a'):
    print(link.get('href'))
    print(href)
tabledata=[]
table = soup.find('table')
if table:
    rows = table.find_all('tr')
    for row in rows[1:]:
        columns = row.find_all('td')
        row_data = [col.test.strip() for col in columns]
        print(row_data)
