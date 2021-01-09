import docx
import json

str1 = "Business Description:"


def check(string, sub_str):
    if string.find(sub_str) == -1:
        return False
    else:
        return True


def reading_text_document(file_name="search.docx"):
    doc = docx.Document(file_name)
    txt = []
    for paragraphs in doc.paragraphs:
        txt.append(paragraphs.text)
    return txt


def Remove(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


def business_description():
    val = reading_text_document()
    counter = 0
    bd = []

    for element in val:
        if check(element, str1):
            bd.append(val[counter + 1])
        counter += 1

    bd_list = [i.strip() for i in bd]
    bd_listII = Remove(bd_list)
    print(len(bd_list))

    with open('buisiness_description.json', 'w') as f:
        json.dump(bd_list, f)

    return (bd_listII)


if __name__ == "__main__":
    business_description()
