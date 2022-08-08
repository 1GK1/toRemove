from typing import Union, Any


def caesarCipher(s, k):
    encrypted_text = ''
    k = k % 26

    for letter in s:
        new_letter_ord = ord(letter) + k
        # if ord(letter) in range(97, 123):
        if letter.islower():
            if new_letter_ord in range(97, 123):
                encrypted_letter = chr(new_letter_ord)
            else:
                new_letter_ord = 97 + (new_letter_ord - 123)
                encrypted_letter = chr(new_letter_ord)
            encrypted_text += encrypted_letter

        # elif ord(letter) in range(65, 91):
        elif letter.isupper():
            if new_letter_ord in range(65, 91):
                encrypted_letter = chr(new_letter_ord)
            else:
                new_letter_ord = 65 + (new_letter_ord - 91)
                encrypted_letter = chr(new_letter_ord)
            encrypted_text += encrypted_letter
        else:
            encrypted_text += letter

    return encrypted_text

s = 'Mid <> dle-Outz'
# s = 'z'
k = 2

result = caesarCipher(s, k)
print(result)
#
print(ord('a'), ord('z'), ord('A'), ord('Z'))
#
print('a'.islower())
print('8'.islower())
print('8'.isupper())
# print(26 % 25)