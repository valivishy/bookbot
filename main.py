import sys
from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)


def main():
    if len(sys.argv) < 2:

        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in the document")
        print()

        for item in chars_sorted_list:
            if not item["char"].isalpha():
                continue
            print(f"The '{item['char']}' character was found {item['num']} times")

        print("--- End report ---")
    else:
        book_path = sys.argv[1]

        text = get_book_text(book_path)
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
        print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
