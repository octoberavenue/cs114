"""Convert a number in base-10 into a written out number in English."""
def prompt_for_number():
    return int(input(' Please enter a number between 0 and 99: '))

def get_tens_digit(num):
    return num // 10

def get_ones_digit(num):
    return num % 10

def tens_digit_to_word(tens):
    if tens == 9:
        tens_word = 'ninety'
    elif tens == 8:
        tens_word = 'eighty'
    elif tens == 7:
        tens_word = 'seventy'
    elif tens == 6:
        tens_word = 'sixty'
    elif tens == 5:
        tens_word = 'fifty'
    elif tens == 4:
        tens_word = 'fourty'
    elif tens == 3:
        tens_word = 'thirty'
    elif tens == 2:
        tens_word = 'twenty'
    return tens_word

def ones_digit_to_word(ones):
    if ones == 9:
        ones_word = 'nine'
    elif ones == 8:
        ones_word = 'eight'
    elif ones == 7:
        ones_word = 'seven'
    elif ones == 6:
        ones_word = 'six'
    elif ones == 5:
        ones_word = 'five'
    elif ones == 4:
        ones_word = 'four'
    elif ones == 3:
        ones_word = 'three'
    elif ones == 2:
        ones_word = 'two'
    elif ones == 1:
        ones_word = 'one'
    return ones_word

def assemble_words(tens, ones, tens_word, ones_word):
    if tens == 0:
        output = ones_word
    elif tens == 1:
        output == 'eleven'
    elif ones == 2:
        output = 'twelve'
    elif ones == 3:
        output = 'thirteen'
    return tens_word + '-' + ones_word

num = prompt_for_number()

tens = get_tens_digit(num)
ones = get_ones_digit(num)
tens_word = tens_digit_to_word(tens)
ones_word = ones_digit_to_word(ones)
output = assemble_words(tens, ones, tens_word, ones_word)

print(output)
