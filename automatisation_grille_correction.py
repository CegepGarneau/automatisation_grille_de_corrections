import shutil
import os
import pandas as pd

def format_file_path(filePath):
    filePath = filePath.replace("\\", "/")
    filePath = filePath.replace("\"", "")
    return filePath

def generate_new_names(input_file, suffix):
    df = pd.read_csv(input_file, header=0, encoding='ISO-8859-1', sep=';')
    
    new_names = []

    for index, row in df.iterrows():
        part1 = str(row.iloc[0]).replace(" ", "_")
        part2 = str(row.iloc[1]).replace(" ", "_")
        part3 = str(row.iloc[2]).replace(" ", "_")
        combined_name = f"{part1}_{part2}_{part3}_{suffix}.xlsx"
        new_names.append(combined_name)  
    return new_names

def copy_and_rename_file(source_file, destination_folder, new_names):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for name in new_names:
        new_file_path = os.path.join(destination_folder, name)
        shutil.copy(source_file, new_file_path)
        print(f'Copied and renamed to: {new_file_path}')

if __name__ == "__main__":
    input_file = format_file_path(input("Entrez le chemin du fichier CSV avec entête contenant la liste d'étudiants en format (DA;Nom;Prénom;): "))
    source_file = format_file_path(input("Entrez le chemin de la grille de correction en format excel .xlsx: "))
    destination_folder = format_file_path(input("Entrez le chemin du dossier de destination (destination folder): "))
    suffix = input("Entrez le suffixe pour les fichiers (par exemple : TP1, TP2, etc.): ")

    if not os.path.exists(input_file):
        print("Le fichier CSV spécifié n'existe pas.")
    elif not os.path.exists(source_file):
        print("Le fichier source spécifié n'existe pas.")
    elif not os.path.exists(destination_folder):
        print("Le dossier de destination spécifié n'existe pas.")
    else:
        new_names = generate_new_names(input_file, suffix)
        copy_and_rename_file(source_file, destination_folder, new_names)
