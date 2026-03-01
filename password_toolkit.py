import re
import math
import getpass
import random
import string
import time


# ==============================
# Constants
# ==============================

MIN_LENGTH = 8
RECOMMENDED_LENGTH = 16

CHAR_POOLS = {
    "lowercase": 26,
    "uppercase": 26,
    "digits": 10,
    "special": 32
}

ATTACK_SPEEDS = {
    "Online attack (rate limited)": 1_000,
    "Online attack (no limit)": 100_000,
    "Offline GPU attack": 1_000_000_000,
    "Supercomputer attack": 100_000_000_000
}


# ==============================
# Load common passwords
# ==============================

def load_common_passwords():

    try:
        with open("common_passwords.txt", "r") as file:
            return set(line.strip().lower() for line in file)
    except FileNotFoundError:
        return set()


COMMON_PASSWORDS = load_common_passwords()


# ==============================
# Entropy calculation
# ==============================

def calculate_entropy(password):

    pool_size = 0

    if re.search(r"[a-z]", password):
        pool_size += CHAR_POOLS["lowercase"]

    if re.search(r"[A-Z]", password):
        pool_size += CHAR_POOLS["uppercase"]

    if re.search(r"[0-9]", password):
        pool_size += CHAR_POOLS["digits"]

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        pool_size += CHAR_POOLS["special"]

    if pool_size == 0:
        return 0

    entropy = len(password) * math.log2(pool_size)

    return entropy


# ==============================
# Crack time estimation
# ==============================

def estimate_crack_time(entropy):

    results = {}

    combinations = 2 ** entropy

    for attack_type, speed in ATTACK_SPEEDS.items():

        seconds = combinations / speed

        if seconds < 60:
            time_str = f"{seconds:.2f} seconds"
        elif seconds < 3600:
            time_str = f"{seconds/60:.2f} minutes"
        elif seconds < 86400:
            time_str = f"{seconds/3600:.2f} hours"
        elif seconds < 31536000:
            time_str = f"{seconds/86400:.2f} days"
        elif seconds < 31536000 * 1000:
            time_str = f"{seconds/31536000:.2f} years"
        else:
            time_str = "millions of years"

        results[attack_type] = time_str

    return results


# ==============================
# Strength scoring
# ==============================

def calculate_score(password):

    score = 0
    feedback = []

    length = len(password)

    # Blacklist check
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["Password found in common password database"]

    # Length scoring
    if length >= RECOMMENDED_LENGTH:
        score += 35
    elif length >= 12:
        score += 25
        feedback.append("Increase length to 16+ characters")
    elif length >= MIN_LENGTH:
        score += 15
        feedback.append("Increase length to at least 12–16 characters")
    else:
        feedback.append("Password too short")

    # Character diversity scoring
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[0-9]", password):
        score += 15
    else:
        feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        feedback.append("Add special characters")

    return min(score, 100), feedback


# ==============================
# Password generator
# ==============================

def generate_password(length=16):

    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        "!@#$%^&*()"
    )

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


# ==============================
# Strength classification
# ==============================

def classify_strength(score):

    if score >= 90:
        return "VERY STRONG"
    elif score >= 70:
        return "STRONG"
    elif score >= 50:
        return "MODERATE"
    else:
        return "WEAK"


# ==============================
# UI Functions
# ==============================

def show_banner():

    print("="*60)
    print("PASSWORD SECURITY TOOLKIT")
    print("Cybersecurity Password Strength Analyzer")
    print("="*60)


def show_progress():

    print("Analyzing password", end="")

    for _ in range(15):
        print(".", end="", flush=True)
        time.sleep(0.03)

    print("\n")


# ==============================
# Main Application
# ==============================

def main():

    show_banner()

    while True:

        print("\nMenu:")
        print("1. Analyze password")
        print("2. Generate secure password")
        print("3. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":

            password = getpass.getpass("Enter password: ")

            show_progress()

            score, feedback = calculate_score(password)

            entropy = calculate_entropy(password)

            crack_times = estimate_crack_time(entropy)

            strength = classify_strength(score)

            print("Score:", score, "/100")
            print("Strength:", strength)
            print(f"Entropy: {entropy:.2f} bits")

            print("\nCrack Time Estimates:")

            for attack, time_str in crack_times.items():
                print(f"{attack}: {time_str}")

            if feedback:
                print("\nRecommendations:")
                for item in feedback:
                    print("-", item)
            else:
                print("\nPassword meets security requirements")

        elif choice == "2":

            length = input("Enter password length (default 16): ")

            if length.isdigit():
                length = int(length)
            else:
                length = 16

            password = generate_password(length)

            print("\nGenerated password:")
            print(password)

        elif choice == "3":

            print("Exiting...")
            break

        else:
            print("Invalid option")


# Entry point
if __name__ == "__main__":
    main()
