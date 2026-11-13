Ttnfees = (input("enter tution fees: "))
Labfees = (input("enter lab fees: "))
Libraryfees = (input("enter library fees: "))
Examfees = (input("enter exam fees: "))
Discountamount = (input("enter discount amount: "))

totalfees = int(Ttnfees) + int(Labfees) + int(Libraryfees) + int(Examfees)
print("total fees:", totalfees)

feeafterdiscount = totalfees - int(Discountamount)
print("fee after discount:", feeafterdiscount)

annualfees = feeafterdiscount * 2
print("annual fees:", annualfees)

monthlyinstallment = annualfees/12
print("monthly installment:", monthlyinstallment)
