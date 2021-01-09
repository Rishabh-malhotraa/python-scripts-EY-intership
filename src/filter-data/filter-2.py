# accepted companies 557
# rejected companies 3378
# IDI companies 1299
# NCS companies 929
# NCF companies 1149
# -----------------------
# NCS done -> 935
# NCF done -> 682
# -----------------------
# Companies Left -> 3378 - 1299 - 935 - 682 === 462
# -----------------------
import pandas as pd
import math

df = pd.read_excel("rejected-info-5.xlsx")

keys = [
    "Data processing, hosting and related activities",
    "Computer facilities",
    "polling",
    "Computer consultancy",
    "Advertising agencies",
    "Other professional, scientific and technical activities nec"
    # "marketing",
]

key_reason = [
    "company is involved in data processing services",
    "provides computer related services",
    "public opinion and polling agency",
    "Provdides Computer Consultancy Activities",
    "companies into marketing and advertising",
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

    response = df.at[j, "Accept/ Reject"]
    if response == "Reject":
        reason = df.at[j, "Reasons"]
        if reason == "NCF":
            text = df.at[j, "NACE Rev. 2, primary code description"]
            dReason = df.at[j, "Detailed Reasons"]
            if (isNaN(text) == False) and (isNaN(dReason) == True):
                if any(key in text for key in keys):
                    c = c + 1
                    flags = [key in text for key in keys]
                    pos = count(flags)
                    df.loc[j, "Detailed Reasons"] = key_reason[pos]
                    df.loc[j, "Reasons"] = "NCF"
                    # if pos == 9:
                    # else:
                    #     df.loc[j, "Reasons"] = "NCS"

    else:
        continue

    # print(text)


print(c)
# print(type(df["Full overview"][0]))

df.to_excel("rejected-info-3.xlsx")