number=1

### RULES INPUT ###

fizzbuzz=int(input('Play fizzbuzz until what number : '))
fizz=int(input('fizz for multiply of : '))
buzz=int(input('buzz for multiply of : '))

### FIZZBUZZ ###

while number<=fizzbuzz:
    if((number%fizz==0) and (number%buzz==0)):
        print('fizzbuzz')
    elif((number%fizz==0) and (not(number%buzz==0))):
        print('fizz')
    elif((not(number%fizz==0)) and (number%buzz==0)):
        print('buzz')
    else:
        print(str(number))
    number+=1
