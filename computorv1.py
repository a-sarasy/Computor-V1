# -*- coding: utf-8 -*-

import sys


def parsingEq(baseForm):
#Parsing de l'entrée(String de forme 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0)
#Liste en sortie avec les valeurs ordonnées
    sign = '+'
    stockNumber = []
    postEqual = 1

    for x in baseForm:
        if x.startswith('X'):
            prime = int(x[2:])
            stockNumber.append([prime, nbr])
        elif x == '+' or x == '-' or x == '*':
            sign = x
        elif x == '=':
            postEqual = -1
            sign = '+' 
        else:
            x = sign + x
            if '.' in x:
                nbr = float(x) * postEqual
            else:
                nbr = int(x) * postEqual
    reducedList = []
    for term in stockNumber :
        while term[0] >= len(reducedList):
            reducedList.append(0)
        reducedList[term[0]] += term[1]
    while reducedList[-1] == 0:
        reducedList = reducedList[:-1]

    return(reducedList)

def fraction(up, down, iUp = 0):
    if iUp != 0:
        if iUp/down > 0: output = str(up/down) + ' + ' + str(iUp/down) + 'i'
        else: output = str(up/down) + ' - ' + str(abs(iUp/down)) + 'i'
        print(output)
    elif '.' in str(up) or '.' in str(down):
        print(str((up)/(down)))
    else:
        x = abs(up)  if abs(up) < abs(down) else abs(down)
        while x > 0:
            if abs(up) % x == 0 and abs(down) % x == 0:
                up,down = up/x,down/x
                if down == 1:
                    print(str(int(up)))
                else:
                    print (str(int(up/x)) + '/' + str(int(down/x)))
                break
            x -= 1

def secondPolynom(a, b, c):
    solution = []
    disc = b**2 - 4 * a * c
    racDisc = disc ** 0.5 if disc > 0 else abs(disc) ** 0.5
    racDisc = int(racDisc) if racDisc % int(racDisc) == 0 else racDisc
    if disc < 0:
        print("There are no solutions in the reals")
        print("The complex solutions are :")
        up, iUp = -b, - racDisc
        down = 2 * a
        fraction(up,down,iUp)
        up, iUp = -b, racDisc
        fraction(up,down,iUp)
        
    if disc == 0:
        fraction(-b, 2*a)
    if disc > 0:
        up,upBis = -b+racDisc,-b-racDisc
        down,downBis = 2 * a,2*a
        print("The solutions are : ")
        fraction(up,down)
        fraction(upBis,downBis)

if(len(sys.argv) < 2):
    print("usage : python computorv1.py \"polynomial expression\"")
    exit()
baseForm = sys.argv[1].split(' ')
reducedList = parsingEq(baseForm)
outReduc = "Reduced form:"
for x in range(len(reducedList)):   
    sign = ' + ' if reducedList[x] > 0 else ' - '
    if x == 0 and reducedList[x] > 0: sign = " "

    outReduc += sign + str(abs(reducedList[x])) + " * X^" + str(x)
print(outReduc + " = 0")
polyNbr = len(reducedList) - 1
print("Polynomial degree: " + str(polyNbr))
if polyNbr > 2:
    print("The polynomial degree is stricly greater than 2, I can't solve.")
    exit(0)
if polyNbr == 2:
    secondPolynom(reducedList[2], reducedList[1], reducedList[0])
if polyNbr == 1:
    print("The solution is : " + str(-reducedList[0] / reducedList[1]))
if polyNbr == 0:
    print("No unknown : all numbers are solutions")
