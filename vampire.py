"""THIS IS A PROGRAM TO DETERMINE IF YOU ARE A VAMPIRE"""

print('Are you a vampire?')
while True:
    is_vampire = input("yes or no? ")
    vampire_lower = is_vampire.lower()

    if vampire_lower == 'yes':
        print("How old are you?")
        break
    else:
        print("Too bad.")
        print("Are you sure you are not a vampire?")

age = int(input())

if age ==100:
    print ("Fledgling.")
elif age <=1000:
    print("Thats a long time to be alive I mean dead I mean undead.")
elif age >=4000:
    print("Do you even remember the sun?")
    remember_sun = input("yes or no?  ")
    remember_lower = remember_sun.lower()

    if remember_sun == 'yes':
        print("You have a really good memory.")
    else:
        print:("I thought so.")
