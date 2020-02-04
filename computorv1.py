# -*- coding: utf-8 -*-

import sys
from parser import parsingEquation

def fraction(up, down, iUp = 0):
    if iUp != 0:
        if iUp/down > 0: output = str(up/down) + ' + ' + str((iUp/down)) + 'i'
        else: output = str(up/down) + ' - ' + str(abs(iUp/down)) + 'i'
        print(output)
    elif '.' in str(up) or '.' in str(down):
        print(str((up)/(down)))
    
    else:
        x = abs(up)  if abs(up) < abs(down) else abs(down)
        if x == 0:
            print('0')
        while x > 0:
            if abs(up) % x == 0 and abs(down) % x == 0:
                up,down = up/x,down/x
                if down == 1:
                    print(str(int(up)))
                else:
                    print (str(int(up)) + '/' + str(int(down)))
                break
            x -= 1

def secondPolynom(a, b, c):
    solution = []
    disc = b**2 - 4 * a * c
    racDisc = disc ** 0.5 if disc > 0 else abs(disc) ** 0.5
    racDisc = int(racDisc) if racDisc % int(racDisc) == 0 else racDisc
    if disc < 0:  
        print("Discriminant is strictly negative")     
        print("There are no solutions in the reals")
        print("The complex solutions are :")
        up, iUp = -b, - racDisc
        down = 2 * a
        fraction(up,down,iUp)
        up, iUp = -b, racDisc
        fraction(up,down,iUp)
        
    if disc == 0:
        print("Discriminant is null, the solution is :")
        fraction(-b, 2*a)
    if disc > 0:
        up,upBis = -b+racDisc,-b-racDisc
        down,downBis = 2 * a,2*a
        print("Discriminant is strictly positive, the two solutions are")
        print("The solutions are : ")
        fraction(up,down)
        fraction(upBis,downBis)

def computorv1():
    if(len(sys.argv) != 2):
        print("usage : python computorv1.py \"polynomial expression\"")
        exit()
    reducedList = parsingEquation(sys.argv[1])
    polyNbr = len(reducedList) - 1
    print("Polynomial degree: " + str(polyNbr))
    if polyNbr > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        exit(0)
    if polyNbr == 2:
        secondPolynom(reducedList[2], reducedList[1], reducedList[0])
    if polyNbr == 1:
        print("The solution is : ")
        fraction(-reducedList[0] , reducedList[1])
    if polyNbr == 0:
        print("No unknown : all numbers are solutions")

if __name__ == "__main__":
    computorv1()