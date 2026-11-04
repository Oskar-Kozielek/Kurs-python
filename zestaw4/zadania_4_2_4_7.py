def make_ruler(n):
    if n < 0:
        raise ValueError("Długość miarki nie może być ujemna.")

    bars = "|" + "|".join("...." for _ in range(n)) + "|"
    numbers = "0" + "".join(str(i).rjust(5) for i in range(1, n + 1))

    return bars + "\n" + numbers


def make_grid(rows, cols):
    if rows < 0 or cols < 0:
        raise ValueError("Liczby kolumn i wierszy muszą być nieujemne.")

    horizontal = "+" + "+".join("---" for _ in range(cols)) + "+"
    empty_row = "|" + "|".join("   " for _ in range(cols)) + "|"

    lines = [horizontal]
    for _ in range(rows):
        lines.append(empty_row)
        lines.append(horizontal)
    return "\n".join(lines)


def factorial(n):
    if n < 0:
        raise ValueError("n musi być liczbą nieujemną.")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n < 0:
        raise ValueError("n musi być liczbą nieujemną.")

    if n in (0, 1):
        return n

    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current


def odwracanie(L, left, right):
    if not isinstance(L, list):
        raise TypeError("L musi być listą.")
    if not (0 <= left <= right < len(L)):
        raise ValueError("Nieprawidłowe indeksy left i right.")

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return L


def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        else:
            total += item
    return total


def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def run_tests():
    assert make_ruler(12).startswith("|....|....|....|....|....|....|....|....|....|....|....|....|")
    assert "0    1    2    3    4    5    6    7    8    9   10   11   12" in make_ruler(12)

    grid = make_grid(2, 4)
    assert grid.startswith("+---+---+---+---+")
    assert "|   |   |   |   |\n+---+---+---+---+\n|   |   |   |   |" in grid

    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(7) == 13
    assert fibonacci(10) == 55

    L = [1, 2, 3, 4, 5, 6]
    assert odwracanie(L, 1, 4) == [1, 5, 4, 3, 2, 6]

    L2 = [10, 20, 30, 40]
    odwracanie(L2, 0, 3)
    assert L2 == [40, 30, 20, 10]

    L3 = [10, 20, 30, 40]
    odwracanie(L3, 0, 2)
    assert L3 == [30, 20, 10, 40]

    assert sum_seq([1, 2, [3, 4], (5, [6, 7])]) == 28
    assert sum_seq([]) == 0
    assert sum_seq([1, (2, 3), [4, (5, 6)]]) == 21

    sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    assert flatten(sequence) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten([[], [1, (2, [3, 4])], 5]) == [1, 2, 3, 4, 5]


def show_demo_outputs():
    print("\n--- Zadanie 4.2: make_ruler ---")
    print(make_ruler(12))

    print("\n--- Zadanie 4.2: make_grid ---")
    print(make_grid(2, 4))

    print("\n--- Zadanie 4.3: factorial ---")
    print(factorial(7))

    print("\n--- Zadanie 4.4: fibonacci ---")
    print(fibonacci(10))

    print("\n--- Zadanie 4.5: odwracanie ---")
    lista = [1, 2, 3, 4, 5, 6]
    print(odwracanie(lista, 1, 4))

    print("\n--- Zadanie 4.6: sum_seq ---")
    print(sum_seq([1, 2, [3, 4], (5, [6, 7])]))

    print("\n--- Zadanie 4.7: flatten ---")
    sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    print(flatten(sequence))


if __name__ == "__main__":
    run_tests()
    show_demo_outputs()
    print("\nWszystkie zadania z zestawu 4 przeszły pomyślnie.")
