# Ces scripts permettent de générer les fichiers de liens et de noeuds en vue de
# visualiser la tendance des artises à occuper les Top50 sur Gephi.

import csv

nodes_file = "data/Artist_gephi/graph_aristes_pays/nodes.csv"
edges_file = "data/Artist_gephi/graph_aristes_pays/edges.csv"

artists_data = {}
edges = {}

# lecture données
with open('data/artists/artists.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)
    
    for row in rows:
        artist_id = row['artists']
        country = row['country']
        name = row['name']
        popularity = row['popularity']
        followers = row['followers']
        
        # ajouter les données des artistes si elles sont pas deja presentes
        if artist_id not in artists_data:
            artists_data[artist_id] = {
                'name': name,
                'popularity': popularity,
                'followers': followers
            }
        
        # ajouter ou maj lien entre artiste et pays
        if (artist_id, country) in edges:
            edges[(artist_id, country)] += 1  # si le lien existe incremente le poids
        else:
            edges[(artist_id, country)] = 1  # si le lien existe pas poids = 1

# extraire les pays
countries = set(row['country'] for row in rows)

# ecrire noeuds
with open(nodes_file, 'w', newline='') as nf:
    writer = csv.writer(nf)
    writer.writerow(["Id", "Label", "Popularity", "Followers", "Type"])
    
    # ajouter les artistes comme noeud
    for artist_id, artist_info in artists_data.items():
        writer.writerow([artist_id, artist_info['name'], artist_info['popularity'], artist_info['followers'], "artist"])
    
    # ajouter les pays comme noeud
    for country in countries:
        writer.writerow([country, country, "", "", "country"])

# ajouter les liens entre artistes et pays
with open(edges_file, 'w', newline='') as ef:
    writer = csv.writer(ef)
    writer.writerow(["Source", "Target", "Weight"]) 
    
    # ajouter les liens entre artistes et pays avec leurs poids
    for (artist_id, country), weight in edges.items():
        writer.writerow([artist_id, country, weight])

print("Les fichiers de noeud et de liens ont été générés.")
