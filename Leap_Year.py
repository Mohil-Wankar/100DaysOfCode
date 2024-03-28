year = int(input("Enter a year:- "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's Leap Year!")
        else:
            print(" It's not a Leap Year!")
    else:
        print("It's a Leap Year!")
else:
    print("It's not a Leap Year!")