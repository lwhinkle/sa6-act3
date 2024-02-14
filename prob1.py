from functools import reduce

num = 1234

digits = map(int, str(num))

sum = reduce(lambda x, y: int(x) + int(y), digits)
print(sum)