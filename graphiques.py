import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

import pandas as pd
import matplotlib.pyplot as plt
import math


def graphique_attribut_position(save_path):
    """Crée des graphiques de la position dans le top 50 en fonction des différents attributs musicaux"""

    liste_attributes = ['danceability', 'energy', 'key',
                        'loudness', 'mode', 'speechiness', 'acousticness',
                        'instrumentalness', 'liveness', 'valence', 'tempo']


    n_plots = len(liste_attributes)
    n_cols = min(3, n_plots)  # Maximum 3 columns
    n_rows = math.ceil(n_plots / n_cols)

    # Create figure with subplots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 4 * n_rows))
    fig.suptitle("Position dans le top 50 en fonction des attributs", y=1.02)

    # Read data once outside the loop
    df = pd.read_csv("./data/all_features.csv")

    # Create each subplot
    for idx, attribute in enumerate(liste_attributes):
        row = idx // n_cols
        col = idx % n_cols

        axes[row, col].scatter(df[attribute], df["position"])
        axes[row, col].set_title(attribute)
        axes[row, col].set_xlabel(attribute)
        axes[row, col].set_ylabel("Position dans Top 50")

    # Hide empty subplots if any
    for idx in range(n_plots, n_rows * n_cols):
        row = idx // n_cols
        col = idx % n_cols
        axes[row, col].set_visible(False)

    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()

def comparaison_attributs_continents(attribute: str, save_path : str):
    # Read data for each continent
    africa_df = pd.read_csv("./data/continent_features/Africa.csv")
    asia_df = pd.read_csv("./data/continent_features/Asia.csv")
    central_america_df = pd.read_csv("./data/continent_features/Central_America.csv")
    europe_df = pd.read_csv("./data/continent_features/Europe.csv")
    oceania_df = pd.read_csv("./data/continent_features/Oceania.csv")
    south_america_df = pd.read_csv("./data/continent_features/South_America.csv")

    # Create list of data for boxplot
    data = [
        africa_df[attribute],
        asia_df[attribute],
        central_america_df[attribute],
        europe_df[attribute],
        oceania_df[attribute],
        south_america_df[attribute]
    ]

    # Create figure with appropriate size
    fig = plt.figure(figsize=(10, 7))

    # Add subplot with proper margins
    ax = fig.add_subplot(111)

    # Set labels for x and y axes
    plt.xlabel('Continents')
    plt.ylabel(attribute.replace('_', ' ').title())

    # Set title
    plt.title(f'Distribution of {attribute.replace("_", " ").title()} by Continent')

    # Create list of continent names for labels
    continent_labels = ['Africa', 'Asia', 'Central America',
                        'Europe', 'Oceania', 'South America']

    # Create boxplot
    bp = plt.boxplot(data, tick_labels=continent_labels)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    plt.savefig(save_path, bbox_inches='tight', dpi=300)

    # Show plot
    plt.show()

    # Optional: Return statistical summary
    summary_stats = {
        continent: {
            'median': np.median(data[i]),
            'mean': np.mean(data[i]),
            'std': np.std(data[i])
        }
        for i, continent in enumerate(continent_labels)
    }
    return summary_stats



def main():
    liste_attributes = ['danceability', 'energy',
                        'loudness', 'speechiness', 'acousticness',
                       'instrumentalness', 'liveness', 'valence', 'tempo']
    for attribut in liste_attributes :
        comparaison_attributs_continents(attribut, f"data/graphiques/analyse_variance/{attribut}_box_plot")
    #graphique_attribut_position("./graphiques/attributs_position")


if __name__ == "__main__":
    main()