from yattag import Doc
from yattag import indent

def gen_table_html(dictlist):
    doc, tag, text = Doc().tagtext()

    with tag('html'):
        with tag('body'):
            with tag('table'):
                titles = grab_titlelist_from_dictlist(dictlist)
                doc.asis(gen_title_row(titles))
                        
                for d in dictlist:
                    doc.asis( gen_record_row(titles, d))
                    
    return indent(doc.getvalue())

def grab_titlelist_from_dictlist(dictlist):
    
    titlelist = []

    for dictitem in dictlist:
        for key in [nk for nk in dictitem if nk not in titlelist]:
            titlelist.append(key)

    return titlelist

def gen_title_row(title_list):
    doc, tag, text = Doc().tagtext()

    with tag('tr'):
        for item in title_list:
            with tag('th'):
                text(item)

    return indent(doc.getvalue())

def gen_record_row(title_list, record_dict):
    doc, tag, text = Doc().tagtext()
 
    with tag('tr'):
        for key in title_list:
            with tag('td'):
                if ('link' in record_dict):
                    with tag('a', href=record_dict['link']):
                        text(record_dict[key] if key in record_dict else '')
                else:
                    text(record_dict[key] if key in record_dict else '')

    return indent(doc.getvalue())

