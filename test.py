age = 23
is_birthday = True

if age >= 21:
    print("Be my guest!")
    if is_birthday:
        print("On the house!!")
elif age >= 18:
    print("Comeon in IN!!")
    if is_birthday:
        print("On the house!!")
else:
    print("Go home kid!")

color = 'teal'
print("Good Choice") if color == 'teal' else print("meh")

def greet(person):
    return print(f"Hello there, {person}.")

greet('billa')

def send_email(to_email, from_email):
    ''' helper function '''
    return print(to_email)

send_email(to_email="me@me.com", from_email="you")

def power(num, power=2):
    return num ** power;