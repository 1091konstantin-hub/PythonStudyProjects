# школьники делят мандарины
n = int(input())  # заданое количество школьников
k = int(input())  # заданое количество мандаринов 
mandarins_for_student = k // n  # сколько мандаринов достанется одному школьнику
mandarins_left = k % n  # сколько мандаринов останется не поделенными 
print(mandarins_for_student, mandarins_left, sep="\n")
