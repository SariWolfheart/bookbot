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
    print(get_book_text("./books/frankenstein.txt"))

main()
