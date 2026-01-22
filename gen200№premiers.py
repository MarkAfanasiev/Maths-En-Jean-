def generer_nombres_premiers(limite=200):
    premiers = []
    for n in range(2, limite):
        est_premier = True
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                est_premier = False
                break
        if est_premier:
            premiers.append(n)
    return premiers

def oublier_nombre_premier(liste_premiers, nombre_a_oublier):
    return [n for n in liste_premiers if n != nombre_a_oublier]

def formater_pour_programme(liste):
    return " ".join(map(str, liste))

if __name__ == "__main__":
    premiers = generer_nombres_premiers(200)
    print("Suite initiale :")
    print(formater_pour_programme(premiers))

    a_oublier = int(input("\nQuel nombre premier veux-tu oublier ? "))
    nouveaux_premiers = oublier_nombre_premier(premiers, a_oublier)

    print("\nSuite après oubli :")
    print(formater_pour_programme(nouveaux_premiers))
