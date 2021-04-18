largest = None
smallest = None

while True:
    snum = input("Enter a number: ")
    if snum == "Done":
        break
    try:
        num = int(snum)
    except:
        print("Invalid Input")
        continue
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum", largest)
print("minimum", smallest)
