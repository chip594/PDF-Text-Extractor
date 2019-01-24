from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import os, sys, getopt
import pymsgbox

def get_user_input():
    user_input = pymsgbox.prompt('Enter name', default=add_txt_ext(''), title='FBPI .pdf Text Extractor')
    if user_input == None:
        exit(0)
    return user_input

def add_txt_ext(user_input):
    if len(user_input) < 1:
        return '_output'
    else:
        return user_input

def pdf_to_text(pdf_file, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    input_file = open(pdf_file, 'rb')
    for page in PDFPage.get_pages(input_file, pagenums):
        interpreter.process_page(page)
    input_file.close()
    converter.close()
    text = output.getvalue()
    output.close()
    return text

def format_text(text):
    name_badge = text.split('\n')
    return name_badge

def main(): 
    user_input = get_user_input()
    output_file = open(add_txt_ext(user_input) + '.txt', 'w')

    file_list = os.listdir(os.getcwd())

    name = []
    title = []
    badges = []

    for files in file_list:
        if files.endswith('.pdf'):
            name_badge = pdf_to_text(files)
            name_badge = format_text(name_badge)
            print(type(name_badge))
            print(name_badge)
            #output_file.write(name_badge)

    output_file.close()

if __name__ == '__main__':
    main()