import tkinter as tk
from PIL import Image, ImageTk
import random


window = tk.Tk()
window.geometry("600x430")
window.title("Dice Simulator")
window.configure(bg="navy")

window.label = tk.Label(window, text="Dice simulator", font=("Helvetica", 16), bg="lightblue")
window.label.pack(pady=10)
def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(Dice)))
    label1.configure(image= image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(Dice)))
    label2.configure(image=image2)
    label2.image = image2


Dice = ["icons/dice 1.png","icons/dice 2.png","icons/dice 3.png","icons/dice 4.png","icons/dice 5.png","icons/dice 6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(Dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(Dice)))

label1 = tk.Label(window, image=image1)
label2 = tk.Label(window, image=image2)

label1.image = image1
label2.image = image2

label1.place(x = 40,y = 150)
label2.place(x = 320, y = 150)

button = tk.Button(window, text="ROLL", bg="black", fg="blue", font= "Times 20", command=dice_roll)
button.place(x = 250, y = 60)

window.mainloop()