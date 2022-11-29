from tkinter import *
from tkinter import ttk
from PIL import Image

root = Tk()
root.title("Ma page nulle") #C'est mieux avec un nom
root.geometry("600x540") #Créait une fenêtre de 600 par 540 pixels

img_cliq = ""
bouger = False
def choix(val): #Fonction permettant de choisir l'image qui sera créé au prochain clique.
	global img_cliq
	if val == 1: #Le "val" correspond à la valeur qu'envoie le bouton, car les différents boutons activent cette même fonction.
		img_cliq = img1
	elif val == 2:
		img_cliq = img2
	elif val == 3:
		img_cliq = img3

def keydown(e):
	if e.char == "c": #Si j'appuie sur c
		print("Ordinateur")
		dessin.create_image(e.x-10,e.y-20,image=img1) #Créais l'image de l'ordinateur sur la position de la souris, et décalé de 10 et 20 pixels pour que ce soit centré sur la souris
	elif e.char == "s":
		print("Switch")
		dessin.create_image(e.x-10,e.y-20,image=img2)
	elif e.char == "r":
		print("Switch")
		dessin.create_image(e.x-10,e.y-20,image=img3)


def sup(image, e):
	global bouger
	global jessai
	print("ok")
	if not bouger:
		dessin.delete(image) #Supprime l'image qu'on déplacé
		jessai = dessin.create_image(e.x-10,e.y-20,image=img1) #Pour en créer une autre
		bouger = True #Flag servant à dire au programme qu'une image suit le curseur

def move(e):
	global bouger
	global jessai
	if bouger: #Si le flag est activé, l'image suis le curseur.
		dessin.delete(jessai)
		jessai = dessin.create_image(e.x-10,e.y-20,image=img1)
		dessin.tag_bind(jessai,"<Button-3>", lambda event: sup(jessai, e))

def clique(pos):
	global img_cliq
	global bouger
	bouger = False #Dit au programme que plus rien ne suis le curseur et fige l'image qui le suivait
	if img_cliq != "" and pos.x > 25 and pos.y>30: #Permet de ne pas poser d'image en dehors du cadre
		image = dessin.create_image(pos.x,pos.y,image=img_cliq) #Créer l'image à la position du clique
		dessin.tag_bind(image,"<Button-3>", lambda event: sup(image, pos, img_cliq)) #Lie une fonction à l'image: au clic droit, déclenche la fonction "sup"
		img_cliq = "" #Il n'y a plus d'image sélectionné, il faut recliquer sur un des boutons


but1=ttk.Button(root, width = 10, text="Ordinateur",command=lambda: choix(1)) #Si j'appuie sur le bouton 1, déclenche la fonction "choix" avec comme valeur "1"
but1.place(x=10,y=10)
but2=ttk.Button(root, width = 10, text="Switch",command=lambda: choix(2))
but2.place(x=100,y=10)
but3=ttk.Button(root, width = 10, text="Routeur",command=lambda: choix(3))
but3.place(x=190,y=10)

lg, ht = 600,540
dessin=Canvas(root,bg="ivory",width=lg,height=ht)
dessin.pack(side='bottom', padx=20, pady=40)

img1 = PhotoImage(file = 'Ordinateur.png') #Définit les différentes images
img2 = PhotoImage(file = 'Switch.png')
img3 = PhotoImage(file = 'Routeur.png')

root.bind("<KeyPress>", keydown) #Si j'appuie sur une touche, déclenche keydown
root.bind("<Motion>",move) #Si je bouge ma souris, déclenche move
root.bind('<Button 1>',clique) #Si je clique gauche, déclenche clique

root.mainloop()
