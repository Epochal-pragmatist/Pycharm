import sys, time

print('Введите начальное число (больше 0) или Выход:')
response = input('> ')

if not response.isdecimal() or response == '0':
    print('Вы должны ввести целое число больше нуля')
    sys.exit()

n = int(response)
print(n, end='', flush=True)
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    print(', ' + str(n), end='', flush=True)
    time.sleep(0.1)
print()
