def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def sort_char_dict(chars):
    sorted_list = []
    for ch in chars:
        sorted_list.append({"char": ch, "num": chars[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in document")
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_char_dict(chars_dict)
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"the '{item['char']}' character was found {item['num']} times")
    
    print("--- End Report ---")
    

main()