def plusPetitEntierNaturel(valeur):
    n = q = 0 # au début on définit n et q à 0
    # tant que la probabilité est inférieure à la valeur on continue d'ajouter une boule
    while q < valeur: 
       n += 1 # on ajoute une boule
       q = 1 - (4/(n+4))**4 # on calcule la probabilité q_n
    return n # on retourne le résultat
