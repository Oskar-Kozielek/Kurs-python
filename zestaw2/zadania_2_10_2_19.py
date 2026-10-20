def count_words(line):
    return len(line.split())


def underscore_word(word):
    return "_".join(word)


def first_and_last_letters(line):
    words = line.split()
    first = "".join(word[0] for word in words)
    last = "".join(word[-1] for word in words)
    return first, last

def total_word_length(line):
    return sum(len(word) for word in line.split())


def longest_word(line):
    words = line.split()
    if not words:
        return "", 0
    longest = max(words, key=len)
    return longest, len(longest)


def number_string_from_list(L):
    return "".join(str(number) for number in L)


def replace_gvr(line):
    return line.replace("GvR", "Guido van Rossum")


def sort_words(line):
    words = line.split()
    return sorted(words), sorted(words, key=len)

def count_zero_digits(number):
    return str(abs(number)).count("0")


def pad_three_digit_blocks(L):
    return "".join(str(number).zfill(3) for number in L)


def run_tests():
    assert count_words("Ala ma kota i psa") == 5
    assert count_words("Ala\tma\nkota   psa") == 4
    assert count_words('''Ala
    ma
    kota 
    i
    psa''') == 5 

    assert underscore_word("python") == "p_y_t_h_o_n"
    assert underscore_word("word") == "w_o_r_d"

    first_chars, last_chars = first_and_last_letters("python jest super")
    assert first_chars == "pjs"
    assert last_chars == "ntr"

    assert total_word_length("python jest super") == 15
    assert total_word_length("Ala ma kota") == 9

    assert longest_word("python jest super") == ("python", 6)
    assert longest_word("to jest krótki tekst") == ("krótki", 6)

    assert number_string_from_list([12, 34, 5]) == "12345"
    assert number_string_from_list([7, 8, 9]) == "789"

    assert replace_gvr("GvR jest twórcą Pythona") == "Guido van Rossum jest twórcą Pythona"
    assert replace_gvr("GvR GvR") == "Guido van Rossum Guido van Rossum"

    alphabetic, by_length = sort_words("kot pies myszka arka")
    assert alphabetic == ["arka", "kot", "myszka", "pies"]
    assert by_length == ["kot", "pies", "arka", "myszka"]

    assert count_zero_digits(100230) == 3
    assert count_zero_digits(909) == 1

    assert pad_three_digit_blocks([7, 24, 123]) == "007024123"
    assert pad_three_digit_blocks([12, 3, 99]) == "012003099"


if __name__ == "__main__":
    run_tests()
    print("Wszystkie testy dla zadań 2.10-2.19 przeszły pomyślnie.")
