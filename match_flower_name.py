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
    FirstLetter = name[0].title()
    username = print('Unique flower name with the first letter:'.format(Flower[FirstLetter]))

ask()
    
# HINT: create a function to ask for user's first and last name


# print the desired output

