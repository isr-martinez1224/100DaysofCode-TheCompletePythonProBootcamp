def hello():
    print("Hello")

#hello()

#Creating the function
def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    # Inside the function

#Outside the function
print("Hello")
get_user_name() # Calling the function

# Reebrog Maze Solution
# def turn_around():
#     turn_left()
#     turn_left()
#
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if front_is_clear():
#         move()
#     elif not right_is_clear():
#         if front_is_clear():
#             move()
#         elif wall_in_front():
#             turn_left()
#     else:
#         turn_right()
#         move()