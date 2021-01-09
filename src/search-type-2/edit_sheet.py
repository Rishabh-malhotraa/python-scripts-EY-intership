import pandas as pd
from get_websites import website
from get_bd import business_description
import json

wb = "Website link"
bd = "Business description"

df = pd.read_excel("search-done-1.xlsx")

# with open('website.json') as f:
#     website_list = json.load(f)
bd_list = []
with open('bd_new.json') as f:
    bd_list = json.load(f)


# website_list = website()
# bd_list = business_description()
n = range(604)

for j in n:
    # df.loc[j, wb] = website_list[j]
    df.loc[j, bd] = bd_list[j]
    print(df.loc[j, bd])

df.to_excel("search-done-2.xlsx")
