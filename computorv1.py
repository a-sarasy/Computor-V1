import sys

print(sys.argv[1])
baseForm = sys.argv[1].split(' ')
sign = '+'
stockNumber = []
postEqual = 1
print(baseForm)
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
print(stockNumber)
reducedList = []
for term in stockNumber :
    while term[0] >= len(reducedList):
        reducedList.append(0)
    reducedList[term[0]] += term[1]
print(reducedList)

outReduc = "Reduced form:"
for x in range(len(reducedList)):   
    sign = ' + ' if reducedList[x] > 0 else ' - '
    if x == 0 : sign = " "
    outReduc += sign + str(abs(reducedList[x])) + " * X^" + str(x)
print(outReduc + " = 0")