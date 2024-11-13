class SalesTable:
    def __init__(self, data: dict[str, list[int]], key_map: dict[str, str], idx_map: dict[int, str]):
        self._data = data
        self._key_map = key_map
        self._idx_map = idx_map
    
    @property
    def data(self) -> dict[str, list[int]]:
        return self._data
    
    @property
    def key_map(self) -> dict[str, str]:
        return self._key_map
    
    @property
    def idx_map(self) -> dict[int, str]:
        return self._idx_map
    
    def __sum(self, vals: list[int]) -> int:
        return sum(vals)
    
    def __avg(self, vals: list[int]) -> int:
        return int(sum(vals) / len(vals))
    
    def print_report(self) -> None:
        row_template = '{0:>10} | {1:>10} | {2:>10}'
        print('Quarterly sales report')
        print()
        print(row_template.format('City', 'Total', 'Average'))
        for key, val in self.data.items():
            print(row_template.format(self.key_map[key], self.__sum(val), self.__avg(val)))
        print()
        print(row_template.format('Month', 'Total', 'Average'))
        for key, val in self.idx_map.items():
            monthly_sales = [sales[key] for city, sales in self.data.items()]
            monthly_total = self.__sum(monthly_sales)
            monthly_average = self.__avg(monthly_sales)
            print(row_template.format(self.idx_map[key], monthly_total, monthly_average))
        
sales_data = {
    'L3': [390, 345, 379],
    'P2': [250, 270, 300],
    'N6': [460, 480, 450],
    'B8': [470, 510, 360],
}

key_mappings = {
    'L3': 'London',
    'P2': 'Paris',
    'N6': 'New York',
    'B8': 'Beijing',
}

index_mappings = {
    0: 'Apr 18',
    1: 'May 18',
    2: 'Jun 18',
}

def menu() -> None:
    st = SalesTable(sales_data, key_mappings, index_mappings)
    while True:
        print('Select an action...\n0. view sales data\n1. view key mappings\n2. view index mappings\n3. print report\nx. exit')
        choice = input('Enter number of action: ')
        match str(choice):
            case '0': print(st.data)
            case '1': print(st.key_map)
            case '2': print(st.idx_map)
            case '3': st.print_report()
            case 'x': break
            case _: print('Invalid input')
        print()

if __name__ == '__main__':
    menu()