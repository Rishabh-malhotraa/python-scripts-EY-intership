import docx
import json
import os

dir = os.getcwd()

doc_path = os.path.join(dir, "search.docx")
companies_info_path = os.path.join(dir, "json", "companies_info.json")


""" 
this function is used to check if the string is NaN ir not there might be a prebaked function but i prefer this :)))
"""


def check(string, sub_str):
    if string.find(sub_str) == -1:
        return False
    else:
        return True


"""
Reading the document from search.docx and addding all the lines into an array
- we loop through the paragraphs array and convert them into text and add them into an array
"""


def reading_text_document(file_name=doc_path):
    doc = docx.Document(file_name)

    txt = []

    for paragraphs in doc.paragraphs:
        txt.append(paragraphs.text)
    return txt


"""
Getting the stock exchange id based on which we will scrape the data
"""


def stock_exchange_id():
    val = reading_text_document()
    # List comprehension to selectively add only the paragarhs which contain exchange ticker
    z = [i for i in val if check(i, "Exchange Ticker:")]
    se_list = [i[16:].strip() for i in z]
    print(len(se_list))

    return se_list


def stock_exchange():
    val = reading_text_document()
    z = [i for i in val if check(i, "Stock Exchange:")]
    se_list = [i[16:].strip() for i in z]
    print(len(se_list))

    # se_set = set(se_list)
    # for i in se_set:
    #     print(i)

    return se_list


def construct():
    se = stock_exchange()
    se_id = stock_exchange_id()

    length = range(len(se_id))
    data = []
    for i in length:
        info = {"name": se[i], "id": se_id[i]}
        data.append(info)

    print(len(data))
    data_dict = {"data": data}
    with open(companies_info_path, "w") as f:
        json.dump(data, f)
    return data


if __name__ == "__main__":
    construct()
