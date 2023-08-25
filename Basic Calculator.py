# Basic Mathematical Calculator:

print ('Welcome To The Calculator!')
print (                                      )
print ("************************************")
print (                                      )

print("1: Addition (+)")
print ("2: Subtraction (-)")
print ("3: Multiplication (*)")
print ("4: Division (/)")
print ('5: To obtain a remainder')

print (                                      )
print ("************************************")
print (                                      )


def add (x,y):
    return x + y

def sub (x,y):
    return x - y

def mul (x,y):
    return x * y

def div (x,y):
    return x / y

def rem (x,y):
    return x % y


choice = int(input("Enter your choice of operation:"))
if choice <1 or choice >5:
    print ("Invalid choice.")

num1 = int(input("Enter your first number here:"))

num2 = int(input("Enter your second number here:"))

if choice == 1:
    print ("The addition of", num1, "and", num2, "is", add (num1, num2),".")

elif choice == 2:
    print ("The difference of", num1, "and", num2, "is", sub (num1 ,num2),".")

elif choice == 3:
    print ("The multiplication of", num1, "and", num2, "is", mul (num1, num2),".")

elif choice == 4:
    print ("The division of", num1, "and", num2, "is", div (num1, num2),".")

elif choice == 5:
    print ("The remainder of", num1, "and", num2, "is", rem (num1, num2),".")

# End of Program.
