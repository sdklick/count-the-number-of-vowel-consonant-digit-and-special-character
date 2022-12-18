# count the number of vowel,consonant,digit and special character

userinput = input('input anything : ')
print('you input : ', userinput)
nu = '0123456789'
vo = 'aAeEiIoOuU'
sc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
countnu= countvo= countsc= countco = 0
for x in userinput:
    if x in nu:
        countnu += 1
    elif x in vo:
        countvo += 1
    elif x in sc:
        countsc += 1
    else:
        countco += 1
print('This input contains', countnu, 'digit')
print('This input contains', countvo, 'vowel')
print('This input contains', countsc, 'character')
print('This input contains', countco, 'consonent')