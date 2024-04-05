from tkinter import *
import os
from tkinter import PhotoImage
from PIL import Image, ImageTk



#Fenêtre principale
root = Tk()


#Configuration de la fenêtre
root.title("Explorateur de fichier")
root.geometry("900x600")


#------------------------Crétaion des frames----------------------------

frame_vertical = Frame(root,bd=0, relief=SOLID, width=200, height=500)
frame_vertical.grid(row=0, column=0,rowspan=2,sticky=N, pady=25)

input_chemin = Entry(root,width=84)
input_chemin.grid(row=0, column=1, sticky=(W,N),padx=5) 

frame_affichage = Frame(root, bg="white", width=680, height=479)
frame_affichage.grid(row=1,column=1,sticky=(W,N),padx=5,pady=5)

#-------------------------END CREATION DES FRAMES----------------------------------------------


#-------------------------------Chemin-----------------------------------

chemin_depart = os.path.expanduser('~')
input_chemin.insert(0,chemin_depart)

#--------------------------------END Chemin--------------------------------------


#----------------------Remplissage du frame vertical-----------------------------

recent = Button(frame_vertical,bg="white", text="Recents",command="",width=20)
recent.grid(row=0, column=0,sticky=N)

favorites = Button(frame_vertical,bg="white",text="Favorites",command="",width=20)
favorites.grid(row=1, column=0, pady=10)

computer = Button(frame_vertical,bg="white",text="Computer",command="",width=20)
computer.grid(row=2, column=0)

tags = Button(frame_vertical,bg="white",text="Tags",command="",width=20)
tags.grid(row=3, column=0,pady=10)

#-----------------------END REMPLISSAGE DU FRAME VERTICAL----------------------------------------------

#Chargeons les images
dossier_path = "dossier.jpg"       
imagee = ImageTk.PhotoImage(file=dossier_path)

dossier_vide_path = "DossierVide.png"
imagee_vide = ImageTk.PhotoImage(file=dossier_vide_path)

fichier_path = "fichier.png"
image_fichier = ImageTk.PhotoImage(file=fichier_path)




# -----------------------------------Fonctions----------------------------------

def ouvrir1(frame):

    for widget in frame.winfo_children():
        widget.destroy()


    """Créer un sous élement"""
    frame_image3 = Frame(frame)
    frame_image3.grid(row=0,column=0)


    aff = Button(frame_image3,image =image_fichier,command=root.quit)
    aff.grid(row=0,column=0)

    texte = Label(frame_image3,text="Ficher1")
    texte.grid(row=1,column=0)

    """Fin création sous élément"""


    """Créer un sous élement"""
    frame_image4 = Frame(frame)
    frame_image4.grid(row=0,column=1)


    aff = Button(frame_image4,image =imagee,command=root.quit)
    aff.grid(row=0,column=0)

    texte = Label(frame_image4,text="Document_Texte")
    texte.grid(row=1,column=0)

    """Fin création sous élément"""
 



def ouvrir2():

    for widget in frame_affichage.winfo_children():
        widget.destroy()
    
    """Création d'un nouveau élément"""

    frame_image5 = Frame(frame_affichage)
    frame_image5.grid(row=0, column=0)

    #charger des images
    nvimgg = "dossier.jpg"       
    imgrr = ImageTk.PhotoImage(file=nvimgg)

    aff = Button(frame_image5, image=imgrr, command="")
    aff.grid(row=0, column=0)

    txt = Label(frame_image5, text="fichier.txt")
    txt.grid(row=1,column=0)

    """Fin de la création d'un nouveau élément"""


def ouvrir3():

    for widget in frame_affichage.winfo_children():
        widget.destroy()
    
    Label(frame_affichage, text="Dossier Vide", font="Times 16 ").grid()

#--------------------------------END FONCTIONS--------------------------------


#-------------------Ajout un élément dans le frame affichage------------------


""" Création d'un dossier """
frame_image = Frame(frame_affichage)
frame_image.grid(row=0,column=0,sticky=N)

#charger des images
dossier_path = "dossier.jpg"       
imagee = ImageTk.PhotoImage(file=dossier_path)

button_image = Button(frame_image, image=imagee,command=lambda: ouvrir1(frame_affichage))
button_image.grid(row=0, column=0)

txt = Label(frame_image, text="Cours")
txt.grid(row=1,column=0)
""" Crétion d'un dossier  Terminer """


""" -------------------------Création d'un dossier------------------------------- """
frame_image1 = Frame(frame_affichage)
frame_image1.grid(row=0,column=1,sticky=N)

""" #charger des images
dossier_path1 = "dossier.jpg"       
imagee1 = ImageTk.PhotoImage(file=dossier_path1) """

button_image1 = Button(frame_image1, image=imagee,command=ouvrir2)
button_image1.grid(row=0, column=0)

txt1 = Label(frame_image1, text="Exercice")
txt1.grid(row=1,column=0)
""" -----------------------Création d'un dossier Terminer------------------------ """



""" --------------------------Création d'un dossier----------------------------- """
frame_image2 = Frame(frame_affichage)
frame_image2.grid(row=0,column=2,sticky=N)

""" #charger des images
dossier_path2 = "dossier.jpg"       
imagee1 = ImageTk.PhotoImage(file=dossier_path2) """

button_image2 = Button(frame_image2, image=imagee,command=ouvrir3)
button_image2.grid(row=0, column=0)

txt1 = Label(frame_image2, text="Travaux")
txt1.grid(row=1,column=0)
""" ---------------------------Création d'un dossier Terminer-------------------- """


#---------------END AJOUT UN ELEMENT DANS LE FRAME AFFICHAGE----------------









root.mainloop() 