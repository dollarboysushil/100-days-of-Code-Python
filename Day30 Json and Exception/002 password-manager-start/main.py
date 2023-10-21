import tkinter.messagebox
from tkinter import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    Password_entry.delete(0, END)
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    Password_entry.insert(0 ,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = Email_entry.get()
    password = Password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password" : password,

        }
    }


    if len(website)== 0 or len(password) ==0:
        tkinter.messagebox.showinfo(title="Alert" , message="Please Enter data in all fields!!!")
    else:

        is_ok = tkinter.messagebox.askokcancel(title="Alert" , message=f"Here are the details: \nEmail: {email} \nPassword:{password}\n Press ok to save")
        if is_ok == True:
            try:
                with open("data.json" , "r") as data_file:

                    data = json.load(data_file)


            except FileNotFoundError:
                with open("data.json" , "w") as data_file:
                    json.dump(new_data , data_file, indent=4)

            else:
                data.update(new_data)


                with open("data.json" , "w") as data_file:
                    json.dump(data, data_file , indent=4)
            finally:
                website_entry.delete(0 , END)
                Password_entry.delete(0,END)

# ---------------------------- Find password ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json" , 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="Error" , message="No datafile found")


    else:

        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            tkinter.messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")

        else:
            tkinter.messagebox.showinfo(title="Error", message=f"Data related to {website} not found!!")



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200 , width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100 , 100,image = logo_img)
canvas.grid(row=0 , column=1)



website_label = Label(text="Website:")
website_label.grid(row=1 , column=0)

Email_label = Label(text="Email/Username:")
Email_label.grid(row=2, column=0)

Password_label= Label(text="Password:")
Password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row= 1 , column=1 , )
website_entry.focus()

search_button  = Button(text="Search"  , width=13 , command=find_password)
search_button.grid(row=1 , column= 2)


Email_entry = Entry(width=35)
Email_entry.grid(row=2 , column= 1 , columnspan=2)
Email_entry.insert(0 , "@gmail.com")

Password_entry = Entry(width= 21)
Password_entry.grid(row=3 , column=1)


generate_button  = Button(text= "Generate Password" , command=password_generator)
generate_button.grid(row= 3, column= 2 )

add_button = Button(text="Add" , width=36 , command=save)
add_button.grid(row=4 , column=1, columnspan=2)

window.mainloop()