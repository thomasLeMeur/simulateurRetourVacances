Ce programme permet de simuler la pose d'un arrêt de travail (RTT, congés, etc.) et savoir à quelle date le travail devra reprendre.
Ce simulateur ne décomptera pas de vos jours d'arrêt les week-ends, jours fériés et ponts (voir la configuration).

La configuration se trouve dans le fichier conf.json.
Elle se décompose en 4 parties:
- date_arret_travail: La date à laquelle l'arrêt de travail débutera (le format attendy est YYYY-MM-DD)
- nb_jours_arret: Le nombre de jours d'arrêt de travail à poser
- ponts_inclus: Indique si le nombre de jours d'arrêt inclus ou non les ponts à poser (true/false)
- zone: Indique la zone géographique de la France où vous travaillez, pour respecter les jours fériés locaux (pour une liste des valeurs possibles, lancer le programme avec une valeur absurde ou se référer à https://pypi.org/project/jours-feries-france/)
