import sys
from stats import word_count, character_count, sort_character


def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
take_dict = character_count(get_book_text(book_path))
# print(take_dict)


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    # print(book_text)
    print(
        "============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt..."
    )

    print("----------- Word Count ----------")
    print(f"Word count: Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    sorted_chars = sort_character(take_dict)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
