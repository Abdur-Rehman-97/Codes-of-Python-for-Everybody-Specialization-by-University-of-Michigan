hrs = input("Enter hours ")
rate_per_hour = input("Enter rate per hour ")

try:
    h = float(hrs)
    rps = float(rate_per_hour)
except:
    print("Error, Please enter correct numberical value")
    quit()

gross_pay  = 0

if h <= 40:
    gross_pay = h * rps
    print(gross_pay)
else:
    basic_pay = 40 * rps
    overtime = (h - 40)*1.5*rps
    gross_pay = basic_pay + overtime
    print(gross_pay)
