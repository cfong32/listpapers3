from list_fn import *
from html_fn import *

path = 'C:/users/luke/papers/'
pdfpath_list = path_to_pdfpathlist(path)

dict_list = pdfpathlist_to_dictlist_wlinks(pdfpath_list)

# print(dict_list)

out = open('output.html','w') 
out.write(gen_table_html(dict_list, order=['year','title','author'])) 
out.close()

print ("done")