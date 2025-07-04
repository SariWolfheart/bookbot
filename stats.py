def get_number_of_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def get_number_of_characters(text):
    """
    Counts the occurrences of each character in the given text, ignoring case.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict: A dictionary where keys are lowercase characters from the input text,
              and values are the number of times each character appears.
    """
    characters = {}
    strip_case = text.lower()

    for char in strip_case:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def sort_on(dict):
    return dict["num"]

def get_stats(chardict):

    stats = []


    for char in chardict:
        char_count = chardict[char]
        # if char.isalpha():
        new_dict = {
            "char": char,
            "num": char_count
        }
        stats.append(new_dict)

    stats.sort(reverse=True, key=sort_on)
    return stats
