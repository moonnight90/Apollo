# Apollo.io Scraper

## Overview
This Python script allows you to scrape company data from Apollo.io using the Apollo API. It logs in to the Apollo.io platform using provided credentials and retrieves company information from a specified list.

## Prerequisites
- Python 3.x
- Required Python packages: `os`, `requests`, `time`, `getpass`, `pandas`

## Usage
1. Install the required packages:
   ```bash
   pip install requests pandas
   ```

2. Run the script:
   ```bash
   python apollo_scraper.py
   ```

3. Enter your Apollo.io email and password when prompted.

4. The script will prompt you to choose a list from your Apollo.io account. Enter the desired list number.

5. The script will then scrape company information from the selected list and save it to a CSV file named `companies_data.csv` in the script's directory.

6. If you want to scrape more lists, the script will ask if you want to continue. Enter 'Y' to scrape more lists or 'N' to exit.

## Important Notes
- Make sure to keep your Apollo.io credentials secure.
- The script appends the scraped data to the `companies_data.csv` file. If you want to start with a fresh file, delete the existing CSV file.

## Disclaimer
This script is for educational and personal use only. Be aware of the terms of service of the platforms you are scraping data from, and use this script responsibly.

## Author
[Ahmad Raza]

Feel free to modify the script to suit your needs and contribute to its improvement!
