'''
File:           pdf_text_extractor.py
Author:         Chip Newman
Date:           01/24/2019
Version:        2.0

Description:    Version 2.0 is the same concept as version 1.0, aside from
                version 2.0 uses the pdfminer library instead of the 
                tika library. Tika was producing an error when the Apache 
                server didn't spin up fast enough upon startup.

                This program is designed for a two-line name badge.
                line #1: Name
                line #2: Title
    
                This program will read every .pdf file within a directory.
                It will convert the .pdf file to text and extract the 
                contents. The contents are wrote to a .txt file in the
                format of 'name TAB title'. The program will ask the user
                for a desired output file name, but if one if not provided
                then a default name will be used.

                The .exe file must be within the same directory as the
                .pdf files.
'''

from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import os, sys, getopt
import pymsgbox

# returns a name of the output file
def get_user_input():
    user_input = pymsgbox.prompt('Enter name', default=add_txt_ext(''), title='FBPI .pdf Text Extractor')
    # properly closes the program if the user clicks 'cancel' on the prompt
    if user_input == None:
        exit(0)
    return user_input

# ensures that the output file will have a name
def add_txt_ext(user_input):
    if len(user_input) < 1:
        return '_output'
    else:
        return user_input

# takes in a pdf file as a parameter 
#   returns the contents as a string
def pdf_to_text(pdf_file, pages=None):
    # allows multiple pages to be passed in as a parameter
    if pages:
        num_of_pages = set(pages)
    else:
        num_of_pages = set()

    output = StringIO()
    manager = PDFResourceManager()

    # parameters require a resource manager and an output text stream
    converter = TextConverter(manager, output, laparams=LAParams())

    # parameters require a resource manager and a text converter
    interpreter = PDFPageInterpreter(manager, converter)

    input_file = open(pdf_file, 'rb')
    for page in PDFPage.get_pages(input_file, num_of_pages):
        interpreter.process_page(page)
    input_file.close()
    converter.close()

    text = output.getvalue()
    output.close()

    return text

# takes in a string as a parameter
#   returns the string in a specific format
#   format:     name TAB title
def name_tab_title(text):
    # stores contents of the input text into a list
    name_badge = text.split('\n')

    badges = []

    # strip the whitespace from every element
    for element in name_badge:
        badges.append(element.strip())

    # return true for as long as the badge has a blank line
    while badges.count(''):
        badges.remove('')
 
    # stores the last string addedsd to the badges stack
    title = badges.pop()
    # stores the first string added to the badges stack
    name = badges.pop()

    # formats the string as 'name TAB title'
    name_badge = ('%s\t%s\n' % (name, title))

    return name_badge

def main(): 
    # stores the name of the output file
    user_input = get_user_input()
    # creates the output .txt file
    output_file = open(add_txt_ext(user_input) + '.txt', 'w')

    # stores a list of all the files in the current working directory
    file_list = os.listdir(os.getcwd())

    # iterates through all the files in the file list
    for files in file_list:
        # will only process .pdf files
        if files.endswith('.pdf'):
            # stores the formated string
            #   pdf_to_text(): will convert the contents of each pdf file to string
            #   name_tab_title(): will provide the desired formatted string
            name_badge = name_tab_title(pdf_to_text(files))
            # writes the formated string to the output .txt file
            output_file.write(name_badge)

    output_file.close()

if __name__ == '__main__':
    main()