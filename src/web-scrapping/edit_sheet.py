import pandas as pd
import json
import os

wb = "Website link (CBTP)"
bd = "Business description (CBTP)"


dir = os.getcwd()

doc_path = os.path.join(dir, "excel", "search.xlsx")
df = pd.read_excel(doc_path)
data = []

with open("company_description.json") as f:
    data = json.load(f)

x = range(len(data))

# z = df["Website link"]


for j in x:
    if len(data[j]) > 0:
        df.loc[j, bd] = data[j]
    else:
        df.loc[j, bd] = ""

df[wb] = df["Website link"]

df.to_excel("search-done.xlsx")
