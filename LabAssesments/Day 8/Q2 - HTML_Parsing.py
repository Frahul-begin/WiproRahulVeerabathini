import requests
from bs4 import BeautifulSoup
import json

def parse_webpage():
    # 1. Fetch HTML webpage
    url = "https://www.w3schools.com/html/html_tables.asp"
    response = requests.get(url)
    response.raise_for_status()   # Handle HTTP errors
    html_content = response.text
# 2.
    soup = BeautifulSoup(html_content, "lxml")
# 3.
    page_title = soup.title.string if soup.title else "No title found"

    links = []
    for link in soup.find_all("a", href=True):
        links.append(link["href"])

    table_data = []
    table = soup.find("table", {"id": "customers"})

    if table:
        rows = table.find_all("tr")[1:]
        for row in rows:
            cols = row.find_all("td")
            table_data.append({
                "Company": cols[0].text.strip(),
                "Contact": cols[1].text.strip(),
                "Country": cols[2].text.strip()
            })
# 4.
    extracted_data = {
        "page_title": page_title,
        "hyperlinks": links,
        "table_data": table_data
    }

    # 5. Save output into a JSON file
    with open("extracted_data.json", "w") as file:
        json.dump(extracted_data, file, indent=4)

    print("HTML data successfully extracted and saved to extracted_data.json")

if __name__ == "__main__":
    parse_webpage()
