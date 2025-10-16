# Count how many numbers are equal among three integers
num_1 = int(input("Enter a number"))
num_2 = int(input("Enter a number"))
num_3 = int(input("Enter a number"))

if num_1 == num_2 == num_3:
    print("All three numbers are equal") 
elif num_1 == num_2 or num_2 == num_3 or num_3 == num_1:
    print("Two numbers are equal")  
else:
    print("All numbers are different")  