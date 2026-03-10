#Declaring data types before using them, so age has to be an int, cannot change it
# age: int
# name: str
# height: float
# is_human: bool

#putting an arrow will specify the data type
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")