def reverse_text(text):
    """Reverse the given text.

    >>> reverse_text("hello")
    'olleh'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text[::-1]


def capitalize_words(text):
    """Capitalize the first letter of each word.

    >>> capitalize_words("hello world")
    'Hello World'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text.title()


def remove_extra_spaces(text):
    """Remove extra spaces from the text.

    >>> remove_extra_spaces("  hello   world  ")
    'hello world'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(text.split())


def is_palindrome(text):
    """Check whether the text is a palindrome.

    >>> is_palindrome("madam")
    True
    >>> is_palindrome("hello")
    False
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]