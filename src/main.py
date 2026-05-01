from generator import generate_password
from utils import evaluate_password_strength

def main():

    password = generate_password(24, True, True, True)
    strength = evaluate_password_strength(password)

    print(f"Base password (12 symbols): {password}")
    print(f"Strength password: {strength}/100")


if __name__ == "__main__":
    main()
