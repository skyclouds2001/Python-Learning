name = input("Enter employee\'s name: ")
hour = eval(input("Enter number of hours worked in a week: "))
payRate = eval(input("Enter hourly pay rate: "))
fTax = eval(input("Enter federal tax withholding rate: "))
sTax = eval(input("Enter state tax withholding rate: "))

pay = hour * payRate
fPay = pay * fTax
sPay = pay * sTax

print("Employee Name:", name)
print("Hours Worked:", float(hour))
print("Pay Rate:", '$', format(payRate, ".2f"))
print("Deductions:")
print("  Federal Withholding (20.0%):", '$', format(fPay, ".2f"))
print("  State Withholding (9.0%):", '$', format(sPay, ".2f"))
print("  Total Deduction:", '$', format(fPay + sPay, ".2f"))
print("Net Pay:", '$', format(pay - fPay - sPay, ".2f"))
