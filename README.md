# PDF Text Extractor

### v2.0 
Version 2.0 is the same concept as version 1.0, aside from version 2.0 uses the pdfminer library instead of the tika library. Tika was producing an error when the Apache server didn't spin up fast enough upon startup.

PDF Text Extractor is a program that I wrote for a local company. The company receives orders from customers, in .pdf form. The text has to be manually transferred to place the actual order, which suffers the risk of a typo not to mention being very time consuming. A solution was requested to not only speed up the process but to also eliminate the possibility of a manual error.



## How it works!

 PDF Text Extractor will scan the current directory and open all of the files with the .pdf extension. It will use tika to unpack the encoded .pdf files and extract out the contents. The extracted contents are then formatted using the specified ‘name TAB title’ and printed to a single output file. The program will ask the user for a desired name for the output file, but if none is given then the program will default to _output.txt.


 PDF Text Extractor is written in Python 3.7

