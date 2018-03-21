#!/usr/bin/python
#-*-coding:utf-8-*-

import corps_pendu_LINUX as imp
import os
from themes_pendu_LINUX import choix_theme

underline="\033[4m" #sous-ligne le texte
normal="\x1b[0m" #mise en forme normal

global compteur_perdu #la variable 'compteur_perdu' devient global
compteur_perdu=7 #on initialise la variable 'compteur_perdu' qui contient la valeur 7
#----------------------------------------------------------------------------------------------------------------------------------------

os.system("clear") #Ctrl + L pour cacher ce que l'utilisateur a entré
print() #on affiche un retour à la ligne
print("Bienvenue dans notre jeu du pendu !") #message de bienvenu dans le jeu
mot=False #on initialise la variable 'mot' qui est un booléen et qui vaut False
while mot==False: #on va faire tourner une boucle WHILE qui va tourner tant que le booleen 'mot' vaut False
	l=choix_theme()
	mot=l[0] #nous demandons a un utilisateur d'entrer le mot qu'il va devoir faire deviner à l'utilisateur2
	nom_theme=l[1]
	print() #on affiche un retour à la ligne
mot_secret=imp.enMAJ(mot) #nous convertissons le mot aléatoire choisi dans un des themes, puis on l'ajoute dans la variable 'mot_secret'
liste_mot_secret=list(mot_secret) #c'est le mot secret que nous convertissons en liste pour qu'il devienne mutable et pour qu'on puisse le parcourir sans probleme
os.system("clear") #Ctrl + L pour cacher ce que l'utilisateur a entré
liste_devinee=imp.tiret(mot_secret) #on initialise la liste_devinee, elle contient tous les indexs du CHAR 'tiret' et le resultat de la fonction 'tiret'
print(" ",underline+"THEME:"+normal,nom_theme.upper())
print()
mot_a_chercher=imp.conversion_char(imp.affichage(liste_devinee)) #on affiche le mot à cherche (ex: M _ _ _ _ _ )
print() #on affiche un retour à la ligne
print("      ",mot_a_chercher) #on affiche la variable 'mot_a_chercher' pour que le joueur puisse reflechir a partir de celle ci
print() #on affiche un retour à la ligne
gagne=False #on initialise la variable 'gagne' qui est un booléen et qui vaut False
compteur=0 #on initialise la variable 'compteur' avec la valeur 0 si cette variable atteind la valeur de 'compteur_perdu' (7) alors le joueur aura perdu la partie
liste_lettres_testees=[] #on initialise une liste qui contiendra toutes les lettres que le joueur aura essayé
while compteur<compteur_perdu and gagne==False:  #on fait tourner une boucle WHILE qui s'arretera lorsque le joueur aura gagné (quand le booléen 'gagne' aura changé de valeur ou lorsqu'il aura perdu (quand la variable compteur sera supérieur à la valeur de la variable 'compteur_perdu' normalement 7)
	print("Quelle lettre souhaitez-vous essayer ? ") #on print un message au joueur qui lui demande qu'elle lettre il veut essayer
	lettre_testee="" #on initialise une variable 'lettre_testee' qui prend comme valeur la CHAR vide
	test=False #on initialise une variable 'test' qui est un booléen et qui vaut 'False'
	while test==False: #TANT QUE la variable 'test' vaut 'False' alors la boucle sera executée elle permet de savoir si l'utilisateur a fait une erreur de frappe ou pas lors de l'entrée de sa variable 'lettre_testee'
		lettre_testee=input() #on initialise une variable 'lettre_testee' qui prend la valeur que le joueur souhaite essayer
		test=imp.test(lettre_testee) #cette variable 'test' prendra comme valeur le booléen de sorti de la fonction 'test'. elle permet de tester si l'utilisateur a bien entré une seule lettre si non, il affichera des messages d'erreur à l'utilisateur et retournera le booléen 'False' si l'utilisateur a bien entré une seule lettre alors le programme continu (et le booléen retourner vaudra 'True')

	lettre_a_tester=lettre_testee.upper() #on fait en sorte que la variable que le joueur a entré soit toujours en majuscule
	if (imp.deja_essaye(liste_lettres_testees,lettre_a_tester))==False: #si ce test est verifie cela signifie que l'utilisateur a déjà essayé d'entrer cette lettre
		print(underline+"ERREUR:"+normal+" vous avez deja essaye cette lettre.") #si le test est verifié alors on dit au joueur qu'il y a une erreur et qu'il a déjà essayé avec cette valeur
	else:
		os.system("clear")
		if (imp.mot_devine(liste_mot_secret,lettre_a_tester,liste_devinee)==False): #le resultat de la fonction 'mot_devine' est faux, si la 'lettre_a_tester' n'appartient pas au 'mot_secret'
			compteur+=1 # on incremente la variable 'compteur' de 1 si la 'lettre_a_tester' n'appartient pas au 'mot_secret'
			#AJOUTER LA PARTIE DES INTERFACES
			print("Desole cette lettre n'est pas dans le mot...")
		else: #sinon c'est que le resultat de la fonction 'mot_devine' est une liste
			liste_devinee=imp.mot_devine(liste_mot_secret,lettre_a_tester,liste_devinee) #on ajoute le resultat de la fonction 'mot_devine' dans la variable 'liste_devinee' (que l'on ecrase parce qu'elle existé déjà)
			if liste_devinee==liste_mot_secret: #on test SI la 'liste_devinee' et égal à la 'liste_mot_secret', si c'est le cas alors le joueur a gagné et la partie est terminé
				gagne=True #comme la condition a été vérifiée alors on donne la valeur TRUE à gagne pour sortir du WHILE
		print()
		mot_devine=imp.conversion_char(imp.affichage(liste_devinee)) #on convertit notre 'mot_devine' en caractere. qui est le resultat de la fonction affichage avec en parametre liste_devinee
		if compteur<compteur_perdu:
			imp.affichage_matrice(imp.quelle_interface(compteur,mot_devine,compteur_perdu,liste_lettres_testees,nom_theme)) #on print la 'liste_devinee' en CHAR

imp.verite(gagne,compteur,compteur_perdu,mot_secret)


""" si la 1ere lettre du mot est deja dans le mot alors elle est considere comme deja teste """
