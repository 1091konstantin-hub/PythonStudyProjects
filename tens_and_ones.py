#  Программа, определяющуя число десятков и единиц в двузначном числе.
number = int(input("Enter a number :  "))  # Просим ввести число
tens_of_number = number // 10 #  Считаем 10ки от числа
ones_of_number = number % 10 #  Считаем единицы от числа
print("Tens of number: ", tens_of_number)  # Выводим десятки
print("Ones of number: ", ones_of_number)  # Выводим единицы