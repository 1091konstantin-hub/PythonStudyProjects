#summ and multiplication of digits of a three-digit number
number = int(input())  # input number
hundreds = number // 100  # hundreds digit
tens = (number // 10) % 10  #  tens digit
ones = number % 10  #  ones digit
print("sum_digits = ", hundreds + tens + ones, "\nmultiplication = ", hundreds * tens * ones,sep="")
