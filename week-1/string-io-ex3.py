def print_calendar(num_days: int, first_dow: int) -> None:
    heading = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    print(format_line(heading))
    day = 1
    while day <= num_days:
        week = [''] * 7
        start = first_dow if day == 1 else 0
        for i in range(start, 7):
            week[i] = day
            day += 1
            if day > num_days: break
        print(format_line(week))

def format_line(vals: list) -> str:
    if len(vals) != 7: raise ValueError
    template = '  '.join(['{{{0}:>2}}'.format(i) for i in range(7)])
    return template.format(*vals)

def run() -> None:
    while True:
        choice = input('Print calendar? (y/n): ')
        match str(choice).lower():
            case 'y': pass
            case 'n': break
            case _: continue
        try:
            num_days = int(input('Enter number of days: '))
            if num_days < 28 or num_days > 31: raise ValueError
            first_dow = int(input('Enter first day of week (0-6): '))
            if first_dow < 0 or first_dow > 6: raise ValueError
            print_calendar(int(num_days), int(first_dow))
        except:
            print('Invalid values')
        finally:
            print()

if __name__ == '__main__':
    run()