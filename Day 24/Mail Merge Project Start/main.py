#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open("./Input/Names/invited_names.txt") as file:
    content = file.readlines()
    for n in content:
        n = n.strip("\n")
        names.append(n)
    file.close()

for n in names:
    letter = []
    with open("./Input/Letters/starting_letter.txt", mode="r") as file:
        content = file.readlines()
        for x in content:
            x = x.strip("\n")
            letter.append(x)
        file.close()

    letter[0] = letter[0].replace("[name]", n)

    with open(f"./Output/ReadyToSend/letter_to_{n}.txt", mode="w") as file:
        for x in range(len(letter)):
            letter[x] += "\n"
            file.write(letter[x])
        file.close()
    letter[0] = letter[0].replace(letter[0], "Dear [name],")
