import pandas as pd

df = pd.read_excel("rejected-info-6.xlsx")


def isNaN(string):
    return string != string


n = range(len(df))
i = ["Reasons"]
accept = 0
idi_count = 0
ncs_count = 0
ncf_count = 0
reject = 0
count = 0

for j in n:
    if isNaN(df.loc[j, "Detailed Reasons"]) == True:
        count += 1
    if df.loc[j, "Accept/ Reject"] == "Accept":
        accept = accept + 1
    else:
        reject = reject + 1
        if df.at[j, "Reasons"] == "IDI":
            idi_count = idi_count + 1
        elif df.at[j, "Reasons"] == "NCS":
            ncs_count = ncs_count + 1
        elif df.at[j, "Reasons"] == "NCF":
            ncf_count = ncf_count + 1


print("Detailed Reasons remaining", (count - idi_count))
print("accepted companies", accept)
print("rejected companies", reject)
print("IDI companies", idi_count)
print("NCS companies", ncs_count)
print("NCF companies", ncf_count)

# Detailed Reasons remaining 100
# accepted companies 557
# rejected companies 3378
# IDI companies 1299
# NCS companies 1004
# NCF companies 1074