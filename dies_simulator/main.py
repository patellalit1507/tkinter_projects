import tkinter

from PIL import Image,ImageTk
import random


dice=tkinter.Tk()
dice.geometry("400x400")
dice.title("dice simultor game")
tkinter.Label(dice,text='hello gamer',font='Arial').place(x=10,y=20)
Dice=['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']
DiceImage=ImageTk.PhotoImage(Image.open(random.choice(Dice)))  #this is just for creatin instance
Image_label=tkinter.Label(dice,image=DiceImage)
#Image_label.image=DiceImage
Image_label.pack(expand=True)
def roll_dice():
    DiceImage=ImageTk.PhotoImage(Image.open(random.choice(Dice)))
    #Image_label=tkinter.Label(dice,image=DiceImage)-----this is wrong because from this we create new Imagelabel weidget which will not work
    Image_label.configure(image=DiceImage)
    Image_label.image=DiceImage
roll_dice=tkinter.Button(dice,text='press to roll',font=("arial",20,'bold'),bg='black',fg='white',command=roll_dice).place(x=100,y=330)
dice.mainloop()
