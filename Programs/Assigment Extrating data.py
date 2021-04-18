import re
file = open("actual.txt",'r');
text = file.read()

output = re.findall('[0-9]+', text)
print(output)
sum = 0
for i in range(0, len(output)):
    output[i] = int(output[i])
    sum = sum + output[i]

print(sum)
