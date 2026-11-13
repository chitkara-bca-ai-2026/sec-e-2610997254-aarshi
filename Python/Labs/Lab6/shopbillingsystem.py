print("=======================================================")
print("             CLOTHING STORE BILLING SYSTEM BY AARSHI                      ")
print("=======================================================")

Custmrname = input("enter customer name:")
Garmname = input("enter garment name:")
Garmprice = float(input("enter garment price:"))
Numgarments = int(input("enter number of garments:"))

print("========================================================")
print("                           BILL                           ")
print("========================================================")

print("Customer Name: ",Custmrname)
print("Garment Name: ", Garmname)   
print("Garment Price: ", Garmprice)
print("quantity: ", Numgarments)
print("Total amount: ", Garmprice * Numgarments)
