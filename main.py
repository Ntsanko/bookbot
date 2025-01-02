def main():
    path = "books/frankenstein.txt"
    text = get_book_content(path)
    words = word_count(text)
    char_count = char_occurrences(text)
    char_count_list = dict_to_list(char_count)
    generate_report(path, words, char_count_list)

def get_book_content(path):
    with open(path) as t:
        return t.read()
    
def dict_to_list(count):
    counts = []
    for k,v in count.items():
        if k.isalpha():
            counts.append({"character": k, "count": v})

    counts.sort(reverse=True, key=sort_on)

    return counts


def sort_on(dict):
    return dict["count"]

def word_count(content):
    return len(content.split())

def char_occurrences(text):
    occurrences = {}
    lowered_text = text.lower()
    for c in lowered_text:
        if c in occurrences:
            occurrences[c] += 1
        else:
            occurrences[c] = 1
    return occurrences

def generate_report(path, word_count, char_count_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words were found in the document")
    print("")
    
    for count in char_count_list:
        print(f"The '{count["character"]}' character was found {count["count"]} times")

    print("--- End report --")

main()