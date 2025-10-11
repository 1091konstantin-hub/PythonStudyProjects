# Transposition of digits in a two-digit number.
number = int(input("Enter the number : "))  # User enters number
tens = number // 10  # Calculation of tens
ones = number % 10 #Calculation of ones
print("Result : ", ones, tens, sep="") # We swaped the tens and ones and got the result
