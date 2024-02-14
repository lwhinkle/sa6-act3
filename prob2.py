words = ["bird", "cat", "fish", "rabbit", "dog"]

sorted_list = sorted(words, key=lambda x: (len(x)))
print(sorted_list)