book_path = "./books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    num_of_letters = count_letters(text)
    print(f'--- Begin report of {book_path} ---')
    print(f'{number_of_words} words in text file')
    letter_report(num_of_letters)
    print("--- End report ---")

def get_book_text(path):
    with open(book_path) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(file):
    words = file.split()
    return len(words)

def count_letters(file):
    string = file
    l_string = string.lower()
    char_dict = {}
    char_compare = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    for letter in l_string:
        if letter in char_compare:
            char_dict[letter] = char_dict.get(letter, 0) + 1
    # sort dict by value, reversed.
    char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return char_dict

def letter_report(dict):
    for item in dict.items():
        print(f'The {item[0]} character was found {item[1]} times')
main()