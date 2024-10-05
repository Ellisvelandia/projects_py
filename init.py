x = 5
y = 3.14
name = "John"
is_cool = True
# print(x, y, name, is_cool)

name = input("What is your name? ")
age = input("How old are you? ")
hobby = input("What is your hobby? ")
city =  input("Where are you from? ")
likes_python = input("Do you like Python? (yes/no) ").lower()

if likes_python == 'yes':
    likes_python = True
else:
    likes_python = False

print(f'\nProfiles summary:')
print(f'Name: {name}')
print(f'Age: {age}')
print(f'Hobby: {hobby}')
print(f'City: {city}')
print(f'Likes Python: {likes_python}')
