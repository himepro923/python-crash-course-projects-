num = input('give me a num and i will see if it is a muti of ten: ')
num = int(num)

if num % 10 == 0:
    print(f'{num} is a muti of ten')
else:
    print(f'{num} is not a muti of ten')