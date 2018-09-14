from list_fn import *
from html_fn import *
from pdf_fn import *

path = 'C:/users/luke/papers/'
pdfpath_list = path_to_pdfpathlist(path)

print (pdfpath_list[0])

tempout = open('tempout.txt', 'w')
tempout.write(pdf_to_str(pdfpath_list[0]))
tempout.close()

print ("done")