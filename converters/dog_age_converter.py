# Convert dog age to human years
dog_age = int(input())

if dog_age == 1:
    print(10.5)  # First dog year = 10.5 human years
elif dog_age == 2:
    print(21)  # Second dog year = 10.5 human years (total 21)
elif dog_age > 2:
    human_years = 21 + (dog_age - 2) * 4  # Each subsequent year = 4 human years
    print(human_years)
