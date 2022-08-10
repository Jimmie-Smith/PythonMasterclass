name = input("what's your name?")
age = input('How old are you?')

def validate_age(age, name):
    assert int(age) >= 0 and int(age) == int(age), "Age must be a positive integer"
    if 18 <= int(age) <= 30:
        print(f"Welcome to your holiday {name}!")
    else:
        print(f"Sorry {name}, you're not old enough to go on holiday")
        
validate_age(age, name)