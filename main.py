#SAISSIR LES VARIABLES NOM ET AGE
nom=input("entrer votre nom:")
age=int(input("entrer votre age:"))

print("Bonjour",nom,"vous avez",age,"ans")
# DERTERMINER SI LA PERSONNE EST MAJEUR OU MINEUR
if age >= 18:
    print("vous etes majeur")
else:
    print("vous etes mineur")
#AFFICHER LES NOMBRES PAIR DE 1 A 100
for i in range(1,101):
    if i % 2 == 0:
        print(i)

#FIN DE NOTRE PROGRAMME

