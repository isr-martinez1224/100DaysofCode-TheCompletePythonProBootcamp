game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]


#no block code means this can be called outside the block
print(new_enemy)





# Accessible anywhere
my_global_var = 1


def my_function():
    # Only accessible within my_function()
    my_local_var = 2


for _ in range(10):
    # Accessible anywhere
    my_block_var = 3