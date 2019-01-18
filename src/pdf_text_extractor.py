#   pdf_text_extractor.py

import sys
import os
from tika import parser
from tika import unpack
import numpy


#input_file = sys.argv[1]

badges = []
names = []
titles = []
name_title = {}

parsed_file = open('parsed_file.txt', 'w')
output_file = open('output.txt', 'w')

file_list = os.listdir(os.getcwd())
for files in file_list:
    if files.endswith('.pdf'):
        parsed = unpack.from_file(files)
        parsed_file.write(parsed['content'])
parsed_file.close()

with open('parsed_file.txt', 'r') as f:
    line = f.read()
    line = line[1:-4]
    line = line.split('\n')
    badges.append(line)

badges = numpy.ravel(badges)

names = badges[0::2]
titles = badges[1::2]

for name, title in zip(names, titles):
    name = name.rstrip()
    name_title[name] = title

print(name_title)

for name, title in name_title.items():
    output_file.write('%s   %s\n' % (name, title))

output_file.close()