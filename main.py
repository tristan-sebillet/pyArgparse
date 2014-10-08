#!/usr/bin/python3

import module.pourcentage
import module.verifargument
from module.argParse import fonctionparser
from module.verifargument import checkSousArgs
''' Fonction de vérification des sous arguments '''


import argparse
import logging

logging.basicConfig(filename='le_fichier_de.log',level=logging.DEBUG)
args=fonctionparser


# Gestion de l'argument genre et ses sous-arguments
# Variable qui contient la somme des pourcentages
somme = 0
# Compteur
i = 0
# Pour chaque argument, si ils sont renseignées, on les affiche dans le fichier de logs
for PremierArg in [args]:
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
            somme = somme + args.genre[i][1]
            i = i + 1
            print("somme: "+ str(somme))

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
