from lp3fn import *

path = 'C:/users/luke/papers/'
pdf_list = path_to_pdf_list(path)
txt_list = pdf_list_to_txt_list(pdf_list)
info_list = txt_list_to_info_list(txt_list)
info_list_wH = txt_list_to_info_list_wH(txt_list)

print_info_list(info_list_wH)


#==========

from yattag import Doc
from yattag import indent

doc, tag, text = Doc().tagtext()
infolistwH = list(info_list_wH)
pdflist = list(pdf_list)

with tag('html'):
    with tag('body'):
        with tag('table'):
            heading = infolistwH.pop(0)
            with tag('tr'):
                for item in heading:
                    with tag('th'):
                        text(item)
                    
            for info in infolistwH:
                link = pdflist.pop(0)
                with tag('tr'):
                    for item in info:
                        with tag('td'):
                            with tag('a', href=link):
                                text(item)

                            
out = open('output.html','w') 
out.write(indent(doc.getvalue())) 
out.close() 

print ("done")