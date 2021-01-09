# Documentation

![Scrapping](assets/../asset/buisness_description_automation.gif)
*Business Description of the publically traded companues being extracted and printed in the terminal (which is then saved to its corresponding json file)*

Prepare the Link (marketwatch and tradingview) to extract the information of the publically traded companies.

## Folder Strucutre

``` bash
└───src
    └───Web Scrapping
        │   count.py
        │   edit_sheet.py
        │   Extracting Website.ipynb
        │   readme.md
        │   scrape.py
        │
        ├───docx
        │       search.docx
        │       serach-2.docx
        │
        ├───excel
        │       Company Description.xlsx
        │       index.py
        │       search-done.xlsx
        │       search.xlsx
        │
        ├───json
        │       companies_info.json
        │       companies_links-II.json
        │       companies_links.json
        │       companies_rejected_links.json
        │       company_description-II.json
        │       company_description.json
        │       company_rejected-II.json
        │       Stock_Exchange_info.json
        │
        ├───scrappedData
        │       company_rejected-II.json
        │       scrapped_company_description.json
        │
        └───util
                get_bd.py
                get_stock_exchange.py
                get_ticker.py
                get_websites.py
                prepare_linkII.py
                prepare_links.py
                search-2.docx
                search.docx
```

**docx/ :-** Contains the docs file which contains information regarding the publically traded companies which need to be scraped.

**utils/ :-** Contains the utility functions needed to preapre data for scrapping.

**json/ :-** Contains the josn files created by utils which would be finally used by edit_sheet.py to combine all data to the excel file.

**edit_sheet.py :-** Prepares the excel file from all the scrapped data.

**excel/** :- Contains the prepared Excel file.

**scape.py** :- Main file which starts the scrapping process.

---

### todos

- [x] get the list of all the company tracker id in a list form
- [x] make a request t0 markget watch site
- [x] scrape the data from beautiful soup
- [x] conditionall add all the data in the array if we have something or not even add null
- [x] edit the xlxs file

---
