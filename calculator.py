import sys

# Python program for simple calculator
 
# Function to add two numbers
def add(num1, num2):
    output = num1 + num2
    file_store(output)
 
# Function to subtract two numbers
def subtract(num1, num2):
    output = num1 - num2
    file_store(output)
 
# Function to multiply two numbers
def multiply(num1, num2):
    output = num1 * num2
    file_store(output)
 
# Function to divide two numbers
def divide(num1, num2):
    output = num1 / num2
    file_store(output)
   
def file_store(output):
    file = open("C:\Users\LOKESH E\sample.txt","w")
    file.write(output)
    file.close()
 
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
 
 
# Take input from the user
print("select the operation")
select = int(sys.argv[1])
print("number1 input")  
number_1 = int(sys.argv[2])
print("number2 input")
number_2 = int(sys.argv[3])
 
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
 
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
 
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
 
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")
