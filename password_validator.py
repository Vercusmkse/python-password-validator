def is_password_secure(password):
    if len(password) < 8:
        return False

    lowercase = uppercase = digit = special = False
    
    for char in password:
        if char.isdigit():
            digit = True
        elif char.islower():
            lowercase = True
        elif char.isupper():
            uppercase = True
        elif not char.isalnum() and char != " ":
            special = True
    
    return digit and lowercase and uppercase and special
