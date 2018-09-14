# These are the functions for manipulating pdfs.

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def pdf_to_str(path, page_limit=0, char_limit=0):
    assert isinstance(page_limit, int), 'page_limit has to be an integer.'    #added by fcy 180911
    assert isinstance(char_limit, int), 'char_limit has to be an integer.'
    
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

    i = 0
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    
        i += 1
        if (page_limit > 0 and page_limit >= i):
            break    #a break - added by Yan 180911

    fp.close()
    device.close()
    pdfstr = retstr.getvalue()
    
    if (char_limit > 0 and char_limit < len(pdfstr)):        #a break - added by Yan 180911
        pdfstr = pdfstr[:char_limit]

    retstr.close()
    return pdfstr