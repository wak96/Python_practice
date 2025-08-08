# Write a python program to do arithmetical operations addintion and division.
# Addition

num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))

addition = num1 + num2
print("Addition of " + str(num1) + " and " + str(num2) + " = " + str(addition)) # Str + Str
print("Addition of ",num1,"and ",num2," = ",addition) # String + int
print(f'Addition of {num1} and {num2} = {addition}') # F-string