# Population growth or compound interest model
initial = int(input())  # initial amount
rate = int(input())  # growth rate in percent
days = int(input())  # number of days/periods

current = initial
for i in range(1, days + 1):
    print(i, current)
    current = current + current * rate / 100
