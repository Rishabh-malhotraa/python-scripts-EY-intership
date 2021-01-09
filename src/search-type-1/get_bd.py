import docx

str1 = "Business Description:"


def check(string, sub_str):
    if string.find(sub_str) == -1:
        return False
    else:
        return True


def reading_text_document(file_name="data/search.docx"):
    doc = docx.Document(file_name)
    txt = []
    for paragraphs in doc.paragraphs:
        txt.append(paragraphs.text)
    return txt


def business_description():
    val = reading_text_document()
    counter = 0
    bd = []

    for element in val:
        if check(element, str1):
            bd.append(val[counter + 1])
        counter += 1

    bd_list = [i[33:] for i in bd]
    return bd_list


if __name__ == "__main__":
    business_description()
