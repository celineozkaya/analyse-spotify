

# NOTES de la prof

- stat sur les artistes des top (plus suivi, moins suivi, etc.)
- maybe pls prises de données sur 3 pays pour montrer evolutions day2day 
- artistes et morceaux communs à plusieurs top50 : artistes qui circulent le mieux? (à l'echelle mondiale+contient)
- prendre tous les artistes et faire un reseau des artistes et des genres (noeuds= genre et artistes et on lie les artistes a leurs genres) et faire un fichier :


fichier des liens (edges): 
taylor swift, pop
taylor swift, country

fichiers des noeuds:
taylor swift, genre, follower, continent, etc
artiste, genre, follower, continent, etc

nodes.csv
Id,Label,Type,main_country
2YZyLoL8N0Wb9xBt1NhZWg,Kendrick Lamar,Artist,United States
1jiZvw42D4oquLl24x2VWV,Lefty Gunplay,Artist,United States
7tYKF4w9nC0nq9CsPZTHyP,SZA,Artist,Malaysia
4VHa48wXlsDA2vWfgIi7cX,Dody6,Artist,United States
6cUpFVxDYWed9WxtC4QgC5,Wallie the Sensei,Artist,United States
7J5UWTbsUFjoSQZQCQCqbQ,Siete7x,Artist,United States
conscious hip hop,conscious hip hop,Genre,
hip hop,hip hop,Genre,
rap,rap,Genre,
west coast rap,west coast rap,Genre,
pop,pop,Genre,
r&b,r&b,Genre,
westcoast flow,westcoast flow,Genre,
cali rap,cali rap,Genre,



edges.csv
Source,Target,Weight
2YZyLoL8N0Wb9xBt1NhZWg,conscious hip hop,1
2YZyLoL8N0Wb9xBt1NhZWg,hip hop,1
2YZyLoL8N0Wb9xBt1NhZWg,rap,1
2YZyLoL8N0Wb9xBt1NhZWg,west coast rap,1
7tYKF4w9nC0nq9CsPZTHyP,pop,1
7tYKF4w9nC0nq9CsPZTHyP,r&b,1
7tYKF4w9nC0nq9CsPZTHyP,rap,1
4VHa48wXlsDA2vWfgIi7cX,westcoast flow,1
6cUpFVxDYWed9WxtC4QgC5,cali rap,1
6cUpFVxDYWed9WxtC4QgC5,westcoast flow,1
7J5UWTbsUFjoSQZQCQCqbQ,westcoast flow,1

## Liste des genres
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
