#add(x,y)
#sub(x,y)
#multiply(x,y)
#divide(x,y)
#modulo(x,y)

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def modulo(x,y):
    return x%y

def salaireNet(salaireBrut, coefficient):
    return salaireBrut*coefficient

def calculSalParSec(salaireHoraire, heureParJO, jO):
    # Je calcule le salaire annuel
    salaireAnnuel = salaireHoraire * heureParJO * jO
    # Je calcule le nombre de secondes dans une annee 
    nbSecondeParAn = 365 * 24 * 60 * 60 
    # Je divise mon salaire par le nombre de secondes
    return salaireAnnuel / nbSecondeParAn
    


#SalaireParSeconde(
# SalaireHoraire,
# heureParJourOuvre,
# NbJoursOuvréParAn)
