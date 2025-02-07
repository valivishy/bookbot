from curses.ascii import isalpha


def open_book(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()


def count_words(content: str) -> int:
    return len(content.split())


def count_symbols(content: str) -> dict:
    result = {}

    for symbol in content:
        value = symbol.lower()
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result


def count_alphabetic(content: str) -> list:
    result = {}

    for symbol in list(map(str.lower, list(filter(isalpha, content)))):
        value = symbol.lower()
        if value in result:
            result[value] += 1
        else:
            result[value] = 1

    return sorted(result.items(), key=lambda x: x[1], reverse=True)


def print_report(source: str, content: str) -> str:
    counter_alphabetic = count_alphabetic(content)

    print(f"--- Begin report of {source} ---")
    print(f"{count_words(content)} words found in the document")
    print()
    for letter, count in counter_alphabetic:
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def main():
    source = "books/frankenstein.txt"
    file_contents = open_book(source)
    # print(file_contents)
    # print(count_words(file_contents))
    # print(count_symbols(file_contents))

    print_report(source, file_contents)


main()
