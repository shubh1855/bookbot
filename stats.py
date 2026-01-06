def get_book_text():
    with open("books/frankenstein.txt") as book:
        book_content = book.read()
        words = book_content.split()
        count = 0
        for word in words:
            count += 1
        print(f"Found {count} total words")


get_book_text()
