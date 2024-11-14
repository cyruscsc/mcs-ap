def analyze_text(text: str) -> None:
    char_map = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0,
        'other': 0,
        'space': 0,
    }
    line_template = '{0:<6}: {1:>3} | {2}'
    n_char = len(text)
    histo_symbol = '*'
    for c in text.lower():
        if c in char_map.keys(): char_map[c] += 1
        elif c == ' ': char_map['space'] += 1
        else: char_map['other'] += 1
    for k, v in char_map.items():
        print(line_template.format(k, v, histo_symbol * v))
    print(line_template.format('total', n_char, histo_symbol * n_char))

def menu() -> None:
    while True:
        content = input('Exter a sentence or "x" to exit: ')
        if content.lower() == 'x': break
        analyze_text(content)
        print()

if __name__ == '__main__':
    menu()