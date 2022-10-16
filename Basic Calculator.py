print ('Welcome To The Calculator!')
print (                                      )
print ('This calculator can add, subtract, multiply and divide!')

print (                                      )
print ("************************************")
print (                                      )

print ("Select operation:")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")

print (                                      )
print ("************************************")
print (                                      )

def add (x,y):
    return x + y

def diff (x,y):
    return x - y

def multi (x,y):
    return (x * y)

def div (x,y):
    return (x / y)

choice = int(input("Enter your choice of operation:"))
if choice <1 or choice >4:
    print ("Invalid choice.")

num1 = int(input("Enter your first number here:"))

num2 = int(input("Enter your second number here:"))

if choice == 1:
    print ("The addition of", num1, "and", num2, "is", add (num1, num2),".")

elif choice == 2:
    print ("The difference of", num1, "and", num2, "is", diff (num1 ,num2),".")

elif choice == 3:
    print ("The multiplication of", num1, "and", num2, "is", multi (num1, num2),".")

elif choice == 4:
    print ("The division of", num1, "and", num2, "is", div (num1, num2),".")







   
  