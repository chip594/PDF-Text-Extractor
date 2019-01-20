#   pdf_text_extractor.py

import os
from tika import unpack

output_file = open('output.txt', 'w')

file_list = os.listdir(os.getcwd())
for files in file_list:
    if files.endswith('.pdf'):
        parsed = unpack.from_file(files)
        parsed = parsed['content']
        parsed = parsed[1:-4]
        name, title = parsed.split('\n')
        output_file.write('%s   %s\n' % (name, title))

output_file.close()