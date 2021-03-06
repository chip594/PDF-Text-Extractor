'''
PDF Text Extractor Main Module

This module will read every .pdf file within a directory. It will 
use the PDFExtractor to extract its contents to a string. That 
string will then be passed to TextFormatter where it will be 
properly formatted to the desired format.

The module will ask the user for a desired output file name, but 
if one if not provided then a default name will be used.

The .exe file must be within the same directory as the .pdf files.
'''

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
            
            # formats the string to the propper format
            name_badge = formatter.name_tab_title(name_badge)

            # writes the formatted string to the output file
            output_file.write(name_badge)

    output_file.close()

if __name__ == '__main__':
    main()
