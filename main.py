from stats import get_book_text, get_char_dict, sorted_char_list

book_path = "books/frankenstein.txt"
count, book_content = get_book_text(book_path)
characters = get_char_dict(book_content)
char_list = sorted_char_list(characters)

print(f"---- Begin report of {book_path}")
print(f"Found {count} total words in the book")
for item in char_list:
    if not item["char"].isalpha():
        continue
    print(f"{item['char']}: {item['num']}")
print("----END of Report----")
