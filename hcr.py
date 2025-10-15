import pymem
from pymem import *

import tkinter as tk
from tkinter import *
from tkinter import messagebox

pm = pymem.Pymem("HillClimbRacing.exe")

#if the address is not update use Cheat Engine 
# version game : 1.41.1.0

address_money = 0x005CCAD4 # <-- address static 
address_diams = 0x005CCAEC # <-- address static

root = tk.Tk()
root.title("Hill Climb Racing Hack v1 | by noth1ng_h3re")
root.geometry("520x400")
root.resizable(False, False)
root.configure(bg="orange")

label = tk.Label(root, text="HCR Hack v1", font=("Arial", 16), bg="orange",pady=3,)
label.pack(pady=10)
tk.messagebox = messagebox
label2 = tk.Label(root, text = "entrer le nombre de piece que vous souhaiter :", font =("roman,12"), bg= "orange", pady = 10)
label2.pack(pady= 10)
entry = tk.Entry(root , text = "Nombre de piece a ajouté :", font=("Arial", 12), bg = "white", state= NORMAL)
entry.pack(pady= 10)
button = tk.Button(root, text="Ajouter Piece", font=("Arial", 12), command=lambda: update_piece(),)
button.pack(pady=10)
label3 = tk.Label(root, text = "entrer le nombre de diams que vous souhaiter :", font =("roman,12"), bg= "orange", pady = 10)
label3.pack(pady= 10)
entry = tk.Entry(root , text = "Nombre de Diams a ajouté :", font=("Arial", 12), bg = "white", state= NORMAL)
entry.pack(pady= 10)
button2 = tk.Button(root, text="Ajouter Diams", font=("Arial", 12), command=lambda: update_diams(),)
button2.pack(pady=10)

def update_piece():
    user_input = int(entry.get())   
    pm.write_int(address_money, user_input)
    messagebox.showinfo(f"SUCCES!", f"Les Pieces on bien étais ajouter : {user_input}")
label3 = tk.Label(root, text="", font=("Arial", 12), bg="orange")
label3.pack(pady=5)

def update_diams():
    user_input = int(entry.get())   
    pm.write_int(address_diams, user_input)
    messagebox.showinfo(f"SUCCES!", f"Les Diams on bien étais ajouter : {user_input}")
label4 = tk.Label(root, text="", font=("Arial", 12), bg="orange")
label4.pack(pady=5)


root.mainloop()