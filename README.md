# Scrape to CSV: Scrape the Web, Make a CSV...

Lorem main description.

- [Python](https://www.python.org/)

Completed for Professional Portfolio Project: Assignment 12, Angela Yu 100 Days of
Code -- "Web Scraping: Custom Web Scraper"

_MIT License: Copyright (c) 2024- Andrew Blais_

---

Future updates will include:

- Some countries' data cannot be processed into .csv and .json files. Check into the
  pre-/post-dataframe contents.

- Consider more global Selenium and BeautifulSoup functionality to allow for use on
  any websites.

---

### Documentation:

```requirements
beautifulsoup4==4.12.3
pandas==2.2.1
selenium==4.19.0
tabulate==0.9.0
webdriver-manager==4.0.1
```

_Docstrings for `main.py`:_

```bash
Help on class WorldFactbook in module __main__:

class WorldFactbook(builtins.object)
 |  WorldFactbook(country: str = '', 
 |                print_df: bool = True, 
 |                save_csv: bool = True, 
 |                save_json: bool = True, 
 |                article_class: str = 'article-content')
 |
 |  A class to scrape and process information from the CIA World Factbook about a
 |   given country.
 |
 |  :param country: The name of the country to scrape data for. If not specified, a
 |                   random country is selected.
 |  :type country: str
 |  :param print_df: Indicates whether to print the dataframe to the console.
 |  :type print_df: bool
 |  :param save_csv: Indicates whether to save the dataframe to a CSV file.
 |  :type save_csv: bool
 |  :param save_json: Indicates whether to save the dataframe to a JSON file.
 |  :type save_json: bool
 |  :param article_class: The class name of the article content in the HTML. Default
 |                         is "article-content".
 |  :type article_class: str
 |
 |  Methods defined here:
 |
 |  __init__(self, 
 |           country: str = '', 
 |           print_df: bool = True, 
 |           save_csv: bool = True, 
 |           save_json: bool = True, 
 |           article_class: str = 'article-content')
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  country_name_select(self)
 |      Selects a country name for scraping. If no country is specified, selects a
 |       random country from the list.
 |
 |  driver_scrape(self)
 |      Orchestrates the scraping process: initializes the Selenium driver, scrapes
 |       the data, and saves it.
 |
 |  driver_selenium(self)
 |      Initializes the Selenium WebDriver, navigates to the FACTBOOK_URL, and
 |       clicks on the specified country link.
 |
 |  make_beautiful_soup(self)
 |      Parses the HTML of the scraped page using BeautifulSoup and extracts
 |       relevant data into a dictionary.
 |
 |  make_dataframe(self)
 |      Converts the scraped data dictionary into a pandas DataFrame and optionally
 |       prints it.
 |
 |  save_csv_file(self)
 |      Saves the DataFrame to a CSV file if the save_csv attribute is True.
 |
 |  save_json_file(self)
 |      Saves the DataFrame to a JSON file if the save_json attribute is True.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```

_Docstrings for `/config/config.py`:_

```bash
Help on module __main__:


config.py

Contains static configurations and utility functions for the World Factbook 
 scraping project.

This includes the URL for the CIA World Factbook, a function to generate filenames 
 in a consistent format, and a function to introduce random sleep intervals between 
 requests to mimic human behavior and reduce the likelihood of being detected as a bot.

Help on function create_filename in module __main__:

create_filename(name, extension)
    Generates a sanitized and standardized file name using a country name and a
     file extension.

    :param name: The country name to be included in the file name.
    :type name: str
    :param extension: The file extension (e.g., 'csv', 'json').
    :type extension: str
    :return: A string containing the sanitized file name.
    :rtype: str

    The country name is sanitized by removing commas, replacing spaces with underscores,
     and converting to lowercase to ensure file system compatibility.

Help on function randsleep in module __main__:

randsleep()
    Pauses the execution for a random interval between 5 and 10 seconds.

    This function is used to mimic human browsing behavior and delay the execution
     of subsequent actions, which can help in avoiding detection by anti-bot mechanisms
     on websites, also helps to respect the site's traffic load.
```

_Docstrings for `/data/country_names.py`:_

```bash
Help on module __main__:

country_names.py

Contains a list of country names used in the World Factbook scraping project. This list
 is used for selecting a country randomly if no specific country is provided for data
 scraping. Based on ISO 3166 Codes standard.

The country names are stored in a list format, making it easy to retrieve a random name
 or iterate over all names for batch processing tasks. The list includes various
 territories and regions in addition to sovereign countries to encompass the wide range
 of entries found in the CIA World Factbook.
```

---

## Created in completing an assignment for Angela Yu's Course:

### **Day 93, Professional Portfolio Project [Web Scraping]**

#### **_Assignment 12, "Custom Web Scraper"_**

Build a custom web scraper to collect data on things that you are interested in.

- _assignment
  for [Angela Yu 100 Days of Code](https://www.udemy.com/course/100-days-of-code/)_

### **Assignment instructions:**

Using what you have learnt about web scraping, scrape a website for data that you are
interested in. Try to build a CSV with the scraped data.

What you scrape is up to you.

Here are some suggestions:

[NBA Player Stats](https://www.nba.com/stats/)

[Audible Books and Ratings](https://www.audible.com/search?keywords=book&node=18573211011)

[Miami House Foreclosure Listing](https://miamidade.realforeclose.com/index.cfm?zaction=AUCTION&Zmethod=PREVIEW&AUCTIONDATE=11/02/2020)

[Steam Games Data](https://steamdb.info/)

[Alibaba Products](https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=paracord&viewtype=&tab=)

[Registered Doctors in Idaho](https://apps-dopl.idaho.gov/IBOMPublic/LPRBrowser.aspx)

[Recipes](https://www.allrecipes.com/)

[Real Estate](https://www.trulia.com/)

[Songs](https://soundcloud.com/)

[Rollercoasters](https://rcdb.com/)

[Food Nutrition](https://www.nutritionvalue.org/Pasta%2C_enriched%2C_dry_nutritional_value.html)

---

### My Submission:

Lorem repo link.

---

### **Questions for this assignment**

#### _Reflection Time:_

**_Write down how you approached the project._**

Lorem ipsum write down how...

**_What was hard?_**

Lorem ipsum what was hard...

**_What was easy?_**

Lorem ipsum what was easy...

**_How might you improve for the next project?_**

Lorem ipsum how might you...

**_What was your biggest learning from today?_**

Lorem ipsum what was your...

**_What would you do differently if you were to tackle this project again?_**

Lorem ipsum what would you...
