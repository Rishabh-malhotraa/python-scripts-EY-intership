# Documentation

## Summary

Extracts the information from the docx file based on certain parameters and prepares the excel file accordingly.

### **Folder Strucutre**

``` bash
└───src
    ├───search-type-2
    │   │   edit_sheet.py
    │   │   get_bd.py
    │   │   get_websites.py
    │   │   index.ipynb
    │   │   new_bd.py
    │   │   readme.md
    │   │
    │   ├───docx
    │   │       search.docx
    │   │
    │   ├───excel
    │   │       search-done-1.xlsx
    │   │       search-done-2.xlsx
    │   │       search.xlsx
    │   │
    │   └───json
    │           app.json
    │           bd_new.json
    │           buisiness_description.json
    │           data.json
    │           data.txt
    │           website.json
```

**get_bd.py** :- Extracts the buisness description of all the companies from the the search.docx file and returns it in an array.

**get_websites.py** :- Extracts the list of websites of the companies from the the search.docx file and returns it in an array.

**index.py**:- Combines the information extracted from the get_bd.py and get_websites.py and prepares the excel sheet accordingly.

**json/**:- Saves the data extracted by `get_bd.py` `get_websites.py` to analyse if the extraction is done properly.

---
