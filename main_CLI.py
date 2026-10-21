import sys
import subprocess
import json
import os

with open ("library.json") as json_file:
    library = json.load(json_file)

def print_books():
    for isbn, info in library.items():
        print(f"Title: {info['title']}\n Author: {info['author']}\n Price:{info['price']}\n Quantity in stock:{info['quantity in stock']}\n ISBN:{isbn}\n")


def print_books_inTable():
    print (f"\n{'ISBN':<15} | {'Title:':<60} | {'Author':<20} | {'Price':<10} | {'Stock':<5}")
    print ("-" * 150)
    for isbn, info in library.items():
        print(f"{isbn:<15} | {info['title']:<60} | {info['author']:<20} | {info['price']:<10} | {info['quantity in stock']:<5}\n")

def is_double(x):
        try:
            float(x)
            return True
        except ValueError:
            return False

def clear_console():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    elif os.name == 'posix':
        print("\033[H\033[2J\033[3J", end="")
        
foundAmount = 0

while True:

    user_selection = input("\nHello! Select what would you like to do?\n" \
        "1. Check the booklist.    \n" \
        "2. Add a book.    \n" \
        "3. Search by ISBN.    \n" \
        "4. Search by Author or Title.    \n" \
        "5. Change the quantity of a certian book.    \n" \
        "6. Delete a book (using ISBN).    \n"
        "0. Exit.\n")


    match user_selection:
        case "1":
            clear_console()
            print_books_inTable()
        case "2":
            clear_console()
            while True:
                isbn=input("Enter an ISBN: ").strip()
                if isbn in library.keys():
                    print("This ISBN already exists!")
                    continue
                L = len(isbn)
                if L != 13 and L!= 10:
                    print("Incorrect length!")
                    continue
                b = all(char.isdigit() for char in isbn)
                if b == False:
                    print("Input only numbers!")
                    continue
                break

            while True:
                title=input("Enter a title: ").strip()
                if (len(title) < 1):
                    print("Please enter a valid title!")
                    continue
                break

            while True:
                author=input("Enter an author: ").strip()
                if (len(author) < 1):
                    print("Please enter a valid author!")
                    continue
                break

            while True:
                price=input("Please enter a price: ").strip()
                if is_double(price) == False:
                    print("Please input a valid price!")
                    continue
                double_price = float(price)
                if double_price < 0:
                    print("Please input a valid price!")
                    continue
                break

            while True:
                stock = input("Enter quantity in stock: ").strip()
                if stock.isdigit() == False:
                    print("Please enter a valid amount! ")
                    continue
                stock_convert = int(stock)
                if stock_convert < 0:
                    print("Please enter a valid amount! ")
                    continue
                break
            library[isbn]={
                "title": title,
                "author": author,
                "price": price,
                "quantity in stock": stock, 
             }
            clear_console()
            print(f"Successfully added '{title}' with ISBN '{isbn}'!\n")
            
        case "3":
            clear_console()
            while True:
                search_query = input("Enter the desired ISBN: ")
                if search_query in library:
                        print (f"\n{'ISBN':<15} | {'Title:':<60} | {'Author':<20} | {'Price':<10} | {'Stock':<5}")
                        print ("-" * 150)
                        info = library[search_query]
                        print(
                            f"{search_query:<15} | {info['title']:<60} | {info['author']:<20} | {info['price']:<10} | {info['quantity in stock']:<5}"
                        )
                else:
                    print("This ISBN does not exist!")
                    break
                break
        case "4":
            clear_console()
            while True:
                search_query = input("Enter the desired Author or Title: ")
                print (f"\n{'ISBN':<15} | {'Title:':<60} | {'Author':<20} | {'Price':<10} | {'Stock':<5}")
                print ("-" * 150)
                for key, info in library.items():
                    if search_query.lower() in info["title"].lower() or search_query.lower() in info["author"].lower():
                          isbn = key
                          print(f"{key:<15} | {info['title']:<60} | {info['author']:<20} | {info['price']:<10} | {info['quantity in stock']:<5}")
                          foundAmount+=1
                    else:
                        print(f"Found {foundAmount} results!")
                        foundAmount=0
                        break
                break
        case "5":
              clear_console()
              print_books_inTable()
              while True:
                isbn_input = input("Input the ISBN: ")
                if isbn_input in library:
                    while True:
                        desired_quantity = input("Input the desired quantity: ")
                        if desired_quantity.isdigit()==False:
                            print("Enter a valid amount!")
                            continue
                        if len(desired_quantity)<1:
                            print("Enter a valid amount!")
                            continue
                        break
                    library[isbn_input]["quantity in stock"] = desired_quantity
                else:
                    print("Enter a valid ISBN!")
                    continue
                break

        case "6":
            clear_console()
            print_books_inTable()
            while True:
                isbn_input_delete = input("Input the ISBN: ")
                if isbn_input_delete in library:
                    del library[isbn_input_delete]
                else:
                    print("Enter a valid ISBN!")
                    continue
                print(f"Book with ISBN {isbn_input_delete} was deleted!")
                break

        case "0":
                with open ("library.json", "w") as f:
                    json.dump(library, f, indent=4)
                clear_console()
                result = sys.exit("Goodbye!")
        case _:
                print("Unknown input!")
