f = open('words.txt','r')
no_ch = 0
no_wds = 0
text = f.read()
wds_list = text.split() 
no_wds = len(wds_list)    
for word in wds_list:
    char = len(word)
    no_ch = no_ch + char
print("Number of words in words.txt file :",no_wds)
print("Number of characters in words.txt file :",no_ch)
