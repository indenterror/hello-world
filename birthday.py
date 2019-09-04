birthday = { 'Neel': 'August 2', 'Shakil':'February 3', 'Arafat': ' March 2'}

while True:
    print('Enter a name: (blank to quite')
    name = input()
    if name == ' ':
        break
    if name in birthday:
        print([name] + 'is the birthday of ' + name)
    else:
        print('I do not have birtdya information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthday[name]= bday
        print('Birthday date updated')
