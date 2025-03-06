import shutil
import os
import pandas as pd
import re

def format_file_path(filePath):
    """ Format the file path to use forward slashes and remove unnecessary quotes. """
    return filePath.strip().replace("\\", "/").replace("\"", "")

def sanitize_filename(filename):
    """ Remove invalid characters for Windows filenames and trim extra underscores. """
    filename = re.sub(r'[\\/*?:"<>|]', '_', filename)  # Replace invalid characters
    filename = re.sub(r'^=+', '', filename)  # Remove leading '=' (Excel issue)
    return filename.strip("_")  # Trim underscores

def generate_new_name(row, suffix):
    """ Generate a new filename based on row data and suffix. """
    part1 = sanitize_filename(str(row.iloc[0]).strip().replace(" ", "_"))
    part2 = sanitize_filename(str(row.iloc[1]).strip().replace(" ", "_"))
    part3 = sanitize_filename(str(row.iloc[2]).strip().replace(" ", "_"))
    return f"{part1}_{part2}_{part3}_{suffix}.xlsx"

def generate_new_names(input_file, suffix):
    """ Read CSV and generate a list of new filenames. """
    df = pd.read_csv(input_file, header=0, encoding='ISO-8859-1', sep=';')
    return [generate_new_name(row, suffix) for _, row in df.iterrows()]

def copy_and_rename_file(source_file, destination_folder, new_names):
    """ Copy and rename the file for each new filename in the list. """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for name in new_names:
        new_file_path = os.path.join(destination_folder, name)
        shutil.copy(source_file, new_file_path)
        print(f'Copied and renamed to: {new_file_path}')

if __name__ == "__main__":
    input_file = format_file_path(input("Entrez le chemin du fichier CSV : "))
    source_file = format_file_path(input("Entrez le chemin de la grille de correction (.xlsx) : "))
    destination_folder = format_file_path(input("Entrez le dossier de destination : "))
    suffix = sanitize_filename(input("Entrez le suffixe : "))

    if not os.path.exists(input_file):
        print("Le fichier CSV spécifié n'existe pas.")
    elif not os.path.exists(source_file):
        print("Le fichier source spécifié n'existe pas.")
    elif not os.path.exists(destination_folder):
        print("Le dossier de destination spécifié n'existe pas.")
    else:
        new_names = generate_new_names(input_file, suffix)
        copy_and_rename_file(source_file, destination_folder, new_names)
