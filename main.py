from collections import Counter

def print_book():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents


def count_words(file_contents):
    words = file_contents.split()
    print(f"{len(words)} words found in the document")


def count_characters(file_contents):
    file_contents_lowered = file_contents.lower()
    for i in Counter(file_contents_lowered):
        if i.isalpha():
            print(f"The {i} was found {Counter(file_contents_lowered)[i]} times in the document")


def main():
    print("--- Begin report of books/frankenstein.txt ---\n")
    file_contents = print_book()
    count_words(file_contents)
    count_characters(file_contents)
    print("\n--- End of report ---")


if __name__ == "__main__":
    main()

