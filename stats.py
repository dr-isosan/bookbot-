def word_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    character_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    return character_dict


def sort_on(items):
    return items["num"]


def sort_character(char_dict):
    # Build list of dicts and sort by 'num' descending
    sorted_list = []
    for char, count in char_dict.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
