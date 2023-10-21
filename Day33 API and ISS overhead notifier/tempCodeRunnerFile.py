from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()

    text = canvas.itemconfig(quote_text ,text=quote["quote"])

screen = Tk()
screen.title("Flashy")
screen.config(padx=50, pady=50)

canvas = Canvas(height=500 , width=300)
background_image = PhotoImage(file="./background.png")
canvas.create_image(150,207,image=background_image)
canvas.grid(row=0,column=0)

quote_text = canvas.create_text(150,207 , text="Click on Kanye Image to show the Quote",width=250, font=("Ariel" , 20))


kanye_img = PhotoImage(file="./kanye.png")
kanye_button = Button(image=kanye_img , command=get_quote)
kanye_button.grid(row=1, column=0)

screen.mainloop()