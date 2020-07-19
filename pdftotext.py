# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:40:39 2020

@author: wwwds
"""

from PyPDF2 import PdfFileReader
pdfFile = open('mypdf.pdf','rb')
pdfReader = PdfFileReader(pdfFile)
print("Pdf File name: " + str(pdfReader.getDocumentInfo().title))
print("Pdf File Created by : " + str(pdfReader.grtDocumentInfo().creator))
print("-------------------------------------")
numOfPages=pdfReader.getNumOfPages()
for i in range(0,numOfPages):
    print("Page Number: " + str(i))
    print("-----------------------")
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())
    print("----------------------------------")
pdfFile.close()