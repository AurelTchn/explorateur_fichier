""" import tkinter as tk

def on_enter(event):
    print("Touche Entrer pressée")

# Création de la fenêtre principale
root = tk.Tk()

# Fonction à appeler lorsque la touche Entrer est pressée
root.bind('<Return>', on_enter)

# Affichage de la fenêtre
root.mainloop() """








#La touche Entrer dans Entry

""" import tkinter as tk

def on_enter(event):
    # Récupérer le texte dans le champ Entry
    entry_text = entry.get()
    # Afficher le texte dans la console
    print("Texte entré :", entry_text)

# Création de la fenêtre principale
root = tk.Tk()

# Champ Entry
entry = tk.Entry(root)
entry.pack()

# Lier l'événement de pression de la touche "Entrer" à la fonction on_enter
entry.bind('<Return>', on_enter)

# Affichage de la fenêtre
root.mainloop()
 """



""" import tkinter as tk

def on_backspace(event):
    print("Touche Backspace enfoncée")

root = tk.Tk()

entry = tk.Entry(root)
entry.grid(row=0, column=0)

root.bind("<BackSpace>", on_backspace)

root.mainloop()
 """


#On focus de Entry
""" import tkinter as tk

def on_leave(event):
    # Récupérer le texte dans le champ Entry
    entry_text = entry.get()
    # Afficher le texte dans la console
    print("Texte quitté :", entry_text)

# Création de la fenêtre principale
root = tk.Tk()

# Champ Entry
entry = tk.Entry(root)
entry.pack()

# Lier l'événement de perte de focus (quitte le champ Entry) à la fonction on_leave
entry.bind('<FocusOut>', on_leave)

# Affichage de la fenêtre
root.mainloop()

 """




#Scroll

""" import tkinter as tk

# Fonction de gestion du défilement
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Création de la fenêtre principale
root = tk.Tk()
root.geometry("400x300")

# Cadre pour contenir le contenu à défiler
frame = tk.Frame(root)

# Ajouter une barre de défilement verticale
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Cadre pour contenir le contenu à défiler
canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Lier la barre de défilement au widget Canvas
scrollbar.config(command=canvas.yview)

# Ajouter un deuxième cadre dans le widget Canvas pour contenir le contenu réel
scrollable_frame = tk.Frame(canvas)

# Configurer le widget Canvas pour un défilement
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.bind("<Configure>", on_configure)

# Ajouter le contenu au cadre scrollable_frame (exemple de contenu)
for i in range(50):
    tk.Label(scrollable_frame, text="Ligne {}".format(i+1)).pack()

# Placer le cadre dans la fenêtre principale
frame.pack(fill=tk.BOTH, expand=True)

# Afficher la fenêtre
root.mainloop() """





#Menu contextuel
""" import tkinter as tk

# Fonction pour afficher le menu contextuel
def show_context_menu(event):
    menu.tk_popup(event.x_root, event.y_root)

# Fonction pour gérer l'action "Renommer"
def rename_action():
    print("Action: Renommer")

# Fonction pour gérer l'action "Supprimer"
def delete_action():
    print("Action: Supprimer")

# Fonction pour gérer l'action "Ajouter favori"
def add_favorite_action():
    print("Action: Ajouter favori")

# Fonction pour gérer l'action "Sélectionner"
def select_action():
    print("Action: Sélectionner")

# Création de la fenêtre principale
root = tk.Tk()

button = tk.Button(root,command="")
button.grid()

# Création du menu contextuel
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Renommer", command=rename_action)
menu.add_command(label="Supprimer", command=delete_action)
menu.add_command(label="Ajouter favori", command=add_favorite_action)
menu.add_command(label="Sélectionner", command=select_action)

# Lier l'événement de clic droit à la fonction show_context_menu
button.bind("<Button-3>", show_context_menu)

# Afficher la fenêtre
root.mainloop()  """





#Savoir sur qui clicqué
""" import tkinter as tk

# Fonction pour afficher le menu contextuel
def show_context_menu(event):
    # On détermine quel bouton a été cliqué
    clicked_button = event.widget
    # Afficher le menu contextuel pour ce bouton
    menu.tk_popup(event.x_root, event.y_root)

# Fonction pour gérer l'action "Action 1"
def action1():
    print("Action 1")

# Fonction pour gérer l'action "Action 2"
def action2():
    print("Action 2")

# Fonction pour gérer l'action "Action 3"
def action3():
    print("Action 3")

# Création de la fenêtre principale
root = tk.Tk()

# Création des boutons
button1 = tk.Button(root, text="Bouton 1", command=action1)
button2 = tk.Button(root, text="Bouton 2", command=action2)
button3 = tk.Button(root, text="Bouton 3", command=action3)

# Création du menu contextuel
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Action 1", command=action1)
menu.add_command(label="Action 2", command=action2)
menu.add_command(label="Action 3", command=action3)

# Lier l'événement de clic droit à la fonction show_context_menu pour chaque bouton
button1.bind("<Button-3>", show_context_menu)
button2.bind("<Button-3>", show_context_menu)
button3.bind("<Button-3>", show_context_menu)

# Placement des boutons dans la fenêtre
button1.pack()
button2.pack()
button3.pack()

# Afficher la fenêtre
root.mainloop() """



#Savoir boutton click droit
""" import tkinter as tk

# Fonction pour afficher le menu contextuel
def show_context_menu(event):
    # On détermine quel bouton a été cliqué
    clicked_button = event.widget
    # Afficher le menu contextuel pour ce bouton
    menu.entryconfigure("Action", label=f"Action venant du {clicked_button['text']}")
    menu.tk_popup(event.x_root, event.y_root)

# Fonction pour gérer l'action "Action 1"
def action1():
    print("Action 1")

# Fonction pour gérer l'action "Action 2"
def action2():
    print("Action 2")

# Fonction pour gérer l'action "Action 3"
def action3():
    print("Action 3")

# Création de la fenêtre principale
root = tk.Tk()

# Création des boutons
button1 = tk.Button(root, text="Bouton 1", command=action1)
button2 = tk.Button(root, text="Bouton 2", command=action2)
button3 = tk.Button(root, text="Bouton 3", command=action3)

# Création du menu contextuel
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Action", command=lambda: print(f"Action venant du {button1['text']}"))

# Lier l'événement de clic droit à la fonction show_context_menu pour chaque bouton
button1.bind("<Button-3>", show_context_menu)
button2.bind("<Button-3>", show_context_menu)
button3.bind("<Button-3>", show_context_menu)

# Placement des boutons dans la fenêtre
button1.pack()
button2.pack()
button3.pack()

# Afficher la fenêtre
root.mainloop() """




#Redimensionner
""" 
import tkinter as tk
from PIL import Image, ImageTk


# Création de la fenêtre Tkinter
root = tk.Tk()

# Charger l'image avec PIL
original_image = Image.open("dossier.jpg")

# Redimensionner l'image
resized_image = original_image.resize((100, 100))  # Redimensionner l'image à la taille souhaitée

# Convertir l'image redimensionnée en un objet PhotoImage
photo = ImageTk.PhotoImage(resized_image)



# Affichage de l'image redimensionnée dans une étiquette
label = tk.Label(root, image=photo)
label.pack()

# Afficher la fenêtre Tkinter
root.mainloop() """





#Enlever fond d'une image
""" import tkinter as tk
from PIL import Image, ImageTk


# Création de la fenêtre Tkinter
root = tk.Tk()

# Charger l'image avec PIL
original_image = Image.open("DossierVide.png")

# Convertir l'image en mode RGBA (avec canal alpha)
original_image = original_image.convert("RGBA")

# Créer un nouveau fond transparent
transparent_bg = Image.new("RGBA", original_image.size, (255, 0,0, 0))

# Fusionner l'image originale avec le fond transparent
no_bg_image = Image.alpha_composite(transparent_bg, original_image)

# Convertir l'image fusionnée en un objet PhotoImage
photo = ImageTk.PhotoImage(no_bg_image)



# Affichage de l'image sans fond dans une étiquette
label = tk.Label(root, image=photo)
label.pack()

# Afficher la fenêtre Tkinter
root.mainloop()
 """


#renormmer
""" import tkinter as tk
from tkinter import simpledialog

# Fonction pour ouvrir la fenêtre modale et mettre à jour le label
def update_label():
    new_name = simpledialog.askstring("Modifier le nom", "Entrez le nouveau nom:")
    if new_name:
        label.config(text=new_name)

# Création de la fenêtre principale
root = tk.Tk()

# Label initial
label = tk.Label(root, text="Label initial")
label.pack()

# Bouton pour modifier le label
update_button = tk.Button(root, text="Modifier le label", command=update_label)
update_button.pack()

# Affichage de la fenêtre principale
root.mainloop() """



""" import tkinter as tk
from tkinter import ttk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

root = tk.Tk()
root.title("Défilement avec Frames et grid()")
root.minsize(400,400)
root.maxsize(500,500)

# Création d'un canvas pour contenir les Frames
canvas = tk.Canvas(root)
canvas.grid(row=0, column=0, sticky="nsew")

# Ajout d'une barre de défilement
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
canvas.configure(yscrollcommand=scrollbar.set)

# Frame intérieur dans le Canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

# Configuration pour permettre le défilement
frame.bind('<Configure>', on_configure)

# Création de quelques widgets pour les Frames
for i in range(30):
    tk.Label(frame, text=f"Élément {i}").grid(row=i, column=0, padx=10, pady=5)

# Configuration pour que le canevas s'étende selon la fenêtre
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop() """



#Entrer dans un Entry
""" import tkinter as tk

def on_entry_focus_in(event):
    print("Entrée dans le champ Entry")

root = tk.Tk()

entry = tk.Entry(root)
entry.grid(row=0, column=0)

entry.bind("<FocusIn>", on_entry_focus_in)

root.mainloop() """




""" import os

def get_drive_letters():
    drives = []
    # Parcourir toutes les lettres de lecteur possibles
    for drive_letter in range(65, 91):
        drive = f"{chr(drive_letter)}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives

# Obtenir les lettres de lecteur des partitions
drive_letters = get_drive_letters()

# Afficher les lettres de lecteur des partitions
print("Lettres de lecteur des partitions sur le disque dur:")
for drive_letter in drive_letters:
    print(drive_letter) """



""" import os

def get_partitions():
    partitions = []
    # Parcourir le système de fichiers pour trouver les partitions
    for root, dirs, files in os.walk('/'):
        for name in dirs:
            partition = os.path.join(root, name)
            partitions.append(partition)
    return partitions

# Obtenir les chemins des partitions
partition_paths = get_partitions()

# Afficher les chemins des partitions
print("Chemins des partitions sur le disque dur:")
for partition_path in partition_paths:
    print(partition_path)
 """

""" import tkinter as tk

def open_file():
    file_path = "Amour.odt_0.odt"  # Chemin vers votre fichier
    with open(file_path, "r") as file:
        content = file.read()
    text_box.insert(tk.END, content)

root = tk.Tk()
root.title("Affichage du contenu d'un fichier")

frame = tk.Frame(root)
frame.pack()

text_box = tk.Text(frame, wrap="word")
text_box.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame, command=text_box.yview)
scrollbar.pack(side="right", fill="y")
text_box.config(yscrollcommand=scrollbar.set)

open_button = tk.Button(root, text="Ouvrir le fichier", command=open_file)
open_button.pack()

root.mainloop() """


""" import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        text_box.insert(tk.END, content)

root = tk.Tk()
root.title("Ouvrir un fichier")

frame = tk.Frame(root)
frame.pack()

text_box = tk.Text(frame, wrap="word")
text_box.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame, command=text_box.yview)
scrollbar.pack(side="right", fill="y")
text_box.config(yscrollcommand=scrollbar.set)

open_button = tk.Button(root, text="Ouvrir un fichier", command=open_file)
open_button.pack()

root.mainloop()
 """



""" import os
import tkinter as tk

def open_file():
    file_path = os.popen('zenity --file-selection').read().strip()
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        text_box.insert(tk.END, content)

root = tk.Tk()
root.title("Ouvrir un fichier")

frame = tk.Frame(root)
frame.pack()

text_box = tk.Text(frame, wrap="word")
text_box.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame, command=text_box.yview)
scrollbar.pack(side="right", fill="y")
text_box.config(yscrollcommand=scrollbar.set)

open_button = tk.Button(root, text="Ouvrir un fichier", command=open_file)
open_button.pack()
 
root.mainloop()"""


#Ouvrir un fichier
""" import os
import webbrowser

def open_file(file_path):
    webbrowser.open(file_path)
# Exemple d'utilisation
open_file("dossier.jpg") """


""" #Ouvrir un fichier
import os
import platform

def open_file(file_path):
    system = platform.system()
    if system == "Windows":
        os.startfile(file_path)
    elif system == "Darwin":  # Pour macOS
        os.system("open " + file_path)
    elif system == "Linux":
        os.system("xdg-open " + file_path)
    else:
        print("Système d'exploitation non pris en charge.")

# Exemple d'utilisation
file_path = "fichier.png"  # Remplacez par le chemin de votre fichier
open_file(file_path) """


""" import subprocess

fichier = "Amour.odt_0.odt"

# subprocess.Popen(["xdg-open",fichier])
subprocess.Popen(["libreoffice",fichier]) """


""" import os

root_path = os.path.abspath(os.sep)
print("Chemin du root de l'ordinateur :", root_path) """


import os

chemin_actuel = os.getcwd()


ext = os.path.join(chemin_actuel,"Amour.odt_0.odt")
texte = ext.split('.')
extension = texte[-1]

texte[-1] = "txt"

new = '.'.join(texte)

print(new)

print(extension)