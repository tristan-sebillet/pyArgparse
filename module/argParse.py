import logging
import argparse

def fonctionparser():

    '''creation d'un objet'''
    parser = argparse.ArgumentParser()
    logging.info("objet créer")
    '''ajout d'arguments'''
    parser.add_argument("nom_playlist", help="Veuillez saisir le nom de votre playlist")

    parser.add_argument("temps",type=int,help="Veuillez saisir la duree de votre playlist")

    parser.add_argument("--titre",nargs=2,help="Saisi d'un titre de morceau inclus dans la playlist et de son pourcentage", action="append")

    parser.add_argument("--genre",nargs=2,help="Saisi d'un genre a inclure dans la playlist et de son pourcentage", action="append")

    parser.add_argument("--sousgenre",nargs=2,help="Saisi d'un sous-genre a inclure dans la playlist et de son pourcentage", action="append")

    parser.add_argument("--artiste",nargs=2,help="Saisi d'un artiste inclus dans la playlist et de son pourcentage", action="append")

    parser.add_argument("--album",nargs=2,help="Saisi d'un album inclus dans la playlist et de son pourcentage", action="append")

    parser.add_argument("--format", choices=['m3u','xspf'])

    '''capturer les arguments'''
    args = parser.parse_args()
    return args