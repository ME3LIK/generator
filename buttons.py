from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from enum import Enum

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

class Characters(Enum):
    btn_upper = ascii_uppercase
    btn_lower = ascii_lowercase
    btn_digits = digits
    btn_special = punctuation
    
CHARACTER_NUMBER = {
    'btn_lower': len(Characters.btn_lower.value),
    'btn_upper': len(Characters.btn_upper.value),
    'btn_digits': len(Characters.btn_digits.value),
    'btn_special': len(Characters.btn_special.value)
}

GENERATE_PASSWORD = (
    'btn_refresh', 'btn_lower', 'btn_upper', 'btn_digits', 'btn_special'
)

