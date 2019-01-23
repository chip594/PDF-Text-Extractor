#   pdf_text_extractor.py

import os
from tika import unpack
import pymsgbox

#   ensures that the output file is a .txt file
#   if no name provided by the user, _output.txt will be the default
def add_txt_ext(user_input):
    #   runs if the prompt box is empty
    if len(user_input) < 1:
        return '_output'
    #   runs if user input is provided
    else:
        return user_input

#   ask the user for a desired output file name
user_input = pymsgbox.prompt('Enter the desiered name of the output file: (without ".txt")', default=add_txt_ext(''), title='FBPI .pdf Text Extractor')

#   closes the progrm if the user clicks the 'cancel' button
if user_input == None:
    exit(0)
    
#   stores a list a files within the current working directory
file_list = os.listdir(os.getcwd())

#   creates the output file, name is based on user input
output_file = open(add_txt_ext(user_input) + '.txt', 'w')

#   cycles through every file in the file list
for files in file_list:
    #   only opens .pdf files
    if files.endswith('.pdf'):
        #   uses Tika to unpack the contents of the .pdf file
        parsed = unpack.from_file(files)
        #   parsed, stores the contents of the .pdf file as a string
        parsed = parsed['content']
        #   strips the whitespace from the parsed string
        parsed = parsed.strip()
        #   splits the string at the return char from the format: 'name\n title'
        name, title = parsed.split('\n')
        #   strips the whitespace from the name
        name = name.strip()
        #   strips the whitespace from the title
        title = title.strip()
        #   formats the output file: 'name TAB title'
        output_file.write('%s\t%s\n' % (name, title))

#   closes the output file
output_file.close()