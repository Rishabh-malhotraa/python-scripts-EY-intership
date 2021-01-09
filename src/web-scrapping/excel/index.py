import pandas as pd
import json
import os

bd = "Business description (CBTP)"

dir = os.getcwd()

search = os.path.join(dir, "excel", "search-done-3.xlsx")

# the remaining data
company_description = os.path.join(dir, "excel", "Company Description.xlsx")

companies_rejected_path = os.path.join(dir, "json", "company_rejected-II.json")

df = pd.read_excel(search)

df_desc = pd.read_excel(company_description)

data = []


with open(companies_rejected_path) as f:
    data = json.load(f)

x = range(1680)

# z = df["Website link"]
count = 0

for j in x:
    if len(df.loc[j, bd]) == 0:
        count += 1


# df.to_excel("search-done-4.xlsx")
