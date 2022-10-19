# Where the user needs to input their choice for the program to calculate the area.
user_input = input("Would you like to find the area of a Circle, Square, Rectangle or Trapezoid:")

possible_input = ["circle", "square", "rectangle", "trapezoid"]

# Fuctions
def circle (a):
        area_of_circle = 3.14 * (a ** 2)
        return (area_of_circle)

def square (a):
    area_of_square = a ** 2
    return (area_of_square)

def rectangle (a,b):
        area_of_rectangle = a * b
        return (area_of_rectangle)

def trapezoid (a,b,h):
    area_of_trapezoid = ((a + b)/2) * h 
    return area_of_trapezoid

# Conditional statements and outputs per outcome.
while True:
    if user_input.lower() == "circle":
        radius = int (input ("Please input the radius of your circle:"))
        print ("The area of your circle is:", circle (radius))
        break

    elif user_input.lower() == "square":
        length = int (input ("Please input the length of your square:"))
        print ("The area of your square is:", square (length))
        break

    elif user_input.lower() == "rectangle":
        length = int (input ("Please input the length of your rectangle:"))
        width = int (input ("Please input the width of your rectangle:"))
        print ("The area of your rectangle is:", rectangle (length, width))
        break

    elif user_input.lower() == "trapezoid":
        a_base = int (input ("Please input the first base value of your trapezoid:"))
        b_base = int (input ("Please input the first base value of your trapezoid:"))
        height = int (input("Please input the height of your trapezoid"))
        print ("The area of your trapezoid is:", trapezoid (a_base, b_base, height))
        break
    
    elif user_input.lower() not in possible_input:
        print ("Invalid choice.")
        user_input = input(("Please try again:"))
        

# End of Program
