'''

Ce script crée les fichiers nescessaires pour le graphe des artistes et des genres avec la coloration par attributs muscicaux

'''

import pandas as pd


def convert_to_list(list_string):
    """convertit la string des artistes sorti du dataframe en vrai liste python"""
    list_string = list_string.strip("[]").split(",")
    for i, string in enumerate(list_string):
        list_string[i] = string.strip(" ")
    return list_string

def calculate_mean_attributes(artist_id, features_df):
    """pour un id d'artiste passé en param, retourne les moyennes pour chaque attribut muscial sous forme de dict"""
    filtered_df = features_df[features_df["artists_id"].apply(lambda x: artist_id in convert_to_list(x))]
    liste_attributes = ['danceability', 'energy',
                        'loudness', 'speechiness', 'acousticness',
                        'instrumentalness', 'liveness', 'valence', 'tempo']
    dict_means = {}
    for attribut in liste_attributes :
        dict_means[f"mean_{attribut}"] = filtered_df[attribut].mean()
    return dict_means



def create_noeuds(save_path):
    features_df = pd.read_csv("./data/all_features.csv")
    noeuds_artiste_genre = pd.read_csv("./data/Artist_gephi/graphe_par_continent/neouds_continent.csv")

    rows = []

    for _, row in noeuds_artiste_genre.iterrows():
        artist_means = calculate_mean_attributes(row['id'], features_df)

        new_row = row.to_dict()
        new_row.update(artist_means)

        rows.append(new_row)

    noeuds_avec_attributs = pd.DataFrame(rows)

    noeuds_avec_attributs.to_csv(save_path,index=False)

def main():
    create_noeuds("./data/Artist_gephi/graph_attributs/noeuds_artiste_attributs.csv")

if __name__ == "__main__":
    main()