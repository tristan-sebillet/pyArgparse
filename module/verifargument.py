import logging


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


