import random

print("Hello, welcome to the chord progression generator.")
input("Please press [enter] to continue")

#generating a chord set
chord numbers = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
random_list = [random.choice(chord numbers) for _ in range(4)]


print(random_list)



