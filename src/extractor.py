# extractor.py

from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

class PDFExtractor(object):

    def pdf_to_text(self, pdf_file, pages=None):
        pass