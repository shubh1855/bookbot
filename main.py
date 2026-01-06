def get_book_text():
    with open("books/frankenstein.txt") as book:
        book_content = book.read()
        print(book_content)


get_book_text()
