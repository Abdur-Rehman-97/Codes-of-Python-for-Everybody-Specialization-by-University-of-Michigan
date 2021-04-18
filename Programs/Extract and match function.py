import re
#text = "My 2 favorite numbers are 20 and 40"
#y = re.findall('[1-9]+', text)
#print(y)

#greedy approach, will select the largest
x = "From: Using this: character"
y = re.findall('^F.+:', x)
print(y)


#use ? after + to get rid of greedy approach
x = "From: Using this: character"
y = re.findall('^F.+?:', x)
print(y)
