import secrets
import string

def generate_password(length=12, use_letters=True, use_digits=True, use_specials=True) -> string:
    """
    Generates a random password with the given parameters.

    Arguments:
    length (int): Length of the length.
    use_letters (bool): Use letters.
    use_digits (bool): Use numbers.
    use_special (bool): Use special characters.

    Return:
    str: Generated password.
    """
    similar_chars = "il1Lo0O"

    if length <= 0:
        raise ValueError("Password length must be greater than 0!")

    # A set of characters is generated based on the parameters
    char_types = []
    if use_letters:
        char_types.append(string.ascii_uppercase)
        char_types.append(string.ascii_lowercase)
    if use_digits:
        char_types.append(string.digits)
    if use_specials:
        char_types.append(string.punctuation)

    # Check, if have some chars
    if not char_types:
        raise ValueError("At least one character type must be selected!")

    all_chars = ''.join(char_types)

    # Ensure minimum length for required character types
    required_types_count = sum([use_letters, use_digits, use_specials])
    if length < required_types_count:
        raise ValueError(f"Password length ({length}) is too small to include all selected character types ({required_types_count})!")

    # Generating password
    password_chars = []

    # Append one char of each type
    for char_set in char_types:
        password_chars.append(secrets.choice(char_set))

    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.extend(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)




