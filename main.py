from stats import get_number_of_words

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
    Reads the text of 'frankenstein.txt', counts the number of words in the document,
    and prints the total word count to the console.
    """
    book_text = get_book_text("./books/frankenstein.txt")
    number_of_words = get_number_of_words(book_text)
    print(f"{number_of_words} words found in the document")

main()