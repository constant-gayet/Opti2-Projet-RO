# Opti2-Projet-RO

2022 Optimization project


Pour lancer la compilation du projet, il suffit de run le fichier main.py.   
Cependant, **il faut modifier au préalable la ligne l.129 du fichier main.py** en remplacant la fonction **main_X** existante avec celle souhaitée (**main_plnecp** execute le premier PL, **main_plnecpm** le second et **main_heuristiques** execute l'heuristique de coloration (la seule en état de fonctionnement)) 

Pour effectuer les tests sur des graphes de 20 à 500 noeuds:  
>python3 main.py Instances/Instances/Spd_Inst_Rid_Final2


Pour effectuer les tests sur des graphes de 500 à 1000 noeuds:  
>python3 main.py Instances/Instances/Spd_Inst_Rid_Final2_500-1000


Les fichiers résultats sont stockés dans le dossier 
>Results/*type d'algorithme testé*
