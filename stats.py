def get_words_count(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items["num"]

def get_char_count(text):
    char_dict = {}

    for char in text:
        char = char.lower()
        if(char in char_dict):
            char_dict[char] += 1 
        else:
            char_dict[char] = 1

    return char_dict

def get_sorted_dicts(char_dict):
    char_dict_list = []
    for key in char_dict:
        char_dict_list.append({"char": key, "num": char_dict[key]})
    char_dict_list.sort(reverse=True, key = sort_on)
    return char_dict_list


    
