def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = len(text.split())