def is_right_angled(a, b, c):
    sides = sorted([a, b, c])
    return (sides[0]**2 + sides[1]**2) == sides[2]**2

side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))

if is_right_angled(side1, side2, side3):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")