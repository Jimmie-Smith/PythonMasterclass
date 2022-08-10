
person_age = input('How old are you?')

def find_age(age):
    assert int(age) == age, 'Age must be an integer'
    if 16 <= age <= 65:
    # if age >= 16 and age <= 65:
        print('Age is between 16 and 65')
    else:
        print('Age must be between 16 and 65')
        
find_age(int(person_age))

i=0

while i <= int(person_age):
    print(f'the new age is {i}')
    i = i+1
