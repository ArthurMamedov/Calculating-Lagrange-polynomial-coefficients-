from modules import Dispenser, GetLagrangeCoefs, GetPolynomial, Lagrange
from colorama import Fore as fr
from sys import argv


try:
    RawX = input(f'{fr.GREEN}Enter X points: {fr.RESET}')
    RawY = input(f'{fr.GREEN}Enter Y points: {fr.RESET}')
    RawX = Dispenser(RawX)
    RawY = Dispenser(RawY)

    if len(RawX) != len(RawY):
        raise RuntimeError('The number of X points is not equal to the number of Y points')

    Polynomial = GetPolynomial(GetLagrangeCoefs(RawX, RawY))
    print(f'Polynomial is {fr.LIGHTBLUE_EX}{Polynomial}{fr.RESET}')

    while True:
        X = float(input('Enter the X: '))
        
        formula_val = Polynomial.replace('^', '**').replace('x', '*(x)').replace('x', str(X))
        formula_val = eval(formula_val if formula_val[0] != '*' else '1'+formula_val)
        
        if len(argv) > 1 and argv[1] == '/cmp':
            calc_val = Lagrange(RawX, RawY, X)
            print(f'Value got with formula:                  {fr.GREEN}{round(formula_val, 5)}{fr.RESET}')
            print(f'Value got with brute force calculations: {fr.GREEN}{round(calc_val, 5)}{fr.RESET}')
        else:
            print(f'Function value is {fr.GREEN}{formula_val}{fr.RESET}')

except RuntimeError as rm:
    print(f'\n{fr.RED}{rm}{fr.RESET}')
except KeyboardInterrupt:
    print(f'\n{fr.RED}Program finished...{fr.RESET}')
except ValueError:
    print(f'\n{fr.RED}Wrong data got{fr.RESET}')
except:
    print(f'\n{fr.RED}Something went wrong{fr.RESET}')
