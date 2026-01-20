import re

def validate_password(password: str) -> bool:
    pattern = (
        r"^(?=.*[A-Z])"        # At least one uppercase letter
        r"(?=.*[a-z])"         # At least one lowercase letter
        r"(?=.*\d)"            # At least one digit
        r"(?=.*[@$!%*?&])"     # At least one special character
        r"[A-Za-z\d@$!%*?&]{8,}$"
    )
    return bool(re.match(pattern, password))


def regex_modifiers_demo():
    # IGNORECASE
    text1 = "Python Programming"
    pattern1 = "python"
    print("IGNORECASE Result:",
          bool(re.search(pattern1, text1, re.IGNORECASE)))

    # MULTILINE
    text2 = "Hello\nPython\nWorld"
    pattern2 = "^Python"
    print("MULTILINE Result:",
          bool(re.search(pattern2, text2, re.MULTILINE)))

    # DOTALL
    text3 = "Hello\nWorld"
    pattern3 = "Hello.*World"
    print("DOTALL Result:",
          bool(re.search(pattern3, text3, re.DOTALL)))

# Main
if __name__ == "__main__":

    #Validation
    passwords = [
        "Abc@1234",
        "abc123",
        "ABC@1234",
        "Abc12345"
    ]

    print("Password Validation Results:")
    for pwd in passwords:
        print(pwd, "→", validate_password(pwd))

    print("\nRegex Modifiers Demonstration:")
    regex_modifiers_demo()
