# DEBUT 
r=12000
s=1250
e=10
rh=230
assertionFinale = (((365 * 3) / (24 - (16 - 8)) ) * (rh) > r) == (e * s > r)
assertLeft = (((365 * 3) / (24 - (16 - 8)) ) * (rh) > r)
assertRight = (e * s < r)
assertionFinale = assertLeft == assertRight
# print (assertLeft) #True
# print (assertRight) #False
# print (assertionFinale) #False

assertionFinalDeux = ((365 * 3) / (4 - (12 - 8)) * (rh) > r) == (e * s < r)
assertLeftDeux = ((365 * 3) / (4 - (12 - 8)) * (rh) > r)
assertRightDeux = (e * s < r)
assertionFinalDeux = assertLeftDeux == assertRightDeux
# print (assertLeftDeux)#Error = False
# print (assertRightDeux)#False
# print (assertionFinalDeux)#True

def retournerSixPlusTrois():
    return 6 + 3
def retournerSixPlusX(x, y):
    return 6 + x

retournerSixPlusTrois()
retournerSixPlusX(9, 4)
# FIN