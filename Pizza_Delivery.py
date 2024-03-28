print("Thank You choosing Gemm Pizza!")
size = print(input("What size pizza do you want? S, M, or L: "))
add_pepperoni = print(input("Do you want pepperoni? Y or N: "))
exta_cheese = print(input("Do you want extra cheese? Y or N: "))

bill = 0
if size == "S":
    bill += 200
elif size == "M":
    bill += 300
else:
    bill += 350

if add_pepperoni == "Y":
    if size == "S":
        bill += 50
    else:
        bill += 70

if exta_cheese == "Y":
    bill += 30

print(f"Your final bill is: ₹{bill}.")