import pandas as pd

# Lire les fichiers
df1 = pd.read_csv('FULL_XRM_GRV.csv')  # ou pd.read_excel('fichier1.xlsx')
df2 = pd.read_csv('FULL_GTS_GRV.csv')  # ou pd.read_excel('fichier2.xlsx')

# Jointure (plusieurs types possibles)
# Jointure interne (seulement les lignes avec clés communes)
resultat = pd.merge(df1, df2, on='Co_codeexterne')

# Jointure gauche (toutes les lignes du fichier de gauche)
resultat = pd.merge(df1, df2, on='Co_codeexterne', how='left')

# Sauvegarder le résultat
resultat.to_csv('resultat_jointure.csv', index=False)
