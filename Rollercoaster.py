print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 30
        print("Child tickets are for ₹30")
    elif age <= 18:
        bill = 50
        print("Youth tickets are for ₹50")
    else: 
        bill = 60
        print("Adult tickets are ₹60")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or "y":
        bill += 20

    print(f"Your final bill amount is ₹ {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
