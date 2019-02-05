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
