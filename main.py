import sys
from stats import get_number_of_words, get_number_of_characters, get_stats

def get_book_text(file_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file_path (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(file_path) as file:
        return file.read()
        
def main():
    """
    Reads the text of a document, counts the number of words in the document,
    and prints the total word count to the console.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    book_text = get_book_text(sys.argv[1])
    number_of_words = get_number_of_words(book_text)
    number_of_characters = get_number_of_characters(book_text)
    book_stats = get_stats(number_of_characters)
    
    
    output = (
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {sys.argv[1]}\n"
        "----------- Word Count ----------\n"
        f"Found {number_of_words} total words\n"
        "--------- Character Count -------\n"
        )

    print(output)

    for stats in book_stats:
        if stats['char'].isalpha():
            print(f"{stats['char']}: {stats['num']}")

    print("============= END ===============")
        
        

main()