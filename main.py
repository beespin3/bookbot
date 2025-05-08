import sys

from stats import get_word_count
from stats import count_characters
from stats import sort_char_counts

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(f):
        return f.read()
    
def print_report(word_count, list):
    print("============ BOOKBOT ============\n" +
          f"Analyzing book found at {sys.argv[1]}...\n" +
          "----------- Word Count ----------\n" + 
          f"Found {word_count} total words\n" + 
          "--------- Character Count -------")
    
    for pair in list:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")
        else:
            continue
    
    print("============= END ===============")

def main():
     with open(f"{sys.argv[1]}") as f:
        book_text = get_book_text(f)
        word_count = get_word_count(book_text)
        char_dict = count_characters(book_text)
        sorted_chars = sort_char_counts(char_dict)
        
        print_report(word_count, sorted_chars)
        
main()