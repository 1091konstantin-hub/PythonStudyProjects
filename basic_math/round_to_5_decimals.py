# Round to 5 decimal places
number = float(input())
fractional_part = number % 1
rounded_fraction = int(fractional_part * 100000) / 100000
print(rounded_fraction)
