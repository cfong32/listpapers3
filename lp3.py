from lp3_fn import *

path = 'C:/users/luke/papers/'
pdfpath_list = path_to_pdfpathlist(path)
txt_list = pdfpathlist_to_txtlist(pdfpath_list)
info_list = txtlist_to_infolist(txt_list)
info_list_wH = txtlist_to_infolist_wH(txt_list)

print_infolist(info_list_wH)


#==========

from yattag import Doc
from yattag import indent

doc, tag, text = Doc().tagtext()
infolistwH = list(info_list_wH)
pdflist = list(pdfpath_list)

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