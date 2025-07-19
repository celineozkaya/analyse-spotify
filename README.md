La musique, en tant que reflet des tendances culturelles et sociales, offre une
opportunité d’analyse à travers les données disponibles sur des plateformes
numériques comme Spotify. Dans le cadre du projet de l’UV IC05, nous avons
exploité les données rendues accessibles par l’API Spotify, un outil permettant
d’accéder à une multitude de données sur les morceaux, les artistes et les genres,
au travers d’une étude sur les Top50 générés par la plateforme. Inspiré du projet
“Data Analysis with Spotify API” d’Erick Lopez (2023), qui portait sur le Billboard Hot
100, ce travail s'inscrit dans une perspective à l’échelle mondiale, continentale et
nationale. En utilisant Python et ses librairies d’analyse et traitement de données,
l’objectif est de mettre en lumière les critères influençant la sélection des morceaux,
de cartographier les relations entre artistes, pays et genres présents dans les Top50,
et d’analyser les facteurs déterminants de la popularité musicale. Ce projet cherche
ainsi à comprendre en quoi les réseaux d’artistes, genres et pays et les
caractéristiques musicales attribuées par Spotify reflètent les préférences des
utilisateurs de la plateforme ?

# Informations sur le repo

**/data** : Contient toutes les données

- data/Artistes_gephi : contient les graphes gephi pour les artistes
- data/artists_info : contient les données pour sur les artistes, globale et par contients
- data/continent_features : contient les features pour les morceaux par continent, utile l'ors de la comparaison des attributs par continent
- data/graphiques : contient les graphiques faits avec matplotlib
- all_features.csv : contient les données sur les attributs de tout les morceaux dans tout les top 50
- top_50_cleaned_playlise_data.csv : contient l'id de toutes les playlist top50 les non officiels ou les erreurs de scrapping
- top50_raw_playlists_data.csv : résultat du scrapping des playlistes top50, contient beaucoup d'incohérences et de mauvaises données

**/extras** : contient touts les scripts et fichiers qui n'ont finallement pas servis dans le rapport final
  
Pour simplifier l'accès aux différents graphes interactifs, il est recommandé de cloner ce répertoire. Sinon il faut télécharger un fichier pour chaque graphe.


## Liste des genres retenus
trap, rap, pop, reggeaton, hip hop, urbano latino, drill, funk, r&b, cumbia, country, rock, bachata, sierreno, house, v-pop,k-pop,dembow, corrido, amapiano

# Caractéristiques audio d'un morceau dans l'API Spotify

Les morceaux dans l'API Spotify possèdent plusieurs caractéristiques audio pour analyser la musique :

- **Acousticness** : Évalue la probabilité qu'une piste soit acoustique, variant de 0.0 (pas du tout) à 1.0 (très acoustique). Ex. : Une valeur de 0.9 indique un morceau probablement acoustique.

- **Danceability** : Indicateur de la capacité d'un morceau à être dansé, basé sur le tempo, la stabilité du rythme, la force du beat et la régularité. Les valeurs s'étendent de 0.0 (peu dansant) à 1.0 (très dansant).

- **Energy** : Mesure de l'intensité et de l'activité, variant de 0.0 (faible énergie) à 1.0 (forte énergie). Ce facteur prend en compte la rapidité, la densité sonore et le niveau d'activité. Ex : Un morceau de métal est perçu comme étant très énergique.

- **Instrumentalness** : Évalue la probabilité qu'un morceau soit instrumental, de 0.0 à 1.0. Plus la valeur est élevée, plus la probabilité qu'il soit instrumental est forte. Valeurs au-dessus de 0.5 suggèrent des morceaux sans voix.

- **Liveness** : Probabilité qu'un morceau soit enregistré en public (live). Les valeurs au-dessus de 0.8 indiquent des pistes avec une forte présence de public.

- **Loudness** : Niveau sonore moyen en décibels (dB), moyenne sur l’ensemble du morceau. Varie de -60 à 0db.

- **Speechiness** : Mesure la quantité de mots parlés. Des valeurs proches de 1.0 indiquent principalement des paroles (comme un podcast). Les morceaux musicaux auront des valeurs plus basses. Entre 0.33 et 0.66, on considère qu'il y a une combinaisons de mots parlés et de musique (ex : rap). En dessous de 0.33 on considère qu'il s'agit de musiques sans paroles.

- **Valence** : Mesure de la positivité d'un morceau, de 0.0 (triste, colère) à 1.0 (joyeux). Exemples : valeurs hautes pour les morceaux heureux et optimistes.

- **Tempo** : Vitesse estimée en battements par minute (BPM).

- **Key & Mode** :
  - **Key** : La tonalité principale de la piste, indiquée de 0 à 11, correspondant à C, C♯/D♭, D, etc. Ex : C=0 (Do majeur), C♯/D♭ = 1 (Do♯/ Ré♭), etc.
  - **Mode** : Indique si le morceau est en majeur (1) ou mineur (0).

Pour plus d’informations : [Spotify API Documentation](https://developer.spotify.com/documentation/web-api/reference/get-audio-features).
