population = int(input())  # население вселенной
half_population = population // 2  # половина населения вселенной
half_poplus = half_population + (population % 2) #  + остаток от деления на 2 для нечетных
print(half_poplus)