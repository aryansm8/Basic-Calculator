#Writing the greeting for the user.
print ('Welcome To The Calculator!')
print ('This calculator can add, subtract, multiple and divide!')

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print ("Select operation:")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")

#Calculations:

choice = input('Enter your choice:(1,2,3,4):')

num1 = int(input('Enter your first input here:'))
num2 = int(input('Enter your second input here:'))

if choice == '1':
    print(num1,"+",num2,"=", add(num1, num2))
elif choice == "2":
    print (num1,"-",num2,"=", subtract(num1, num2))
elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1, num2))
elif choice == '4':
    print(num1,"/",num2,"=", divide(num1, num2))


