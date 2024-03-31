from re import finditer
from math import pi as π, prod
from string import ascii_lowercase as alphabet

alphabet, key, message = [*alphabet], "".join([i if i.isdigit() else "" for i in str(π)]), ""
with open("input.in", "r") as cipher: data = cipher.read()
for pos, char in enumerate(data):
    if not char.isalpha(): message += char; continue
    new_letter = alphabet[alphabet.index(char.lower())-int(key[pos%len(key)])]
    message += new_letter.upper() if char.isupper() else new_letter
shrinked_message, secret_code = "".join([i if i.isalpha() else "" for i in message]).lower(), []
secret_numbers, to_find = {}, {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10}
for num in to_find.keys():
    for i in finditer(num, shrinked_message): secret_numbers[i.start()] = to_find[num]
for i in sorted(list(secret_numbers.keys())): secret_code.append(secret_numbers[i])
result = prod(secret_code)
print(result)
