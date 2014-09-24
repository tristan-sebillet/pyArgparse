import argparse
#creation d'un objet
parser = argparse.ArgumentParser()
#ajout d'arguments
parser.add_argument("nom_playlist", help="Veuillez saisir le nom de votre playlist")

parser.add_argument("temps",type=int,help="Veuillez saisir la duree de votre playlist")

parser.add_argument("--titre",help="Saisi d'un titre de morceau inclus dans la playlist")

parser.add_argument("--genre",nargs=2,help="Saisi d'un genre a inclure dans la playlist")

parser.add_argument("--sousgenre",help="Saisi d'un sous-genre a inclure dans la playlist")

parser.add_argument("--artiste",help="Saisi d'un artiste inclus dans la playlist")

parser.add_argument("--album",help="Saisi d'un album inclus dans la playlist")

parser.add_argument("--format", choices=['m3u','xspf'])

#capturer les arguments
args = parser.parse_args()

#affichage des arguments saisis
print(args.nom_playlist+" a pour duree: ")
print((args.temps))

#test si les arguments son saisis et si oui afichage de ceux-ci
if args.titre:
    print("titre choisi:"+(args.titre))

if args.genre:
    print("genre choisi:"+(args.genre[0])+" "+(args.genre[1])+"%" )
if args.sousgenre:
    print("sousgenre choisi:"+(args.sousgenre) )
if args.artiste:
    print("artiste choisi:"+(args.artiste) )
if args.album:
    print("album choisi:"+(args.album) )
if args.format:
    print("format choisi:"+(args.format) )