'''
Ce script crée les fichiers nescessaires pour faire le graphe des artistes et des genres avec la coloration par pays

'''

import pandas as pd


def pays_principale(artist_id, artists_df):
    """trouve le pays pour lequel l'artiste est dans le top50 le plus de fois et le retourne"""
    df_pays_artist = artists_df[artists_df["artists_info"] == artist_id]["country"]
    most_frequent = df_pays_artist.mode()[0]
    return (most_frequent)

def continent_principale(artist_id, artists_df):
    """trouve le continent pour lequel l'arstiste est dans le top50 le plus de fois"""
    continents = {
        "Africa": ['Egypt', 'Morocco', 'South Africa'],
        "Asia": ['India', 'Indonesia', 'Israel', 'Japan', 'Kazakhstan', 'Malaysia',
                 'Pakistan', 'Philippines', 'Saudi Arabia', 'Singapore', 'Taiwan',
                 'Thailand', 'Turkey', 'Vietnam'],
        "Europe": ['Andorra', 'Austria', 'Belarus', 'Belgium', 'Bulgaria', 'Czech Republic',
                   'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece',
                   'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania',
                   'Luxembourg', 'Netherlands', 'Norway', 'Poland', 'Romania', 'Slovakia',
                   'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom'],
        "North America": ['Canada', 'United States', 'Mexico'],
        "Central America": ['Costa Rica', 'Dominica', 'Dominican Republic', 'El Salvador',
                            'Guatemala', 'Honduras', 'Nicaragua', 'Panama'],
        "South America": ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador',
                          'Paraguay', 'Peru', 'Uruguay', 'Venezuela'],
        "Oceania": ['Australia', 'New Zealand']
    }
    pays_princ = pays_principale(artist_id, artists_df)
    for continent, countries in continents.items():
        if pays_princ in countries:
            return continent

def create_table_noeuds():
    """génère la table des neouds pour le fichier gephi"""
    df_artists = pd.read_csv("data/artists_info/artists.csv")
    df_noeuds = df_artists[["artists_info", "name", "popularity","followers"]].rename(columns={'artists_info': 'id', 'name': 'label'})
    df_noeuds.drop_duplicates(subset=["id"], inplace=True)
    df_noeuds["type"] = "Artist"
    df_noeuds["main_continent"] = df_noeuds["id"].apply(lambda artist_id: continent_principale(artist_id, df_artists))
    styles = ['trap', 'rap', 'pop', 'reggeaton', 'hip hop', 'urbano latino', 'drill', 'funk', 'r&b', 'cumbia', 'country', 'rock', 'bachata', 'sierreno', 'house', 'v-pop','k-pop','dembow', 'corrido', 'amapiano']
    # Initialize an empty list to store the new rows
    new_rows = []

    # Create new rows for each style
    for style in styles:
        new_rows.append({'id': style, 'label': style, 'type': 'Genre'})

    # Convert new rows to a DataFrame and concatenate with the existing DataFrame
    new_rows_df = pd.DataFrame(new_rows)
    df_noeuds = pd.concat([df_noeuds, new_rows_df], ignore_index=True)

    # Save to CSV
    df_noeuds.to_csv("./data/Artist_gephi/graphe_popularite/neouds_continent.csv", index=False)

def create_edges():
    """genère la table des liens pour le fichier gephi"""
    df_artists = pd.read_csv("data/artists_info/artists.csv")
    df_artists.drop_duplicates(subset=["artists_info"], inplace=True)
    styles = ['trap', 'rap', 'pop', 'reggeaton', 'hip hop', 'urbano latino', 'drill', 'funk', 'r&b', 'cumbia',
              'country', 'rock', 'bachata', 'sierreno', 'house', 'v-pop', 'k-pop', 'dembow', 'corrido', 'amapiano']
    edges_df = pd.DataFrame(columns=["Source", "Target"])
    for index, artist in df_artists.iterrows():
       # print(artist)
        for style in styles:
            if type(artist["genres"]) is str and style in artist["genres"]:
                edges_df = pd.concat([edges_df, pd.DataFrame([{"Source": artist["artists_info"], "Target": style}])], ignore_index=True)
    # Save to CSV
    edges_df.to_csv("./data/Artist_gephi/graphe_popularite/edges_continent.csv", index=False)



def main():
    create_table_noeuds()
    create_edges()
    pass

if __name__ == "__main__":
    main()