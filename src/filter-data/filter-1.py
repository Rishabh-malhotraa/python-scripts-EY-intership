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
    "Temporary employment agency",
    "business support",
    "advertising agency",
    "management consultancy",
    "administrative service",
    "General public administration activities",
    "Repair",
    "Engineering activities",
    "Combined facilities support activities",
    "Web portals",
    "Other human resources provision",
    "Other financial service activities, except insurance and pension funding nec",
    "Other activities auxiliary to financial services, except insurance and pension funding",
    "Fund management activities",
    "Activities of employment placement agencies",
    "Activities of insurance agents and brokers",
    "Trusts, funds and similar financial entities",
    "Legal activities",
    "Other information service activities nec",
    "Other information technology and computer service activities",
    "Security and commodity contracts brokerage",
    "Accounting, bookkeeping and auditing activities; tax consultancy"
    # "public opinion polling"
    # "marketing",
]

key_reason = [
    "temporary employement agency",
    "the company is in engaged in non comparable business support services",
    "advertising agency",
    "the company is engaged in management consultancy",
    "the company is engaged in administrative work",
    "the company is engaged in general administrative activities",
    "the company is engaged in repair service",
    "company is engaged in engineering work",
    "company is engaged in non comparable support activities",
    "provides services for software development",
    "provides noncomparable HR services",
    "provides noncomparable financial services",
    "provides noncomparable financial services",
    "provides noncomparable financial services",
    "Recruitment Agency",
    "insurance brokers",
    "credit intermediation and related activities",
    "unrelated legal services",
    "company deals in noncomparable information services",
    "company provides noncomparable information services",
    "company is in the buisiness of brokerage",
    "company provides noncomparable accounting/audtiting services",
    # "public opinion and polling agency",
    # the value of last is -9-
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
                    df.loc[j, "Reasons"] = "NCS"
                    # if pos == 9:
                    # else:
                    #     df.loc[j, "Reasons"] = "NCS"

    else:
        continue

    # print(text)


print(c)
# print(type(df["Full overview"][0]))

df.to_excel("rejected-info-6.xlsx")