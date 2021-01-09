import pandas as pd
from get_websites import website
from get_bd import business_description

wb = "Website link"
bd = "Business description"

df = pd.read_excel("search.xlsx")
website_list = website()
bd_list = business_description()
n = range(len(df))

for j in n:
    df.loc[j, wb] = website_list[j]
    df.loc[j, bd] = bd_list[j]

df.to_excel("search-done.xlsx")
