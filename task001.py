import re

def is_valid_contact_number(number):

    regex = r"^\+[0-9]{1,2}[0-9]{3}[0-9{3}[0-9{4}]"
    if re.match(regex, number):
        return True
    else:
        return False

print(is_valid_contact_number("2124567890"))
print(is_valid_contact_number("212-456-7890"))
print(is_valid_contact_number("(212)456-7890"))
print(is_valid_contact_number("(212)-456-7890"))
print(is_valid_contact_number("212.456.7890"))
print(is_valid_contact_number("212 456 7890"))
print(is_valid_contact_number("+12124567890"))
print(is_valid_contact_number("+12124567890"))
print(is_valid_contact_number("+1 212.456.7890"))
print(is_valid_contact_number("+212-456-7890"))
print(is_valid_contact_number("1-212-456-7890"))
