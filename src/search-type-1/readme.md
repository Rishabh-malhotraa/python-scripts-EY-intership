# Documentation

## Summary

Extracts the information from the docx file based on certain parameters and prepares the excel file accordingly.

## Folder Strucutre

``` bash
└───src
    └───search-type-1
        │   get_bd.py
        │   get_websites.py
        │   index.py
        │   readme.md
        │
        └───data
                search.docx
                search.xlsx
```

**get_bd.py** :- Extracts the buisness description of all the companies from the the search.docx file and returns it in an array.

**get_websites.py** :- Extracts the list of websites of the companies from the the search.docx file and returns it in an array.

**index.py**:- Combines the information extracted from the get_bd.py and get_websites.py and prepares the excel sheet accordingly.

**data/**:- contains the docx file which need to be scanned and templated .xlsx file which needs to be prerared with the data extracted from the .docx file.

---