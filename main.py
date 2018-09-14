from list_fn import *
from html_fn import *

path = 'C:/users/luke/papers/'
pdfpath_list = path_to_pdfpathlist(path)
# txt_list = pdfpathlist_to_txtlist(pdfpath_list)
# # info_list = txtlist_to_infolist(txt_list)
# # info_list_wH = txtlist_to_infolist_wH(txt_list)
# # print_infolist(info_list_wH)

# dict_list = txtlist_to_dictlist(txt_list)

dict_list = pdfpathlist_to_dictlist_wlinks(pdfpath_list)

print(dict_list)

out = open('output.html','w') 
out.write(gen_table_html(dict_list)) 
out.close() 

print ("done")