import PySimpleGUI as sg
import json

with open ("library.json") as json_file:
    library = json.load(json_file)


table_data = [[isbn, item['title'], item['author'], item['price'], item['quantity in stock']] for isbn, item in library.items()]

# ---------- 1. LAYOUT ----------
# A layout is a list of "rows"; each row is a list of widgets.
layout = [
    [sg.Button("Add a book"), 
     sg.Button("Search by ISBN"), 
     sg.Button("Search by Author, Title"), 
     sg.Button("Change book quantity"), 
     sg.Button("Delete")],

    [sg.Text("Library:")],

    [sg.Table(  values=table_data, 
                headings=["ISBN", "TITLE", "AUTHOR", "PRICE", "STOCK"],
                key = "-TABLE-",
                num_rows=25,              # Shows 25 rows before scrolling
                auto_size_columns=False,  # Turn off so we can control width
                col_widths=[15, 25, 20, 8, 8], # Give columns proper widths
                justification="left",
                expand_x=True,            # <--- Fills horizontal space
                expand_y=True,
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
    if event in (sg.WIN_CLOSED, "Exit"):
        break


# ---------- 4. CLEANUP ----------
window.close()