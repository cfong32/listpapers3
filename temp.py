# from html_fn import gen_title_row
# from html_fn import gen_record_row
# from html_fn import grab_titlelist_from_dictlist
from html_fn import *

a = {'title':'T1', 'author':'Fong', 'link':'http://www.yahoo.com/'}
b = {'title':'T2', 'author':'Chan', 'year':2014}
c = {'title':'T3', 'author':'Xi', 'year':2018}

papers = [a, b, c]

titles = grab_titlelist_from_dictlist(papers)

print (gen_table_html(papers))

# print (titles)

# print (gen_title_row(titles))
# for paper in papers:
#     print (gen_record_row(titles, paper))
