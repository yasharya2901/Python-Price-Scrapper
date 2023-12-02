from amazon import *
from flipkart import *
import sys

def main(*args):
    if args:
        response = args[0]
    else:
        response = input("Enter the product name or URL: ")
    if "http" in response:
        url = response
        if "amazon" in url:
            product_amazon = amazon(url)
            product_amazon.print_product_info()

            print("Would you like to search for the product automatically on Flipkart?")
            print("Press 'y' to continue. Or Enter the Flipkart URL")
            response = input("> ")

            if response == "y" or response == "Y":
                flipkart_link = flipkart.search_item(product_amazon.name)
                if (flipkart_link == "exit"):
                    sys.exit("Exiting...")
            else:
                flipkart_link = response
            
            product_flipkart = flipkart(flipkart_link)
            product_flipkart.print_product_info()


        elif "flipkart" in url:
            product_flipkart = flipkart(url)
            product_flipkart.print_product_info()

            print("Would you like to search for the product automatically on Amazon?")
            print("Press 'y' to continue. Or Enter the Amazon URL")
            response = input("> ")

            if response == "y" or response == "Y":
                amazon_link = amazon.search_item(product_flipkart.name)
                if (amazon_link == "exit"):
                    sys.exit("Exiting...")
            else:
                amazon_link = response

            product_amazon = amazon(amazon_link)
            product_amazon.print_product_info()
            
        else:
            print("Website Not Supported")
    else:
        print("Where would you like to search the product? Amazon or Flipkart? ")
        platform = input("> ")
        if platform == "amazon" or platform == "Amazon":
            main(amazon.search_item(response))

        elif platform == "flipkart" or platform == "Flipkart":
            main(flipkart.search_item(response))

        else:
            sys.exit("Platform not supported.")
    return 0

if __name__ == '__main__':
    main()

