# Sort three numbers in descending order
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

min_num = min(num_1, num_2, num_3)
max_num = max(num_1, num_2, num_3)
sum_nums = num_1 + num_2 + num_3
mid_num = sum_nums - max_num - min_num

print(max_num)
print(mid_num)
print(min_num)