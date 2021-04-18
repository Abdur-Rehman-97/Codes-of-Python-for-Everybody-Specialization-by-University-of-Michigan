import re
x = "From abr.rehman1997@gmail.com born 05 05 1997 abdullah@gmail.com"
y = re.findall('\S+@\S+', x) # /S is used for non blank character
z = re.findall('@\S+',x)
a = re.findall('\S+@',x)

print(y, z, a)

#using prefix to extract something

x = "From abr.rehman1997@gmail.com born 05 05 1997 abdullah@gmail.com"
output = re.findall('From (\S+@\S+)', x)
# it will extract abr.rehman1997 only not abdullah
print(output)
