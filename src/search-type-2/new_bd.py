import pandas as pd
import json
import docx
import itertools

df = pd.read_excel("search.xlsx")
name = "Name of the Company"

bd = []


def reading_text_document(file_name="search.docx"):
    doc = docx.Document(file_name)
    txt = []
    for paragraphs in doc.paragraphs:
        txt.append(paragraphs.text)
    return txt


n = range(len(df))


def check(string, sub_str):
    if string.find(sub_str) == -1:
        return False
    else:
        return True


def buisness_description():
    txt = reading_text_document()
    counter = 0
    j = 0
    flag = False
    n = range(len(df))
    for j in n:
      # this is to loop through all the companies name
        x = df.loc[j, name]
        # print(x)
        counter = -1
        for element in txt:
            counter += 1
            if check(element, x):
                flag = True
            if flag == True:
                if check(element, 'Business Description:'):
                  # formating the string
                    sentence = txt[counter+1]
                    i1 = sentence.find(': ')

                    i2 = sentence.find('Vendor Provided Native Language')
                    print(i1, i2, '\n')
                    if i2 != -1 or i2 != 0:
                        bd.append(sentence[i1+2:i2])
                    else:
                        bd.append(sentence[i1+2:])

                    # print(txt[counter + 1])
                    counter += 1
                    flag = False
                    break

    with open('bd_new.json', 'w') as f:
        json.dump(bd, f)
    print(len(bd))


if __name__ == "__main__":
    buisness_description()
