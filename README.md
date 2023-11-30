# Python Price Scraper
The Python Price Scraper is a tool that fetches product information (name and price) from Amazon and Flipkart product pages using their URLs.

## Setup Instructions
Follow these steps to get the Python Price Scraper up and running:

1. **Install Required Modules**: The `requirements.txt` file contains a list of necessary modules. Install them by running the command `pip install -r requirements.txt`.
2. **Execute the Script**: Run the `main.py` script using the command `python main.py` or `python3 main.py`.

## Usage Guide

Here’s how to use the Python Price Scraper:

1. **Enter URL**: Upon executing the main.py script, you will be prompted to enter either a URL or the name of the product you want to search for. If you provide a URL, ensure it is from a product page on Amazon or Flipkart. Entering a URL from a different platform will result in an error message, terminating the script. If you enter the product name, you will be prompted to choose whether to search for it on Amazon or Flipkart.
2. **View Product Information**: If the URL is valid, the script will display the product information, including the source (Amazon or Flipkart), name, and price.
3. **Search on Other Platform**: The script will then ask if you want to search for the same product on the other platform (Amazon or Flipkart) automatically, or if you would like to enter the link manually. Press y to continue the automatic search, or enter the link manually.
4. **View Product Information from Other Source**: The script will display the same product information, but this time from the other source.

Please note that the Python Price Scraper is designed to work only with Amazon and Flipkart product pages. Other URLs may cause the script to terminate with an error.
