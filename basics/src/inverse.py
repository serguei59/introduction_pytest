def inverse(chaine):
    if isinstance(chaine, int):
        raise ValueError("Vous devez passer une chaine de caractères")
    
    
    for element in chaine:
        if not isinstance(element, str):
            raise ValueError("vous devez passer une chaine de caractères")
        

    if len(chaine) == 4 and isinstance(chaine, list):
        chaine.pop()
        
    chaine = "".join(chaine)

    
        
    return chaine[::-1]

# # j utilise la syntaxe if __name_  == "__main__"
# _name__ est une var d env créée ds chaque dossier pyhton qui est main quand je l execute directement et pas par importation
# le name prendrait alors le nom du fichier qui importe
# donc: si j execute ce fichier directement et non par import execute print(inverse("hello"))
if __name__ == "__main__":
    print(inverse(["a","b","c","d"]))
    print(inverse(["a","b",0,"c"]))

