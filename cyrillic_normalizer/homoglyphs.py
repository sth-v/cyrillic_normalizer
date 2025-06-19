
latin_to_cyrillic={"A":"А","a":"а","B":"В","E":"Е","e":"е","K":"К","k":"к","M":"М","O":"О","o":"о","P":"Р","p":"р","C":"С","c":"с","T":"Т","H":"Н","h":"н","X":"Х","x":"х","Y":"У","y":"у","I":"І","i":"і","J":"Ј","S":"Ѕ"}
cyrillic_to_latin={v:k for k,v in latin_to_cyrillic.items()}

def fix_homoglyphs_cyrillic(text: str) -> str:
    """
    
    :param text: A string containing a mixed set of cyrillic and latin characters.
    :return: A string containing only cyrillic characters (if possible).
    
    Example:
    --------
    >>> crazy_input="Веc" # latin 'c'
    >>> crazy_input[0].encode()
    b'\xd0\x92' # Ok
    >>> crazy_input[1].encode()
    b'\xd0\xb5' # Ok
    >>> crazy_input[2].encode()
    b'c' # Error (latin 'c')
    >>> fine_output=fix_homoglyphs_cyrillic(crazy_input)
    >>> fine_output
    'Вес'
    >>> fine_output[2].encode()
    b'\xd1\x81' # Ok
    >>> crazy_input == fine_output
    False

    """
    return text.translate(str.maketrans(latin_to_cyrillic))


def fix_homoglyphs_latin(text: str) -> str:
    """

    :param text: A string containing a mixed set of latin and cyrillic characters.
    :return: A string containing only latin characters (if possible).

    Example:
    --------
    >>> crazy_input="Аrea" # cyrillic 'А'
    >>> crazy_input[0].encode()
    b'\xd0\x90'  # Error (cyrillic 'А')
    >>> crazy_input[1].encode()
    b'r' # Ok
    >>> crazy_input[2].encode()
    b'e' # Ok
    >>> crazy_input[3].encode()
    b'a' # Ok

    >>> fine_output=fix_homoglyphs_latin(crazy_input)
    >>> fine_output
    'Area'
    >>> fine_output[0].encode()
    b'A' # Ok
    >>> crazy_input == fine_output
    False
    
    """
    return text.translate(str.maketrans(cyrillic_to_latin))
