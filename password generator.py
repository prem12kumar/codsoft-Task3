
import random
import string

'''to generate a password'''
def generate_password(length, complexity):
    if complexity == 'low':
        characters = string.ascii_letters
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

"we are generating"
print("Password Generator")
print("Choose complexity level:")
print("1.low  (only letters)")
print("2.medium (letters and numbers)")
print("3. high 3(letters, numbers, and special characters)")

complexity_choice = input("Enter the desired complexity level (1/2/3): ")

if complexity_choice == '1':
    complexity = 'low'
elif complexity_choice == '2':
    complexity = 'medium'
elif complexity_choice == '3':
    complexity = 'high'
else:
    print("Invalid complexity choice")
    exit()

try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        raise ValueError
except ValueError:
    print("Invalid password length")
    exit()

password = generate_password(length, complexity)

print("Generated Password: " + password)