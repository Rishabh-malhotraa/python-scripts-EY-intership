# Prepare Link For MarketWatch Scrapping

import json
import os
import pandas as pd


dir = os.getcwd()
df = pd.read_excel(os.path.join(dir, "excel", "search.xlsx"))

nameOfCompany = "Name of the company"


companies_data = []
companies_desc = []
with open(os.path.join(dir, "json", "companies_info.json")) as f:
    companies_data = json.load(f)
with open(os.path.join(dir, "json", "company_description.json")) as f:
    companies_desc = json.load(f)
with open(os.path.join(dir, "json", "company_rejected-II.json")) as f:
    rejected = json.load(f)

website = "https://www.marketwatch.com/investing/stock/"

link_list = []
counter = 0
counter2 = 0

j = 0

for i in companies_desc:
    if len(i) == 0:
        ticker = companies_data[j]["id"]
        link = website + ticker
        index = i
        name = (df.iloc[j][nameOfCompany],)
        data = {"link": link, "index": index, "name": name}
        link_list.append(data)
    j += 1

for i in link_list:
    if len(i) == 0:
        counter += 1
    else:
        counter2 += 1

with open(os.path.join(dir, "json", "companies_rejected_links.json"), "w") as f:
    json.dump(link_list, f)

print("no link found", counter)
print("link found", counter2)
