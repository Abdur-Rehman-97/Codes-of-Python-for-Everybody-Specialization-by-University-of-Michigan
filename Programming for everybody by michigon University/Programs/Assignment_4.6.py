def computepay(h,r):
    hr = float(h)
    rps = float(r)
    if hr <= 40:
        gross_pay = hr * rps
        return gross_pay
    else:
        basic_pay = 40 * rps
        overtime = (hr - 40)*1.5*rps
        gross_pay = basic_pay + overtime
        return gross_pay

h = input("Enter Hours: ")
r = input("Enter Rate: ")
p = computepay(h, r)
print("Pay",p)
