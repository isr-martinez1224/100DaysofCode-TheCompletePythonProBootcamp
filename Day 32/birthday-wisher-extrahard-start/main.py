##################### Extra Hard Starting Project ######################
import random
import pandas
import datetime as dt
import smtplib
# 1. Update the birthdays.csv
names = []
with open("birthdays.csv") as file:
    content = file.readlines()
    for n in content:
        n = n.strip("\n")
        names.append(n)
    file.close()

data = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
todays_date = (month, day)

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
person = birthdays_dict[todays_date]

if todays_date in birthdays_dict:
    print("Today was found")

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    random_letter = random.choice(letters)

    with open(f"./letter_templates/{random_letter}", mode="r") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", person["name"])

    recipient_email = person["email"]

    print(content)
    # 4. Send the letter generated in step 3 to that person's email address.
    my_email = "martinez.2400.i@gmail.com"
    password = "hzbqwourfwlzivxs"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # secures our connection to the servers MOST IMPORTANT
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                            msg=f"Subject:Happy Birthday!\n\n{letter}")
    connection.close()

#Be sure to edit the letters to make it your name as a signature


