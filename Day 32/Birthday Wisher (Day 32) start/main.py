### SENDING EMAILS

# import smtplib
#
#
# my_email = "martinez.2400.i@gmail.com"
# password = "hzbqwourfwlzivxs" #this needs to be the app password for google services, any service has different processes
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls() #secures our connection to the servers MOST IMPORTANT
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="im201414@hotmail.com",
#                         msg="Subject:Port 587\n\nHello, testing sending emails from port 587 the modern secure form.")
# connection.close()


### USING DATETIME
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(now)
# if year == 2026:
#     print(f"Year is: {year}")
# print(day_of_week)
#
#
# date_of_birth = dt.datetime(year=2000, month=7, day=10, hour=7)
# print(date_of_birth)


import datetime as dt
import random
import smtplib


now = dt.datetime.now()
day_of_week = now.weekday()

#Can later implement a individual days thing
# if day_of_week == 0:
#     day_of_week = "Monday"
# elif day_of_week == 1:
#     day_of_week = "Tuesday"
# elif day_of_week == 2:
#     day_of_week = "Wednesday"
# elif day_of_week == 3:
#     day_of_week = "Thursday"
# elif day_of_week == 4:
#     day_of_week = "Friday"

if day_of_week == 0:
    with open("quotes.txt") as file:
        content = file.readlines()
        quote = random.choice(content)
        file.close()
    day_of_week = "Monday"
    # print(quote)
    #
    #
    # print(f"Subject:{day_of_week} Motivational Quote\n\n{quote}")
    my_email = "martinez.2400.i@gmail.com"
    password = "hzbqwourfwlzivxs" #this needs to be the app password for google services, any service has different processes

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls() #secures our connection to the servers MOST IMPORTANT
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:{day_of_week} Motivational Quote\n\n{quote}")
    connection.close()