from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import os

name = "Name of the company"

dir = os.getcwd()

doc_path = os.path.join(dir, "excel", "search.xlsx")
df = pd.read_excel(doc_path)

companies_links = []

with open(os.path.join(dir, "json", "companies_links.json")) as f:
    companies_links = json.load(f)

data = []
counter = 0

"""
1. check the conditional if link is present
2. if not present append ""
3. try catch block to find the case in which there is no description 
"""
rejected = []
i = 0
for link in companies_links:
    if len(link) > 0:
        source = requests.get(link).text
        soup = BeautifulSoup(source, "lxml")
        try:
            summary = soup.find("div", class_="tv-widget-description__text")
            print(summary.text.strip())
            data.append(summary.text.strip())
        except Exception as e:
            data.append("")
            val = {
                "index": i,
                "name": df.iloc[i][name],
                "link": link,
            }
            print(val)
            rejected.append(val)
            counter += 1
    else:
        data.append("")
    i += 1

# exceptional cases-->196

# 1679

print("exceptional cases", counter)
# print(len(data))

with open("company_description-II.json", "w") as f:
    json.dump(data, f)
with open("company_rejected-II.json", "w") as f:
    json.dump(rejected, f)
