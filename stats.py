def get_book_text(book_path):
    with open(book_path) as book:
        book_content = book.read()
        words = book_content.split()
        count = len(words)
        print(f"Found {count} total words")
        return count, book_content


def get_char_dict(text):
    chars = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1
    return chars


def sort_on(d):
    return d["num"]


def sorted_char_list(chars):
    sorted_list = []
    for char in chars:
        sorted_list.append({"char": char, "num": chars[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
