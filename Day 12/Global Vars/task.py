# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies #this allows you to modify the global variable and avoid the error having same name variables in local scope
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


