import os
import random
import sys
import time
from urllib.parse import urlparse
from colorama import init, Fore, Style

# Initialize colorama
init()

# Colors
red = Fore.RED
green = Fore.GREEN
defcol = Style.RESET_ALL

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
   ___
 o|* *|o  ╔╦═╦╗╔╦╗╔╦═╦╗
 o|* *|o  ║║╔╣╚╝║║║║║║║
 o|* *|o  ║║╚╣╔╗║╚╝║╩║║
  ║===/   ║╚═╩╝╚╩══╩╩╝║
   |||    ╚═══════════╝
   |||  K.E.U.R - I.P - A.N.N.A.Q.I.T.T.Y
   |||    ╔═╦═╦╦═╦╦═╗╔═╦╦══╦══╦╦╗
   |||    ║╩║║║║║║║╩║║╚║╠╗╔╩╗╔╩╗║
___|||___ ╚╩╩╩═╩╩═╩╩╝╚═╩╝╚╝ ╚╝ ╚╝

  By : AnnaQitty
  Github : github.com/annaqitty    
                                              
              
              
                          """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)

def menu():
    print(f"{green}=== MENU ==={defcol}")
    print("1. Remove Duplicate URLs")
    print("2. Extract Domains from URLs")
    print("0. Exit")
    choice = input("Enter your choice: ").strip()
    return choice

def add_http_prefix(url):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return "http://" + url

def remove_duplicate_urls(input_file, output_file):
    unique_urls = set()

    try:
        with open(input_file, 'r') as f:
            for line in f:
                url = line.strip()
                if url:  # Ensure line is not empty
                    url_with_http = add_http_prefix(url)
                    unique_urls.add(url_with_http)

        with open(output_file, 'w') as f:
            for url in unique_urls:
                f.write(url + '\n')

        print(f"{green}Unique URLs saved to {output_file}{defcol}")
    
    except IOError as e:
        print(f"{red}Error reading or writing files: {e}{defcol}")

def get_domains_from_urls(input_file, output_file):
    domains = set()

    try:
        with open(input_file, 'r') as f:
            for line in f:
                url = line.strip()
                if url:  # Ensure line is not empty
                    parsed_url = urlparse(url)
                    domain = parsed_url.netloc
                    if domain:
                        domains.add(domain)

        with open(output_file, 'w') as f:
            for domain in domains:
                f.write(domain + '\n')

        print(f"{green}Domains extracted and saved to {output_file}{defcol}")
    
    except IOError as e:
        print(f"{red}Error reading or writing files: {e}{defcol}")

def get_input_filename(prompt):
    while True:
        filename = input(prompt).strip()
        if not filename:
            return None
        if os.path.isfile(filename):
            return filename
        else:
            print(f"{red}File '{filename}' not found. Please create the file and input URLs.{defcol}")

# Example usage:
def main():
    logo()  # Display logo first
    while True:
        choice = menu()
        
        if choice == "1":
            print(f"{green}=== REMOVE DUPLICATE URLs ==={defcol}")
            input_file = get_input_filename("Enter the input file name (or press Enter to exit): ")
            if input_file:
                output_file = input(f"{green}Enter the filename to save unique URLs: {defcol}").strip()
                remove_duplicate_urls(input_file, output_file)
        elif choice == "2":
            print(f"{green}=== EXTRACT DOMAINS FROM URLs ==={defcol}")
            input_file = get_input_filename("Enter the input file name (or press Enter to exit): ")
            if input_file:
                output_file = input(f"{green}Enter the filename to save domains: {defcol}").strip()
                get_domains_from_urls(input_file, output_file)
        elif choice == "0":
            print(f"{green}Thank you! Goodbye.{defcol}")
            break
        else:
            print(f"{red}Invalid choice. Please choose 1, 2, or 0.{defcol}")

if __name__ == "__main__":
    main()
