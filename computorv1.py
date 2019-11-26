import sys

print(sys.argv[1])
baseForm = sys.argv[1].split(' ')
sign = 1
stockNumber = []
postEqual = 1
print(baseForm)
for x in baseForm:
    if x.startswith('X'):
        prime = int(x[2:])
        stockNumber.append(prime, nbr)
    elif x == '+' or x == '-':
        sign = x
    elif x == '=':
        postEqual = -1
   
    else:
        if '.' in x:
            nbr = float(x) * postEqual * sign
        else:
            nbr = int(x) * postEqual * sign
print(stockNumber)



