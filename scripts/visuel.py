import pandas as pd
import matplotlib.pyplot as plt

def generate_graph(input_path, output_path):
    # Chargement des données nettoyées
    df = pd.read_csv(input_path)

    # Vérifier les colonnes nécessaires
    if 'Country' in df.columns and 'Subscribers' in df.columns:
        # Regrouper les abonnés par pays
        country_data = df.groupby('Country')['Subscribers'].sum().sort_values(ascending=False).head(10)

        # Création du graphique
        plt.figure(figsize=(10, 6))
        country_data.plot(kind='bar', color='skyblue')
        plt.title('Top 10 Countries by Total Subscribers', fontsize=14)
        plt.xlabel('Country', fontsize=12)
        plt.ylabel('Total Subscribers (Millions)', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        # Sauvegarde du graphique dans un fichier PDF
        plt.savefig(output_path)
        print(f"Graph saved to {output_path}")
    else:
        print("Required columns ('Country', 'Subscribers') are missing in the dataset.")

if __name__ == "__main__":
    input_file = "data/Cleaned_Youtube_Channels_Dataset.csv"
    output_file = "data/Top_Countries_Subscribers.pdf"

    generate_graph(input_file, output_file)
