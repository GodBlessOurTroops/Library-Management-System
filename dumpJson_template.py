import json

library = {
    "9780545582889":{
        "title" : "Harry Potter and the Sorcerer's Stone",
        "author": "J. K. Rowling",
        "price": 15.00,
        "quantity in stock": 5,
    },
    "9780451524935": {
        "title": "1984",
        "author": "George Orwell",
        "price": 12.99,
        "quantity in stock": 8,
    },
    "9780060935467": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "price": 14.50,
        "quantity in stock": 12,
    },
    "9780743273565": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "price": 10.00,
        "quantity in stock": 4,
    },
    "9780441172719": {
        "title": "Dune",
        "author": "Frank Herbert",
        "price": 18.00,
        "quantity in stock": 20,
    },
    "9780547928227": {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "price": 13.95,
        "quantity in stock": 7,
    },
}

with open ("library.json", "w") as f:
    json.dump(library, f, indent=4)