# Greedy coin change algorithm (US coins: 25, 10, 5, 1)
money = int(input())
quarter, dime, nickel, penny = 25, 10, 5, 1
total_coins = 0

while money > 0:
    if money >= quarter:
        money -= quarter
        total_coins += 1
    elif money >= dime:
        money -= dime
        total_coins += 1
    elif money >= nickel:
        money -= nickel
        total_coins += 1
    else:
        money -= penny
        total_coins += 1

print(total_coins)
