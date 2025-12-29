def get_num_words(text):
    return len(text.split())


def get_char_counts(book):
    char_counts = {}

    for char in book:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_on(item):
    return item["num"]


def sort_char_counts(char_counts):
    result = []

    for char, count in char_counts.items():
        if not char.isalpha():
            continue

        result.append({
            "char": char,
            "num": count
        })

    result.sort(reverse=True, key=sort_on)
    return result
