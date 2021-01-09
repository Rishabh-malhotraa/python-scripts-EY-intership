import pandas as pd
import math

df = pd.read_excel("Non-tech services-1.xlsx")

keys = [
    "construction",
    "marketing",
    "livestock",
    "security",
    "car dealer",
    "dealership",
    "manifacturing goods",
    "recruitment",
    "repair",
    "computer hardware",
    # "marketing",
]

key_reason = [
    "the company is in construction business",
    "engaged in marketing",
    "the company trading of livestock",
    "provides security services",
    "car dealership",
    "is in dealership business",
    "the company is in manufacturing of goods",
    "recruitment agency",
    "engaged in repair services",
    "engaged in computer repair services",
]


def isNaN(string):
    return string != string


def count(flag):
    c = 0
    for i in flag:
        if i == False:
            c = c + 1
        else:
            return c


c = 0
n = range(len(df))
i = ["Accept/ Reject"]

for j in n:

    response = df["Accept/ Reject"][j]
    if response == "Reject":
        text = df.at[j, "Full overview"]
        if isNaN(text) == False:
            if any(key in text for key in keys):
                c = c + 1
                flags = [key in text for key in keys]
                pos = count(flags)
                df.loc[j, "Detailed Reasons"] = key_reason[pos]

    else:
        continue

    # print(text)


print(c)
# print(type(df["Full overview"][0]))

df.to_excel("rejected-info.xlsx")