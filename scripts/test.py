import os
import pandas as pd

def process_excel(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier '{file_path}' est introuvable.")
    
    # Lecture du fichier Excel
    df = pd.read_excel(file_path)
    print("Contenu du fichier Excel :")
    print(df)

if __name__ == "__main__":
    # Chemin relatif vers le fichier Excel
    file_path = "data/note.xlsx"
    
    try:
        process_excel(file_path)
    except FileNotFoundError as e:
        print(e)