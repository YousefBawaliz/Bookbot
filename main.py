import stats

def main():
    content = stats.get_book_text("books/frankenstein.txt")
    # print(f"Found {count_words(content)} total words")

    # print(stats.count_chars(content))

    # print(stats.convert_to_list_of_dict(stats.count_chars(content)))

    print(stats.sort_dict(stats.convert_to_list_of_dict(stats.count_chars(content))))

main()