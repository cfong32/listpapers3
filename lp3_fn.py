import os
import re
from pdf_fn import pdf_to_str

def path_to_pdfpathlist(path):
    pdfpathlist = []
    for r,d,f in os.walk(path):
        for name in f:
            prefix, ext = os.path.splitext(name)
            if ext == '.pdf':
                pdfpathlist.append(os.path.join(r, name))
    return pdfpathlist


def pdfpathlist_to_txtlist(pdfpathlist):
    txtlist = []
    for item in pdfpathlist:
        txtlist.append(pdf_to_str(item, page_limit=1, char_limit=1000))
    return txtlist


def txtlist_to_infolist(txtlist, with_headings=False):
    infolist = []
    
    if with_headings == True:
        infolist.append(grab_info_from_txt('### headings ###'))
        
    for item in txtlist:
        infolist.append(grab_info_from_txt(item))

    return infolist


def txtlist_to_infolist_wH(txtlist):
    return txtlist_to_infolist(txtlist, with_headings=True)


def grab_info_from_txt(txt):
    if txt == '### headings ###':
        return ['title', 'author']
    
    #grab the first part as title
    title = txt.split('\n')[0]
    
    #grab the second part
    p2 = txt[len(title):].strip('\n')
    p3 = re.split(',|\n|1|2|3|4|5|6|7|8|9|0', p2)[0]
    
    author = p3.strip()
    
    return [title, author]


# print functions for debugging
def print_txtlist(txtlist):
    for item in txtlist:
        p1 = item.split('\n')[0]
        p2 = item[len(p1):].strip('\n')
        p3 = re.split(',|\n|1|2|3|4|5|6|7|8|9|0', p2)[0]
        title = p1
        author = p3.strip()
        
        print (title)
        print (author)
        print ('====================')  

def print_infolist(infolist):
    for item in infolist:
        print (item)
