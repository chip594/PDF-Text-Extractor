#   pdf_text_extractor.py

import os
from tika import unpack
import pymsgbox

def add_txt_ext(user_input):
    if len(user_input) < 1:
        return '_output'
    else:
        return user_input

user_input = pymsgbox.prompt('Enter the desiered name of the output file: (without ".txt")', default=add_txt_ext(''), title='FBPI .pdf Text Extractor')

if user_input == None:
    exit(0)

output_file = open(add_txt_ext(user_input) + '.txt', 'w')

file_list = os.listdir(os.getcwd())
for files in file_list:
    if files.endswith('.pdf'):
        parsed = unpack.from_file(files)
        parsed = parsed['content']
        parsed = parsed[1:-4]
        name, title = parsed.split('\n')
        output_file.write('%s   %s\n' % (name, title))

output_file.close()