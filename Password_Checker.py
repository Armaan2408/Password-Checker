from passwordlib.commonly_used import is_commonly_used

def check_password(password):
    if is_commonly_used(password):
        return "Password is WEAK! It is easily guessable."

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in password)
    is_long_enough = len(password) >= 8

    if all([has_upper, has_lower, has_digit, has_special, is_long_enough]):
        return "Password is STRONG."
    else:
        issues = []
        if not has_upper:
            issues.append("At least one uppercase letter")
        if not has_lower:
            issues.append("At least one lowercase letter")
        if not has_digit:
            issues.append("At least one digit")
        if not has_special:
            issues.append("At least one special character")
        if not is_long_enough:
            issues.append("A minimum length of 8 characters")

        return "Password is WEAK. It should include:\n" + '\n'.join(issues)


password = input("Enter your password: ")
print(check_password(password))
