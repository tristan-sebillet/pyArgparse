#!/usr/bin/python3

''' Fonction de vérification des sous arguments '''
def checkSousArgs2(unArgument, nomDeLArgument):
    logging.info("verifie argument 2")
    try:
        unArgument[1] = int(unArgument[1])
        if unArgument[1]<0:
            unArgument[1] = abs(unArgument[1])
            logging.warning('La quantité saisie doit etre positive')
            print(str(unArgument[1]))
            logging.info('Nombre négatif transformé en positif: ' + str(unArgument[1]))
            return unArgument[1]
        elif unArgument[1]>100:
            unArgument[1] = None
            logging.warning('La quantité saisie est supérieur à 100')
            print(unArgument[1])
            logging.info('Nombre supérieur à 100 transformé en : ' + str(unArgument[1]))
            return unArgument[1]
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

parser.add_argument("--genre",nargs=2,help="Saisi d'un genre a inclure dans la playlist et de son pourcentage")

parser.add_argument("--sousgenre",nargs=2,help="Saisi d'un sous-genre a inclure dans la playlist et de son pourcentage")

parser.add_argument("--artiste",nargs=2,help="Saisi d'un artiste inclus dans la playlist et de son pourcentage")

parser.add_argument("--album",nargs=2,help="Saisi d'un album inclus dans la playlist et de son pourcentage")

parser.add_argument("--format", choices=['m3u','xspf'])

'''capturer les arguments'''
args = parser.parse_args()

'''affichage des arguments saisis'''
#print(args.nom_playlist+" a pour duree: "+str(args.temps)+" minutes.")

'''test si les arguments son saisis et si oui affichage de ceux-ci'''
#if args.titre:
#    checkSousArgs2(args.titre)
#    print("titre choisi:"+(args.titre))

#if args.genre:
#    checkSousArgs2(args.genre)
#    print("Vous avez choisi:"+(args.genre[1])+"% du genre "+(args.nb) )

#if args.sousgenre:
#    checkSousArgs2(args.sousgenre)
#    print("vous avez choisi:"+(args.sousgenre[1])+"% du sousgenre "+(args.sousgenre[0]) )

#if args.artiste:
#    checkSousArgs2(args.artiste)
#    print("vous avez choisi:"+(args.artiste[1])+"% de l'artiste "+(args.artiste[0]) )

#if args.album :
#    checkSousArgs2(args.album)
#    print("vous avez choisi:"+(args.album[1])+"% de l'album "+(args.album[0]) )

#if args.format:
#    print("format choisi:"+(args.format) )
#''' Boucle pour tester l'ensemble des paramètres optionnels, et réalise le test uniquement si l'argument est renseigné '''
# for ARG in ['titre','genre','sousgenre','artiste','album']:
#     if getattr(args, ARG) is not None:
#         checkSousArgs(getattr(args, ARG), ARG)

# Gestion de l'argument genre et ses sous-arguments
# Pour chaque argument, si ils sont renseignées, on les affiche dans le fichier de logs
for PremierArg in ['titre','genre','sousgenre','artiste','album']:
    # Si l'argument est renseigné
    if getattr(args, PremierArg) is not None:
        # On écrit la valeur de ses ss-arg dans le fichier de logs
        logging.info(' Argument --' + PremierArg + ' :\t' + getattr(args, PremierArg)[0] + ' ; ' + getattr(args, PremierArg)[1])
        # Puis on vérifie que le 2eme ss-arg de l'argument est correct et on le remplace par la nouvelle valeure créée lors de la vérification
        checkSousArgs2(getattr(args, PremierArg), PremierArg)
# Ecriture d'une ligne d'étoiles dans le fichier de log, pour séparrer les infos en fonction de chaque exécution
logging.debug(' *****************************************')
logging.shutdown()
# la commande exit(0) permet de quitter le programme en indiquant qu'il n'y a pas eu d'erreurs
exit(0)
# la commande exit(0) permet de quitter le programme sans omettre d'erreur, alors que exit(1) lève une erreur







