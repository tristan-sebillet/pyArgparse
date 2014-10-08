#!/usr/bin/python3



''' Fonction de vérification des sous arguments '''
def checkSousArgs(unArgument, nomDeLArgument, indice):
    logging.info("verifie argument 2")
    try:
        '''unArgument[1]=le pourcentage '''
        unArgument[1] = int(unArgument[1])
        if unArgument[1]<0:
            unArgument[1] = abs(unArgument[1])
            logging.warning('La quantité saisie doit etre positive')
            print(str(unArgument[1]))
            logging.info('Nombre négatif transformé en positif: ' + str(unArgument[1]))
            return unArgument[1]
        elif unArgument[1]>100:
            unArgument[1] = 0
            logging.warning('La quantité saisie est supérieur à 100')
            print(str(unArgument[1]))
            logging.info('Nombre supérieur à 100 transformé en : ' + str(unArgument[1]))
            return unArgument[1]

        global args
        setattr(args, nomDeLArgument[indice], [unArgument[0], unArgument[1]])

    except ValueError:
        print ("Impossible de convertir \""  + nomDeLArgument + + unArgument[1] + "\" en nombre entier !")
        logging.error(' --' + nomDeLArgument + ', impossible de convertir "' + unArgument[1] + '" en nombre entier !')
        logging.debug(' *****************************************')
        exit(1)

import argparse
import logging

logging.basicConfig(filename='le_fichier_de.log',level=logging.DEBUG)

'''creation d'un objet'''
parser = argparse.ArgumentParser()
logging.info("objet créer")
'''ajout d'arguments'''
parser.add_argument("nom_playlist", help="Veuillez saisir le nom de votre playlist")

parser.add_argument("temps",type=int,help="Veuillez saisir la duree de votre playlist")

parser.add_argument("--titre",nargs=2,help="Saisi d'un titre de morceau inclus dans la playlist et de son pourcentage")

parser.add_argument("--genre",nargs=2,help="Saisi d'un genre a inclure dans la playlist et de son pourcentage", action="append")

parser.add_argument("--sousgenre",nargs=2,help="Saisi d'un sous-genre a inclure dans la playlist et de son pourcentage")

parser.add_argument("--artiste",nargs=2,help="Saisi d'un artiste inclus dans la playlist et de son pourcentage")

parser.add_argument("--album",nargs=2,help="Saisi d'un album inclus dans la playlist et de son pourcentage")

parser.add_argument("--format", choices=['m3u','xspf'])

'''capturer les arguments'''
args = parser.parse_args()

''' Boucle pour tester l'ensemble des paramètres optionnels, et réalise le test uniquement si l'argument est renseigné '''


'''affichage des arguments saisis'''
#print(args.nom_playlist+" a pour duree: "+str(args.temps)+" minutes.")

'''test si les arguments son saisis et si oui affichage de ceux-ci'''
# if args.titre:
#     checkSousArgs(args.titre)
#     print("titre choisi:"+(args.titre))
#
# #if args.genre:
#
# #   print("Vous avez choisi:"+(args.genre[1])+"% du genre "+(args.genre[0]) )
#
# if args.sousgenre:
#     checkSousArgs(args.sousgenre)
#     print("vous avez choisi:"+(args.sousgenre[1])+"% du sousgenre "+(args.sousgenre[0]) )
#
# if args.artiste:
#     checkSousArgs(args.artiste)
#     print("vous avez choisi:"+(args.artiste[1])+"% de l'artiste "+(args.artiste[0]) )
#
# if args.album :
#     checkSousArgs(args.album)
#     print("vous avez choisi:"+(args.album[1])+"% de l'album "+(args.album[0]) )
#
# if args.format:
#     print("format choisi:"+(args.format) )

# Gestion de l'argument genre et ses sous-arguments

# Variable qui contient la somme des pourcentages
somme = 0
# Compteur
i = 0
# Pour chaque argument, si ils sont renseignées, on les affiche dans le fichier de logs
for PremierArg in ['titre','genre','sousgenre','artiste','album']:
    # Si l'argument est renseigné
    if getattr(args, PremierArg) is not None:
        # On écrit la valeur de ses ss-arg dans le fichier de logs
        logging.info(' Argument --' + PremierArg + ' :\t' + getattr(args, PremierArg)[0][0] + ' ; ' + getattr(args, PremierArg)[0][1])
        # Puis on vérifie que le 2eme ss-arg de l'argument est correct et on le remplace par la nouvelle valeure créée lors de la vérification
        # On parcourt la liste d'argument ags.genre (dans le cas où on a renseigné plusieurs fois l'argument --genre)
        print("taille du tableau : " + str(len(args.genre)))
        while i < len(args.genre):
            logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
            print ('coucou bob : ' + str(args.genre[i][1]))
            checkSousArgs(args.genre[i], 'genre', i)
            print("bobinou : " + str(args.genre[i][1]))
            somme = somme + args.genre[i][1]
            i = i + 1

i = 0
if somme > 100:
    while i < len(args.genre):
        args.genre[i][1] = int(args.genre[i][1])*100/somme
        arrondiPro = round(args.genre[i][1])
        print(arrondiPro)
        i = i +1




# Ecriture d'une ligne d'étoiles dans le fichier de log, pour séparrer les infos en fonction de chaque exécution
logging.debug(' *****************************************')
logging.shutdown()
# la commande exit(0) permet de quitter le programme en indiquant qu'il n'y a pas eu d'erreurs
exit(0)
# la commande exit(0) permet de quitter le programme sans omettre d'erreur, alors que exit(1) lève une erreur







