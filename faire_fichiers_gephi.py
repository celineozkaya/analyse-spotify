import pandas as pd



def pays_principale(artist_id, artists_df):
    df_pays_artist = artists_df[artists_df["artists"] == artist_id]["country"]
    most_frequent = df_pays_artist.mode()[0]
    return (most_frequent)


def create_table_noeuds():
    df_artists = pd.read_csv("./data/artists/artists.csv")
    df_neouds = df_artists[["artists", "name"]].rename(columns={'artists': 'id', 'name': 'label'})
    df_neouds.drop_duplicates(subset=["id"], inplace=True)
    df_neouds["type"] = "Artist"
    df_neouds["main_country"] = df_neouds["id"].apply(lambda artist_id: pays_principale(artist_id, df_artists))

    styles = ['trap', 'rap', 'pop', 'reggeaton', 'hip hop', 'urbano latino', 'drill', 'funk', 'r&b', 'cumbia', 'country', 'rock', 'bachata', 'sierreno', 'house', 'v-pop','k-pop','dembow', 'corrido', 'amapiano']
    # Initialize an empty list to store the new rows
    new_rows = []

    # Create new rows for each style
    for style in styles:
        new_rows.append({'id': style, 'label': style, 'type': 'Genre'})

    # Convert new rows to a DataFrame and concatenate with the existing DataFrame
    new_rows_df = pd.DataFrame(new_rows)
    df_neouds = pd.concat([df_neouds, new_rows_df], ignore_index=True)

    # Save to CSV
    df_neouds.to_csv("./data/Artist_gephi/neouds.csv", index=False)

def create_edges():
    pass


def main():
    create_table_noeuds()
    pass

if __name__ == "__main__":
    main()