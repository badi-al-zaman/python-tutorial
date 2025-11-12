# https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true
n = int(input())
credits_cards = []
for i in range(n):
    credits_cards.append(input())

import re


def validate_credit_card(credit_card):
    is_valid = "Invalid"

    if re.search(r'^[456]', credit_card) and re.search(r'(\d{4}-?){4}|\d{16}', credit_card):
        is_valid = "Valid"
    credit_card = credit_card.replace('-', '')
    if re.search(r'(0{4}|1{4}|2{4}|3{4}|4{4}|5{4}|6{4}|7{4}|8{4}|9{4})', credit_card):
        is_valid = "Invalid"
    if ('-' in credit_card and not len(credit_card) == 19) or not len(credit_card) == 16:
        is_valid = "Invalid"
    return is_valid


for i in range(n):
    print(validate_credit_card(credits_cards[i]))
