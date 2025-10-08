# Write a programm that takes a three-digit number and display it digits 
#(separated by comma) on the screen.

number = int(input("Enter a three-digit number: "))  # three-digit number input
hundreds = number // 100  # counts hundred
tens = number // 10 % 10  # counts tens  
ones = number % 100 % 10  # counts ones
print(hundreds, tens, ones, sep=",")  # display three-digit number (separated by comma)