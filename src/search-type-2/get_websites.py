import docx
import json


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


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


def website():
    val = reading_text_document()
    z = [i for i in val if check(i, "Website URL:")]
    website_list = [i.strip() for i in z]
    website_listII = Remove(website_list)
    for i in website_listII:
        print(i.strip())
    print(len(website_listII))

    with open('website.json', 'w') as f:
        json.dump(website_listII, f)

    return (website_listII)


if __name__ == "__main__":
    website()
