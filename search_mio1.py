import os
import re
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

pre = "/home/mau/Scaricati/pdf/"
li = os.listdir(pre)
print("listdir=",li)
n = 0
for i in range(len(li)):
    if re.findall(".pdf",li[i]) != []:
        n = n+1
        print("Found!",n)
        output_string = StringIO()
        with open(pre+li[i], 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
        print(output_string.getvalue())
# start to read a text file previously stored (to be done)
