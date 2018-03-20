#!/usr/bin/python3
#-*-coding:utf-8-*-
# coding: utf8

from random import randint
import corps_pendu as cp

global underline, normal
underline="\033[4m"
normal="\x1b[0m"

#------------------------------------------------------------------------------------------------------

def choix_theme():
	""" cette fonction 'choix_theme' se lance en debut de partie et propose au joueur plusieurs themes de jeu. c'est a lui de choisir qu'elle genre de mot il souhaite essayer de trouver """
	all_themes={"Animaux":["Baleine","Beluga","Phoque","Cachalot","Dauphin","Abeille","Alpaga","Ane","Ara","Antilope","Autruche","Babouin","Bison","Boeuf","Bouquetin","Bouledogue","Brochet","Buffle","Cacatoes","Cameleon","Canard","Capucin","Capybara","Caracal","Castor","Chacal","Chameau","Chat","Chevre","Chien","Chimpanze","Chouette","Cigale","Cigogne","Coati","Corbeau","Coq","Corneille","Cormoran","Dendrolague","Dindon","Dingo","Dromadaire","Lamantin","Orque","Otarie","Phoque","Rorqual","Morse","Marsouin","Morse","Narval","Caribou","Cerf","Chevreuil","Elan","Daim","Ornithorynque"],
"Metiers":["Boulanger","Boucher","Chevalier","Peripateticienne","Acupuncteur","Hotesse","Ingenieur","Couvreur","Peintre","Programmateur","Comportementaliste","Comptable","Banquier","Avocat","Juge","Livreur","Mannequin","Douanier","Pompier","Cascadeur","Acteur","Ecrivain","Webmaster","Eboueur","Economiste","Elagueur","Electricien","Agriculteur","Serveur","Serrurier","Sociologue","Sondeur","Anesthesiste","Standardiste","Statisticien","Programmeur"],
"Fruits":["Fraise","Framboise","Melon","Pasteque","Pomme","Mirabelle","Ananas","Papaye","Banane","Orange","Clementine","Pamplemousse","Poire","Grenade","Avocat","Figue","Datte","Groseille","Myrtille","Cassis","Prune","Abricot","Peche","Noix","Amande","Pistache","Raisin","Mure","Kiwi","Goyave"],"Pokemon":["Bulbizarre","Herbizarre","Florizarre","Salameche","Reptincel","Dracaufeu","Carapuce","Carabaffe","Tortank","Chenipan","Chrysacier","Papilusion","Aspicot","Coconfort","Dardargnan","Roucool","Roucoups","Roucarnage","Rattata","Rattatac","Piafabec","Rapasdepic","Abo","Arbok","Pikachu","Raichu","Sabelette","Sablaireau","Nidoran","Nidorina","Nidoqueen","Nidorino","Nidoking","Melofee","Melodelfe","Goupix","Feunard","Rondoudou","Grodoudou","Nosferapti","Nosferalto","Mystherbe","Ortide","Rafflesia","Paras","Parasect","Mimitoss","Aeromite","Taupiqueur","Triopikeur","Miaouss","Persian","Psykokwak","Akwakwak","Ferosinge","Colossinge","Caninos","Arcanin","Ptitard","Tetarte","Tartard","Abra","Kadabra","Alakazam","Machoc","Machopeur","Mackogneur","Chetiflor","Boustiflor","Empiflor","Tentacool","Tentacruel","Racaillou","Gravalanch","Grolem","Ponyta","Galopa","Ramoloss","Flagadoss","Magneti","Magneton","Canarticho","Doduo","Dodrio","Otaria","Lamantine","Tadmorv","Grotadmorv","Kokiyas","Crustabri","Fantominus","Spectrum","Ectoplasma","Onix","Soporifik","Hypnomade","Krabby","Krabboss","Voltorbe","Electrode","Noeunoeuf","Noadkoko","Osselait","Ossatueur","Kicklee","Tygnon","Excelangue","Smogo","Smogogo","Rhinocorne","Rhinoferos","Leveinard","Saquedeneu","Kangourex","Hypotrempe","Hypocean","Poissirene","Poissoroy","Stari","Staross","Mr Mime","Insecateur","Lippoutou","Elektek","Magmar","Scarabrute","Tauros","Magicarpe","Leviator","Lokhlass","Metamorph","Evoli","Aquali","Voltali","Pyroli","Porygon","Amonita","Amonistar","Kabuto","Kabutops","Ptera","Ronflex","Artikodin","Elector","Sulfura","Minidraco","Draco","Dracolosse","Mewtwo","Mew"],"Colin":["TeteDeProute"]}
	#on initialise un dictionnaire 'theme'. elle va contenir tous les mots que le pendu va pouvoir choisir (aléatoirement) pour les faire deviner au joueur (le mot qui sera choisi sera stocké dans 'mot_secret'). les clefs du dictionnaire sont tous les themes proposé à l'utilisateur
	noms_themes=cp.list_keys_up(cp.de_mutabilisation(list(all_themes)))

	print("Avant de commencer, il vous faut choisir un thème : ")
	print()
	for i in noms_themes:
		print("- ",i)
	print()
	print("Entrez le nom du theme choisi ? ")
	t=input()
	themes=t[0].upper() #la premiere lettre du mot 't' est mise en majuscule
	for i in range(1,len(t)): #nous mettons le theme transformons les caracteres du 't' entré par l'utilisateur pour pouvoir tester si il appartient bien a notre liste 'mots_theme' (qui contient tous les noms des themes disponibles)
		themes+=t[i].lower() #toutes les lettres après la premiere sont mises en minuscules

	for i in range(0,len(noms_themes)): #nous fesons une boucle FOR qui va parcourir toutes le liste 'noms_themes' 
		if themes==noms_themes[i]: #on test SI le theme entré par le joueur existe bel et bien dans la liste 'noms_themes'
			for k in all_themes[themes]: #nous savons que les indexs des listes 'noms_themes' et 'mots_theme' sont concordants alors le theme i de 'noms_themes' trouvera ses mots dans la ligne i de 'mots_theme' c'est pour ça que nous parcourons la liste mots_theme[i]
				mot=all_themes[themes][randint(0,len(all_themes[themes])-1)] #nous sommes à present dans la ligne choisit par le joueur et nous allons choisir aléatoirement un des index de cette ligne puis nous allons donner sa valeur à la variable 'mot'
				return([mot,themes]) #en resultat de la fonction 'choix_theme' si le mot 't' entré par l'utilisateur est bien dans la liste 'noms_themes' alors nous retournons le mot
	
	print(underline+"ERREUR:"+normal+" le theme",themes,"n'existe pas.") #si lorsque la boucle FOR n'a pas trouvé dans sa liste le 'themes' correspondant au 'noms_themes[i]', alors c'est que le theme recherché par l'utilisateur n'existe pas il faut donc le printer une ERREUR
	return(False) #si le theme n'existe pas nous retournons un bouléen qui vaut 'False' pour que le programme principal demande à nouveau au joueur de choisir son thème



""" CREER DIFFERENTES DIFFICULTEES AVEC UNE CATEGORIE 'TOUS' (QUI REGROUPE TOUS LES THEMES!) """

