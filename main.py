from stats import get_book_text, get_char_dict, sorted_char_list

book_path = "books/frankenstein.txt"
count, book_content = get_book_text(book_path)
characters = get_char_dict(book_content)
char_list = sorted_char_list(characters)
print(char_list)
