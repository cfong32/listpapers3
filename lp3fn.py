import os

def a():
    return 'a'

def path_to_pdf_list(path):
    list1 = []
    for r,d,f in os.walk(path):
        for name in f:
            prefix, ext = os.path.splitext(name)
            if ext == '.pdf':
                list1.append(os.path.join(r, name))
    return list1

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
        #a break - added by Yan 180906 
        break
    fp.close()
    device.close()
    str = retstr.getvalue()[:1000] #only first 1000 characters - added by Yan 180906 
    retstr.close()
    return str

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

def pdf_list_to_txt_list(pdf_list):
    str_list = []
    for item in pdf_list:
        str_list.append(pdf_to_txt(item))
    return str_list

def txt_list_to_info_list(txt_list, with_headings=False):
    info_list = []
    
    if with_headings == True:
        info_list.append(grab_info_from_txt('### headings ###'))
        
    for item in txt_list:
        info_list.append(grab_info_from_txt(item))
    return info_list

def txt_list_to_info_list_wH(txt_list):
    return txt_list_to_info_list(txt_list, with_headings=True)

import re

def print_txt_list(txt_list):
    for item in txt_list:
        p1 = item.split('\n')[0]
        p2 = item[len(p1):].strip('\n')
        p3 = re.split(',|\n|1|2|3|4|5|6|7|8|9|0', p2)[0]
        title = p1
        author = p3.strip()
        
        print (title)
        print (author)
        print ('====================')  

def print_info_list(info_list):
    for item in info_list:
        print (item)
