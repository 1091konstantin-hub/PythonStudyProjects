# Color mixing calculator (red, blue, yellow)
color_1 = str(input())
color_2 = str(input())

if (color_1 == color_2) and (
    color_1 == "red" or color_1 == "blue" or color_1 == "yellow"
):
    print(color_1)
elif (color_1 == "red" and color_2 == "blue") or (
    color_1 == "blue" and color_2 == "red"
):
    print("purple")
elif (color_1 == "yellow" and color_2 == "blue") or (
    color_1 == "blue" and color_2 == "yellow"
):
    print("green")
elif (color_1 == "yellow" and color_2 == "red") or (
    color_1 == "red" and color_2 == "yellow"
):
    print("orange")
else:
    print("color error")
