import json

company_description = []

with open("company_description.json") as f:
    company_description = json.load(f)

count = 0

for i in company_description:
    if len(i) == 0:
        count += 1

print(count)