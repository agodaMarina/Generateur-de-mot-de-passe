import random

nombre="123456789"
lettre="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbole="&$%!{}()"

caractere =lettre + lettre.lower() + nombre + symbole
caractere_sans_symbole= lettre+lettre.lower()+nombre

while True:
    longueur_mdp = 8
    choix=str(input("voulez-vous un caractère spéciale ?"))
    if choix=="oui":
        mdp=""
        mdpv=""
        for i in range (0,longueur_mdp):
            cmdp=random.choice(caractere)
            
            mdp=mdp+cmdp
        print("votre mot de passe est :",mdp)
    
            
    elif choix=="non":
        for i in range (0,longueur_mdp):
            cmdpv=random.choice(caractere_sans_symbole)
            
            mdpv=mdpv+cmdpv
        print("votre mot de passe est : ",mdpv)
    break
        


