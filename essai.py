""" import tkinter as tk

def effacer_et_remplacer(frame):
    # Détruire tous les widgets existants dans le frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Ajouter de nouveaux widgets
    label = tk.Label(frame, text="Nouveau contenu")
    label.pack()
    bouton = tk.Button(frame, text="Cliquez ici")
    bouton.pack()

# Créer la fenêtre principale
root = tk.Tk()
root.geometry("400x300")

# Créer un frame
frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

# Créer des widgets initiaux dans le frame
label_initial = tk.Label(frame, text="Contenu initial")
label_initial.pack()
bouton_initial = tk.Button(frame, text="Effacer et remplacer", command=lambda: effacer_et_remplacer(frame))
bouton_initial.pack()

# Lancer la boucle principale
root.mainloop()
 """




""" import tkinter as tk
from tkinter import filedialog

def parcourir_fichiers():
    fichier = filedialog.askopenfilename(initialdir="/", title="Sélectionner un fichier")
    print("Fichier sélectionné:", fichier)

def parcourir_repertoire():
    repertoire = filedialog.askdirectory(initialdir="/", title="Sélectionner un répertoire")
    print("Répertoire sélectionné:", repertoire)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Explorateur de fichiers")

# Créer le cadre principal
frame_f = tk.Frame(root)
frame_f.pack()

# Bouton pour parcourir les fichiers
bouton_fichier = tk.Button(frame_f, text="Parcourir les fichiers", command=parcourir_fichiers)
bouton_fichier.pack()

# Bouton pour parcourir les répertoires
bouton_repertoire = tk.Button(frame_f, text="Parcourir les répertoires", command=parcourir_repertoire)
bouton_repertoire.pack()

# Lancer la boucle principale de l'interface graphique
root.mainloop() """


#créé un dossier

""" import tkinter as tk
from tkinter import messagebox
import os

def creer_dossier():
    nouveau_dossier = entry_nom_dossier.get()
    if nouveau_dossier:
        try:
            os.mkdir(nouveau_dossier)
            messagebox.showinfo("Succès", f"Le dossier '{nouveau_dossier}' a été créé avec succès.")
        except FileExistsError:
            messagebox.showerror("Erreur", f"Le dossier '{nouveau_dossier}' existe déjà.")
    else:
        messagebox.showerror("Erreur", "Veuillez entrer un nom de dossier.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Créer un nouveau dossier")

# Création du frame
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Création du label et de l'entrée pour le nom du dossier
label_nom_dossier = tk.Label(frame, text="Nom du dossier :")
label_nom_dossier.grid(row=0, column=0, padx=5, pady=5)

entry_nom_dossier = tk.Entry(frame)
entry_nom_dossier.grid(row=0, column=1, padx=5, pady=5)

# Bouton pour créer le dossier
bouton_creer = tk.Button(frame, text="Créer Dossier", command=creer_dossier)
bouton_creer.grid(row=1, columnspan=2, padx=5, pady=5)

root.mainloop() """


#Créer un fichier

""" import tkinter as tk
from tkinter import messagebox
import os

def creer_fichier():
    nouveau_fichier = entry_nom_fichier.get()
    if nouveau_fichier:
        try:
            with open(nouveau_fichier, 'w'):
                pass
            messagebox.showinfo("Succès", f"Le fichier '{nouveau_fichier}' a été créé avec succès.")
        except FileExistsError:
            messagebox.showerror("Erreur", f"Le fichier '{nouveau_fichier}' existe déjà.")
    else:
        messagebox.showerror("Erreur", "Veuillez entrer un nom de fichier.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Créer un nouveau fichier")

# Création du frame
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Création du label et de l'entrée pour le nom du fichier
label_nom_fichier = tk.Label(frame, text="Nom du fichier :")
label_nom_fichier.grid(row=0, column=0, padx=5, pady=5)

entry_nom_fichier = tk.Entry(frame)
entry_nom_fichier.grid(row=0, column=1, padx=5, pady=5)

# Bouton pour créer le fichier
bouton_creer = tk.Button(frame, text="Créer Fichier", command=creer_fichier)
bouton_creer.grid(row=1, columnspan=2, padx=5, pady=5)

root.mainloop() """


import os

dossier = "Cours/Web/Dev"

print(os.path.basename(dossier))


contenu = os.listdir(dossier)

print(contenu)

for i,element in enumerate(os.listdir(dossier)):
    print(element)

# print('\n')

dossier = "Cours"
for dossier_parent, sous_dossier, fichiers in os.walk(dossier):
    print("Dossier parent : ",dossier_parent)
    print("Sous dossier : ",sous_dossier)
    print("Fichiers : ",fichiers)

if os.path.isdir(dossier):
    print("Dossier existe")

# dossier = "Cours"

# for element in os.listdir(dossier):
#     chemin_complet = os.path.join(dossier, element)
#     print(chemin_complet)


# dossier = "Cours/Web/Dev"

# remonter = os.path.dirname(dossier) 

# print("\n",remonter)