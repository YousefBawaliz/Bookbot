import stats
import sys

args = sys.argv

if (len(args) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = args[1]

def main():
    content = stats.get_book_text(file_path)

    # content = stats.get_book_text("books/frankenstein.txt")

    # print(stats.count_chars(content))

    # print(stats.convert_to_list_of_dict(stats.count_chars(content)))

    # print(stats.sort_dict(stats.convert_to_list_of_dict(stats.count_chars(content))))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {stats.count_words(content)} total words")
    print("--------- Character Count -------")
    
    sorted_list = stats.sort_dict(stats.convert_to_list_of_dict(stats.count_chars(content)))
    for d in sorted_list:
        print(f"{d["char"]}: {d["num"]}")

main()