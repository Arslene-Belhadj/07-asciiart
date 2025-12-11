"ASCII"
#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 
    en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 
    en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    if not s:
        return []
    first_char = s[0]
    count = 0
    while count < len(s) and s[count] == first_char:
        count += 1
    return [(first_char, count)] + artcode_r(s[count:])

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif

#### Fonction principale


def main():
    "fonction main"
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
