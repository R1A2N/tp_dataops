import pandas as pd
def process_data(file_path, output_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
   
    
    # Step 2: Remove unwanted rows (like a specific index)
    df.drop(100, inplace=True)
        
    # Step 5: Remove duplicate rows
    df.drop_duplicates(inplace=True)
    
   # Nettoyage de base
    df.dropna(subset=['Country'], inplace=True)  # Supprime les chaînes sans pays
    df['Subscribers'] = df['Subscribers'].str.replace('M', 'e6').astype(float)  # Convertir "M" en valeurs numériques
    df['Views'] = df['Views'].str.replace(',', '').astype(float)  # Enlever les virgules et convertir en float
    df['Uploads'] = df['Uploads'].str.replace(',', '').astype(float)
    # Step 7: Save the cleaned dataset to a new Excel file
    df.to_csv(output_path, index=False)
    
    # Display dataset summary
    print("Cleaned Data Overview:")
    print(df.head())
    print("\nDataset Description:")
    print(df.describe())

if __name__ == "__main__":
    input_file = "data/YOUTUBE_CHANNELS_DATASET.csv"
    output_file = "data/Cleaned_Youtube_Channels_Dataset.csv"
    
    process_data(input_file, output_file)
    print(f"Data cleaned and saved to {output_file}")
