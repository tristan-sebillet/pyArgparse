import argparse
'''creation d'un objet'''
parser = argparse.ArgumentParser()
'''ajout d'arguments'''
parser.add_argument("nom_playlist", help="Veuillez saisir le nom de votre playlist")

parser.add_argument("temps",type=int,help="Veuillez saisir la duree de votre playlist")

parser.add_argument("--titre",help="Saisi d'un titre de morceau inclus dans la playlist")

parser.add_argument("--genre",nargs=2,help="Saisi d'un genre a inclure dans la playlist")

parser.add_argument("--sousgenre",nargs=2,help="Saisi d'un sous-genre a inclure dans la playlist")

parser.add_argument("--artiste",nargs=2,help="Saisi d'un artiste inclus dans la playlist")

parser.add_argument("--album",nargs=2,help="Saisi d'un album inclus dans la playlist")

parser.add_argument("--format", choices=['m3u','xspf'])

'''capturer les arguments'''
args = parser.parse_args()

''' Fonction de vérification des sous arguments '''
def checkSousArgs(arg):
    try:
        nb = int(arg[1])
        if (checkIntNatural(nb) == False):
            print ("La quantité doit être positive ! (" + arg[1] + ")")
            exit(1)
        return 0
    except ValueError:
        print ("Impossible de convertir \"" + arg[1] + "\" en nombre entier !")
        exit(1)

''' Vérifie qu'un nombre est un entier naturel '''
def checkIntNatural(nb):
    if nb > 0:
        return True
checkSousArgs(args.artiste)
checkSousArgs(args.album)
checkSousArgs(args.sousgenre)
checkSousArgs(args.genre)

'''affichage des arguments saisis'''
print(args.nom_playlist+" a pour duree: "+str(args.temps)+" minutes.")

'''test si les arguments son saisis et si oui affichage de ceux-ci'''
if args.titre:
    print("titre choisi:"+(args.titre))

if args.genre:
    print("Vous avez choisi:"+(args.genre[1])+"% du genre "+(args.genre[0]) )


if args.sousgenre:
    print("vous avez choisi:"+(args.sousgenre[1])+"% du sousgenre "+(args.sousgenre[0]) )


if args.artiste:
    print("vous avez choisi:"+(args.artiste[1])+"% de l'artiste "+(args.artiste[0]) )


if args.album :
    print("vous avez choisi:"+(args.album[1])+"% de l'album "+(args.album[0]) )


if args.format:
    print("format choisi:"+(args.format) )









