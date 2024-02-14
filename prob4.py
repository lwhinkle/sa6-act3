numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [7, 5, 6, 1, 9]

intersection = list(filter(lambda x: x in numbers_1, numbers_2))
print(intersection)