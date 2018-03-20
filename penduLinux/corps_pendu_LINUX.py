²#!/usr/bin/python3
#-*-coding:utf-8-*-

import os
import time
import string

global underline, normal, r, b, c, p
underline="\033[4m"	
r="\x1b[2;31;20m" #red color
b="\x1b[0m" #white color
c="\x1b[1;34;20m" #cyan color
p="\x1b[1;35;20m" #pink color
y="\x1b[1;33;20m" #yellow color
bold="\033[1m" #bold
normal="\x1b[0m" #rien

#----------FONCTIONS--------------------------------------------------------------------------------------------------------------------------


def enMAJ(mott:str):
	""" cette fonction 'enMAJ' prend en entrée un mot et le convertit entierement en majuscules """
	mot=mott.upper() #on aggrandit le mot avec la focntion upper
	return(mot) #à la fin de la fonction 'enMAJ', on retourne la CHAR 'mot'

def conversion_char(l:list):
	""" cette fonction 'conversion_char' prend en entrée une liste et la convertie en chaine de caractere"""
	bob="" #on initialise une variable 'bob' qui est une chaine de caractere vide
	for i in range(len(l)): #on parcourt l'input avec une boucle for
		bob+=l[i] #à chaque index de celle-ci on ajoute a notre variable bob chaque index converti en STR de notre liste
	return(bob) #à la fin de la fonction, on retourne la CHAR 'bob'
     
def tiret(mot:str): 
	"""cette fonction transforme un mot en liste composée de n tiret qui correspondent à la longueur du mot (ex:["m","_","_","_","_","_","_"])"""
	l=[] #on initialise un liste 'l' vide
	l.append(mot[0]) #on append la 1ere lettre du 'mot_secret'
	for i in range (1,len(mot)): #on parcourt l'input avec une boucle for
		l.append("_") #à chaque tour de boucle on ajoute la CHAR "_ " dans notre liste 'l'
	return(l) #en resultat de la fonction 'tiret' on retourne notre liste 'l'

def de_mutabilisation(l:list):
	""" cette fonction permet de copier une liste dans une nouvelle liste 'nl' """
	nl=[] #on initialise une nouvelle liste 'nl' vide
	for i in range(len(l)): #on parcourt la liste l
		nl.append(l[i]) #à chaque tour de boucle on ajoute chaque index de 'l' dans 'nl'
	return(nl) #en resultat de la fonction 'de_mutabilisaion' nous allons retourner une copie de la liste donnée en entrée 'nl'

def test(lettre:str):
	if len(lettre)==0:
		print(underline+"ERREUR:"+normal+" vous avez oublié d'entrer une lettre.")
		return(False)
	elif len(lettre)==1:
		if lettre[0] not in string.ascii_lowercase and lettre[0] not in string.ascii_uppercase:
			print(underline+"ERREUR:"+normal+" vous ne pouvez entrer que des lettres.")
			return(False)
	elif len(lettre)>1:#on verifie que le joueur n'a entré qu'une seule lettre
		que_des_lettres=True #on initialise une variable booléene 'que_des_lettres' pour tester si il n'y a que des lettres dans 'lettre_testees'
		for i in range(len(lettre)):
			if lettre[i] not in string.ascii_lowercase and lettre[i] not in string.ascii_uppercase: #la variable'que_des_lettres' prend le booléen False si 'lettre_testee' n'est pas composé que de lettre
				que_des_lettres=False 
		if que_des_lettres==False:
			print(underline+"ERREUR:"+normal+" vous ne pouvez entrer qu'un seul caractere, qui doit etre une lettre.")
			return(False)
		else: 
			print(underline+"ERREUR:"+normal+" vous ne pouvez pas entrer plusieurs lettres.")
			return(False)
	return(True)

def affichage(li:list):
	""" cette fonction permet d'afficher clairement le 'mot_devinee' pour que l'utilisateur voit bien ou il en est ; elle ajoute des espaces entre chaque index de la liste de base """
	l=de_mutabilisation(li)
	for i in range(1,len(l)*2-1,2): #avec une boucle for nous allons parcourir la liste 'l' avec un pas de 2   
		l.insert(i," ") #à chaque index i de la liste nous allons inserer un espace pour rendre notre liste lisible
	return(l) #en resultat de la fonction 'affichage' nous allons retourner la liste

def affichage_matrice(li:list):
	"""cette fonction 'affichage_matrice' permet d'afficher proprement une matrice (ici elle sera utilisée pour afficher le "dessin" du pendu)"""
	l=de_mutabilisation(li)
	for i in range(len(l)): #nous parcourons notre liste avec i
		somme=""
		for j in range(len(l[i])): #nous parcourons nos sous-listes avec j
			if len(l[i])>1:
				somme+=l[i][j]
		l[i]=somme
	for i in range(len(l)):
		print(l[i])
	return("")

def affichage_lettre_testees(li:list):
	""" cette fonction 'affichage_lettre_testees' prend en parametre une liste 'li', elle permet de faire un bel affichage des lettres que le joueur a deja testée, cette fonction va être utilisée dans la fonction 'quelle_interface' """
	l=de_mutabilisation(li)
	bob="[ "
	for i in range(len(l)):
		if i<(len(l))-1:
			bob+=str(l[i])+", "
		else:
			bob+=str(l[i])+" ]"
	return(bob) #en resultat de la fonction 'affichage_lettre_testees' nous allons retourner la CHAR 'bob'

def list_keys_up(l:list): 
	""" cette fonction 'list_keys_up' prend en parametre une liste 'l', elle permet de up la 1ere lettre de chacun des noms des themes """
	for i in l:
		for j in i:
			b=j.upper()
			j=b
	return(l)

def animation_perdu(mot:str):
	game_over=[["",r+bold+"  ___   __   _  _  ____     __   _  _  ____  ____ "+b+normal],["",r+bold+" / __) / _\ ( \/ )(  __)   /  \ / )( \(  __)(  _ \ "+b+normal],["",r+bold+"( (_ \/    \/ \/ \ ) _)   (  O )\ \/ / ) _)  )   /"+normal+b],["",r+bold+" \___/\_/\_/\_)(_/(____)   \__/  \__/ (____)(__\_)"+b+normal]]
	inter7a=[["Le mot secret était : ",r+underline+mot+normal+b,"."],[""],["                 ","     ┏━━━━━━┓"],["                 ","     ┃    "+r+"  ⬤  `"+b],["                 ","     ┃   "+r+" ╾━╋━╼ "+b],["                 ","     ┃     "+r+"◞┃◟"+b],["                 ","     ┃  "+r+"   ┛ ┗ "+b],["                 ","     ┃"],["                 "," ▔▔▔▔▔▔▔▔▔"],[""]]
	inter7b=[["Le mot secret était : ",r+underline+mot+normal+b,"."],[""],["                 ","     ┏━━━━━━┓"],["                 ","     ┃    "+r+"  ⬤  `"+b],["                 ","     ┃   "+r+" ╾━╋━╼ `"+b],["                 ","     ┃     "+r+"◞┃◟   "+b],["                 ","     ┃  "+r+"   ┛ ┗ "+b],["                 ","     ┃"],["                 "," ▔▔▔▔▔▔▔▔▔"],[""]]
	inter7c=[["Le mot secret était : ",r+underline+mot+normal+b,"."],[""],["                 ","     ┏━━━━━━┓"],["                 ","     ┃    "+r+"  ⬤  `"+b],["                 ","     ┃   "+r+" ╾━╋━╼ `"+b],["                 ","     ┃     "+r+"◞┃◟   `"+b],["                 ","     ┃  "+r+"   ┛ ┗ "+b],["                 ","     ┃"],["                 "," ▔▔▔▔▔▔▔▔▔"],[""]]
	inter7d=[["Le mot secret était : ",r+underline+mot+normal+b,"."],[""],["                 ","     ┏━━━━━━┓"],["                 ","     ┃    "+r+"  ⬤  `"+b],["                 ","     ┃   "+r+" ╾━╋━╼ `"+b],["                 ","     ┃     "+r+"◞┃◟   `"+b],["                 ","     ┃  "+r+"   ┛ ┗    `"+b],["                 ","     ┃"],["                 "," ▔▔▔▔▔▔▔▔▔"],[""]]
	inter7e=[["Le mot secret était : ",r+underline+mot+normal+b,"."],[""],["                 ","     ┏━━━━━━┓"],["                 ","     ┃    "+r+"  ⬤  `"+b],["                  ","    ┃   "+r+" ╾━╋━╼ `"+b],["                 ","     ┃     "+r+"◞┃◟   `"+b],["                 ","     ┃  "+r+"   ┛ ┗    "+b],["                 ","     ┃          "+r+"_▁▂▂▁_"+b],["                 "," ▔▔▔▔▔▔▔▔▔"],[""]]
	inter7f=[["Le mot secret était : ",r+underline+mot+normal+b,"."],[""],["                 ","     ┏━━━━━━┓"],["                 ","     ┃    "+r+"  ⬤  `"+b],["                 ","     ┃   "+r+" ╾━╋━╼ `"+b],["                 ","     ┃     "+r+"◞┃◟   `"+b],["                 ","     ┃  "+r+"   ┛ ┗    `"+b],["                 ","     ┃         "+r+"__▁▂▂▁__"+b],["                 "," ▔▔▔▔▔▔▔▔▔"],[""]]
	os.system("clear")
	affichage_matrice(inter7a)
	affichage_matrice(game_over)
	time.sleep(0.75)
	os.system("clear")
	affichage_matrice(inter7b)
	time.sleep(0.75)
	os.system("clear")
	affichage_matrice(inter7c)
	affichage_matrice(game_over)
	time.sleep(0.75)
	os.system("clear")
	affichage_matrice(inter7d)
	time.sleep(0.75)
	affichage_matrice(game_over)
	t=time.time()
	t+=10 #on ajoute 10 secondes à la variable 'time.time()' qui nous donne le temps
	while time.time()<t: #on initialise une boucle tant que qui tournera tant que la variable 't' (affecter precedement) est plus grande que la variable time.time() (qui est une variable qui bouge puisqu'elle nous donne l'heure en temps réél)
		os.system("clear")
		affichage_matrice(inter7e)
		affichage_matrice(game_over)
		time.sleep(0.5)
		os.system("clear")
		affichage_matrice(inter7f)
		time.sleep(0.5)
	return("")

def animation_gagne(mot:str):
	you_win=[["   ",c+bold+" _  _  __  _  _    _  _   __  _  _  ___    _    _  __  _  _    _ "+b+normal],["   ",c+bold+"( \/ )/  \( )( )  ( )( ) (  )( )( )(  _)  ( \/\/ )(  )( \( )  / \\"+b+normal],["   ",c+bold+"  \  /( () ))()(    )__(  /__\ \\\\//  ) _)   \    /  )(  )  (   \_/"+normal+b],["   ",c+bold+"(__/  \__/ \__/   (_)(_)(_)(_)(__) (___)    \/\/  (__)(_)\_)  (_)"+b+normal]]

	inter7a=[[""],
			 [""],
			 ["              ","     ┏━━━━━━┓"],
			 ["              ","     ┃    "+c+"  ⬤  "+b],
			 ["              ","     ┃   "+c+" ╾━╋━╼ "+b],
			 ["              ","     ┃     "+c+"◞┃◟"+b],
			 ["              ","     ┃  "+c+"   ┛ ┗ "+b],
			 ["              ","     ┃"],
			 [y+"▔▔▔▔▔▔▔▔▔"+b," ▔▔▔▔▔▔▔▔▔",y+" ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔"+b],
			 [""]]

	inter7b=[[""],[""],["              ","     ┏━━━━━━┓"],["              ","     ┃"],["              ","     ┃    "+c+"  ⬤  "+b],["              ","     ┃   "+c+" ╾━╋━╼ "+b],["              ","     ┃     "+c+"◞┃◟"+b],["              ","     ┃  "+c+"   ┛ ┗ "+b],[y+"▔▔▔▔▔▔▔▔▔▔▔▔▔▔"+b," ▔▔▔▔▔▔▔▔▔",y+" ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔"+b],[""]]

	inter7c=[[""],[""],["             ","     ┏━━━━━━┓"],["             ","     ┃"],["             ","     ┃    "+c+"     ⬤  "+b],["             ","     ┃   "+c+"    ╾━╋━╼ "+b],["             ","     ┃     "+c+"   ◞┃◟"+b],["             ","     ┃  "+c+"      ┛ ┗ "+b],[y+"▔▔▔▔▔▔▔▔▔▔▔▔▔"+b," ▔▔▔▔▔▔▔▔▔",y+" ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔"+b],[""]]

	inter7d=[[""],[""],["            ","     ┏━━━━━━┓"],["            ","     ┃"],["            ","     ┃    "+c+"       ⬤  "+b],["            ","     ┃   "+c+"      ╾━╋━╼ "+b],["            ","     ┃     "+c+"     ◞┃◟"+b],["            ","     ┃  "+c+"        ┛ ┗ "+b],[y+"▔▔▔▔▔▔▔▔▔▔▔▔"+b," ▔▔▔▔▔▔▔▔▔",y+" ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔"+b],[""]]
	inter7e=[[""],[""],["           ","     ┏━━━━━━┓"],["           ","     ┃"],["           ","     ┃    "+c+"         ⬤  "+b],["           ","     ┃   "+c+"        ╾━╋━╼ "+b],["           ","     ┃     "+c+"       ◞┃◟"+b],["           ","     ┃  "+c+"          ┛ ┗ "+b],[y+"▔▔▔▔▔▔▔▔▔▔▔"+b," ▔▔▔▔▔▔▔▔▔",y+" ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔"+b],[""]]
	inter7f=[[""],[""],["          ","     ┏━━━━━━┓"],["          ","     ┃"],["          ","     ┃    "+c+"           ⬤  "+b],["          ","     ┃   "+c+"          ╾━╋━╼ "+b],["          ","     ┃     "+c+"         ◞┃◟"+b],["          ","     ┃  "+c+"            ┛ ┗ "+b],[y+"▔▔▔▔▔▔▔▔▔▔"+b," ▔▔▔▔▔▔▔▔▔",y+" ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔"+b],[""]]

	inter7g=[[""],[""],["         ","     ┏━━━━━━┓"],["         ","     ┃"],["         ","     ┃    "+c+"             ⬤  "+b],["         ","     ┃   "+c+"            ╾━╋━╼ "+b],["         ","     ┃     "+c+"           ◞┃◟"+b],["         ","     ┃  "+c+"              ┛ ┗ "+b],[y+"▔▔▔▔▔▔▔▔▔"+b," ▔▔▔▔▔▔▔▔▔",y+" ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔"+b],[""]]

	inter7h=[[""],[""],["        ","     ┏━━━━━━┓"],["        ","     ┃"],["        ","     ┃    "+c+"               ⬤  "+b],["        ","     ┃   "+c+"              ╾━╋━╼ "+b],["        ","     ┃     "+c+"             ◞┃◟"+b],["        ","     ┃  "+c+"                ┛ ┗ "+b],[y+"▔▔▔▔▔▔▔▔"+b," ▔▔▔▔▔▔▔▔▔",y+" ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔"+b],[""]]

	inter7i=[[""],[""],["       ","     ┏━━━━━━┓"],["       ","     ┃"],["       ","     ┃    "+c+"                 ⬤  "+b],["       ","     ┃   "+c+"                ╾━╋━╼ "+b],["       ","     ┃     "+c+"               ◞┃◟"+b],["       ","     ┃  "+c+"                  ┛ ┗ "+b],[y+"▔▔▔▔▔▔▔"+b," ▔▔▔▔▔▔▔▔▔",y+" ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔"+b],[""]]

	inter7j=[[""],[""],["      ","     ┏━━━━━━┓"],["      ","     ┃"],["      ","     ┃    "+c+"                   ⬤  "+b],["      ","     ┃   "+c+"                  ╾━╋━╼ "+b],["      ","     ┃     "+c+"                 ◞┃◟"+b],["      ","     ┃  "+c+"                    ┛ ┗ "+b],[y+"▔▔▔▔▔▔"+b," ▔▔▔▔▔▔▔▔▔",y+" ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔"+b],[""]]

	os.system("clear")
	affichage_matrice(inter7a)
	affichage_matrice(you_win)
	time.sleep(0.65)
	os.system("clear")
	affichage_matrice(inter7b)
	time.sleep(0.65)

	os.system("clear")
	affichage_matrice(inter7c)
	affichage_matrice(you_win)
	time.sleep(0.65)
	os.system("clear")
	affichage_matrice(inter7d)
	time.sleep(0.65)

	os.system("clear")
	affichage_matrice(inter7e)
	affichage_matrice(you_win)
	time.sleep(0.65)
	os.system("clear")
	affichage_matrice(inter7f)
	time.sleep(0.65)

	os.system("clear")
	affichage_matrice(inter7g)
	affichage_matrice(you_win)
	time.sleep(0.65)
	os.system("clear")
	affichage_matrice(inter7h)
	time.sleep(0.65)

	os.system("clear")
	affichage_matrice(inter7i)
	affichage_matrice(you_win)
	time.sleep(0.65)
	os.system("clear")
	affichage_matrice(inter7j)

	return("")

def quelle_interface(compteur:int,mot:str,huit:int,liste_des_testees:list,nom_theme:str):
	""" cette fonction 'quelle_interface' permet de trouver ou en est l'utilisateur et donc quelle interface il doit utiliser """
	tenta=huit-compteur #on initialise une variable 'tenta' qui compte le nombre de tentatives restantes à l'utilisateur avant de perdre
	tentas=str(tenta)
	#les variables pour l'interface graphique
	inter0=[[" ",underline+"THEME:"+normal," ",nom_theme.upper()],["",""],["       ",mot],[""],[""],["           ",tentas," tentatives restantes!"],["              ",affichage_lettre_testees(liste_des_testees)],[""]]
	inter1=[[" ",underline+"THEME:"+normal," ",nom_theme.upper()],["",""],[" ","     "],[" ","     ","                 ",mot],[" ","     "],[" ","     "],[" ","     ","          ",tentas," tentatives restantes!"],["                    ",affichage_lettre_testees(liste_des_testees)],[" ",p+"▔▔▔▔▔▔▔▔▔"+b]]
	inter2=[[" ",underline+"THEME :"+normal," ",nom_theme.upper()],["",""],[p+" ","    ╻"+b],[p+" ","    ┃"+b,"                 ",mot],[p+" ","    ┃"+b],[p+" ","    ┃"+b],[p+" ","    ┃"+b,"          ",tentas," tentatives restantes!"],[p+" ","    ┃"+b,"              ",affichage_lettre_testees(liste_des_testees)],[" ","▔▔▔▔▔▔▔▔▔"]]
	inter3=[[" ",underline+"THEME :"+normal," ",nom_theme.upper()],["",""],[p+" ","    ┏━━━━━━┓"+b],[" ","    ┃","                 ",mot],[" ","    ┃"],[" ","    ┃"],[" ","    ┃","          ",tentas," tentatives restantes!"],[" ","    ┃","              ",affichage_lettre_testees(liste_des_testees)],[" ","▔▔▔▔▔▔▔▔▔"]]
	inter4=[[" ",underline+"THEME :"+normal," ",nom_theme.upper()],["",""],[" ","    ┏━━━━━━┓"],["     ┃ "+p+"     ⬤"+b,"         ",mot],[" ","    ┃"],[" ","    ┃"],[" ","    ┃","            ",tentas," tentatives restantes!"],[" ","    ┃","              ",affichage_lettre_testees(liste_des_testees)],[" ","▔▔▔▔▔▔▔▔▔"]]
	inter5=[[" ",underline+"THEME :"+normal," ",nom_theme.upper()],["",""],[" ","    ┏━━━━━━┓"],[" ","    ┃      ⬤","          ",mot],["  ","   ┃"+p+"      ┃"+b],[" ","    ┃ "+p+"     ┃"+b],[" ","    ┃","            ",tentas," tentatives restantes!"],[" ","    ┃","              ",affichage_lettre_testees(liste_des_testees)],[" ","▔▔▔▔▔▔▔▔▔"]]
	inter6=[[" ",underline+"THEME :"+normal," ",nom_theme.upper()],["",""],[" ","    ┏━━━━━━┓"],[" ","    ┃      ⬤","        ",mot],[" ","    ┃"+p+"    ╾━"+b+"╋"+p+"━╼"+b],[" ","    ┃      ┃"],[" ","    ┃","            ",tentas," tentative restante!"],[" ","    ┃","              ",affichage_lettre_testees(liste_des_testees)],[" ","▔▔▔▔▔▔▔▔▔"]]

	if compteur<1:
		return(inter0)
	elif compteur==1:
		return(inter1)
	elif compteur==2:
		return(inter2)
	elif compteur==3:
		return(inter3)
	elif compteur==4:
		return(inter4)
	elif compteur==5:
		return(inter5)
	elif compteur==6:
		return(inter6)

def deja_essaye(l:list,lettre:str):
	""" cette fonction ('deja_essaye') permet de tester si la lettre que l'utilisateur veut essayer ('lettre_a_tester') appartient ou pas à la liste 'lettres_liste_testees' (c'est la liste des lettres que l'utilisateur a déjà entrées) """
	if lettre not in l: #on verifie si la 'lettre_a_tester' n'appartient pas 'liste_lettres_testees'
		l.append(lettre) #du coup, on ajoute cette 'lettre_a_tester' dans le liste
		return(True) #on retourne le bouléen True si le test est verifie (il va donc nous permettre de poursuivre)
	else:
		return(False) #on retourne le bouléen False si le test n'est pas verifié (ce qui va nous arreter)

def mot_devine(liste_mot_secret:list,lettre_a_tester:str,liste_devinee:list):
	""" cette fonction ('mot_devine') est appelée SI le resultat de la fonction 'deja_essaye' est TRUE. 
elle sert à chercher dans la 'liste_mot_secret' si il existe ou non la 'lettre_a_tester' que l'utilisateur a entrée et il regarde si elle existe dans le mot, si c'est le cas alors il va ajouter à la liste 'liste_devinée' les lettres qui correspondent à 'lettre_a_tester' c'est ce que l'utilisateur aura sur son ecran"""
	if lettre_a_tester in liste_mot_secret: #on verifie si la 'lettre_a_tester appartient à la 'liste_mot_secret' 
		for i in range(len(liste_mot_secret)): #on parcout la 'liste_mot_secret' 
			if lettre_a_tester==liste_mot_secret[i]: #on verifie à chaque index si la 'lettre_a_tester' est dans le mot 
				liste_devinee[i]=liste_mot_secret[i] #on remplace les lettres du mot que l'utilisateur a trouve dans la 'liste_devinee'
		return(liste_devinee) #en resultat de la fonction'mot_devine' nous allons retourner la 'liste_devinee' (c'est la liste que l'utilisateur a déjà trouvée)
	else: #si la 'lettre_a_tester n'appartient pas à la 'liste_mot_secret' alors ça ne sert a rien de parcourir le mot pour tester si la lettre est bien presente comme elle n'y est pas
		return(False) #on retourne le bouléen False si le test n'est pas verifié (ce qui va nous arreter)

def verite(gagne:bool,compteur:int,compteur_perdu:int,mot:str):
	""" cette fonction 'verite' verifie si le joueur a gagné ou perdu, elle se lance lorsque le programme est sorti de la boucle while (lorsque le joueur a soit gagné soit perdu) """
	if gagne==True: #cette condition verifie si le joueur a gagne
		print(animation_gagne(mot))
	elif compteur==compteur_perdu: #cette condition verifie si le joueur a perdu
		print(animation_perdu(mot))
	
