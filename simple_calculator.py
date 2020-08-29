# A Simple Calculator 

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

while True:
    print('Please, Select an Operation to perform')
    print('1. ADDITION')
    print('2. SUBSTRACTION')
    print('3. MULTIPLICATION')
    print('4. DIVISION')
    a = input('Enter Choice (1/2/3/4) : ')

    if a in ('1','2','3','4'):
        first_num = float(input('Enter the First Number :'))
        second_num = float(input('Enter the Second Number :'))

        if a == '1':
            print(first_num,'+',second_num,'=',add(first_num,second_num))
        elif a == '2':
            print(first_num,'-',second_num,'=',sub(first_num,second_num))
        elif a == '3':
            print(first_num,'x',second_num,'=',mul(first_num,second_num))
        elif a == '4':
            print(first_num,'%',second_num,'=',div(first_num,second_num))
        else:
            print('Invalid Input')