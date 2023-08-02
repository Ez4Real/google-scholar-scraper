# Google Scholar Scraper

## Overview
The Google Scholar Scraper is a Python script that allows you to extract information from Google Scholar articles about "iMotions" Company. It utilizes the scholarly library to perform the search and retrieve article details such as title, authors, publication year, and publication URL. The extracted data is then saved to a Google Sheets spreadsheet using the gspread library.

## Technology Stack
- Python 3.10.0

## Project Setup
1. Clone the repository
2. Create a virtual environment: ```python -m venv env```
3. Activate the virtual environment:
    ```source env/bin/activate```  # Linux/Mac
    ```env\Scripts\activate```     # Windows
4. Install the required packages: ```pip install -r requirements.txt```
5. Create .env file in root directory and fill in the necessary ScraperAPI KEY and email id to which the google sheet will be shared
6. Place the client_key.json file in the root of the project from your Google App
