#file not found error
# with open("file.txt") as file:
#     file.read()

#key error
# dictionary = {"key" : "value"}
# value = dictionary["non_existent_key"]

#index error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#type error
# text = "abc"
# print(text + 5)

# try:
#     file = open("file.txt")
#     dictionary = {"key": "value"}
#     print(dictionary["key"])
# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error I made up")


# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)

#go back to day 29 for password management edits