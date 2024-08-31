# Password Checker

This script checks the strength of a password by evaluating its commonness and compliance with basic security criteria. It uses the `passwordlib` library to verify if the password is commonly used and applies additional checks for password strength.

## Features

- **Common Password Check**: Determines if the password is commonly used and therefore potentially weak.
- **Strength Criteria**: Evaluates the password based on several criteria:
  - Contains at least one uppercase letter.
  - Contains at least one lowercase letter.
  - Contains at least one digit.
  - Contains at least one special character.
  - Is at least 8 characters long.

## Requirements

- **Python**: 3.11.4 or newer
- **Libraries**: `passwordlib`

To install the required library, use the following command:
```bash
pip install passwordlib
