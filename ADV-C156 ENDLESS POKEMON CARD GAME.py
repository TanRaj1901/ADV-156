from tkinter import *
from PIL import ImageTk,Image
import random

root=Tk()
root.title("Pokemon Game")
root.geometry("900x800")
root.configure(background="yellow")


abra= ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour= ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender= ImageTk.PhotoImage(Image.open("charmender.jpg"))
jigglypuff= ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra= ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth= ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking= ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras= ImageTk.PhotoImage(Image.open("paras.jpg"))
persion= ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu= ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata= ImageTk.PhotoImage(Image.open("ratata.jpg"))
dice = ImageTk.PhotoImage(Image.open("button.jpg"))

player1 = Label(root,text="Player 1 ",bg="royal blue" ,fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)
player2 = Label(root,text="Player 2 ", bg="royal blue",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)
player1_score=Label(root,bg="royal blue",fg="white")
player1_score.place(relx=0.1,rely=0.4,anchor=CENTER)
player2_score=Label(root,bg="royal blue",fg="white")
player2_score.place(relx=0.9,rely=0.4,anchor=CENTER)
random_dice=Label(root,bg="chocolate1",fg="white")
random_dice.place(relx=0.5,rely=0.5,anchor=CENTER)

pokemon = [abra,bulbasour,charmender,jigglypuff,kadabra,meowth,nidoking,paras,persion,pikachu,ratata]
power = [30,60,50,70,70,60,90,40,70,200,40]

player1_scorer = 0
player2_scorer = 0

def player1():
    global player1_scorer
    random_no=random.randint(0,11)
    random_pokemon=pokemon[random_no]
    random_dice["image"]=random_pokemon
    random_power_list=power[random_no]
    player1_scorer=player1_scorer+random_power_list
    player1_score["text"]=str(player1_scorer)
    
def player2():
    global player2_scorer
    random_no=random.randint(0,11)
    random_pokemon=pokemon[random_no]
    random_dice["image"]=random_pokemon
    random_power_list=power[random_no]
    player2_scorer=player2_scorer+random_power_list
    player2_score["text"]=str(player2_scorer)

btn=Button(root,image=dice,command=player1)
btn.place(relx=0.1,rely=0.5,anchor=CENTER)
btn1=Button(root,image=dice,command=player2)
btn1.place(relx=0.9,rely=0.5,anchor=CENTER)

root.mainloop()