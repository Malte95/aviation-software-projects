x = int(input("Choose: 1=knots, 2=feet, 3=gallons"))
if x == 1:
    knot = float(input("Enter knots:"))
    print(knot * 1.852, "km/h")
elif x == 2:
    feet = float(input("Enter feet:"))
    print(feet * 0.3048, "m")
else:
    gallon = float(input("Enter gallons:"))
    print(gallon * 3.78541, "l")

