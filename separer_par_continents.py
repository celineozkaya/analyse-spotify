'''
    Ce script classe les morceaux avec leur attributs par continents, utile pour pouvoir faire des
    comparaisons par contient.

'''


import pandas as pd

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



features_df = pd.read_csv("data/all_features.csv")
print(features_df["country"])
for continent, countries in continents.items():
    continent_features_df = features_df[features_df["country"].isin(countries)]
    #print(continent_features_df)
    continent_features_df.to_csv(f"./data/continent_features/{continent}.csv", index = False)

