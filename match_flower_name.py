# Write your code here

# HINT: create a dictionary from flowers.txt
def flower(filename):
    dict = {}
    with open('flowers.txt') as f:
        for line in f:
            line = line.split(':')
            key = line[0]
            value = line[1].strip()
            dict[key] = value
    return dict

def ask():
    Flower = flower('flowers.txt')
    name = input('enter your first [space] last name only:')
    first_name = name[0].lower()
    FirstLetter = first_name[0]
    username = print('Unique flower name with the first letter:'.format(flower[FirstLetter]))
    
    
# HINT: create a function to ask for user's first and last name
ask()

# print the desired output

