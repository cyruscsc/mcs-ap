def even_mul_table(multiplicand: int) -> None:
    print(f'The even timetable for {multiplicand} is:')
    for i in range(1, 11):
        multiplier = i * 2
        product = multiplier * multiplicand
        message = '{0:2d} times {1:2d} is {2:4d}'.format(multiplier, multiplicand, product)
        print(message.center(30, ' '))

def run() -> None:
    while True:
        choice = input('Enter an integer (0 < x < 100, or "x" to exit): ')
        if choice == 'x': break
        try:
            integer = int(choice)
            if integer < 1 or integer > 99: raise ValueError
        except:
            print('Invalid input')
        else:
            even_mul_table(integer)
        finally:
            print()

if __name__ == "__main__":
    run()