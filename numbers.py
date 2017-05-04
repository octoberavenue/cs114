"""Convert a bse-10 number between 1 and 99
to a wrietten out form of the number in Enlgish"""

print("enter a number between 1 and 99.")
num = int(input())
#double division only gives whole numbers no remainder.
tens = num // 10
#mod only keeps the remainder.
ones = num % 10

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
    tens_word = 'forty'
elif tens == 3:
    ten_word = 'thirty'
elif tens == 2:
    ten_word = 'twenty'

if tens == 1:
    ones == 3:
    teens_word = 'thirteen'

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


if tens ==1:
    output = teens_word

if tens == 0:
    output = ones_word
else:
    output = tens_word + '-' + ones_word

print(output)
