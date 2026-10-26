import PySimpleGUI as sg
import json

def is_double(x):
        try:
            float(x)
            return True
        except ValueError:
            return False

with open ("library.json") as json_file:
    library = json.load(json_file)

def open_addBook_window():
    layout = [
         [sg.Text("Enter an ISBN:")],
         [sg.Input(default_text="", key = '-ISBN_INPUT-')],
         [sg.Text("Enter a title:")],
         [sg.Input(default_text="", key= '-TITLE_INPUT-')],
         [sg.Text("Enter an Author:")],
         [sg.Input(default_text="", key= '-AUTHOR_INPUT-')],
         [sg.Text("Enter a price:")],
         [sg.Input(default_text="", key= '-PRICE_INPUT-')],
         [sg.Text("Enter quantity in stock:")],
         [sg.Input(default_text="", key= '-STOCK_INPUT-')],
         [sg.Button("Save")],
    ]
    addBookWindow = sg.Window("Add a book!",layout, modal=True)

    while True:
            event, values = addBookWindow.read()
            if event == sg.WIN_CLOSED or event == "Close Window 2":
                break

            if event =="Save":
                 raw_ISBN = values["-ISBN_INPUT-"]
                 raw_Title = values["-TITLE_INPUT-"]
                 raw_Author = values["-AUTHOR_INPUT-"]
                 raw_Price = values["-PRICE_INPUT-"]
                 raw_Stock = values["-STOCK_INPUT-"]

                 errors = []
                 if not raw_ISBN:
                      errors.append("ISBN can not be empty.\n")
                 L = len(raw_ISBN)
                 if raw_ISBN in library.keys():
                      errors.append("This ISBN already exists.\n")
                 if L != 13 and L!= 10:
                      errors.append("Incorect length.\n")
                 b = all(char.isdigit() for char in raw_ISBN)
                 if b == False:
                      errors.append("Input only numbers.\n")

                 if not raw_Title:
                     errors.append("Title can not be empty.\n")

                 if not raw_Author:
                     errors.append("Author can not be empty.\n")
                 if not raw_Price:
                    errors.append("Price cannot be empty.\n")
                 else:
                    try:
                        double_raw_price = float(raw_Price)
                        if double_raw_price < 0:
                            errors.append("Price cannot be negative.\n")
                    except ValueError:
                        errors.append("Price must be a valid number.\n")

                 if not raw_Stock:
                      errors.append("Stock cant be empty.\n")
                 elif raw_Stock.isdigit() == False:
                      errors.append("Stock must be an integer.\n")
                 else:
                    stock_amount = int(raw_Stock)
                    if stock_amount < 0:
                        errors.append("Stock must be a positive integer.\n")
                 if errors:
                    sg.popup_error("\n".join(errors), title="Error.")
                 else:
                      library[raw_ISBN]={
                          "title": raw_Title,
                          "author": raw_Author,
                          "price": raw_Price,
                          "quantity in stock": raw_Stock,
                      }
                      sg.popup("Data saved successfully.")
                      break
    addBookWindow.close()
    return library


def open_quantity_window():
        layout = [
         [sg.Text("Enter an ISBN:")],
         [sg.Input(default_text="", key = '-ISBN_INPUT-')],
         [sg.Text("Enter the desired quantity in stock:")],
         [sg.Input(default_text="", key= '-STOCK_INPUT-')],
         [sg.Button("Save")],
        ]
        quantityWindow=sg.Window("Edit the quantity",layout, modal=True)
        while True:
            event, values = quantityWindow.read()
            if event == sg.WIN_CLOSED or event == "Close Window 2":
                break             
            if event == "Save":
                raw_ISBN = values["-ISBN_INPUT-"]
                raw_Stock= values["-STOCK_INPUT-"]
                errors=[]
                if raw_ISBN not in library:
                    errors.append("Such book does not exist!")
                if not raw_Stock:
                      errors.append("Stock cant be empty.\n")
                elif raw_Stock.isdigit() == False:
                      errors.append("Stock must be an integer.\n")
                else:
                    stock_amount = int(raw_Stock)
                    if stock_amount < 0:
                        errors.append("Stock must be a positive integer.\n")
                if errors:
                    sg.popup_error("\n".join(errors), title="Error.")
                else:
                    library[raw_ISBN]["quantity in stock"] = raw_Stock
                    sg.popup("Quantity changed successfully.")
                    break
        quantityWindow.close()
        return library

def open_search_window():
    table_data_search = [[isbn, item['title'], item['author'], item['price'], item['quantity in stock']] for isbn, item in library.items()]

    layout = [
        [sg.Text("Input ISBN, Author or Title:"),
        sg.Input(default_text="", key= '-SEARCH_INPUT-'),
        sg.Button("Search"),
        [sg.Table( values=table_data_search, 
                headings=["ISBN", "TITLE", "AUTHOR", "PRICE", "STOCK"],
                key = "-TABLE_SEARCH-",
                num_rows=25,              # Shows 25 rows before scrolling
                auto_size_columns=False,  # Turn off so we can control width
                col_widths=[15, 25, 20, 8, 8], # Give columns proper widths
                justification="left",
                expand_x=True,            # <--- Fills horizontal space
                expand_y=True,
                                )
            ]
        ]
    ]
    SearchWindow = sg.Window("Search",layout, modal=True)
    while True:
            event, values = SearchWindow.read()
            if event == sg.WIN_CLOSED or event == "Close Window 2":
                break
            if event == "Search":
                raw_Input = values["-SEARCH_INPUT-"].strip().lower()
                filtered_data= []
            for isbn, item in library.items():
                if (raw_Input in isbn.lower() or 
                    raw_Input in item['title'].lower() or
                    raw_Input in item['author'].lower()):
                    filtered_data.append([
                        isbn, 
                        item['title'], 
                        item['author'], 
                        item['price'], 
                        item['quantity in stock']
                    ])


            if not raw_Input:
                table_data_search = [[isbn, item['title'], item['author'], item['price'], item['quantity in stock']] for isbn, item in library.items()]

                
            SearchWindow['-TABLE_SEARCH-'].update(values=filtered_data)
    SearchWindow.close()



table_data = [[isbn, item['title'], item['author'], item['price'], item['quantity in stock']] for isbn, item in library.items()]

# ---------- 1. LAYOUT ----------
# A layout is a list of "rows"; each row is a list of widgets.
layout = [
    [sg.Button("Add a book"), 
     sg.Button("Change book quantity"), 
     sg.Button("Delete"),
     sg.Button("Search by ISBN, Author, Title")],

[sg.Table(      values=table_data, 
                headings=["ISBN", "TITLE", "AUTHOR", "PRICE", "STOCK"],
                key = "-TABLE-",
                num_rows=25,              # Shows 25 rows before scrolling
                auto_size_columns=False,  # Turn off so we can control width
                col_widths=[15, 25, 20, 8, 8], # Give columns proper widths
                justification="left",
                expand_x=True,            # <--- Fills horizontal space
                expand_y=True,
                select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
            )
    ]
]

# ---------- 2. WINDOW ---------
window = sg.Window("Library management system", layout)

# ---------- 3. EVENT LOOP ----------
# This is the heart of every PySimpleGUI app.
while True:
    event, values = window.read()

    # Window closed with the X button, or "Exit" clicked
    if event == sg.WIN_CLOSED or event == "Exit":
        with open ("library.json", "w") as f:
            json.dump(library, f, indent=4)
        break
    
    if event == "Add a book":
         open_addBook_window()

         table_data = [[isbn, item['title'], item['author'], item['price'], item['quantity in stock']] for isbn, item in library.items()]

    if event == "Delete":
        selected_rows = values['-TABLE-']

        if selected_rows:

            keys_list = list(library.keys())

            key_to_delete = [keys_list[row_index] for row_index in selected_rows]

            for key in key_to_delete:
                del library[key]

            table_data = [[isbn, item['title'], item['author'], item['price'], item['quantity in stock']] for isbn, item in library.items()]

        else:
            sg.popup("Choose a row first.")

    if event == "Change book quantity":
        open_quantity_window()
        table_data = [[isbn, item['title'], item['author'], item['price'], item['quantity in stock']] for isbn, item in library.items()]

    if event == "Search by ISBN, Author, Title":
        open_search_window()

    window['-TABLE-'].update(values=table_data)

# ---------- 4. CLEANUP ----------
window.close()