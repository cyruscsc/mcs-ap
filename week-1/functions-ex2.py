def is_anagram(w1: str, w2: str) -> bool:
    if len(w1) != len(w2): return False
    w1_map = {}
    w2_map = {}
    for i in range(len(w1)):
        c1 = w1[i]
        c2 = w2[i]
        w1_map[c1] = w1_map.get(c1, 0) + 1
        w2_map[c2] = w2_map.get(c2, 0) + 1
    return w1_map == w2_map

def check_anagram() -> None:
    w1 = input('Enter word 1: ').lower()
    w2 = input('Enter word 2: ').lower()
    msg = 'they are anagrams' if is_anagram(w1, w2) else 'they are not anagrams'
    print(msg)

def menu() -> None:
    while True:
        choice = input('Check anagram? (y/n): ').lower()
        match choice:
            case 'y': pass
            case 'n': break
            case _: continue
        check_anagram()
        print()

if __name__ == '__main__':
    menu()