def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# i is incrementing from 1 to 20 and the if statement is checked to see if i equals 20 in order for the inside statement to execute
# However, it never prints out the sentence in the end
# 2. When is the function meant to print "You got it"?
# When i is equal to 20
# 3. What are your assumptions about the value of i?
# i is starting at 1 and incrementing but stops short of 20 due to the range function not being inclusive of the second value