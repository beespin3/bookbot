def get_word_count(book_text):
    word_list = book_text.split()
    count = len(word_list)
    return count

def count_characters(book_text):
    char_dict = {}
    
    for char in book_text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_char_counts(dict):
    pairs = []
    
    # c is char, n is count of char
    for c, n in dict.items():
        new_pair = {}
        
        new_pair["char"] = c
        new_pair["num"] = n
        pairs.append(new_pair)
        
    def sort_on(dict):
        return dict["num"]
    
    pairs.sort(reverse=True, key=sort_on)
    
    return pairs
        
    
        