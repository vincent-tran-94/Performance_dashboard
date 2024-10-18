import pandas as pd
from sqlalchemy import create_engine

# Chemin vers votre fichier de base de données
def create_table(path):

    # Créer un moteur SQLAlchemy
    engine = create_engine(f'sqlite:///{path}')

    # Charger les données des fichiers CSV
    rowers_df = pd.read_csv('data/rowers.csv')
    speed_length_df = pd.read_csv('data/speed_length.csv')

    # Vérifier et renommer la colonne 'Unnamed: 0' en 'id' si elle existe dans les DataFrames
    if 'Unnamed: 0' in rowers_df.columns:
        rowers_df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

    if 'Unnamed: 0' in speed_length_df.columns:
        speed_length_df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

    # Enregistrer chaque DataFrame dans une table distincte
    rowers_df.to_sql('infos_performance', con=engine, if_exists='replace', index=False)
    speed_length_df.to_sql('speed_length', con=engine, if_exists='replace', index=False)

    print("Les données ont été insérées avec succès dans deux tables : 'infos_performance' et 'speed_length'.")
