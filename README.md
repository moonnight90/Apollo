# Apollo.io Data Scraper

This Python script allows you to scrape data from [Apollo.io](https://app.apollo.io/) using their API. It can retrieve information about companies and people associated with specific lists.

## Prerequisites

Before using the script, ensure you have the following:

- Python installed (version 3.x recommended)
- Required Python packages installed: `requests`, `pandas`

```bash
pip install requests pandas
```

## Usage

1. Clone the repository or download the script directly.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:

```bash
python apollo_scraper.py
```

4. Enter your Apollo.io credentials (email and password) when prompted.
5. Choose whether to scrape data for people or companies.
6. Select the list you want to scrape data from.
7. The script will start scraping the data and save it to a CSV file (`companies_data.csv` for companies, `people_data.csv` for people).
8. If you want to scrape more lists, the script will prompt you accordingly.

**Note:** It is advisable to review and understand Apollo.io's terms of service and API usage policies before using this script.

## Disclaimer

This script is provided for educational and informational purposes only. Use it responsibly and ensure compliance with Apollo.io's terms of service. The script author is not responsible for any misuse or violation of terms.

## References

- [Apollo.io API Documentation](https://docs.apollo.io/docs/introduction)
- [Requests Library Documentation](https://docs.python-requests.org/en/latest/)

Feel free to customize the script based on your specific needs or contribute to its improvement. Happy scraping!