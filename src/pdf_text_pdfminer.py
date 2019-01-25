from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import os, sys, getopt
import pymsgbox
from collections import deque

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
    badge_queue = []

    name_badge = text.split('\n')
    for element in name_badge:
        badge_queue.append(element.strip())
    while badge_queue.count(''):
        badge_queue.remove('')
    title = badge_queue.pop()
    name = badge_queue.pop()

    name_badge = ('%s\t%s\n' % (name, title))
    return name_badge

def main(): 
    user_input = get_user_input()
    output_file = open(add_txt_ext(user_input) + '.txt', 'w')

    file_list = os.listdir(os.getcwd())

    for files in file_list:
        if files.endswith('.pdf'):
            name_badge = format_text(pdf_to_text(files))
            output_file.write(name_badge)

    output_file.close()

if __name__ == '__main__':
    main()