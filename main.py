from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import PyPDF3
import pyttsx3
import pdfplumber

root = Tk()

root.title('Convert Your PDF To Audio')
root.geometry('600x400')

entry_path = tk.Entry(root, font=('#82AAE3', 16))
btn_browse = tk.Button(root, text='Select Your PDF', font=('verdana', 12))
instruct = tk.Label(root, text="Input A Name for Your AudioBook and Press Convert.")
entry = tk.Entry(root, font=('#82AAE3', 16))

pdf_text = ""


def find_file():
    global filepath
    global pdf_text

    file = filedialog.askopenfile(mode='r', filetypes=[('PDF Files', '*.pdf')])
    if file:
        filepath = os.path.abspath(file.name)

    book = open(filepath, 'rb')
    reader = PyPDF3.PdfFileReader(book)
    pages = reader.numPages

    with pdfplumber.open(filepath) as pdf:
        for a in range(0, pages):
            page = pdf.pages[a]
            text = page.extract_text()
            pdf_text += text

    entry_path.insert(0, filepath)


def audiobook():
    name = entry.get()
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.save_to_file(pdf_text, f'{name}.mp3')
    engine.runAndWait()


btn_browse['command'] = find_file

entry_path.grid(column=1, row=0, pady=20, padx=40)
btn_browse.grid(column=2, row=0, pady=20, padx=20)

instruct.grid(column=1, row=1)
entry.grid(column=2, row=1)

ttk.Button(root, text="Press Here To Convert", width=20, command=audiobook).grid(column=1, row=2, pady=20, columnspan=2)

root.mainloop()
