from tkinter import messagebox

import pygame
import random
import tkinter as tk


def cancel():
    click.play()
    window.destroy()


def guess():
    click.play()
    nom = nom_entry.get()
    if len(nom) != 6 or nom.isdigit() == False or int(nom) < 0:
        mistake.play()
        tk.messagebox.showwarning('Неверный ввод!', 'Нужно ввести 6-ти значное, целое, положительное число!')
        return 0

    nom_entry.delete(0, 6)
    # turns_countdown()

    part1 = list(nom[:3])
    part2 = list(nom[3:])

    random.shuffle(part1)
    random.shuffle(part2)
    
    part1, part2 = "".join(part1), "".join(part2)
    part3 = str(int(part1) + int(part2))
    if len(part3) < 4:
        part3 = "0" + part3

    part1 += "".join(random.choices(ALTHA, k=2))
    part2 += "".join(random.choices(ALTHA, k=2))


    password_label.configure(text=part1 + "-" + part2 + " " + part3)


ALTHA = "QWERTYUIOPASDFGHJKLZXCVBNM"

pygame.mixer.init()

mistake = pygame.mixer.Sound("gameover.ogg")
start = pygame.mixer.Sound("gamestart.ogg")
click = pygame.mixer.Sound("click.ogg")
start.play()

window = tk.Tk()
window.title('My app')
window.geometry('414x414')
bg_img = tk.PhotoImage(file='tanks.png')

label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

password_label = tk.Label(window, text='', font=('Consolas', 20), bg='red', fg='white')
password_label.place(x=0, y=300, relwidth=1)

nom_label = tk.Label(window, text='Введите 6-ти значное натуральное число: ', font=('Verdana', 13))
nom_label.place(relwidth=1, rely=0.35)

nom_entry = tk.Entry(window, width=6, font=('Verdana', 16))
nom_entry.insert(0, '123456')
nom_entry.place(relx=0.4, rely=0.45)

btn_guess = tk.Button(window, text='Создать', bg="LawnGreen", width=15, command=guess)
btn_guess.place(relx=0.15, rely=0.6)

btn_cancel = tk.Button(window, text='Cancel', width=15, command=cancel)
btn_cancel.place(relx=0.6, rely=0.6)

window.mainloop()