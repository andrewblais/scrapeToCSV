# Python Imports:
from bs4 import BeautifulSoup  # Parsing HTML and navigating the parsed document tree.
import os  # Accessing operating system-dependent functionality like paths.
import pandas as pd  # Data manipulation and analysis.
import random  # Used for choosing random country names and managing operation delays.
from selenium import webdriver  # Automating web browser interaction.
from selenium.webdriver.common.by import By  # For locating elements within a page.
# Firefox driver service:
from selenium.webdriver.firefox.service import Service as FoxService
# Conditions for explicit waits:
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.ui import WebDriverWait  # Waiting for elements to load.
from tabulate import tabulate  # Pretty-printing tabular data.
# Managing Firefox driver:
from webdriver_manager.firefox import GeckoDriverManager as GeckoMan

# Local, custom imports:
from config.config import create_filename, FACTBOOK_URL, randsleep  # Utils/constants.
from data.country_names import iso_3166_country_names  # List of countries for scraping.


class WorldFactbook:
    """
    A class to scrape and process information from the CIA World Factbook about a
     given country.

    :param country: The name of the country to scrape data for. If not specified, a
                     random country is selected.
    :type country: str
    :param print_df: Indicates whether to print the dataframe to the console.
    :type print_df: bool
    :param save_csv: Indicates whether to save the dataframe to a CSV file.
    :type save_csv: bool
    :param save_json: Indicates whether to save the dataframe to a JSON file.
    :type save_json: bool
    :param article_class: The class name of the article content in the HTML. Default
                           is "article-content".
    :type article_class: str
    """

    def __init__(self, country: str = "", print_df: bool = True, save_csv: bool = True,
                 save_json: bool = True, article_class: str = "article-content"):
        self.article_class = article_class  # For flexibility if site's layout changes.
        self.country_name = country
        self.country_names = iso_3166_country_names
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.df = None
        self.df_dict = {}
        self.driver = None
        self.html = None
        self.pre_csv_list = []
        self.print_df = print_df
        self.save_csv = save_csv
        self.save_json = save_json
        self.soup = None

        self.country_name_select()

    def country_name_select(self):
        """
        Selects a country name for scraping. If no country is specified, selects a
         random country from the list.
        """
        if not self.country_name:
            self.country_name = random.choice(self.country_names)
        print(f"Country selected: {self.country_name}")

    def driver_scrape(self):
        """
        Orchestrates the scraping process: initializes the Selenium driver, scrapes
         the data, and saves it.
        """
        self.driver_selenium()
        self.make_dataframe()
        self.save_csv_file()
        self.save_json_file()

    def driver_selenium(self):
        """
        Initializes the Selenium WebDriver, navigates to the FACTBOOK_URL, and
         clicks on the specified country link.
        """
        try:
            self.driver = webdriver.Firefox(service=FoxService(GeckoMan().install()))
            self.driver.get(FACTBOOK_URL)
            randsleep()
            country_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.country_name))
            )
            country_link.click()
            randsleep()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME,
                                                     self.article_class))
            )
            self.html = self.driver.page_source
        except (Exception,) as e:
            print(f"Link click error: {e}.")
        finally:
            self.driver.quit()
            if self.html:
                self.make_beautiful_soup()

    def make_beautiful_soup(self):
        """
        Parses the HTML of the scraped page using BeautifulSoup and extracts
         relevant data into a dictionary.
        """
        if self.html:
            try:
                self.soup = BeautifulSoup(self.html, "html.parser")
                all_content = self.soup.find(class_="article-content")
                mainsects = all_content.find_all(class_="wfb-nav-article")
                for mainsect in mainsects:
                    mainsect_title = mainsect.find("h2").text
                    subsects = mainsect.select("div")
                    for subsect in subsects:
                        try:
                            subsect_title = f"{mainsect_title}: {subsect.find('h3').text}"
                            subsect_tags = subsect.find("p")
                            subsecttext_list = []
                            for subsect_tag in subsect_tags.children:
                                subsect_text = subsect_tag.text.strip()
                                if subsect_text:
                                    subsecttext_list.append(subsect_text)
                            subsecttext_str = ";".join([i for i in subsecttext_list])
                            self.df_dict[subsect_title] = subsecttext_str
                        except (Exception, AttributeError):
                            pass
            except (Exception,) as e:
                print(f"`make_beautiful_soup` error: {e}.")
        else:
            print("`make_beautiful_soup` error: self.html not available for parsing.")

    def make_dataframe(self):
        """
        Converts the scraped data dictionary into a pandas DataFrame and optionally
         prints it.
        """
        try:
            self.df = pd.DataFrame(self.df_dict, index=[0])
            if self.print_df:
                print(tabulate(self.df, headers="keys", tablefmt="psql"))
        except (ValueError, Exception) as e:
            print(f"`make_dataframe` error: {e}.")

    def save_csv_file(self):
        """
        Saves the DataFrame to a CSV file if the save_csv attribute is True.
        """
        if self.save_csv and not self.df.empty:
            file_name = create_filename(self.country_name, "csv")
            csv_path = os.path.join(self.current_dir, "savedFiles", file_name)
            self.df.to_csv(csv_path, index=False)
            print("Successfully created .csv file.")
        else:
            print("No valid dataframe to create .csv file from.")

    def save_json_file(self):
        """
        Saves the DataFrame to a JSON file if the save_json attribute is True.
        """
        if self.save_json and not self.df.empty:
            file_name = create_filename(self.country_name, "json")
            json_path = os.path.join(self.current_dir, "savedFiles", file_name)
            self.df.to_json(json_path, orient="records", lines=True, force_ascii=False)
            print("Successfully created .json file.")
        else:
            print("No valid dataframe to create .json file from.")


# Local implementation for testing:
if __name__ == "__main__":
    # Returns randomly selected country since no country param entered:
    world_factbook = WorldFactbook(print_df=False, save_csv=True, save_json=True)
    world_factbook.driver_scrape()
    # help(WorldFactbook)
