from tkinter import *
import random
from PIL import ImageTk, Image
import sys
import os

root = Tk()
root.title("GSSR")

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

servants = "Alexander, Illya, Skadi, Nero(Caster), Merlin, DaVinci, Cleopatra, Shuten, Semiramis, MHX, Hassan, Kintoki, Hijikata, MHXA, Raikou, Amakusa, ShiHuangDi, Holmes, Dantes, Okita(Alter), Kiara, Melt, BB, Abigail, Hokusai, Arthur, Okita, Nero(Bride), Musashi, Shiki(Saber), Artoria(Archer), Ishtar, Gilgamesh, Jeanne(Archer), Moriarty, Ereshkigal, Schatach, Tamamo(Lancer), Brynhild, Artoria(Rider), Ivan"

random_servant = random.choice(servants.split(", "))


my_img = ImageTk.PhotoImage(Image.open("C:/Users/Earl/Pictures/Servant Icons/" + random_servant + ".png"))
my_label = Label(image=my_img)
my_label.pack()

exit_button = Button(root, text="Roll", command=restart_program)
exit_button.pack()

root.mainloop()