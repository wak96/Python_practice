# write a program to swap two variable.

a = input("Enter the value of first variable (a): ")
b = input("Enter the value of second variable (b): ")

# Displaying the orginal values
print(f"Orginal values: a = {a}, b = {b}")

# Swap the values using a temporary variable
temp = a
a = b
b = temp

# Displaying the swapped values
print(f"Swapped values: a = {a}, b = {b}")