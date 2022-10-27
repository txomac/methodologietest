from datetime import *


def miroir(chaine):
    if chaine == chaine[::-1]:
        print("Bien jouer")
        return True
    else:
        print("Ce n'est pas un palindrome")
        return False


def heureActuelle(now):
    if 12 < now.hour < 14:
        return "Bon appétit"
    elif 5 < now.hour < 17:
        return "Bonjour"
    elif 17 < now.hour < 20:
        return "Bonsoir"
    elif now.hour > 20:
        return "Bonne nuit"


def console():
    now = datetime.now()
    print(heureActuelle(now))
    mot = str(input("Veuillez saisir un mot : "))
    miroir(mot)
    print("Au revoir")


if __name__ == "__main__":
    console()
