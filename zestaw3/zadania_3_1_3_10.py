def zadanie_3_3_for(limit=30):
    return [i for i in range(limit + 1) if i % 3 != 0]


def zadanie_3_3_while(limit=30):
    result = []
    i = 0
    while i <= limit:
        if i % 3 != 0:
            result.append(i)
        i += 1
    return result


def zadanie_3_4(entries):
    wyniki = []

    for entry in entries:
        if entry == "stop":
            break

        try:
            x = float(entry)
        except ValueError:
            print("Błąd: wpisana wartość nie jest liczbą rzeczywistą.")
            continue

        wyniki.append((x, x ** 3))

    return wyniki
def zadanie_3_5(length):
    if length < 0:
        raise ValueError("Długość miarki nie może być ujemna.")

    bars = "|" + "|".join("...." for _ in range(length)) + "|"
    numbers = "0" + "".join(str(i).rjust(5) for i in range(1, length + 1))

    return bars + "\n" + numbers


def zadanie_3_6(columns, rows):
    if columns < 0 or rows < 0:
        raise ValueError("Liczby kolumn i wierszy muszą być nieujemne.")

    horizontal = "+" + "+".join("---" for _ in range(columns)) + "+"
    empty_row = "|" + "|".join("   " for _ in range(columns)) + "|"

    lines = [horizontal]
    for _ in range(rows):
        lines.append(empty_row)
        lines.append(horizontal)
    return "\n".join(lines)


def zadanie_3_8(seq1, seq2):
    common = list(dict.fromkeys(x for x in seq1 if x in seq2))
    total = list(dict.fromkeys(list(seq1) + list(seq2)))
    return common, total


def zadanie_3_9(sequences):
    return [sum(seq) for seq in sequences]


def zadanie_3_10():
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }


    #Inne sposoby tworzenia słownika:
    roman_dict2 = dict(zip("IVXLCDM", [1, 5, 10, 50, 100, 500, 1000]))
    roman_dict3 = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)])
    roman_dict4 = {k: v for k, v in zip("IVXLCDM", [1, 5, 10, 50, 100, 500, 1000])}
    roman_dict5 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

    return roman_dict


def roman2int(roman):
    roman_dict = zadanie_3_10()
    total = 0
    prev = 0
    for ch in reversed(roman):
        value = roman_dict[ch]
        if value < prev:
            total -= value
        else:
            total += value
            prev = value
    return total



def run_tests():
    assert zadanie_3_3_for(30) == [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]
    assert zadanie_3_3_while(30) == [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]

    wynik = zadanie_3_4(["2", "3.5", "abc", "stop", "9"])
    assert wynik[0] == (2.0, 8.0)
    assert wynik[1] == (3.5, 42.875)
    assert wynik == [(2.0, 8.0), (3.5, 42.875)]

    ruler = zadanie_3_5(12)
    assert "|....|....|....|....|....|....|....|....|....|....|....|....|" in ruler
    assert "0    1    2    3    4    5    6    7    8    9   10   11   12" in ruler

    rect = zadanie_3_6(4, 2)
    assert rect.startswith("+---+---+---+---+")
    assert "|   |   |   |   |\n+---+---+---+---+\n|   |   |   |   |" in rect

    common, total = zadanie_3_8([1, 2, 3, 4, 5], [3, 4, 5, 6])
    assert common == [3, 4, 5]
    assert total == [1, 2, 3, 4, 5, 6]

    assert zadanie_3_9([[], [4], (1, 2), [3, 4], (5, 6, 7)]) == [0, 4, 3, 7, 18]

    roman_dict = zadanie_3_10()
    assert roman_dict["X"] == 10
    assert roman2int("XIV") == 14
    assert roman2int("MCMXCIV") == 1994


def show_demo_outputs():
    print("\n--- Zadanie 3.3 (for) ---")
    print(zadanie_3_3_for(30))

    print("\n--- Zadanie 3.3 (while) ---")
    print(zadanie_3_3_while(30))

    print("\n--- Zadanie 3.4 ---")
    print(zadanie_3_4(["2", "3.5", "abc", "stop", "9"]))

    print("\n--- Zadanie 3.5 ---")
    print(zadanie_3_5(12))

    print("\n--- Zadanie 3.6 ---")
    print(zadanie_3_6(4, 2))

    print("\n--- Zadanie 3.8 ---")
    print(zadanie_3_8([1, 2, 3, 4, 5], [3, 4, 5, 6]))

    print("\n--- Zadanie 3.9 ---")
    print(zadanie_3_9([[], [4], (1, 2), [3, 4], (5, 6, 7)]))

    roman_dict = zadanie_3_10()
    print("\n--- Zadanie 3.10 - słownik ---")
    print(roman_dict)
    print("\n--- Zadanie 3.10 - konwersja ---")
    print({"XIV": roman2int("XIV"), "MCMXCIV": roman2int("MCMXCIV")})


if __name__ == "__main__":
    run_tests()
    show_demo_outputs()
    print("\nWszystkie zadania z zestawu 3 przeszły pomyślnie.")
