student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)
#Loop through rows of a data frame instead of columns
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #print(index)
    #print(row)
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato_data)

# for (index, row) in nato_data.iterrows():
#     #Access index and row
#     #print(index)
#     #print(row)
#     print(row.code)

nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
#2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ")
user_input = user_input.upper()

input_list = list(user_input)


nato_results_list = [nato_dict[letter] for letter in user_input]
print(nato_results_list)