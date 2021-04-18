

import re
text = "From abr.rehman1997@gmail.com born 05 05 1997 abdullah@gmail.com"
atpos = text.find('@')
print(atpos)
sppos = text.find(' ', atpos)
print(sppos)
host =  text[atpos+1 : sppos]
print(host)


#using split function
word = text.split()
email = word[1]
hostname = email.split('@')
print(hostname[0])
print(hostname[1])



#using Regular Expression
# [^ ] used to match not-blanck character
y = re.findall('@([^ ]*)', text)
print(y)

#using prefix
a = re.findall('^From .*@([^ ]*)', text)
print(a)
