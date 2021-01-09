# Preprate Links for Trading View Scrapping

import json
import os


dir = os.getcwd()

companies_data = []
SE_codes = {}
with open(os.path.join(dir, "json", "companies_info.json")) as f:
    comapanies_data = json.load(f)
with open(os.path.join(dir, "json", "SE_info.json")) as f:
    SE_codes = json.load(f)

# https://in.tradingview.com/symbols/TSE-3387/
# https://in.tradingview.com/symbols/{Stock-Exchange}-{ticker}/
website = "https://in.tradingview.com/symbols/"

link_list = []

for i in comapanies_data:
    SE_name = i["name"]
    ticker = i["id"]

    SE_short = SE_codes[SE_name]["code"]
    if SE_short == " ":
        link_list.append("")
    else:
        link = website + SE_short + "-" + ticker
        link_list.append(link)

counter = 0
counter2 = 0
for i in link_list:
    if len(i) == 0:
        counter += 1
    else:
        counter2 += 1
    print(i)

with open(os.path.join(dir, "json", "companies_links.json"), "w") as f:
    json.dump(link_list, f)

print("no link found", counter)
print("link found", counter2)
