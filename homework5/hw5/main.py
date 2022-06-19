from check import ValidCarNumber
a = "y"
while a == 'y':
    chech1 = ValidCarNumber(input('Enter car number in format 01KG111ABC: '))
    chech1.is_valid()
    a = input('Will you check one more car number? Type "y" or "n": ')
    if a != 'y':
        print('bye...')