import shutil
import os
import pandas as pd
import re
from collections import defaultdict

def format_file_path(filePath):
    """ Format the file path to use forward slashes and remove unnecessary quotes. """
    return filePath.strip().replace("\\", "/").replace("\"", "")

def sanitize_filename(filename):
    """ Remove invalid characters for Windows filenames and trim extra underscores. """
    filename = re.sub(r'[\\/*?:"<>|]', '_', filename)
    filename = re.sub(r'^=+', '', filename)
    return filename.strip("_")

def generate_new_name(group, suffix):
    """ Generate a new filename based on a group of students. """
    name_parts = []
    for row in group:
        part1 = sanitize_filename(str(row[0]).strip().replace(" ", "_"))
        part2 = sanitize_filename(str(row[1]).strip().replace(" ", "_"))
        part3 = sanitize_filename(str(row[2]).strip().replace(" ", "_"))
        name_parts.append(f"{part1}_{part2}_{part3}")
    
    return "_".join(name_parts) + "_" + suffix + ".xlsx"

def generate_new_names(input_file, suffix):
    """ Read CSV and generate grouped filenames. """
    df = pd.read_csv(input_file, header=0, encoding='ISO-8859-1', sep=';')

    groups = defaultdict(list)
    
    for _, row in df.iterrows():
        group_key = row.iloc[3] if len(row) > 3 and pd.notna(row.iloc[3]) else str(row.iloc[0])
        groups[group_key].append((row.iloc[0], row.iloc[1], row.iloc[2]))

    return {group_key: generate_new_name(group, suffix) for group_key, group in groups.items()}

def copy_and_rename_file(source_file, destination_folder, new_names):
    """ Copy and rename the file for each new filename in the list. """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for _, name in new_names.items():
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