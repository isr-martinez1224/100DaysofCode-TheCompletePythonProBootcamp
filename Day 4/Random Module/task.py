import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.my_favorite_number)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1, 10) #inclusive between a and b
print(random_float)

flip = random.randint(1,2)
if flip == 1:
    print("Heads")
elif flip == 2:
    print("Tails")
else:
    print("Somehow none")