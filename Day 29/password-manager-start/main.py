from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(END, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                #Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #Update old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ----------------------- SEARCH BUTTON ------------------------------- #
def find_password():
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            website = website_input.get().title()
            email = data[website]["email"]
            password = data[website]["password"]

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for the website exists")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas/Image setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Website Label/Field
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()

#Search Button
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")


#Email/Username Label/Field
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry()
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "myemail@gmail.com")


#Password Label/Field
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")


#Generate Password Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")


#Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()