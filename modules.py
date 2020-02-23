from itertools import combinations as cb


def Dispenser(tmp: 'str'):
    '''
    Splits the string to a list of floats
    '''
    if(type(tmp) is not str):
        raise TypeError
    array = tmp.split()
    for c in range(len(array)):
        array[c] = float(array[c])
    return array


def prod(iterable):
    '''
    Finds product but taking negative values of elements in 'iterable'
    '''
    acc = 1
    for elem in iterable: 
        acc *= -elem
    return acc


def CalculateK(i: 'int', X: 'int list', y: 'float'):
    '''
    Calculates const multipliers
    '''
    for j in range(len(X)):
        if i != j:
            y /= X[i] - X[j]
    return y


def MultiplyAllSubcombs(Combinations: 'list', Size: 'int'):
    '''
    Multiplies all subcombinations in combimation
    '''
    SubCombinations = [[j for j in cb(Combinations, i)] for i in range(Size)]
    result = list()
    for i, sublist in enumerate(SubCombinations):
        result.append(sum([prod(subtuple) for subtuple in sublist]))
    return result


def GetLagrangeCoefs(RawX: 'list', RawY: 'list'):
    '''
    This function finds coefficients of Lagrange polynomial
    '''
    Size = len(RawX)
    Polynomial = [0] * Size
    Constants = [CalculateK(i, RawX, y) for i, y in enumerate(RawY)]
    for i in range(Size):
        Combinations = [RawX[j] for j in range(Size) if j != i]
        tmp = MultiplyAllSubcombs(Combinations, Size)
        for j, val in enumerate(tmp):
            Polynomial[j] += Constants[i] * val
    for i, coef in enumerate(Polynomial):
        Polynomial[i] = round(coef, 5) if coef != -0.0 else 0.0
    return Polynomial


def Lagrange(XPoints, YPoints, X):
    '''
    Finds Y value in X point by Lagrange polynomial
    '''
    DesiredValue = 0; L = 1
    for c in range(len(YPoints)):
        for p in range(len(XPoints)):
            if(c == p): continue
            L *= (X - XPoints[p])/(XPoints[c] - XPoints[p])
        DesiredValue += YPoints[c] * L
        L = 1
    return DesiredValue


def GetPolynomial(Coefficients: 'list'):
    '''
    Returns the polynomial in a human language form
    '''
    Formula = str()
    for deg, coef in zip(range(len(Coefficients)-1, -1, -1), Coefficients):
        if coef == 0:
            continue
        elif coef == 1:
            if deg == 0:
                Formula += f'1 '
            elif deg == 1:
                Formula += f'x '
            else:
                Formula += f'x^{deg} '
        else:
            if deg == 0:
                Formula += f'{coef} '
            elif deg == 1:
                Formula += f'{coef}x '
            else:
                Formula += f'{coef}x^{deg} '
    Formula = list(Formula)
    Formula.pop()
    for i in range(len(Formula)-1):
        if Formula[i] == ' ' and Formula[i+1] != '-':
            Formula[i] = '+'
    return ''.join(Formula).replace(' -', ' - ').replace('+', ' + ')
