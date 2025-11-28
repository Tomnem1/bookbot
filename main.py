from stats import get_words_count, get_char_count, get_sorted_dicts
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    words_count = get_words_count(text)
    char_count = get_sorted_dicts(get_char_count(text))
    
    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {sys.argv[1]}...\n" \
    "----------- Word Count ----------\n" \
    f"Found {words_count} total words\n" \
    "--------- Character Count -------")
    for item in char_count:
        if(item["char"].isalpha() == True):
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
        

        


main()