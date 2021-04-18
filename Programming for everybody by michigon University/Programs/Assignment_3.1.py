hrs = input("Enter hours ")
h = float(hrs)
rate_per_hour = input("Enter rate per hour ")
rps = float(rate_per_hour)
gross_pay  = 0

if h <= 40:
    gross_pay = h * rps
    print(gross_pay)
else:
    basic_pay = 40 * rps
    overtime = (h - 40)*1.5*rps
    gross_pay = basic_pay + overtime
    print(gross_pay)
