def get_book_text(book_path):
    with open(book_path) as book:
        book_content = book.read()
        words = book_content.split()
        count = len(words)
        print(f"Found {count} total words")
