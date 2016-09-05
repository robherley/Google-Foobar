'''

@author: Rob Herley

'''
import itertools
Months = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, \
          '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
def answer(x,y,z):
    L = x, y, z
    if len(str(x)) < 2:
        XX = '0' + str(x)
    else:
        XX = str(x)
    if len(str(y)) < 2:
        YY = '0' + str(y)
    else:
        YY = str(y)
    if len(str(z)) < 2:
        ZZ = '0' + str(z)
    else:
        ZZ = str(z)
    possibleList = list(itertools.permutations([XX,YY,ZZ], 3))
    newList = []
    for x in possibleList:
        if int(x[0]) <= 12:
            maxDays = Months[x[0]]
            if int(x[1]) in range(maxDays + 1):
                newList += [x]
    if not newList:
        return 'Ambiguous'
    elif newList[1:] == newList[:-1]:
        date = newList[0]
        return date[0] + '/' + date[1] + '/' + date[2]
    else:
        return 'Ambiguous'

print(answer(1,31,12))
print(answer(99,99,3))

