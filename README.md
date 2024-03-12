
# InfoScraper

## Description
This Python script scrapes faculty information, specifically names and email addresses. The data extracted is then compiled into a CSV file for easy access and manipulation. The script utilizes `requests-html` for web scraping and `pandas` for data manipulation and saving.

## Requirements
- `Python 3.x`
- `pandas`
- `requests-html`

You can install the necessary libraries using pip:

```bash
pip install pandas requests-html
```

## Setup
1. Clone the repository or download the script to your local machine.
3. Install the required Python packages listed under [**Requirements**](#requirements).

## Usage
To run the script, navigate to the directory containing the script and execute it with Python:

```bash
python faculty_scraper.py
```

The script will scrape the faculty information from the specified URL and save it to a CSV file named `filename.csv` in the same directory.

## Output
The output CSV file will contain the following columns:
- `FName`: The first names of the faculty members.
- `Email`: The email addresses of the faculty members.
