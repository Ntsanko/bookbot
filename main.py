def main():
    path = "books/frankenstein.txt"
    text = get_book_content(path)
    words = word_count(text)
    char_count_list = get_sorted_char_counts(text)
    generate_report(path, words, char_count_list)

def get_book_content(path):
    with open(path) as t:
        return t.read()

def word_count(content):
    return len(content.split())

def get_sorted_char_counts(text):
    char_counts = {c: text.lower().count(c) for c in set(text.lower()) if c.isalpha()}
    return sorted(
        [{"character": k, "count": v} for k, v in char_counts.items()],
        key=lambda x: x["count"],
        reverse=True,
    )

def generate_report(path, word_count, char_count_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words were found in the document\n")
    for count in char_count_list:
        print(f"The '{count['character']}' character was found {count['count']} times")
    print("--- End report ---")

main()
