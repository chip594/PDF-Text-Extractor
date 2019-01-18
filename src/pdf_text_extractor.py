#   pdf_text_extractor.py

from tika import parser

names = []

raw = parser.from_file('input0.pdf')
output_file = open('output.txt', 'w')

name = ''.join(raw['content'])

print(name)

#   print(raw['content'])