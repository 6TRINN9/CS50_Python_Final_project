import string

def evaluate_password_strength(password: str) -> int:
    """
    Estimates password complexity on a scale from 0 to 100
    """
    if not password:
        return 0

    score = 0

    # Base score for length
    length = len(password)
    if length >= 8:
        score += 10
    if length >= 12:
        score += 20
    if length >= 16:
        score += 20

    # Score for character variety
    char_categories = [
        (string.ascii_lowercase, 10),
        (string.ascii_uppercase, 10),
        (string.digits, 10),
        (string.punctuation, 10)
    ]
    for char_set, points in char_categories:
        if any(c in char_set for c in password):
            score += points

    if len(set(password)) >= len(password) * 0.8:
        score += 10

    return min(score, 100) # Cap score at 100

