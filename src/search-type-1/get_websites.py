import docx


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


def website():
    val = reading_text_document()
    z = [i for i in val if check(i, "Website URL:")]
    website_list = [i[23:] for i in z]
    # for i in z:
    #     print(i[24:])
    # i[24:]
    print(len(website_list))
    return website_list


if __name__ == "__main__":
    website()
