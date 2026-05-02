import secrets
import string
from math import log2

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_specials=True) -> string:
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
    if use_lowercase:
        char_types.append(string.ascii_lowercase)
    if use_uppercase:
        char_types.append(string.ascii_uppercase)
    if use_digits:
        char_types.append(string.digits)
    if use_specials:
        char_types.append(string.punctuation)

    # Check, if have some chars
    if not char_types:
        raise ValueError("At least one character type must be selected!")

    all_chars = ''.join(char_types)

    # Ensure minimum length for required character types
    required_types_count = sum([use_lowercase, use_uppercase, use_digits, use_specials])
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

def evaluate_password_strength(entropy) -> string:
    """
    Evaluates password strength based on entropy
    """
    match entropy:
        case entropy if entropy <= 20:
            return "Strength: Pathetic"
        case entropy if 20 < entropy < 50:
            return "Strength: Pathetic"
        case entropy if 50 <= entropy <= 60:
            return "Strength: Pathetic"
        case entropy if 60 < entropy < 100:
            return "Strength: Strong"
        case entropy if entropy > 100:
            return "Strength: Excellent"

def calculate_password_entropy(password = None) -> int:
    """
    Calculates entropy by dynamically determining the character set.
    Only considers characters actually present in the password.
    """

    if password is None:
        raise ValueError(f"Invalid password '{password}' for calculate entropy!")
    
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digits = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)

    N = 0

    char_categories = [
        (string.ascii_lowercase, 26),
        (string.ascii_uppercase, 26),
        (string.digits, 10),
        (string.punctuation, len(string.punctuation))
    ]
    for char_set, points in char_categories:
        if any(c in char_set for c in password):
            N += points
    
    L = len(password)
    entropy = L * log2(N) if N > 0 else 0
    return round(entropy, 2)

