import random

print("Hello, welcome to the chord progression generator.")
input("Please press [enter] to continue")

words = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
random_list = [random.choice(words) for _ in range(4)]

print(random_list)



