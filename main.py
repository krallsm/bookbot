
def read_file():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents

def count_words():
    file_contents = read_file()
    words = file_contents.split()
    number_of_words = len(words)
    return(number_of_words)

def count_characters():
    file_contents = read_file()
    lowered_string = file_contents.lower()
    char_count = {}
    for char in lowered_string:
        if char in lowered_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return(char_count)

def alpha_characters():
    char_count = count_characters()
    alpha_char_count = {char: count for char, count in char_count.items() if char.isalpha()}
    return alpha_char_count

def convert_dict_to_list():
    char_count = alpha_characters()
    char_list = [{"character": char, "count": count} for char, count in char_count.items()]
    return char_list

def generate_report():
    char_list = convert_dict_to_list()
    number_of_words = count_words()

    def sort_on(char_list):
        return char_list["count"]
    char_list.sort(key=sort_on, reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print()
    for item in char_list:
        print(f"The '{item['character']}' character was found {item['count']} times")
    print("--- End report ---")

def main():
    generate_report()

main()