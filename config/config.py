"""
config.py

Contains static configurations and utility functions for the World Factbook scraping project.

This includes the URL for the CIA World Factbook, a function to generate filenames in a consistent
format, and a function to introduce random sleep intervals between requests to mimic human behavior
and reduce the likelihood of being detected as a bot.
"""

import random  # randint function used to create ints for random delay times.
import time  # sleep function used to create delays.

# URL for the CIA World Factbook country data codes page:
FACTBOOK_URL = "https://www.cia.gov/the-world-factbook/references/country-data-codes"


def create_filename(name, extension):
    """
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
    """
    # Sanitize and standardize the country name to generate a consistent file name:
    file_prefix = "_".join(name.replace(",", "").split()).lower()
    file_name = f"{file_prefix}.{extension}"
    return file_name


def randsleep():
    """
    Pauses the execution for a random interval between 5 and 10 seconds.

    This function is used to mimic human browsing behavior and delay the execution
     of subsequent actions, which can help in avoiding detection by anti-bot mechanisms
     on websites, also helps to respect the site's traffic load.
    """
    # Random sleep to mimic human interaction respect site's load:
    time.sleep(random.randint(5, 10))


if __name__ == "__main__":
    help(create_filename)
    help(randsleep)
