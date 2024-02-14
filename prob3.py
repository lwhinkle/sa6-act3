from functools import reduce

numbers = [1, 2, 3, 10, 100]

greatest_num = reduce(lambda x, y: x if (x > y) else y, numbers)
print(greatest_num)