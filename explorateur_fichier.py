from tkinter import *
import os
from tkinter import PhotoImage
from PIL import Image, ImageTk
import time
from tkinter import simpledialog
from tkinter import messagebox
import subprocess

#Fenêtre principale
root = Tk()

#Configuration de la fenêtre
root.title("Explorateur de fichier")
root.geometry("1200x580")
root.minsize(1200,580)
root.maxsize(1200,580)



#-------------------------Crétaion des frames--------------------------
frame_vertical = Frame(root,bd=0, relief=SOLID, width=200, height=500)
frame_vertical.grid(row=0, column=0,rowspan=2,sticky=N, pady=25)

frame_haut = Frame(root)
frame_haut.grid(row=0,column=1,sticky=N)
input_chemin = Entry(frame_haut, font="Times 16 ",width=50)
input_chemin.grid(row=0, column=0, sticky=(W,N),padx=5)

#Création du frame pour la recherche
recherche = Entry(frame_haut,font="Times 16 ")
recherche.grid(row=0, column=1, sticky=(W,N),padx=5)

recherche.insert(0,"Rechercher")

#Ecouter l'évènement entrer sur le champ recherche
def on_entry_focus_in(event):
    recherche.delete(0,END)

recherche.bind("<FocusIn>", on_entry_focus_in)


def quitter(event):
    recherche.delete(0,END)
    recherche.insert(0,"Recherche")

# Ecouter l'évènement lorsqu'on sort du champ de la recherche
recherche.bind('<FocusOut>', quitter)


#Chemin principal du système d'exploitation en question
chemin_actuel = os.path.expanduser('~')
input_chemin.insert(0,chemin_actuel)

def on_enter(event):
    global chemin_actuel
    # Récupérer le texte dans le champ Entry
    entry_text = input_chemin.get()
    #Actualiser le chemin_actuel
    chemin_actuel = entry_text
    
    try:
        for widget in frame_affichage.winfo_children():
            widget.destroy()    
        if len(os.listdir(chemin_actuel)) != 0: 
            r = 0
            j = 0
            for ell in os.listdir(chemin_actuel):
                if j == 7:
                    r +=2
                    j = 0

                if os.path.isdir(os.path.join(chemin_actuel,ell)):
                
                    if not ell.startswith('.'):
                        frame_image1 = Frame(frame_affichage)
                        frame_image1.grid(row=r,column=j,sticky=N)
                        mondossier1 = Dossier(os.path.basename(ell),frame_image1)
                        mondossier1.AffDossier()
                        j +=1
                
                if os.path.isfile(os.path.join(chemin_actuel,ell)):
                    if not ell.startswith('.'):
                        frame_image = Frame(frame_affichage)
                        frame_image.grid(row=r,column=j,sticky=N)
                        mondossier1 = Dossier(os.path.basename(ell),frame_image)
                        mondossier1.AffFichier()
                        j +=1
                

        else:
            frame_image = Frame(frame_affichage)
            frame_image.grid(row=0,column=0,sticky=N,padx=300)
            aff = Label(frame_image, text= "Dossier vide" ,font="Times 16 bold")
            aff.grid(row=0,column=0) 
        
    except Exception as e:
        messagebox.showerror("Erreur", f"Chemin incorrecte ")



# Lier l'événement de pression de la touche "Entrer" à la fonction on_enter
input_chemin.bind('<Return>', on_enter)


#-------------------Backspace

def backspace(event):
    global chemin_actuel
    chem = chemin_actuel
    chemin_actuel = os.path.dirname(chem)
    input_chemin.delete(0,END)
    input_chemin.insert(0,chemin_actuel)

    try:
         
        for widget in frame_affichage.winfo_children():
            widget.destroy()
        

        if len(os.listdir(chemin_actuel)) != 0: 

            r = 0
            j = 0
            for ell in os.listdir(chemin_actuel):
                if j == 7:
                    r +=2
                    j = 0

                if os.path.isdir(os.path.join(chemin_actuel,ell)):
                
                    if not ell.startswith('.'):
                        frame_image1 = Frame(frame_affichage)
                        frame_image1.grid(row=r,column=j,sticky=N)
                        mondossier1 = Dossier(os.path.basename(ell),frame_image1)
                        mondossier1.AffDossier()
                        j +=1
                
                if os.path.isfile(os.path.join(chemin_actuel,ell)):
                    if not ell.startswith('.'):
                        frame_image = Frame(frame_affichage)
                        frame_image.grid(row=r,column=j,sticky=N)
                        mondossier1 = Dossier(os.path.basename(ell),frame_image)
                        mondossier1.AffFichier()
                        j +=1
                

        else:
            frame_image = Frame(frame_affichage)
            frame_image.grid(row=0,column=0,sticky=N,padx=300)
            aff = Label(frame_image, text= "Dossier vide" ,font="Times 16 bold")
            aff.grid(row=0,column=0) 

    except Exception as e:
            messagebox.showerror("Erreur", f"Chemin incorrecte.")

#Evenement backspace sur la fenêtre principale
root.bind("<BackSpace>",backspace)


#-------------------------scroll-----------------------------
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

# Création d'un canvas pour contenir les Frames
canvas = Canvas(root)
canvas.grid(row=1, column=1, sticky="nsew")

# Ajouter un poids à la rangée pour agrandir le canevas
root.grid_rowconfigure(1, weight=1)

# Ajout d'une barre de défilement
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.grid(row=0, column=5,rowspan=5, sticky="ns")
canvas.configure(yscrollcommand=scrollbar.set)


# Frame intérieur dans le Canvas
frame_affichage = Frame(canvas,bd=1, relief=SOLID,width=680)
canvas.create_window((0, 0), window=frame_affichage, anchor='nw')


# Configuration pour permettre le défilement
frame_affichage.bind('<Configure>', on_configure)


#Fonction du boutton Computer
def computer():
    global chemin_actuel
    chemin_actuel = os.path.abspath(os.sep)
    input_chemin.delete(0,END)
    input_chemin.insert(0,chemin_actuel)

    try:
         
        for widget in frame_affichage.winfo_children():
            widget.destroy()
        

        if len(os.listdir(chemin_actuel)) != 0: 

            r = 0
            j = 0
            for ell in os.listdir(chemin_actuel):
                if j == 7:
                    r +=2
                    j = 0

                if os.path.isdir(os.path.join(chemin_actuel,ell)):
                
                    if not ell.startswith('.'):
                        frame_image1 = Frame(frame_affichage)
                        frame_image1.grid(row=r,column=j,sticky=N)
                        mondossier1 = Dossier(os.path.basename(ell),frame_image1)
                        mondossier1.AffDossier()
                        j +=1
                
                if os.path.isfile(os.path.join(chemin_actuel,ell)):
                    if not ell.startswith('.'):
                        frame_image = Frame(frame_affichage)
                        frame_image.grid(row=r,column=j,sticky=N)
                        mondossier1 = Dossier(os.path.basename(ell),frame_image)
                        mondossier1.AffFichier()
                        j +=1
                

        else:
            frame_image = Frame(frame_affichage)
            frame_image.grid(row=0,column=0,sticky=N,padx=300)
            aff = Label(frame_image, text= "Dossier vide" ,font="Times 16 bold")
            aff.grid(row=0,column=0) 

    except Exception as e:
            messagebox.showerror("Erreur", f"Chemin incorrecte")




#-------------------------Remplissage du frame vertical----------------------

recent = Button(frame_vertical,bg="white",font="Times 16 bold ", text="Recents",command="",width=20)
recent.grid(row=0, column=0,sticky=N)

favorites = Button(frame_vertical,bg="white",font="Times 16 bold ",text="Favorites",command="",width=20)
favorites.grid(row=1, column=0, pady=10)

computer = Button(frame_vertical,bg="white",font="Times 16 bold ",text="Computer",command=computer,width=20)
computer.grid(row=2, column=0)

tags = Button(frame_vertical,bg="white",font="Times 16 bold ",text="Tags",command="",width=20)
tags.grid(row=3, column=0,pady=10)

#---------------------------------------------------------


#Chargeons les images

path_dossier = Image.open("Sans.png")
dossier_resize = path_dossier.resize((100,100))
image_dossier = ImageTk.PhotoImage(dossier_resize)

path_fichier = Image.open("imagesFichier.png")
path_fichier_resize = path_fichier.resize((100,100))
image_fichier = ImageTk.PhotoImage(path_fichier_resize)

#Temps pour un click sur un boutton dossier
last_click_time = 0

#--------------------------Création du dossier parent -----------------

dossier_principal = chemin_actuel.split("/")
dossier_principal = dossier_principal[-1]

if not os.path.exists(dossier_principal):
    os.mkdir(dossier_principal)


#Temps click sur un button fichier
last_click_time_fichier = 0


#----------------------Classe--------------------------------------

class Dossier():

    def __init__(self, texte,frame):
        self.texte = texte
        self.frame = frame

    
    def command_ouvrir(self):
        
        try : 
            global chemin_actuel
            global dossier_principal
            global chemin_actuel
            global last_click_time

        
            for widget in frame_affichage.winfo_children():
                widget.destroy()

            chemin_actuel = os.path.join(chemin_actuel,self.texte)
            input_chemin.delete(0,END)
            input_chemin.insert(0, chemin_actuel)

            chemin_parent = os.getcwd()
            chemin_complet = os.path.join(chemin_parent,self.texte)
                    

            if len(os.listdir(chemin_actuel)) != 0:
                une_fois_aff = False
                r = 0
                i = 0
                for el in os.listdir(chemin_actuel):
                            
                        if i == 7:
                            r += 2 
                            i = 0

                        if os.path.isdir(os.path.join(chemin_actuel,el)):
                            if not el.startswith('.'):
                                    
                                    
                                frame_image3 = Frame(frame_affichage)
                                frame_image3.grid(row=r,column=i,sticky=N)
                                mondossier = Dossier(os.path.basename(el),frame_image3)
                                mondossier.AffDossier()
                                i += 1
                                une_fois_aff = True
                                    
                            
                        elif os.path.isfile(os.path.join(chemin_actuel,el)):
                                
                            if not el.startswith('.'):
                                frame_image = Frame(frame_affichage)
                                frame_image.grid(row=r,column=i,sticky=N)
                                monfichier = Dossier(os.path.basename(el),frame_image)
                                monfichier.AffFichier()
                                i += 1
                                une_fois_aff = True
                                
                            
                if une_fois_aff == False :
                                frame_image = Frame(frame_affichage)
                                frame_image.grid(row=0,column=0,sticky=N,padx=300)
                                aff = Label(frame_image, text= "Dossier vide" ,font="Times 16 bold")
                                aff.grid(row=0,column=0)

            else:
                    frame_image = Frame(frame_affichage)
                    frame_image.grid(row=0,column=0,sticky=N,padx=380)
                    aff = Label(frame_image, text= "Dossier vide" ,font="Times 16 bold")
                    aff.grid(row=0,column=0)
        except Exception as e:
            messagebox.showerror("Erreur",f"Impossible d'ouvrir {e}")
    
    def ouvrir(self):
        try :   
            global chemin_actuel
            global dossier_principal
            global chemin_actuel
            global last_click_time

            if time.time() - last_click_time < 0.25:

                for widget in frame_affichage.winfo_children():
                    widget.destroy()

                chemin_actuel = os.path.join(chemin_actuel,self.texte)
                input_chemin.delete(0,END)
                input_chemin.insert(0, chemin_actuel)

                chemin_parent = os.getcwd()
                chemin_complet = os.path.join(chemin_parent,self.texte)
                
                if len(os.listdir(chemin_actuel)) != 0:
                    une_fois_aff = False
                    r = 0
                    i = 0
                    for el in os.listdir(chemin_actuel):
                        
                        if i == 7:
                            r += 2 
                            i = 0

                        if os.path.isdir(os.path.join(chemin_actuel,el)):
                            if not el.startswith('.'):
                                
                                
                                frame_image3 = Frame(frame_affichage)
                                frame_image3.grid(row=r,column=i,sticky=N)
                                mondossier = Dossier(os.path.basename(el),frame_image3)
                                mondossier.AffDossier()
                                i += 1
                                une_fois_aff = True
                                
                        
                        elif os.path.isfile(os.path.join(chemin_actuel,el)):
                            
                            if not el.startswith('.'):
                                frame_image = Frame(frame_affichage)
                                frame_image.grid(row=r,column=i,sticky=N)
                                monfichier = Dossier(os.path.basename(el),frame_image)
                                monfichier.AffFichier()
                                i += 1
                                une_fois_aff = True
                               
                        
                    if une_fois_aff == False :
                            frame_image = Frame(frame_affichage)
                            frame_image.grid(row=0,column=0,sticky=N,padx=300)
                            aff = Label(frame_image, text= "Dossier vide" ,font="Times 16 bold")
                            aff.grid(row=0,column=0)

                else:
                    frame_image = Frame(frame_affichage)
                    frame_image.grid(row=0,column=0,sticky=N,padx=380)
                    aff = Label(frame_image, text= "Dossier vide" ,font="Times 16 bold")
                    aff.grid(row=0,column=0)

                last_click_time = 0

            else:
                last_click_time = time.time()
        except Exception as e:
            messagebox.showerror("Erreur",f"Impossible d'ouvrir: {e}")
    
    def ouvrir_fichier(self):
        global last_click_time_fichier
        global chemin_actuel

        if time.time() - last_click_time_fichier < 0.25:
            subprocess.Popen(["xdg-open",os.path.join(chemin_actuel,self.texte)])
        else:
            last_click_time_fichier = time.time()
        
    
    def AffFichier(self):
        aff = Button(self.frame,image=image_fichier,command=self.ouvrir_fichier)
        aff.grid(row=0,column=0)

        autre_nom = self.texte
        if len(self.texte) > 10: 
            autre_nom = self.texte[:10]+"..."

        self.txt = Label(self.frame,text=autre_nom,font="Times 16 ",width=13)
        self.txt.grid(row=1,column=0)

        # Ecouter l'évènement du click droit sur un fichier
        aff.bind("<Button-3>", self.show_context_menu_fichier)

    
  
    def AffDossier(self):
        
        
        aff = Button(self.frame,image=image_dossier,command=self.ouvrir)
        aff.grid(row=0,column=0)

        autre_nom = self.texte
        
        if len(self.texte) > 10: 
            autre_nom = self.texte[:10]+"..."
        self.txt = Label(self.frame,text=autre_nom,font="Times 16 ",width=13)
        self.txt.grid(row=1,column=0)


        # Ecouter l'évènement du click droit sur un dossier
        aff.bind("<Button-3>", self.show_context_menu)

    def ouvrir_fichier_context(self):
        try:
            global last_click_time_fichier
            global chemin_actuel
            subprocess.Popen(["xdg-open",os.path.join(chemin_actuel,self.texte)])
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir {e}")

    # Fonction pour afficher le menu contextuel
    def show_context_menu_fichier(self,event):
        # Création du menu contextuel
        menu = Menu(root, tearoff=0)
        menu.add_command(label="Ouvrir",font="Times 14 bold", command=self.ouvrir_fichier_context)
        menu.add_command(label="Renommer",font="Times 14 bold", command=self.update_label)
        menu.add_command(label="Ajouter favori",font="Times 14 bold", command=self.ajout_favori)
        menu.add_command(label="Supprimer",font="Times 14 bold", command=self.supprimer_dossier)

        menu.tk_popup(event.x_root, event.y_root)   

    # Fonction pour afficher le menu contextuel
    def show_context_menu(self,event):
        # Création du menu contextuel
        menu = Menu(root, tearoff=0)
        menu.add_command(label="Ouvrir",font="Times 14 bold", command=self.command_ouvrir)
        menu.add_command(label="Renommer",font="Times 14 bold", command=self.update_label)
        menu.add_command(label="Ajouter favori",font="Times 14 bold", command=self.ajout_favori)
        menu.add_command(label="Supprimer",font="Times 14 bold", command=self.supprimer_dossier)

        menu.tk_popup(event.x_root, event.y_root)


    def supprimer_dossier(self):
        global chemin_actuel
        global frame_affichage
        try:
            confirmation = messagebox.askquestion("Confirmation", f"Voulez-vous vraiment supprimer le dossier '{self.texte}' ?")
            
            if confirmation == "yes":
                os.rmdir(os.path.join(chemin_actuel, self.texte))
                print("Vous aviez supprimer : ",os.path.join(chemin_actuel, self.texte))
                
                for widget in frame_affichage.winfo_children():
                    widget.destroy()

                if len(os.listdir(chemin_actuel)) != 0: 

                    r = 0
                    j = 0
                    for ell in os.listdir(chemin_actuel):
                        if j == 7:
                            r +=2
                            j = 0
                        
                        if os.path.isdir(os.path.join(chemin_actuel,ell)):
                        
                            if not ell.startswith('.'):
                                frame_image1 = Frame(frame_affichage)
                                frame_image1.grid(row=r,column=j,sticky=N)
                                mondossier1 = Dossier(os.path.basename(ell),frame_image1)
                                mondossier1.AffDossier()
                                j +=1
                        
                        if os.path.isfile(os.path.join(chemin_actuel,ell)):
                            if not ell.startswith('.'):
                                frame_image = Frame(frame_affichage)
                                frame_image.grid(row=r,column=j,sticky=N)
                                mondossier1 = Dossier(os.path.basename(ell),frame_image)
                                mondossier1.AffFichier()
                                j +=1
                        
                else:
                    frame_image = Frame(frame_affichage)
                    frame_image.grid(row=0,column=0,sticky=N,padx=300)
                    aff = Label(frame_image, text= "Dossier vide" ,font="Times 16 bold")
                    aff.grid(row=0,column=0) 
            else:
                pass
        except OSError as e:
            print(f"Erreur: {os.path.join(chemin_actuel, self.texte)} : {e.strerror}")
            
    # Fonction pour gérer l'action "Renommer" appeller update_label
    def renommer(self):
        global chemin_actuel
        new_name = simpledialog.askstring("Modifier le nom", "Entrez le nouveau nom:")
        
        if new_name:
            try:
                os.rename(os.path.join(chemin_actuel,self.texte), os.path.join(chemin_actuel,new_name))
                chemin_actuel = os.path.join(chemin_actuel,new_name)
                chemin_actuel = os.path.dirname(chemin_actuel)
                self.txt.config(text=new_name)
                self.texte = new_name
                messagebox.showinfo("Succès", f"Le dossier '{self.texte}' a été renommé en '{new_name}'.")
            
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors du renommage du dossier : {e}")

    # Fonction pour gérer l'action "Ajouter favori"
    def ajout_favori(self):
        global favori
        global chemin_actuel

        favori.append(os.path.join(chemin_actuel, self.texte))
        print(favori)

with open("favori","a+",newline="") as file:
    file.write("Oui")


favori = [] 


#Menu contextuel

def show_context_menu_simple(event):
        menu_simple.tk_popup(event.x_root, event.y_root)


# Fonction pour gérer l'action "Renommer"
def nDossier():
    pass
        

# Création du menu contextuel pour root
menu_simple = Menu(root, tearoff=0)
menu_simple.add_command(label="Nouveau Dossier",font="Times 14 bold", command=nDossier)

frame_affichage.bind("<Button-3>", show_context_menu_simple)

    
def go_back_():
        global chemin_actuel
        global dossier_principal

        chemin_actuel = os.path.dirname(chemin_actuel)
        input_chemin.delete(0,END)
        input_chemin.insert(0,chemin_actuel)

        for widget in frame_affichage.winfo_children():
            widget.destroy()
        

        if len(os.listdir(chemin_actuel)) != 0: 

            r = 0
            j = 0
            for ell in os.listdir(chemin_actuel):
                if j == 7:
                    r +=2
                    j = 0


                if os.path.isdir(os.path.join(chemin_actuel,ell)):
                
                    if not ell.startswith('.'):
                        frame_image1 = Frame(frame_affichage)
                        frame_image1.grid(row=r,column=j,sticky=N)
                        mondossier1 = Dossier(os.path.basename(ell),frame_image1)
                        mondossier1.AffDossier()
                        j +=1
                
                if os.path.isfile(os.path.join(chemin_actuel,ell)):
                    if not ell.startswith('.'):
                        frame_image = Frame(frame_affichage)
                        frame_image.grid(row=r,column=j,sticky=N)
                        mondossier1 = Dossier(os.path.basename(ell),frame_image)
                        mondossier1.AffFichier()
                        j +=1
                

        else:
            frame_image = Frame(frame_affichage)
            frame_image.grid(row=0,column=0,sticky=N,padx=300)
            aff = Label(frame_image, text= "Dossier vide" ,font="Times 16 bold")
            aff.grid(row=0,column=0) 


#Création du boutton go_back
back = Button(frame_haut, text="Back",font="Times 16 bold ",command=go_back_)
back.grid(row=0,column=2)


dossier_personnel = os.listdir(os.path.expanduser('~'))

def main(path):

    for widget in frame_affichage.winfo_children():
            widget.destroy()

    if len(path) != 0: 

        r = 0
        j = 0
        for i,obj in enumerate(path):
            if j == 7:
                r +=2
                j = 0

            if os.path.isdir(os.path.join(os.path.expanduser('~'),obj)):
            
                if not obj.startswith('.'):
                    frame_image1 = Frame(frame_affichage)
                    frame_image1.grid(row=r,column=j,sticky=N)
                    mondossier1 = Dossier(os.path.basename(obj),frame_image1)
                    mondossier1.AffDossier()
                    j +=1
            
            if os.path.isfile(os.path.join(os.path.expanduser('~'),obj)):
                
                if not obj.startswith('.'):
                    frame_image = Frame(frame_affichage)
                    frame_image.grid(row=r,column=j,sticky=N)
                    mondossier1 = Dossier(os.path.basename(obj),frame_image)
                    mondossier1.AffFichier()
                    j +=1
            

    else:
        frame_image = Frame(frame_affichage)
        frame_image.grid(row=0,column=0,sticky=N,padx=300)
        aff = Label(frame_image, text= "Dossier vide" ,font="Times 16 bold")
        aff.grid(row=0,column=0) 


if __name__ == "__main__":
    main(dossier_personnel)

#Affichage de la fenêtre
root.mainloop()