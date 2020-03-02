import re
import sys

def errorParsing(error):
    print(error)
    exit(0)

def delete_whitespace(to_purge):
    purged = ""
    for x in to_purge:
        if not x == ' ':
            purged += x
    if purged == '=':
        errorParsing("Not correct input")
    return purged

def get_value(expressions,mult):
    if expressions == "":
        errorParsing("Incorrect Expression")
    dict_return = {}
    x = re.search("^([+-]?[0-9]+(?:\.[0-9]+)?)\*X\^([0-9]+)",expressions)
    y = 0
    while y < len(expressions):    
        if x == None:
            errorParsing("Incorrect Expression")
        y += x.span()[1]
        if int(x.group(2)) in dict_return.keys():
            dict_return[int(x.group(2))] += float(x.group(1)) * mult
        else:
            dict_return[int(x.group(2))] = float(x.group(1)) * mult
        x = re.search("^([+-][0-9]+(?:\.[0-9]+)?)\*X\^([0-9]+)",expressions[y:])
    return dict_return

def fusionDict(dict1, dict2):
    for x,y in dict2.items():
        if x in dict1.keys():
            dict1[x] += y
        else:
            dict1[x] = y
    outReduc = "Reduced form:"     
    for x in list(dict1):
        if dict1[x] == 0:
            dict1.pop(x)
        elif int(dict1[x]) != 0 and dict1[x] % int(dict1[x]) == 0:
            dict1[x] = int(dict1[x])
    reducedList = []
    for key in sorted(dict1):
        while key >= len(reducedList):
            reducedList.append(0)
        reducedList[key] += dict1[key]
        sign=' +'
        if len(outReduc) == 13:
            sign=''
        if dict1[key] < 0:
            sign=' -'
        outReduc += "{} {} * X^{}".format(sign, abs(dict1[key]), key)
    outReduc += ' = 0'
    if len(reducedList) > 1:
        print (outReduc)
    return reducedList

def parsingEquation(all_str):
    cleaned_str = delete_whitespace(all_str)
    splited = cleaned_str.split('=')
    if len(splited) != 2:
        errorParsing('Not correct input')
    before_equal = splited[0]
    after_equal = splited[1]
    dict1,dict2 = {},{}
    if before_equal == '0' and after_equal == '0':
        errorParsing('Not correct input')
    if before_equal != '0':
        dict1 = get_value(before_equal, 1)
    if after_equal != '0':
        dict2 = get_value(after_equal, -1)
    return fusionDict(dict1,dict2)