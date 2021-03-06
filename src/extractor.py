'''
PDF Text Extractor Module

This module will extract the text from a .pdf file and return the
contents as a string. 
'''

from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import getopt

class PDFExtractor(object):

    # takes in a parameter of a pdf file
    # returns the contents as a string
    def pdf_to_text(self, pdf_file, pages=None):
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