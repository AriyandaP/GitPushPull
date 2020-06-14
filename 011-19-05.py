'''
SELASA - 19 Mei 2020
'''

number=1

fizzbuzz=int(input('Play fizzbuzz until what number : '))
fizz=int(input('fizz for multiply of : '))
buzz=int(input('buzz for multiply of : '))

while number<=fizzbuzz:
    pembagi = 0
    for number1 in range(2,fizzbuzz+1):
        if number%number1==0:
            pembagi+=1
        else:
            pembagi+=0
    if pembagi==1:
        if((number%fizz==0) and (number%buzz==0)):
            print('fizzbuzzPRIME')
        elif((number%fizz==0) and (not(number%buzz==0))):
            print('fizzPRIME')
        elif((not(number%fizz==0)) and (number%buzz==0)):
            print('buzzPRIME')
        else:
            (print('PRIME'))
    else:
        if((number%fizz==0) and (number%buzz==0)):
            print('fizzbuzz')
        elif((number%fizz==0) and (not(number%buzz==0))):
            print('fizz')
        elif((not(number%fizz==0)) and (number%buzz==0)):
            print('buzz')
        else:
            print(str(number))
    number+=1
