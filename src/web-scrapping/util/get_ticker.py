import docx


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


def ticker():
    val = reading_text_document()
    z = [i for i in val if check(i, "Exchange Ticker:")]
    ticker_list = [i[17:].strip() for i in z]
    # for i in ticker_list:
    #     print(i)
    print(len(ticker_list))
    return ticker_list


if __name__ == "__main__":
    ticker()
