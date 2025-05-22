import random

seed_value = 23
random.seed(seed_value)

# Generate a pseudo-random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 1000000000000)

print("Pseudo-random integer:", random_integer)