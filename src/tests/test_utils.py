import pytest
from src.utils import generate_password, calculate_password_entropy, evaluate_password_strength
import string

class TestGeneratePassword:

    def test_default_length(self):
        password = generate_password()
        assert len(password) == 12

    @pytest.mark.parametrize("length", [4,8,12,16,20])
    def test_custom_length(self, length):
        password = generate_password(length)
        assert len(password) == length

    @pytest.mark.parametrize("lower, upper, digits, specials, expected_chars", [
        (True, False, False, False, string.ascii_lowercase),
        (False, True, False, False, string.ascii_uppercase),
        (False, False, True, False, string.digits),
        (True, True, True, False, string.ascii_lowercase + string.ascii_uppercase + string.digits),
    ])
    def test_only_lowercase(self, lower, upper, digits, specials, expected_chars):
        password = generate_password(16, lower, upper, digits, specials)
        assert all(c in expected_chars for c in password)

    def test_min_len_with_all_types(self):
        password = generate_password(length=4)
        assert len(password) == 4

        assert any(c in string.ascii_lowercase for c in password)
        assert any(c in string.ascii_uppercase for c in password)
        assert any(c in string.digits for c in password)
        assert any(c in string.punctuation for c in password)

    def test_negative_len_error(self):
        with pytest.raises(ValueError):
            generate_password(length=-6)

    def test_zero_len_error(self):
        with pytest.raises(ValueError):
            generate_password(length=0)

    def test_no_char_types_error(self):
        with pytest.raises(ValueError):
            generate_password(use_lowercase=False, use_uppercase=False, use_digits=False, use_specials=False)


class TestEntropy:
    @pytest.mark.parametrize("password, expected_entropy", [
        ("abcde", 23.0),
        ("abc123", 30.0),
        ("A!b2#c", 39.33),
        ("12345678", 26.58),
        ("", 0)
    ])
    def test_calculate_entropy(self, password, expected_entropy):
        entropy = calculate_password_entropy(password)
        assert entropy >= expected_entropy

    def test_calculate_entropy_error_on_none(self):
        with pytest.raises(ValueError, match="Invalid password"):
            calculate_password_entropy(None)

    @pytest.mark.parametrize("entropy, expected_substring", [
        (10, "Pathetic"),
        (40, "Weak"),
        (55, "Good"),
        (70, "Strong"),
        (95, "Strong"),
        (120, "Excellent"),
    ])
    def test_evaluate_strength(self, entropy, expected_substring):
        assert expected_substring in evaluate_password_strength(entropy)