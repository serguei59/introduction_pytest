from exercices.src.fonctions_difficiles import input_function_fois_deux, create_file, randomize
from unittest.mock import patch
import random

def test_input_function_fois_deux():
    with patch('builtins.input', return_value='3'):
        assert input_function_fois_deux() == 6

def test_create_file(tmpdir):
    # tmpdir crée un dossier temporaire et j y verifie dans une copie du fichier, tout sera supprimé automatiquement
    print(tmpdir)
    file_path = tmpdir.join("liste_apprenants.txt")
    print(file_path)
    create_file(file_path, "\nAlfred")
    with open(file_path, "r") as fichier:
        assert "\nAlfred" in fichier.read()

random.seed(42)

def test_randomize():
    assert randomize() == 0.6394267984578837