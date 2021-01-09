import pandas as pd
import math

df = pd.read_excel("data/demo.xlsx")


keys = [
    "corporate managemenet",
    "R&D",
    "financial transactions",
    "reinsurance",
    "it services",
    "administrative services",
    "research and development",
    "public relation",
    "human resources",
    "Human Resources",
    "legal services",
    "insurance",
    "accounting",
    # "marketing",
]

key_reason = [
    "provides corporate management services",
    "the company is engaged in Research and Development",
    "offers financial transaction services",
    "provides insurance-reinsurance services",
    "provides IT services",
    "provides adminstrative services",
    "the company is engaged in Research and Development",
    "offers PR services",
    "offers human resource services",
    "offers human resource services",
    "engaged in offering legal services",
    "provides insurance services",
    "practices in offering accounting services",
    # "provides help in marketing",
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


def second(df, i, j):
    text = df[i][j]
    if isNaN(text):
        df.loc[j, "Accept/ Reject"] = "Reject"
        df.loc[j, "Reasons"] = "IDI"
        return
    if any(key in text for key in keys):
        flags = [key in text for key in keys]
        pos = count(flags)
        df.loc[j, "Accept/ Reject"] = "Accept"
        df.loc[j, "Reasons"] = "Engaged into comparable Activities"
        df.loc[j, "Detailed Reasons"] = key_reason[pos]
        if isNaN(df["Website address(es)"][j]) == False:
            df.loc[j, "Links"] = df["Website address(es)"][j]
    else:
        df.loc[j, "Accept/ Reject"] = "Reject"
        df.loc[j, "Reasons"] = "NCF"


n = range(len(df))
c = 0
i = "Full overview"
new_df = df
for j in n:
    text = df[i][j]
    if isNaN(text):
        second(df, "Trade description (English)", j)
        continue
    if any(key in text for key in keys):
        c = c + 1
        flags = [key in text for key in keys]
        pos = count(flags)
        df.at[j, "Accept/ Reject"] = "Accept"
        df.at[j, "Reasons"] = "Engaged into comparable Activities"
        df.loc[j, "Detailed Reasons"] = key_reason[pos]
        if isNaN(df["Website address(es)"][j]) == False:
            df.loc[j, "Links"] = df["Website address(es)"][j]
    else:
        df.at[j, "Accept/ Reject"] = "Reject"
        df.at[j, "Reasons"] = "NCF"

    # print(text)


print(c)
# print(type(df["Full overview"][0]))

df.to_excel("demo-2.xlsx")
