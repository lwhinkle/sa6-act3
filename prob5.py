numbers = [1, 2, 3, 4, 5]
power = 3

new_list = list(map(lambda x: pow(x, power), numbers))
print(new_list)