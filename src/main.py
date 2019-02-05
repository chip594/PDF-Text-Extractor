# main.py

import os
import pymsgbox

from extractor import PDFExtractor
from formatter import TextFormatter

# returs a name of the output file
def get_user_input():
    user_input = pymsgbox.prompt('Enter name', default=add_txt_ext(''), title='FBPI .pdf Text Extractor')
    # closes program if user clicks cancel
    if user_input == None:
        exit(0)
    return user_input

# ensure the output file has a name
def add_txt_ext(user_input):
    if len(user_input) < 1:
        return '_output'
    else:
        return user_input

# main function, runs on program startup
def main():
    #create an pdf extractor
    extractor = PDFExtractor()

    # create a text formatter
    formatter = TextFormatter()

    # stores the name of the output file
    user_input = get_user_input()

    # create the output .txt file
    output_file = open(add_txt_ext(user_input) + '.txt', 'w')

    # stores a list of all files in the current directory
    file_list = os.listdir(os.getcwd())

    # interate through all the files in the file list
    for files in file_list:
        # will only process .pdf files
        if files.endswith('.pdf'):
            # convert contents of each pdf file to a string
            name_badge = extractor.pdf_to_text(files)

