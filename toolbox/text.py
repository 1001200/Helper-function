"""Text helpers. The worked example every contribution is modelled on."""


def word_count(text):
    """Count whitespace-separated words.

    >>> word_count("one two three")
    3
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())


def truncate(text, limit, suffix="..."):
    """Shorten text to limit characters, ending with suffix.

    The result is never longer than limit.

    >>> truncate("hello world", 8)
    'hello...'
    >>> truncate("short", 20)
    'short'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if limit < len(suffix):
        raise ValueError("limit must be at least len(suffix)")
    if len(text) <= limit:
        return text
    return text[:limit - len(suffix)] + suffix


def character_count(text):
    """Count the number of characters in text.

    >>> character_count("hello")
    5
    >>> character_count("hello world")
    11
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text)


def capitalize_words(text):
    """Capitalize the first letter of every word.

    >>> capitalize_words("hello world")
    'Hello World'
    >>> capitalize_words("python is fun")
    'Python Is Fun'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text.title()