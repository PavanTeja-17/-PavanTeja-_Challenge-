import re
import sys

def validate_credit_card(card_number):
    pattern = r'^(?!.*(\d)(?:-?\1){3})[4-6]\d{3}(?:-?\d{4}){3}$'
    return bool(re.match(pattern, card_number))

# Read the number of credit card numbers
n = int(input())

# Read and validate each credit card number
for _ in range(n):
    card_number = input().strip()
    if validate_credit_card(card_number):
        print("Valid")
    else:
        print("Invalid")