from amazon_scrapper import *
from flipkart_scrapper import *
import sys

def main():
    url = input("Enter the URL: ")
    if "amazon" in url:
        product_amazon = amazon(url)
        product_amazon.print_product_info()

        print("Would you like to search for the product automatically on Flipkart?")
        print("Press 'y' to continue. Press any other key to enter the link manually.")
        response = input("> ")

        if response == "y" or response == "Y":
            flipkart_link = flipkart.search_item(product_amazon.name)
            if (flipkart_link == "exit"):
                sys.exit("Exiting...")
        else:
            flipkart_link = input("Enter the Flipkart URL: ")
        
        product_flipkart = flipkart(flipkart_link)
        product_flipkart.print_product_info()


    elif "flipkart" in url:
        product_flipkart = flipkart(url)
        product_flipkart.print_product_info()

        print("Would you like to search for the product automatically on Amazon? Press 'y' to continue. Press any other key to enter the link manually.")
        response = input("> ")

        if response == "y" or response == "Y":
            amazon_link = amazon.search_item(product_flipkart.name)
            if (amazon_link == "exit"):
                sys.exit("Exiting...")
        else:
            amazon_link = input("Enter the Amazon URL: ")

        product_amazon = amazon(amazon_link)
        product_amazon.print_product_info()
        
    else:
        print("Website Not Supported")
    
    return 0

if __name__ == '__main__':
    main()

