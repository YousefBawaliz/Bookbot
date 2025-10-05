from typing import Dict


def get_book_text(filepath : str) -> str:
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(txt: str) -> int:
    return len(txt.split())


def count_chars(txt: str) -> float:
    contents: list[str] = txt.split()

    all_letters_count = {}

    for s in contents:
        # letters = s.split()
        for letter in s:
            char = letter.lower()
            # set default num if it doesn't exist
            all_letters_count.setdefault(char, 0)
            all_letters_count[char] += 1
            # all_letters_count[char] = char
            # all_letters_count["num"] +=1


    return all_letters_count


def sort_on(items):
    return items["num"]

def sort_dict(dict):
    return dict.sort(reverse = True, key=sort_on)


def convert_to_list_of_dict(dict) -> list[dict]:
    list_of_dict = []
    for key in dict:
        tmp = {"char" : key , "num": dict[key]}
        list_of_dict.append(tmp)
    return list_of_dict



