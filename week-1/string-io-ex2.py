def draw_triangle(style: int) -> None:
    label = None
    match style:
        case 0:
            for i in range(1, 5):
                line = f'{"*" * i}'
                print(line.ljust(4, ' ').center(10, ' '))
            print('left-sided'.center(10, ' '))
        case 1:
            for i in range(1, 5):
                line = f'{"*" * i}'
                print(line.rjust(4, ' ').center(10, ' '))
            print('right-sided'.center(10, ' '))
        case 2:
            i = 1
            n = 1
            while n > 0:
                line = f'{"*" * n}'
                print(line.center(5, ' ').center(10, ' '))
                n += 2 if i < 3 else -2
                i += 1
            print('diamond'.center(10, ' '))
        case _: raise ValueError

def menu() -> None:
    while True:
        print('Draw a triangle!\n0. left-sided\n1. right-sided\n2. diamond')
        choice = input('Enter style number or "x" to exit: ')
        if choice == 'x': break
        try:
            integer = int(choice)
            draw_triangle(integer)
        except:
            print('Invalid value')
        finally:
            print()

if __name__ == '__main__':
    menu()