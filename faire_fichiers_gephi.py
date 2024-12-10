import pandas as pd



def pays_principale(artist_id, artists_df):
    df_pays_artist = artists_df[artists_df["artists"] == artist_id]["country"]
    most_frequent = df_pays_artist.mode()[0]
    return (most_frequent)


def create_table_noeuds():
    df_artists = pd.read_csv("./data/artists/artists.csv")
    df_neouds = df_artists.drop_duplicates(subset=["artists"]).copy()
    df_neouds["main_country"] = df_neouds["artists"].apply(lambda artist_id: pays_principale(artist_id, df_artists))
    new_row = pd.DataFrame({'name': ['rap', 'trap', 'pop','reggaeton', 'hip hop', 'urbano latino', 'rock', 'drill', 'funk', 'r&b']})
    df_neouds = pd.concat([df_neouds, new_row], ignore_index=True)
    df_neouds.to_csv("./data/Artist_gephi/neouds.csv")

def create_edges():
    pass


def main():
    #create_table_noeuds()

if __name__ == "__main__":
    main()