import sys
import secrets

numbers = []

def main():
    menu()

    try:
        selection = int(input(f'Type the number to select: '))
        if selection > 0 and selection < 5:
            if selection == 1: megaSena()
            if selection == 2: lotoFacil()
            if selection == 3: lotoMania()
            if selection == 4: quiNa()
        else:
            print(f'invalid number range ( 1 - 4 )\n')
    except Exception as e:
        print(e, '\n')

def menu():
    print(f'1. MEGA SENA')
    print(f'2. LOTO FACIL')
    print(f'3. LOTO MANIA')
    print(f'4. QUI NA')
    print(f'')

def megaSena():
    _games = 1; _rows = 3; _columns = 6; _range = 60
    print(f'MEGA SENA')
    loop(_games, _rows, _columns, _range)
    
def lotoFacil():
    _games = 1; _rows = 4; _columns = 15; _range = 60
    print(f'LOTO FACIL')
    loop(_games, _rows, _columns, _range)
    
def lotoMania():
    _games = 4; _rows = 5; _columns = 11; _range = 99
    print(f'LOTO MANIA')
    loop(_games, _rows, _columns, _range)
    
def quiNa():
    _games = 1; _rows = 4; _columns = 5; _range = 99
    print(f'QUI NA')
    loop(_games, _rows, _columns, _range)
    
def loop(w, x, y, z):
    for k in range(w):
        for j in range(x):
            for i in range( y ):
                numbers.append(secrets.randbelow(z))
            show()
        print('')

def show():
    numbers.sort()
    print(numbers)
    numbers.clear()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()